import tkinter as tk


class BillCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Test 10")
        self.root.configure(bg='light grey')
        self.root.resizable(False, False)
        self.root.geometry('350x450')
        
        self.food_var = tk.StringVar(value="")
        self.drink_var = tk.StringVar(value="")
        self.dessert_var = tk.StringVar(value="")
        self.tip_var = tk.IntVar(value=10)
        
        tk.Label(root, text="BILL CALCULATOR", bg='light grey').grid(row=0, column=0, columnspan=4, pady=10)
        
        tk.Label(root, text="Food", bg='light grey').grid(row=1, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.food_var).grid(row=1, column=1, columnspan=3, padx=10, pady=5, sticky='ew')
        
        tk.Label(root, text="Drink", bg='light grey').grid(row=2, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.drink_var).grid(row=2, column=1, columnspan=3, padx=10, pady=5, sticky='ew')
        
        tk.Label(root, text="Dessert", bg='light grey').grid(row=3, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.dessert_var).grid(row=3, column=1, columnspan=3, padx=10, pady=5, sticky='ew')
        
        tk.Label(root, text="Tip", bg='light grey').grid(row=4, column=0, padx=10, pady=5)
        tk.Radiobutton(root, text="10%", variable=self.tip_var, value=10, bg='light grey').grid(row=4, column=1, padx=5)
        tk.Radiobutton(root, text="15%", variable=self.tip_var, value=15, bg='light grey').grid(row=4, column=2, padx=5)
        tk.Radiobutton(root, text="20%", variable=self.tip_var, value=20, bg='light grey').grid(row=4, column=3, padx=5)
        
        self.summary_label = tk.Label(root, text="SUMMARY", bg='light grey')
        self.summary_label.grid(row=5, column=0, columnspan=4, pady=10)
        
        self.summary_text = tk.Text(root, height=10, width=40, bg='light grey', relief='flat')
        self.summary_text.grid(row=6, column=0, columnspan=4, padx=10, pady=5)
        
        tk.Button(root, text="SUBMIT", command=self.calculate_bill).grid(row=7, column=0, columnspan=2, pady=10, padx=10)
        tk.Button(root, text="CLEAR", command=self.clear_entries).grid(row=7, column=2, columnspan=2, pady=10, padx=10)
        
    def calculate_bill(self):
        try:
            food_cost = float(self.food_var.get())
            drink_cost = float(self.drink_var.get())
            dessert_cost = float(self.dessert_var.get())
            
            subtotal = food_cost + drink_cost + dessert_cost
            tax = subtotal * 0.1
            tip = (subtotal + tax) * (self.tip_var.get() / 100)
            total = subtotal + tax + tip
            
            self.summary_text.delete('1.0', tk.END)

            self.summary_text.insert(tk.END, f"         Food:        ${food_cost:.2f}\n")
            self.summary_text.insert(tk.END, f"         Drink:       ${drink_cost:.2f}\n")
            self.summary_text.insert(tk.END, f"         Dessert:     ${dessert_cost:.2f}\n")
            self.summary_text.insert(tk.END, f"         Tax:         ${tax:.2f}\n")
            self.summary_text.insert(tk.END, f"         Tip:         ${tip:.2f}\n\n")
            self.summary_text.insert(tk.END, f"         TOTAL:       ${total:.2f}\n")
        except ValueError:
            self.summary_text.insert(tk.END,"         Food, drink, and dessert\n         need to be numeric\n         e.g. 10.25 not $10.25\n")
            
    def clear_entries(self):
        self.food_var.set("")
        self.drink_var.set("")
        self.dessert_var.set("")
        self.tip_var.set(10)
        self.summary_text.delete('1.0', tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = BillCalculator(root)
    root.mainloop()