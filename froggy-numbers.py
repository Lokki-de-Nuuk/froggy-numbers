import tkinter as tk
from tkinter import ttk
import random

def generate_numbers():
    try:
        min_range = int(min_entry.get())
        max_range = int(max_entry.get())
        num_numbers = int(num_entry.get())
        unique_numbers = unique_var.get()

        if min_range >= max_range:
            result_var.set("Error: Min should be less than Max")
            return

        if unique_numbers:
            if num_numbers > (max_range - min_range + 1):
                result_var.set("Error: Cannot generate unique numbers, not enough range")
                return

            random_numbers = random.sample(range(min_range, max_range + 1), num_numbers)
        else:
            random_numbers = [random.randint(min_range, max_range) for _ in range(num_numbers)]

        average = sum(random_numbers) / len(random_numbers)
        random_numbers.sort()

        result_var.set(f"Froggy Numbers: {random_numbers}\nAverage: {average:.2f}")
    except ValueError:
        result_var.set("Error: Please enter valid numbers")

# Create the main window
window = tk.Tk()
window.title("Froggy Numbers")

# Create and place widgets
min_label = ttk.Label(window, text="Minimum:")
min_label.grid(row=0, column=0, padx=5, pady=5)
min_entry = ttk.Entry(window)
min_entry.grid(row=0, column=1, padx=5, pady=5)

max_label = ttk.Label(window, text="Maximum:")
max_label.grid(row=1, column=0, padx=5, pady=5)
max_entry = ttk.Entry(window)
max_entry.grid(row=1, column=1, padx=5, pady=5)

num_label = ttk.Label(window, text="How many Froggy numbers?")
num_label.grid(row=2, column=0, padx=5, pady=5)
num_entry = ttk.Entry(window)
num_entry.grid(row=2, column=1, padx=5, pady=5)

unique_var = tk.BooleanVar()
unique_checkbox = ttk.Checkbutton(window, text="Only unique numbers", variable=unique_var)
unique_checkbox.grid(row=3, column=0, columnspan=2, pady=5)

generate_button = ttk.Button(window, text="Generate Froggy Numbers", command=generate_numbers)
generate_button.grid(row=4, column=0, columnspan=2, pady=10)

result_var = tk.StringVar()
result_label = ttk.Label(window, textvariable=result_var)
result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Start the main loop
window.mainloop()
