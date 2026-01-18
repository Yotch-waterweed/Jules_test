def add(a, b):
    """This function adds two numbers."""
    return a + b

def multiply(a, b):
    """This function multiplies two numbers."""
    return a * b

def main():
    """Main function to run the CLI application."""
    try:
        num1_str = input("Enter the first number: ")
        num1 = float(num1_str)

        num2_str = input("Enter the second number: ")
        num2 = float(num2_str)

        # Calculate sum and product
        sum_result = add(num1, num2)
        product_result = multiply(num1, num2)

        # Print the results
        print(f"The sum is: {sum_result}")
        print(f"The product is: {product_result}")

    except ValueError:
        print("Invalid input. Please enter only numbers.")

if __name__ == "__main__":
    main()
