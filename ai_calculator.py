import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import pytesseract
import re
import numpy as np
import pdfplumber  # For PDF text extraction
import pandas as pd

# Tesseract executable path (update based on your installation)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Function to extract text from image using OCR
def extract_text_from_image(image_path):
    try:
        # Open the image using Pillow
        img = Image.open(image_path)
        # Use pytesseract to extract text
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        messagebox.showerror("Error", f"Error in OCR processing: {e}")
        return None

# Function to extract text from PDF using pdfplumber
def extract_text_from_pdf(pdf_path):
    try:
        text = ""
        # Open the PDF file using pdfplumber
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text()  # Extract text from each page
        return text
    except Exception as e:
        messagebox.showerror("Error", f"Error in PDF processing: {e}")
        return None

# Function to process CSV and extract numbers for calculations
def extract_numbers_from_csv(csv_path):
    try:
        df = pd.read_csv(csv_path)
        # Flatten the DataFrame to extract all numbers
        numbers = df.values.flatten()
        # Filter out any non-numeric values
        return [float(num) for num in numbers if isinstance(num, (int, float))]
    except Exception as e:
        messagebox.showerror("Error", f"Error in CSV processing: {e}")
        return None

# Function to perform the appropriate calculation based on the selected operation
def auto_calculate(numbers, operation):
    try:
        if not numbers:
            return "No numbers detected in the file."

        # Perform the calculation based on the detected operation
        if operation == "Addition":
            result = sum(numbers)
        elif operation == "Subtraction":
            result = numbers[0] - sum(numbers[1:])
        elif operation == "Multiplication":
            result = np.prod(numbers)
        elif operation == "Division":
            if len(numbers) == 2 and numbers[1] != 0:
                result = numbers[0] / numbers[1]
            else:
                result = "Division Error"
        else:
            result = "Invalid Operation"
        return result
    except Exception as e:
        return f"Error in processing: {e}"

# Function to handle file upload and start processing
def upload_file():
    file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png"), 
                                                                           ("PDF Files", "*.pdf"), 
                                                                           ("CSV Files", "*.csv")])
    if file_path:
        file_extension = file_path.split('.')[-1].lower()

        # Extract text from different file types
        extracted_text = ""
        numbers = []

        if file_extension in ['jpg', 'jpeg', 'png']:
            extracted_text = extract_text_from_image(file_path)
            numbers = [float(num) for num in re.findall(r'\d+\.?\d*', extracted_text)]
        elif file_extension == 'pdf':
            extracted_text = extract_text_from_pdf(file_path)
            numbers = [float(num) for num in re.findall(r'\d+\.?\d*', extracted_text)]
        elif file_extension == 'csv':
            numbers = extract_numbers_from_csv(file_path)
            extracted_text = f"Numbers from CSV: {numbers}"  # Show extracted numbers for reference

        if numbers:
            cleaned_text.set(extracted_text)
            result = auto_calculate(numbers, operation_menu.get())
            result_label.config(text=f"Result: {result}")
        else:
            cleaned_text.set("No numbers found in the file.")

# Setting up the GUI using Tkinter
root = tk.Tk()
root.title("Arpit Calculator - Auto Solve")

# Set window size
root.geometry("1000x800")  # Increased window size
root.config(bg="lightblue")

# Add a background image
background_image = Image.open("360_F_167235520_AFrB955JhCwhkpz1ev2L7X9SBcpVgAyg.jpg")  # Replace with your image path
background_image = background_image.resize((1500, 800), Image.Resampling.LANCZOS)  # Use LANCZOS resampling
bg = ImageTk.PhotoImage(background_image)

# Use a Label widget to display the background image
bg_label = tk.Label(root, image=bg)
bg_label.place(relwidth=1, relheight=1)  # This will fill the entire window

# Title Label (3D Effect)
title_label = tk.Label(root, text="CHUTIYA CALCULATOR", font=("Arial", 20, 'bold'), fg="#FFFFFF", bg="#5D9B9B", relief="raised", padx=20, pady=15)
title_label.pack(pady=30)

# Upload Button (with 3D effect)
upload_button = tk.Button(root, text="Upload File", font=("Arial", 14, 'bold'), command=upload_file, relief="raised", bg="#4CAF50", fg="white", width=20, height=2)
upload_button.pack(pady=30)

# Operation selection menu
operation_menu = ttk.Combobox(root, values=["Addition", "Subtraction", "Multiplication", "Division"], font=("Arial", 14))
operation_menu.set("Addition")  # Default operation
operation_menu.pack(pady=20)

# Label for showing cleaned text from image
cleaned_text = tk.StringVar()
text_label = tk.Label(root, textvariable=cleaned_text, font=("Arial", 12), wraplength=800, justify="left", bg="lightblue", fg="black", height=5)
text_label.pack(pady=30)

# Label to display result
result_label = tk.Label(root, text="Result: ", font=("Arial", 20), fg="blue", bg="lightblue", height=4)
result_label.pack(pady=40)

# Run the Tkinter event loop
root.mainloop()
