import tkinter as tk
from models.session import Session

class StudentView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Student Dashboard")

    def run(self):
        tk.Label(
            self.root,
            text=f"Student Panel - {Session.username}"
        ).pack(pady=20)

        self.root.mainloop()
