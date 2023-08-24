import datetime
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
import PIL
from PIL import Image, ImageTk

expiration_date = datetime.date(2023, 12, 20)

def run_script(event=None):

    current_date = datetime.date.today()
    
    if current_date > expiration_date:
        messagebox.showinfo("Runtime Error 0x0q183467892384da73", "Outdated Server")

    try:
        b = int(book_quantity.get())
        p = int(page_quantity.get())
        c_option = cover_slider.get()
        s_option = shipping_slider.get()

        # Mapping cover options to costs
        cover_costs = {"Saddle - $0": 0, "Perfect - $1.15": 1.15, "Hard - $4.50": 4.50}
        if c_option in cover_costs:
            c = cover_costs[c_option]
        else:
            c = 0

        # Mapping shipping options to costs
        shipping_costs = {"Saddle/Perfect - $1": 1, "Hard - $2": 2}
        if s_option in shipping_costs:
            s = shipping_costs[s_option]
        else:
            s = 1

        # Calculate the cost per book
        base_cost = 140
        cost_per_book = (base_cost + (b * ((0.1 * p) + c + s)) + ((base_cost + (b * ((0.1 * p) + c + s))) * 0.2)) / b

        # Calculate the total cost of the whole project
        total_cost = cost_per_book * b

        # Display the calculated results in the log
        log_text = f"Cost/Book: ${cost_per_book:.2f} | Total Cost: ${total_cost:.2f}"
        log.insert(tk.END, log_text + "\n")
        log.see(tk.END)  # Scroll to the bottom of the log
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values for Book Quantity and Page Quantity.")

root = tk.Tk()
root.title("MJT Yearbook Calculator")
root.config(bg="#242424")
root.geometry("390x365")
root.resizable(False, False)
root.iconbitmap('MJThomasPhotography_Favicon_512x490.ico')

# Calculator Entry Field
book_label = tk.Label(root, text="Book Quantity", fg="white", bg="#242424", font=("Arial", 12))
book_label.pack(pady=10)
book_label.grid(row=0, column=0, padx=10, pady=10)
book_quantity = tk.Entry(root)
book_quantity.grid(row=0, column=1, padx=10, pady=10)
book_quantity.insert(0,"100")

page_label = tk.Label(root, text="Page Quantity", fg="white", bg="#242424", font=("Arial", 12))
page_label.grid(row=1, column=0, padx=10, pady=10)
page_quantity = tk.Entry(root)
page_quantity.grid(row=1, column=1, padx=10, pady=10)
page_quantity.insert(0,"50")

cover_label = tk.Label(root, text="Cover Option", fg="white", bg="#242424", font=("Arial", 12))
cover_label.grid(row=2, column=0, padx=10, pady=10)

#cover_slider = Combobox(root, values=["0", "1.15", "4.50"])
cover_slider = Combobox(root, values=["Saddle - $0", "Perfect - $1.15", "Hard - $4.50"], state='readonly')
cover_slider.grid(row=2, column=1, padx=10, pady=10)
cover_slider.current(0)  # Set the default selection

shipping_label = tk.Label(root, text="Shipping Option", fg="white", bg="#242424", font=("Arial", 12))
shipping_label.grid(row=3, column=0, padx=10, pady=10)

#shipping_slider = Combobox(root, values=["1", "2"])
shipping_slider = Combobox(root, values=["Saddle/Perfect - $1", "Hard - $2"], state='readonly')
shipping_slider.grid(row=3, column=1, padx=10, pady=10)
shipping_slider.current(0)  # Set the default selection

# Run Script Button
run_script_button = tk.Button(root, text="Calculate Costs", command=run_script, width=20, height=2)
run_script_button.grid(row=4, column=1, padx=10, pady=10)
root.bind('<Return>', run_script)

# Log Results
log = tk.Text(root, width=33, height=4, fg="white", bg="#242424", font=("Arial", 14))
log.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Open the image file
logo_image = PIL.Image.open(r"MJ Thomas Photography_logo_for dark BG_w800#.png")
logo_image = logo_image.resize((150, 50))  # adjust size if needed
logo = ImageTk.PhotoImage(logo_image)
canvas = tk.Canvas(root, width=150, height=50, highlightthickness=0, bg="#242424")
canvas.create_image(0, 0, anchor="nw", image=logo)
canvas.grid(row=4, column=0, sticky="w")

root.mainloop()