import tkinter as tk
from tkinter import messagebox
from auth.login import validate_login
from models.session import Session

class LoginView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SRMS Login")
        self.root.geometry("300x200")

    def run(self):
        tk.Label(self.root, text="Username").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        tk.Label(self.root, text="Password").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        tk.Button(self.root, text="Login", command=self.login).pack(pady=10)

        self.root.mainloop()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            row = validate_login(username, password)
            if row:
                Session.username = row.Username
                Session.role = row.RoleName
                Session.clearance = row.ClearanceLevel

                messagebox.showinfo(
                    "Success",
                    f"Welcome {Session.role}"
                )

                self.root.destroy()
                self.open_dashboard()

        except Exception as e:
            messagebox.showerror("Login Failed", str(e))

    def open_dashboard(self):
        if Session.role == "Admin":
            from gui.admin_view import AdminView
            AdminView().run()
        elif Session.role == "Instructor":
            from gui.instructor_view import InstructorView
            InstructorView().run()
        elif Session.role == "TA":
            from gui.ta_view import TAView
            TAView().run()
        elif Session.role == "Student":
            from gui.student_view import StudentView
            StudentView().run()
        else:
            from gui.guest_view import GuestView
            GuestView().run()
