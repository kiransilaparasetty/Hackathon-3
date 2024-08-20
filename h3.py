import time

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bids = []

class Auction:
    def __init__(self, item_name, starting_price):
        self.item_name = item_name
        self.starting_price = starting_price
        self.current_price = starting_price
        self.bids = []
        self.is_active = True

    def place_bid(self, user, bid_amount):
        if not self.is_active:
            print("Auction has ended.")
            return
        
        if bid_amount > self.current_price:
            self.current_price = bid_amount
            self.bids.append((user.username, bid_amount))
            user.bids.append((self.item_name, bid_amount))
            print(f"Bid of ${bid_amount} placed by {user.username}.")
        else:
            print("Bid amount must be higher than the current price.")

    def end_auction(self):
        self.is_active = False
        print(f"Auction for {self.item_name} has ended. Final price: ${self.current_price}")

class AuctionSystem:
    def __init__(self):
        self.users = {}
        self.auctions = {}

    def register_user(self):
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        if username in self.users:
            print("Username already exists.")
        else:
            self.users[username] = User(username, password)
            print(f"User {username} registered successfully.")

    def login_user(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        user = self.users.get(username)
        if user and user.password == password:
            print(f"User {username} logged in successfully.")
            return user
        else:
            print("Invalid username or password.")
            return None

    def create_auction(self):
        item_name = input("Enter the item name: ")
        starting_price = float(input("Enter the starting price: "))
        if item_name in self.auctions:
            print("Auction for this item already exists.")
        else:
            self.auctions[item_name] = Auction(item_name, starting_price)
            print(f"Auction for {item_name} created with starting price ${starting_price}.")

    def view_auctions(self):
        if not self.auctions:
            print("No auctions available.")
        for item_name, auction in self.auctions.items():
            status = "Active" if auction.is_active else "Ended"
            print(f"Item: {item_name}, Current Price: ${auction.current_price}, Status: {status}")

    def place_bid(self, user):
        item_name = input("Enter the item name you want to bid on: ")
        bid_amount = float(input("Enter your bid amount: "))
        auction = self.auctions.get(item_name)
        
        if not auction:
            print("Auction not found.")
            return

        auction.place_bid(user, bid_amount)

    def end_auction(self):
        item_name = input("Enter the item name of the auction to end: ")
        auction = self.auctions.get(item_name)
        if auction:
            auction.end_auction()
        else:
            print("Auction not found.")

def main():
    system = AuctionSystem()
    
    while True:
        print("\n--- Auction System Menu ---")
        print("1. Register")
        print("2. Login")
        print("3. Create Auction")
        print("4. View Auctions")
        print("5. Place Bid")
        print("6. End Auction")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            system.register_user()
        elif choice == '2':
            user = system.login_user()
            if user:
                while True:
                    print("\n--- User Menu ---")
                    print("1. View Auctions")
                    print("2. Place Bid")
                    print("3. Logout")

                    user_choice = input("Enter your choice: ")

                    if user_choice == '1':
                        system.view_auctions()
                    elif user_choice == '2':
                        system.place_bid(user)
                    elif user_choice == '3':
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == '3':
            system.create_auction()
        elif choice == '4':
            system.view_auctions()
        elif choice == '5':
            print("You need to log in first.")
        elif choice == '6':
            system.end_auction()
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
