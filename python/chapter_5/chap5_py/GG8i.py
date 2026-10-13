import requests
import re
import threading    
import time
import os


def get_email_info():
    """Fetch emails from website and return them as a list."""
    url = "https://www.webhouseindia.com/contact-us"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
            raw_html = response.text
            found_emails = re.findall(email_pattern, raw_html)  # Returns LIST of emails
            
            # FIXED: Check if list is not empty, then return it
            # OLD BUG: Was checking if regex pattern STRING is in the list (always False!)
            if found_emails:  # If list has emails
                return found_emails  # Return the list directly
            else:
                return []  # Return empty list if no emails found
                
        elif response.status_code == 429:
            # We don't print this to the main terminal because it interrupts the user's typing!
            return []  # FIXED: Return empty list instead of None
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching emails: {e}")  # FIXED: Show actual error
        return []  # FIXED: Return empty list instead of None
    
    return []  # FIXED: Return empty list as fallback

def total_emails():  # FIXED: Typo - was 'toal_emails'
    """Background Thread: Quietly updates the file every 10 seconds."""
    while True:
        emails = get_email_info()
        if emails:  # FIXED: Check if list is not empty (empty list is falsy)
            # FIXED: Changed from 'a' (append) to 'w' (write) to overwrite
            # This way you keep only the latest emails, not accumulate forever
            with open("all_emails.txt", "w") as file:
                file.write(f"Sir, This is your emails : {emails}\n")
        time.sleep(10)

# FIXED: Changed filename from 'all_emails_.txt' to 'all_emails.txt' to match what gets written
# Also wrapped in try-except since file might not exist yet
try:
    with open("all_emails.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("No emails file found yet. Starting email fetcher...")



# def user_ask():
#     """Foreground Thread: Talks to the user."""
#     time.sleep(1) # Let the background thread start up first
#     while True:
#         user_input = input("\nAsk (type 'exit' to exit) ?: ").strip().lower()
        
#         if user_input == "exit":
#             print("Goodbye!")
#             # --- ARCHITECT FIX 2: The Zombie Process ---
#             # If you just use 'break', this loop dies, but your background 'coin_price' thread 
#             # will keep running forever in the background like a zombie!
#             # os._exit(0) instantly kills the entire program and all background threads.
#             os._exit(0)
            
#         elif user_input == "emails":
#             try:
#                 with open("all_emails.txt", "r") as file:
#                     print(file.read())
#             except FileNotFoundError:
#                 print("Data is still downloading. Please try again in a few seconds.")
#         else:
#             print("Please type 'emails'.") 

# # --- ARCHITECT FIX 3: Daemon Threads ---
# # Adding daemon=True tells Python: "If the main program closes, kill this thread immediately."
# chore1 = threading.Thread(target=toal_emails, daemon=True)
# chore1.start()

# # You don't actually need to thread the second chore! 
# # You can just run the user interface on the main thread.
# user_ask()