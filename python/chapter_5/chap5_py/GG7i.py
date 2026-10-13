import requests
import threading    
import time

def coin_price():


    base_url = "https://api.coingecko.com/api/v3/simple"

    while True:
        time.sleep(10)

        def get_coin_info(name):
            url = f"{base_url}/price?ids={name}&vs_currencies=usd"
            
            try:
                response = requests.get(url)
                
                if response.status_code == 200:
                    data = response.json()
                    
                    if name in data:
                        price = data[name]["usd"]
                        return price
                    else:
                        return None 
                elif response.status_code == 429:
                    print("Rate limited by CoinGecko. Waiting before retrying.")
                    return None
                else:
                    print(f"Failed to retrieve data. Status: {response.status_code}")
                    return None
                    
            except requests.exceptions.RequestException as e:
                print(f"Network Error: {e}")
                return None

        coin_name = "bitcoin"
        price = get_coin_info(coin_name)

        # We only print the price if the function successfully returned a number
        if price is not None:
            with open("btc_logs.txt", "w") as file:
                file.write(f"Sir, the current price of {coin_name} is ${price}\n")
        else:
            with open("mainframe_data.txt", "w") as file:
                file.write(f"Sir, I could not locate financial data for '{coin_name}'.")

def user_ask():
    time.sleep(1)
    while True:
        user_input = input("Ask (type 'exit' to exit) ? :")
        if user_input.lower() == "exit":
            print("Good bye!")
            break
        try:
            user_input = str(user_input)
            if user_input == "price":
                with open("btc_logs.txt", "r") as file:
                    remembered_data = file.read()
                    print(remembered_data)
            else:
                print("Please! type 'price'.")        
        except :
            print("Error! You didn't type price. ")

chore1 = threading.Thread(target=coin_price)
chore1.start()

chore2 = threading.Thread(target=user_ask)
chore2.start()

