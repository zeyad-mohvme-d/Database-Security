import tkinter as tk
from models.session import Session

class GuestView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Guest Dashboard")

    def run(self):
        tk.Label(
            self.root,
            text=f"Guest Panel - {Session.username}"
        ).pack(pady=20)

        self.root.mainloop()
