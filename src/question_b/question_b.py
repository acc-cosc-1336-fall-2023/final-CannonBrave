def create_multiplication_table():
    table = []
    for i in range(1, 11):
        row = [i * j for j in range(1, 11)]
        table.append(row)
    return table

def display_multiplication_table(table):
    for row in table:
        print(" ".join(f"{num:2}" for num in row))

def main():
    while True:
        table = create_multiplication_table()
        display_multiplication_table(table)

        exit = input("Do you want to display the table again? (y/n): ")
        if exit != 'y':
            break