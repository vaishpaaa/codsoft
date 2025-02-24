import tkinter as tk
from tkinter import messagebox

def on_click(event):
    """Handles button clicks and updates the entry field."""
    text = event.widget.cget("text")

    if text == "=":
        try:
            expression = entry_var.get()
            result = eval(expression)  # Evaluates the mathematical expression
            show_result(expression, result)
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero!")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
    elif text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + text)

def show_result(expression, result):
    """Displays the result in a visually appealing external window."""
    result_window = tk.Toplevel(root)
    result_window.title("Calculation Result")
    result_window.geometry("500x250")
    result_window.configure(bg="#2C3E50")  # Dark background

    # Title Label
    label_title = tk.Label(result_window, text="Calculation Result", font=("Arial", 18, "bold"), fg="white", bg="#2C3E50")
    label_title.pack(pady=10)

    # Expression Label
    label_expression = tk.Label(result_window, text=f"Expression: {expression}", font=("Arial", 14), fg="cyan", bg="#2C3E50")
    label_expression.pack(pady=5)

    # Result Label
    label_result = tk.Label(result_window, text=f"Result: {result}", font=("Arial", 22, "bold"), fg="#00FF00", bg="#2C3E50")
    label_result.pack(pady=10)

    # OK Button
    ok_button = tk.Button(result_window, text="OK", font=("Arial", 14, "bold"), fg="white", bg="#E74C3C", command=result_window.destroy)
    ok_button.pack(pady=10, ipadx=20)

# Main application window
root = tk.Tk()
root.title("Responsive GUI Calculator")
root.geometry("600x700")  # Default size but resizable
root.configure(bg="#34495E")
root.resizable(True, True)  # Allows maximizing and resizing

entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font=("Arial", 30), bd=10, relief="ridge", justify="right", bg="#ECF0F1")
entry.pack(fill="both", padx=10, pady=10, ipadx=10, ipady=10)

# Button Layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+'),
    ('.', '(', ')', '**')  # Extra row for advanced operations
]

frame = tk.Frame(root, bg="#34495E")
frame.pack(expand=True, fill="both")

for i, row in enumerate(buttons):
    for j, btn in enumerate(row):
        button = tk.Button(frame, text=btn, font=("Arial", 24, "bold"), padx=20, pady=20, 
                           bg="#3498DB", fg="white", relief="raised", bd=5, activebackground="#2980B9")
        button.grid(row=i, column=j, sticky="nsew", padx=5, pady=5)
        button.bind("<Button-1>", on_click)

# Make buttons expand to fill available space
for i in range(len(buttons)):
    frame.rowconfigure(i, weight=1)
for j in range(len(buttons[0])):
    frame.columnconfigure(j, weight=1)

root.mainloop()
