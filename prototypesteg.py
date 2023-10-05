import tkinter as tk
from tkinter import ttk
from cryptography.fernet import Fernet
from PIL import ImageTk, Image
from tkinter import messagebox
import os

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Text and Image Cryptography')
        self.root.geometry('500x600')
        self.root.configure(bg='#1877f2')
        self.root.resizable(width=False, height=False)
        self.initialize_ui()

    def initialize_ui(self):
        title_label = ttk.Label(self.root, text='Text and Image Cryptography', font=('Arial', 18, 'bold'), foreground='white', background='#1877f2')
        title_label.pack(pady=20)

        text_encryption_button = self.create_button(self.root, 'Text Encryption', self.open_text_encryption)
        text_decryption_button = self.create_button(self.root, 'Text Decryption', self.open_text_decryption)
        image_steganography_button = self.create_button(self.root, 'Image Steganography', self.open_image_steganography)

        text_encryption_button.pack(pady=10)
        text_decryption_button.pack(pady=10)
        image_steganography_button.pack(pady=10)

    def create_button(self, parent, text, command):
        button = ttk.Button(parent, text=text, command=command, style="Rounded.TButton")
        return button

    def open_text_encryption(self):
        text_encryption_window = tk.Toplevel(self.root)
        text_encryption_window.title('Text Encryption')
        text_encryption_window.geometry('400x400')
        text_encryption_window.configure(bg='#1877f2')
        TextEncryptionApp(text_encryption_window)

    def open_text_decryption(self):
        text_decryption_window = tk.Toplevel(self.root)
        text_decryption_window.title('Text Decryption')
        text_decryption_window.geometry('400x400')
        text_decryption_window.configure(bg='#1877f2')
        TextDecryptionApp(text_decryption_window)

    def open_image_steganography(self):
        image_steganography_window = tk.Toplevel(self.root)
        image_steganography_window.title('Image Steganography')
        image_steganography_window.geometry('600x600')
        image_steganography_window.configure(bg='#1877f2')
        SteganographyApp(image_steganography_window)

class TextEncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Text Encryption')
        self.style = ttk.Style()
        self.style.configure("Rounded.TButton", relief="flat", background="#1877f2", foreground="white", font=('Arial', 12))
        self.initialize_ui()

    def initialize_ui(self):
        # Add your Text Encryption GUI here

class TextDecryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Text Decryption')
        self.style = ttk.Style()
        self.style.configure("Rounded.TButton", relief="flat", background="#1877f2", foreground="white", font=('Arial', 12))
        self.initialize_ui()

    def initialize_ui(self):
        # Add your Text Decryption GUI here

class SteganographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Image Steganography')
        self.style = ttk.Style()
        self.style.configure("Rounded.TButton", relief="flat", background="#1877f2", foreground="white", font=('Arial', 12))
        self.initialize_ui()

    def initialize_ui(self):
        # Add your Image Steganography GUI here

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
