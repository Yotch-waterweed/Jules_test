import tkinter as tk
from tkinter import ttk

def add(a, b):
    """This function adds two numbers."""
    return a + b

def multiply(a, b):
    """This function multiplies two numbers."""
    return a * b

def calculate():
    """Handles the calculation and updates the GUI."""
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        sum_result = add(num1, num2)
        product_result = multiply(num1, num2)

        result_label.config(text=f"Sum: {sum_result}\nProduct: {product_result}")
    except ValueError:
        result_label.config(text="Error: Please enter valid numbers.")

# --- GUI Setup ---
def main():
    """Main function to create and run the GUI application."""
    global entry1, entry2, result_label  # Make widgets globally accessible within the module

    root = tk.Tk()
    root.title("Simple Calculator")
    root.geometry("300x200")

    # Use a frame for better organization
    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # Input for the first number
    ttk.Label(frame, text="First Number:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    entry1 = ttk.Entry(frame)
    entry1.grid(row=0, column=1, padx=5, pady=5)

    # Input for the second number
    ttk.Label(frame, text="Second Number:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
    entry2 = ttk.Entry(frame)
    entry2.grid(row=1, column=1, padx=5, pady=5)

    # Calculate button
    calculate_button = ttk.Button(frame, text="Calculate", command=calculate)
    calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

    # Label to display the result
    result_label = ttk.Label(frame, text="Results will be shown here.")
    result_label.grid(row=3, column=0, columnspan=2, pady=5)

    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()
