import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Animasi Chat App")
        self.root.geometry("500x600")

        # Styling utama
        self.root.configure(bg="#f0f0f0")
        self.root.resizable(True, True)

        # Frame untuk menampilkan pesan
        self.chat_frame = ttk.Frame(self.root, padding=(10, 10))
        self.chat_frame.pack(fill=tk.BOTH, expand=True)

        # Scrollable chat area
        self.scrollable_area = ScrolledText(
            self.chat_frame, wrap=tk.WORD, state="disabled", bg="#ffffff", font=("Arial", 10)
        )
        self.scrollable_area.pack(fill=tk.BOTH, expand=True)

        # Entry dan tombol untuk mengirim pesan
        self.input_frame = ttk.Frame(self.root, padding=(10, 10))
        self.input_frame.pack(fill=tk.X, side=tk.BOTTOM)

        self.message_entry = ttk.Entry(self.input_frame, font=("Arial", 12))
        self.message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.message_entry.bind("<Return>", self.send_message)

        self.send_button = ttk.Button(
            self.input_frame, text="Send", command=self.send_message
        )
        self.send_button.pack(side=tk.RIGHT)

        # Menambahkan fitur wrapping
        self.wrap_var = tk.BooleanVar(value=True)
        self.wrap_checkbox = ttk.Checkbutton(
            self.input_frame, text="Wrap Text", variable=self.wrap_var, command=self.toggle_wrap
        )
        self.wrap_checkbox.pack(side=tk.RIGHT, padx=(0, 10))

    def send_message(self, event=None):
        message = self.message_entry.get().strip()
        if message:
            self.display_message("You", message)  # Menampilkan pesan pengirim
            self.message_entry.delete(0, tk.END)

            # Simulasi pengiriman pesan ke API
            self.send_to_api(message)

    def display_message(self, sender, message):
        self.scrollable_area.configure(state="normal")
        self.scrollable_area.insert(tk.END, f"{sender}: {message}\n")
        self.scrollable_area.yview(tk.END)  # Scroll otomatis ke pesan terbaru
        self.scrollable_area.configure(state="disabled")

    def send_to_api(self, message):
        # Simulasi pengiriman data ke API
        print(f"Sending message to API: {message}")
        # Bisa ditambahkan logic request ke API di sini

    def toggle_wrap(self):
        wrap_type = tk.WORD if self.wrap_var.get() else tk.CHAR
        self.scrollable_area.configure(wrap=wrap_type)

# Dibuat oleh : Hafizh H Asyhari hafizhhasyhari
if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()
