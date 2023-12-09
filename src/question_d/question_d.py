class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol

    def get_company_name(self):
        return self.__company_name

def get_stock_list():
    stock_dict = {}
    with open("stock_file.txt", "r") as file:
        for line in file:
            tickers = line.strip().split(maxsplit=1)
            symbol, company_name = tickers
            stock_dict[symbol] = Stock(symbol, company_name)
    return stock_dict

def display_stock_list(stock_dict):
    print("Company - Symbol")
    for symbol, stock in stock_dict.items():
        print(f"{stock.get_company_name()} - {stock.get_symbol()}")

def main():
    stock_dict = get_stock_list()

    while True:
        print("Menu:")
        print("1 - Display stock purchase history")
        print("2 - Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_stock_list(stock_dict)
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")

main()
