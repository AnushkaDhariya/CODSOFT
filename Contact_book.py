import tkinter as tk
from tkinter import messagebox

# Main System Window
window = tk.Tk()
window.title("CodSoft - Contact Book")
window.geometry("500x550")
window.configure(bg="#2C3E50")  # Dark elegant background

# Global list to store contacts
all_contacts = []

# --- CORE FUNCTIONS ---

def clear_fields():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

def refresh_list(custom_list=None):
    listbox.delete(0, tk.END)
    display_list = custom_list if custom_list is not None else all_contacts
    for c in display_list:
        listbox.insert(tk.END, f"👤 {c['name']}  |  📞 {c['phone']}")

def add_contact():
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    email = entry_email.get().strip()
    address = entry_address.get().strip()
    
    if not name or not phone:
        messagebox.showwarning("Required Fields", "Name and Phone Number are compulsory!")
        return
        
    all_contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    messagebox.showinfo("Success", "New contact saved!")
    clear_fields()
    refresh_list()

def load_selected_contact(event):
    try:
        selected_index = listbox.curselection()[0]
        selected_text = listbox.get(selected_index)
        
        # Extracting name from the listbox format
        name_part = selected_text.replace("👤 ", "").split("  |  ")[0]
        
        for c in all_contacts:
            if c['name'] == name_part:
                clear_fields()
                entry_name.insert(0, c['name'])
                entry_phone.insert(0, c['phone'])
                entry_email.insert(0, c['email'])
                entry_address.insert(0, c['address'])
                break
    except IndexError:
        pass

def update_contact():
    try:
        selected_index = listbox.curselection()[0]
        selected_text = listbox.get(selected_index)
        name_part = selected_text.replace("👤 ", "").split("  |  ")[0]
        
        for c in all_contacts:
            if c['name'] == name_part:
                c['name'] = entry_name.get().strip()
                c['phone'] = entry_phone.get().strip()
                c['email'] = entry_email.get().strip()
                c['address'] = entry_address.get().strip()
                messagebox.showinfo("Updated", "Contact details updated successfully!")
                clear_fields()
                refresh_list()
                return
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a contact from the list first!")

def delete_contact():
    try:
        selected_index = listbox.curselection()[0]
        selected_text = listbox.get(selected_index)
        name_part = selected_text.replace("👤 ", "").split("  |  ")[0]
        
        for c in all_contacts:
            if c['name'] == name_part:
                all_contacts.remove(c)
                messagebox.showinfo("Deleted", "Contact removed!")
                clear_fields()
                refresh_list()
                return
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a contact to delete!")

def search_contact():
    query = entry_search.get().strip().lower()
    if not query:
        refresh_list()
        return
    
    results = [c for c in all_contacts if query in c['name'].lower() or query in c['phone']]
    refresh_list(results)


# --- MODERN STUDENT UI DESIGN ---

# Header Title
title_lbl = tk.Label(window, text="CONTACT BOOK", font=("Helvetica", 16, "bold"), bg="#2C3E50", fg="#ECF0F1")
title_lbl.pack(pady=15)

# Input Container Frame
input_frame = tk.Frame(window, bg="#34495E", bd=2, relief="groove", padx=10, pady=10)
input_frame.pack(fill="x", padx=20, pady=5)

# Style configuration for standard labels
lbl_style = {"bg": "#34495E", "fg": "#ECF0F1", "font": ("Helvetica", 10, "bold")}

# Grid Form Layout
tk.Label(input_frame, text="Name:", **lbl_style).grid(row=0, column=0, sticky="w", pady=5)
entry_name = tk.Entry(input_frame, width=38, font=("Helvetica", 10))
entry_name.grid(row=0, column=1, pady=5, padx=5)

tk.Label(input_frame, text="Phone:", **lbl_style).grid(row=1, column=0, sticky="w", pady=5)
entry_phone = tk.Entry(input_frame, width=38, font=("Helvetica", 10))
entry_phone.grid(row=1, column=1, pady=5, padx=5)

tk.Label(input_frame, text="Email:", **lbl_style).grid(row=2, column=0, sticky="w", pady=5)
entry_email = tk.Entry(input_frame, width=38, font=("Helvetica", 10))
entry_email.grid(row=2, column=1, pady=5, padx=5)

tk.Label(input_frame, text="Address:", **lbl_style).grid(row=3, column=0, sticky="w", pady=5)
entry_address = tk.Entry(input_frame, width=38, font=("Helvetica", 10))
entry_address.grid(row=3, column=1, pady=5, padx=5)


# Buttons Panel
btn_frame = tk.Frame(window, bg="#2C3E50")
btn_frame.pack(fill="x", padx=20, pady=10)

btn_add = tk.Button(btn_frame, text="➕ Add", command=add_contact, bg="#2ECC71", fg="white", font=("Helvetica", 10, "bold"), width=9, bd=0, cursor="hand2")
btn_add.pack(side="left", padx=4)

btn_update = tk.Button(btn_frame, text="🔄 Update", command=update_contact, bg="#3498DB", fg="white", font=("Helvetica", 10, "bold"), width=9, bd=0, cursor="hand2")
btn_update.pack(side="left", padx=4)

btn_delete = tk.Button(btn_frame, text="🗑️ Delete", command=delete_contact, bg="#E74C3C", fg="white", font=("Helvetica", 10, "bold"), width=9, bd=0, cursor="hand2")
btn_delete.pack(side="left", padx=4)

btn_clear = tk.Button(btn_frame, text="🧹 Clear", command=clear_fields, bg="#7F8C8D", fg="white", font=("Helvetica", 10, "bold"), width=9, bd=0, cursor="hand2")
btn_clear.pack(side="left", padx=4)


# Search Bar Section
search_frame = tk.Frame(window, bg="#2C3E50")
search_frame.pack(fill="x", padx=20, pady=5)

entry_search = tk.Entry(search_frame, width=34, font=("Helvetica", 11))
entry_search.pack(side="left", padx=2, ipady=3)

# FIXED: ipady moved from tk.Button into .pack()
btn_search = tk.Button(search_frame, text="🔍 Search", command=search_contact, bg="#1ABC9C", fg="white", font=("Helvetica", 9, "bold"), bd=0, padx=10, cursor="hand2")
btn_search.pack(side="left", padx=4, ipady=3)


# Output Listbox Display
list_frame = tk.Frame(window, bg="#2C3E50")
list_frame.pack(fill="both", expand=True, padx=20, pady=15)

scroller = tk.Scrollbar(list_frame)
scroller.pack(side="right", fill="y")

listbox = tk.Listbox(list_frame, font=("Helvetica", 11), bg="#ECF0F1", fg="#2C3E50", selectbackground="#3498DB", yscrollcommand=scroller.set, bd=0)
listbox.pack(fill="both", expand=True)
scroller.config(command=listbox.yview)

# Binding selection action
listbox.bind("<<ListboxSelect>>", load_selected_contact)

# Start application loop
window.mainloop()