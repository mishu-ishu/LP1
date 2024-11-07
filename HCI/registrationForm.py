import tkinter as tk
from tkinter import ttk

# Function to handle form submission
def submit_form():
    print("Name:", entry_name.get())
    print("Email:", entry_email.get())
    print("Phone:", entry_phone.get())
    print("Gender:", gender_var.get())
    print("Password:", entry_password.get())
    print("Accept Terms:", terms_var.get())

    selected_interests = listbox_interests.curselection()
    interests = [listbox_interests.get(i) for i in selected_interests]
    print("Interests:", interests)

# Create the main application window
root = tk.Tk()
root.title("Registration Form")

# Set the size of the window
root.geometry("400x450")

# Name
label_name = ttk.Label(root, text="Name:")
label_name.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
entry_name = ttk.Entry(root, width=30)
entry_name.grid(row=0, column=1, padx=10, pady=10)

# Email
label_email = ttk.Label(root, text="Email:")
label_email.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
entry_email = ttk.Entry(root, width=30)
entry_email.grid(row=1, column=1, padx=10, pady=10)

# Phone
label_phone = ttk.Label(root, text="Phone:")
label_phone.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
entry_phone = ttk.Entry(root, width=30)
entry_phone.grid(row=2, column=1, padx=10, pady=10)

# Gender
label_gender = ttk.Label(root, text="Gender:")
label_gender.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
gender_var = tk.StringVar()
combobox_gender = ttk.Combobox(root, textvariable=gender_var, values=("Male", "Female", "Other"), state="readonly")
combobox_gender.grid(row=3, column=1, padx=10, pady=10)

# Password
label_password = ttk.Label(root, text="Password:")
label_password.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
entry_password = ttk.Entry(root, show="*", width=30)
entry_password.grid(row=4, column=1, padx=10, pady=10)

# Interests
label_interests = ttk.Label(root, text="Interests:")
label_interests.grid(row=5, column=0, padx=10, pady=10, sticky=tk.W)
listbox_interests = tk.Listbox(root, selectmode=tk.MULTIPLE, height=5)
listbox_interests.grid(row=5, column=1, padx=10, pady=10)
interests = ["Reading", "Traveling", "Cooking", "Sports", "Music", "Movies"]
for interest in interests:
    listbox_interests.insert(tk.END, interest)

# Accept Terms
terms_var = tk.IntVar()
checkbutton_terms = ttk.Checkbutton(root, text="Accept Terms and Conditions", variable=terms_var)
checkbutton_terms.grid(row=6, columnspan=2, padx=10, pady=10)

# Submit button
button_submit = ttk.Button(root, text="Submit", command=submit_form)
button_submit.grid(row=7, columnspan=2, pady=20)

# Run the main loop
root.mainloop()
