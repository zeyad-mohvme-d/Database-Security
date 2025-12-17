import tkinter as tk
from models.session import Session

class AdminView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Admin Dashboard")

    def run(self):
        tk.Label(
            self.root,
            text=f"Admin Panel - {Session.username}"
        ).pack(pady=20)

        self.root.mainloop()
