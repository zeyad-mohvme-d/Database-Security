import tkinter as tk
from models.session import Session

class InstructorView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Instructor Dashboard")

    def run(self):
        tk.Label(
            self.root,
            text=f"Instructor Panel - {Session.username}"
        ).pack(pady=20)

        self.root.mainloop()
