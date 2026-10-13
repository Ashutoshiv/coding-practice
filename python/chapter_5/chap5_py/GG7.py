import requests
import threading    
import time
import os

# --- ARCHITECT FIX 1: Functions live outside of loops ---
# You had defined 'get_coin_info' INSIDE the while loop. That means Python was 
# destroying and recreating the function in memory every 10 seconds! 
# Functions must always be defined at the root level.
base_url = "https://api.coingecko.com/api/v3/simple"

def get_coin_info(name):
    url = f"{base_url}/price?ids={name}&vs_currencies=usd"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if name in data:
                return data[name]["usd"]
        elif response.status_code == 429:
            # We don't print this to the main terminal because it interrupts the user's typing!
            pass 
    except requests.exceptions.RequestException:
        pass
    return None

def coin_price():
    """Background Thread: Quietly updates the file every 10 seconds."""
    while True:
        price = get_coin_info("bitcoin")
        if price is not None:
            # 'w' is actually PERFECT here. You don't want a massive log of thousands of prices.
            # You just want to overwrite the file with the "Current State" so the user can read it.
            with open("btc_logs.txt", "w") as file:
                file.write(f"Sir, the current price of bitcoin is ${price}")
        time.sleep(10)

def user_ask():
    """Foreground Thread: Talks to the user."""
    time.sleep(1) # Let the background thread start up first
    while True:
        user_input = input("\nAsk (type 'exit' to exit) ?: ").strip().lower()
        
        if user_input == "exit":
            print("Goodbye!")
            # --- ARCHITECT FIX 2: The Zombie Process ---
            # If you just use 'break', this loop dies, but your background 'coin_price' thread 
            # will keep running forever in the background like a zombie!
            # os._exit(0) instantly kills the entire program and all background threads.
            os._exit(0)
            
        elif user_input == "price":
            try:
                with open("btc_logs.txt", "r") as file:
                    print(file.read())
            except FileNotFoundError:
                print("Data is still downloading. Please try again in a few seconds.")
        else:
            print("Please type 'price'.") 

# --- ARCHITECT FIX 3: Daemon Threads ---
# Adding daemon=True tells Python: "If the main program closes, kill this thread immediately."
chore1 = threading.Thread(target=coin_price, daemon=True)
chore1.start()

# You don't actually need to thread the second chore! 
# You can just run the user interface on the main thread.
user_ask()