my_list = ["10", "manzana", "5.5", "3", "n/a"]

def sum_values(list):
    result = 0
    for item in list:
        try:
            convertion = float(item)
            result += convertion
            print(f"Element {item} was successfully added")

        except ValueError as error:
            print(f"Invalid element: {item}")

    print(f"Total: {result}")


def main():
    sum_values(my_list)


if __name__ == "__main__":
    main()
