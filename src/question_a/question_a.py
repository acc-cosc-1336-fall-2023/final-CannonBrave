class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol

    def get_company_name(self):
        return self.__company_name

def stock_purchase_history():
    stocks = [
        Stock("AAPL", "Apple Inc"),
        Stock("CAT", "Caterpillar"),
        Stock("EK", "Eastman Kodak"),
        Stock("GOOG", "Google"),
        Stock("MSFT", "Microsoft")
    ]

    stock_dict = {stock.get_symbol(): stock.get_company_name() for stock in stocks}

    for symbol, company in stock_dict.items():
        print(f"{symbol} - {company}")

def main():
    while True:
        print("Menu:")
        print("1 - Display stock purchase history")
        print("2 - Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            stock_purchase_history()
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")