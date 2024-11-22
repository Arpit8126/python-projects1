import tkinter as tk
from tkinter import font, simpledialog, messagebox
import math
import time
import subprocess
from PIL import Image, ImageTk
# Splash screen class
class SplashScreen(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry(f"{parent.winfo_screenwidth()}x{parent.winfo_screenheight()}+0+0")
        self.configure(bg="#F0F0F0")
        self.overrideredirect(True)
        

        # Display main text with animation
        self.label = tk.Label(self, text="Arpit Pandey Creation", font=("Helvetica", 70, "bold"), fg="#2D3142")
        self.label.pack(pady=120)

        # Subtitle text
        self.subtitle = tk.Label(self, text="AUSK Group Presents : Calculator Vault", font=("Arial", 50, "italic"), fg="#2D3142")
        self.subtitle.pack(pady=10)
        

        # Small calculator logo
        self.logo = tk.Label(self, text="🖩", font=("Arial", 300), fg="#FF5733")
        self.logo.pack(pady=20)  # Add vertical padding

        # Fade-in animation
        self.attributes("-alpha", 0)
        self.fade_in()

    def fade_in(self):
        alpha = 0
        while alpha < 1:
            alpha += 0.05
            self.attributes("-alpha", alpha)
            self.update()
            time.sleep(0.05)


# ... (rest of your code)
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to open the vault
def open_vault():
    subprocess.run(["python", "vault.py"])
def open_ai_calc():
    subprocess.run(["python", "ai_calculator.py"])


# Password-related functions
password = "1234"
passw='00'

def set_password():
    global password
    new_password = simpledialog.askstring("Set Password", "Enter new 4-digit password:", parent=app, show="*")
    if new_password and len(new_password) == 4 and new_password.isdigit():
        password = new_password
        messagebox.showinfo("Success", "Password has been set successfully!")
    else:
        messagebox.showerror("Error", "Password must be 4 digits.")

def change_password():
    global password
    old_password = simpledialog.askstring("Change Password", "Enter current password:", parent=app, show="*")
    if old_password == password:
        new_password = simpledialog.askstring("New Password", "Enter new 4-digit password:", parent=app, show="*")
        if new_password and len(new_password) == 4 and new_password.isdigit():
            password = new_password
            messagebox.showinfo("Success", "Password has been changed successfully!")
        else:
            messagebox.showerror("Error", "New password must be 4 digits.")
    else:
        messagebox.showerror("Error", "Old password is incorrect.")


def change_theme():
    theme = simpledialog.askinteger("Change Theme", "Enter 1 for Light Theme, 2 for Dark Theme:", parent=app)
    if theme == 1:
        app.configure(bg="#F0F0F0")
    elif theme == 2:
        app.configure(bg="#2D3142")
    else:
        messagebox.showerror("Error", "Invalid theme choice.")

def equalpress():
    global expression
    try:
        if expression == password:  # The code to access the media vault
            open_vault()
            clear()
        elif expression==passw:
            open_ai_calc()
            
            clear
        else:
            expression = expression.replace('x²', '**2')
            while '√' in expression:
                index = expression.index('√')
                end_index = index + 1
                while end_index < len(expression) and expression[end_index].isdigit():
                    end_index += 1
                number = float(expression[index + 1:end_index])
                expression = expression[:index] + str(math.sqrt(number)) + expression[end_index:]
            total = str(eval(expression))
            equation.set(total)
            add_to_history(f"{expression} = {total}")
            expression = total
    except Exception as e:
        equation.set("Error")
        expression = ""

# Function to clear the contents of text entry
def clear():
    global expression
    expression = ""
    equation.set("0")


# Function to delete one character from the end
def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression if expression else "0")

# Function to add a calculation to the history
def add_to_history(entry):
    history_list.insert(tk.END, entry)

# Function to handle keyboard input
def key_input(event):
    key = event.keysym
    if key.isdigit() or event.char in "+-*/().":
        press(event.char)
    elif key == 'Return':  # Enter key
        equalpress()
    elif key == 'Escape':  # Esc key
        clear()
    elif key == 'BackSpace':
        backspace()

# Function to show/hide history
def toggle_history():
    if history_frame.winfo_viewable():
        history_frame.grid_remove()
    else:
        history_frame.grid()

# Main GUI application
app = tk.Tk()
app.title("Arpit Personal Calculator")
app.geometry("700x600")
app.configure(bg="#F0F0F0")

expression = ""
equation = tk.StringVar()

entry_font = font.Font(size=24, weight='bold')
entry_field = tk.Entry(app, textvariable=equation, font=entry_font, bd=10, insertwidth=4, width=20, borderwidth=4, justify='right')
entry_field.grid(row=0, column=0, columnspan=4, pady=20)
equation.set("0")
button_font = font.Font(size=18, weight='bold')
# Menu button
menu_button = tk.Menubutton(app, text="⋮", font=button_font, bg="#A8DADC")
menu_button.grid(row=0, column=3, sticky="ne")

menu = tk.Menu(menu_button, tearoff=0)
menu.add_command(label="Set Password", command=set_password)
menu.add_command(label="Change Password", command=change_password)
menu.add_command(label="Change Theme", command=change_theme)
menu_button.config(menu=menu)

button_font = font.Font(size=18, weight='bold')

buttons = [
    ('x²', 1, 0), ('√', 1, 1), ('←', 1, 2), ('C', 1, 3),
    ('%', 2, 0), ('(', 2, 1), (')', 2, 2), ('+', 2, 3),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('-', 3, 3),
    ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('*', 4, 3),
    ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), ('/', 5, 3),
    ('00', 6, 0), ('0', 6, 1), ('.', 6, 2), ('=', 6, 3),
]

button_color = "#A8DADC"
for (text, row, col) in buttons:
    button = tk.Button(app, text=text, padx=20, pady=20, font=button_font, bg=button_color,
                       command=lambda t=text: press(t) if t not in ['=', 'C', '←'] else (equalpress() if t == '=' else (clear() if t == 'C' else backspace())))
    button.grid(row=row, column=col, sticky="nsew")

for i in range(7):
    app.grid_rowconfigure(i, weight=1)
    app.grid_columnconfigure(i, weight=1)

history_frame = tk.Frame(app, bg="#FFFFFF", relief=tk.RIDGE, bd=3, padx=5, pady=5)
history_frame.grid(row=0, column=5, rowspan=7, padx=(10, 0), sticky="nsew")

history_label = tk.Label(history_frame, text="History", font=button_font, bg="#FFFFFF", fg="#333333")
history_label.pack(pady=5)

history_list_frame = tk.Frame(history_frame, bg="#FFFFFF")
history_list_frame.pack(fill=tk.BOTH, expand=True)

history_scroll = tk.Scrollbar(history_list_frame, orient=tk.VERTICAL)
history_list = tk.Listbox(history_list_frame, width=30, height=20, font=("Arial", 12), yscrollcommand=history_scroll.set, bg="#F0F0F0", fg="#333333", selectbackground="#A8DADC", borderwidth=0)
history_scroll.config(command=history_list.yview)
history_scroll.pack(side=tk.RIGHT, fill=tk.Y)
history_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, pady=5, padx=5)

history_button = tk.Button(app, text="History", command=toggle_history, font=button_font, bg=button_color)
history_button.grid(row=7, column=5, pady=5, padx=10, sticky="ew")

app.bind('<Key>', key_input)

# Launch splash screen and then main calculator app
if __name__ == "__main__":
    app.withdraw()  # Hide main window initially

    # Show splash screen
    splash = SplashScreen(app)
    # After the splash screen is destroyed
    app.after(3000, lambda: (splash.destroy(), app.deiconify(), app.state('zoomed')))  # Destroy splash screen after 3 seconds

    # Initialize calculator app
    app.mainloop()
  