import tkinter as tk
from tkinter import ttk, messagebox
from team import Team


class HockeyGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hockey Team Management System")

        self.teams = []

        # ---------- Form ----------
        form_frame = tk.Frame(root)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Team Name:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(form_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Team Type:").grid(row=1, column=0, padx=5, pady=5)
        self.team_type_var = tk.StringVar(value="boys")
        team_type_menu = ttk.Combobox(
            form_frame,
            textvariable=self.team_type_var,
            values=["boys", "girls"],
            state="readonly"
        )
        team_type_menu.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Fee Paid:").grid(row=2, column=0, padx=5, pady=5)
        self.fee_paid_var = tk.StringVar(value="yes")
        fee_paid_menu = ttk.Combobox(
            form_frame,
            textvariable=self.fee_paid_var,
            values=["yes", "no"],
            state="readonly"
        )
        fee_paid_menu.grid(row=2, column=1, padx=5, pady=5)

        # ---------- Buttons ----------
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        add_button = tk.Button(button_frame, text="Register Team", command=self.add_team)
        add_button.grid(row=0, column=0, padx=5)

        delete_button = tk.Button(button_frame, text="Delete Team", command=self.delete_team)
        delete_button.grid(row=0, column=1, padx=5)

        stats_button = tk.Button(button_frame, text="Show Statistics", command=self.show_stats)
        stats_button.grid(row=0, column=2, padx=5)

        # ---------- Table ----------
        self.tree = ttk.Treeview(
            root,
            columns=("ID", "Name", "Type", "Fee Paid"),
            show="headings"
        )
        self.tree.pack(pady=10)

        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Type", text="Type")
        self.tree.heading("Fee Paid", text="Fee Paid")

    # ---------- Add Team ----------
    def add_team(self):
        name = self.name_entry.get().strip()
        team_type = self.team_type_var.get()
        fee_paid = self.fee_paid_var.get() == "yes"

        if not name:
            messagebox.showerror("Input Error", "Team name cannot be empty")
            return

        team = Team(name, team_type, fee_paid)
        self.teams.append(team)

        self.tree.insert(
            "",
            "end",
            values=(team.id, team.name, team.team_type, team.fee_paid)
        )

        # Clear form after adding
        self.name_entry.delete(0, tk.END)

    # ---------- Delete Team ----------
    def delete_team(self):
        selected = self.tree.selection()

        if not selected:
            messagebox.showwarning("Selection Error", "Please select a team to delete")
            return

        for item in selected:
            self.tree.delete(item)

    # ---------- Statistics ----------
    def show_stats(self):
        total = len(self.teams)
        boys = sum(1 for t in self.teams if t.team_type == "boys")
        girls = sum(1 for t in self.teams if t.team_type == "girls")

        stats_text = (
            f"Total teams: {total}\n"
            f"Boys teams: {boys}\n"
            f"Girls teams: {girls}"
        )

        messagebox.showinfo("Team Statistics", stats_text)


# ---------- Run Program ----------
if __name__ == "__main__":
    root = tk.Tk()
    app = HockeyGUI(root)
    root.mainloop()
