import tkinter as tk
from models.session import Session

class TAView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("TA Dashboard")

    def run(self):
        tk.Label(
            self.root,
            text=f"TA Panel - {Session.username}"
        ).pack(pady=20)

        self.root.mainloop()
