import tkinter as tk
from tkinter import ttk
from cryptography.fernet import Fernet

class TextCryptographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Text Cryptography App')
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 12))

        # Create a notebook for encryption and decryption tabs
        self.notebook = ttk.Notebook(root)
        self.encrypt_tab = ttk.Frame(self.notebook)
        self.decrypt_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.encrypt_tab, text='Encryption')
        self.notebook.add(self.decrypt_tab, text='Decryption')
        self.notebook.pack(fill='both', expand=True)

        # Create encryption tab
        self.create_encryption_tab()

        # Create decryption tab
        self.create_decryption_tab()

    def create_encryption_tab(self):
        # Encryption tab content
        self.label_input = ttk.Label(self.encrypt_tab, text="Enter your string:", font=('Arial', 12))
        self.label_input.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.input_text = ttk.Entry(self.encrypt_tab, width=40, font=('Arial', 12))
        self.input_text.grid(row=1, column=0, padx=10, pady=10)
        self.encrypt_button = ttk.Button(self.encrypt_tab, text="Encrypt", command=self.encrypt_text)
        self.encrypt_button.grid(row=2, column=0, padx=10, pady=10)
        self.encrypted_text = tk.Text(self.encrypt_tab, width=40, height=5, font=('Arial', 12))
        self.encrypted_text.grid(row=3, column=0, padx=10, pady=10)
        self.key_text = tk.Text(self.encrypt_tab, width=40, height=1, font=('Arial', 12))
        self.key_text.grid(row=4, column=0, padx=10, pady=10)
        self.key_text.config(state='disabled')

    def create_decryption_tab(self):
        # Decryption tab content
        self.label_key = ttk.Label(self.decrypt_tab, text="Enter the key:", font=('Arial', 12))
        self.label_key.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.key_text_decrypt = ttk.Entry(self.decrypt_tab, width=40, font=('Arial', 12))
        self.key_text_decrypt.grid(row=1, column=0, padx=10, pady=10)
        self.label_encrypted = ttk.Label(self.decrypt_tab, text="Enter the cipher text:", font=('Arial', 12))
        self.label_encrypted.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.encrypted_text_decrypt = ttk.Entry(self.decrypt_tab, width=40, font=('Arial', 12))
        self.encrypted_text_decrypt.grid(row=3, column=0, padx=10, pady=10)
        self.decrypt_button = ttk.Button(self.decrypt_tab, text="Decrypt", command=self.decrypt_text)
        self.decrypt_button.grid(row=4, column=0, padx=10, pady=10)
        self.decrypted_text = tk.Text(self.decrypt_tab, width=40, height=5, font=('Arial', 12))
        self.decrypted_text.grid(row=5, column=0, padx=10, pady=10)
        self.decrypted_text.config(state='disabled')

    def encrypt_text(self):
        input_text = self.input_text.get()

        if input_text:
            key = Fernet.generate_key()
            crypter = Fernet(key)
            input_bytes = input_text.encode('utf-8')
            encrypted_text = crypter.encrypt(input_bytes).decode('utf-8')

            self.encrypted_text.delete(1.0, tk.END)
            self.encrypted_text.insert(tk.END, encrypted_text)

            self.key_text.config(state='normal')
            self.key_text.delete(1.0, tk.END)
            self.key_text.insert(tk.END, key.decode('utf-8'))
            self.key_text.config(state='disabled')

    def decrypt_text(self):
        key = self.key_text_decrypt.get()
        encrypted_string = self.encrypted_text_decrypt.get()

        try:
            crypter = Fernet(key.encode())
            decrypted_bytes = crypter.decrypt(encrypted_string.encode('utf-8'))
            decrypted_text = decrypted_bytes.decode('utf-8')

            self.decrypted_text.config(state='normal')
            self.decrypted_text.delete(1.0, tk.END)
            self.decrypted_text.insert(tk.END, decrypted_text)
            self.decrypted_text.config(state='disabled')
        except Exception as e:
            self.decrypted_text.config(state='normal')
            self.decrypted_text.delete(1.0, tk.END)
            self.decrypted_text.insert(tk.END, "Error decrypting the string: " + str(e))
            self.decrypted_text.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = TextCryptographyApp(root)
    root.mainloop()
