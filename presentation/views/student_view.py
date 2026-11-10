
import tkinter as tk
from tkinter import ttk, messagebox


class StudentView(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Sistem Informasi Data Mahasiswa")
        self.geometry("850x550")
        self.minsize(750, 450)

        self.controller = None

        self._build_ui()

    def set_controller(self, controller):
        self.controller = controller

    def _build_ui(self):
        title = ttk.Label(
            self,
            text="DATA MAHASISWA",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=15)

        ttk.Label(
            self,
            text="Aplikasi CRUD Python - Tkinter & MySQL"
        ).pack(pady=3)

        form = ttk.LabelFrame(
            self,
            text=" Form Data Mahasiswa ",
            padding=15
        )
        form.pack(fill="x", padx=15, pady=10)

        ttk.Label(form, text="NIM:").grid(
            row=0, column=0, sticky="w", pady=5
        )

        self.ent_nim = ttk.Entry(form, width=30)
        self.ent_nim.grid(row=0, column=1, padx=10)

        ttk.Label(form, text="Nama:").grid(
            row=0, column=2, sticky="w"
        )

        self.ent_nama = ttk.Entry(form, width=35)
        self.ent_nama.grid(row=0, column=3, padx=10)

        ttk.Label(form, text="Program Studi:").grid(
            row=1, column=0, sticky="w", pady=5
        )

        self.ent_prodi = ttk.Entry(form, width=30)
        self.ent_prodi.grid(row=1, column=1, padx=10)

        ttk.Label(form, text="Angkatan:").grid(
            row=1, column=2, sticky="w"
        )

        self.ent_angkatan = ttk.Entry(form, width=15)
        self.ent_angkatan.grid(
            row=1, column=3, padx=10, sticky="w"
        )

        buttons = ttk.Frame(self)
        buttons.pack(fill="x", padx=15, pady=5)

        ttk.Button(
            buttons,
            text="Tambah",
            command=self._add
        ).pack(side="left", padx=5)

        ttk.Button(
            buttons,
            text="Update",
            command=self._update
        ).pack(side="left", padx=5)

        ttk.Button(
            buttons,
            text="Hapus",
            command=self._delete
        ).pack(side="left", padx=5)

        ttk.Button(
            buttons,
            text="Reset",
            command=self.clear_inputs
        ).pack(side="left", padx=5)

        ttk.Button(
            buttons,
            text="Refresh",
            command=self._refresh
        ).pack(side="left", padx=5)

        table_frame = ttk.LabelFrame(
            self,
            text=" Daftar Mahasiswa ",
            padding=10
        )
        table_frame.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )

        columns = ("nim", "nama", "prodi", "angkatan")

        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        headings = {
            "nim": "NIM",
            "nama": "Nama Mahasiswa",
            "prodi": "Program Studi",
            "angkatan": "Angkatan"
        }

        for col, heading in headings.items():
            self.tree.heading(col, text=heading)

        self.tree.column("nim", width=120)
        self.tree.column("nama", width=220)
        self.tree.column("prodi", width=200)
        self.tree.column("angkatan", width=100, anchor="center")

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.tree.yview
        )

        self.tree.configure(
            yscrollcommand=scrollbar.set
        )

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.tree.bind(
            "<<TreeviewSelect>>",
            self._on_row_select
        )

    def get_inputs(self):
        return (
            self.ent_nim.get().strip(),
            self.ent_nama.get().strip(),
            self.ent_prodi.get().strip(),
            self.ent_angkatan.get().strip()
        )

    def set_inputs(self, nim, nama, prodi, angkatan):
        fields = (
            self.ent_nim,
            self.ent_nama,
            self.ent_prodi,
            self.ent_angkatan
        )

        values = (nim, nama, prodi, angkatan)

        for field, value in zip(fields, values):
            field.delete(0, tk.END)
            field.insert(0, str(value))

    def clear_inputs(self):
        self.set_inputs("", "", "", "")
        self.ent_nim.focus_set()

    def display_students(self, students):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for mhs in students:
            self.tree.insert(
                "",
                tk.END,
                values=(
                    mhs.nim,
                    mhs.nama,
                    mhs.prodi,
                    mhs.angkatan
                )
            )

    def _on_row_select(self, event):
        selected = self.tree.focus()

        if selected:
            values = self.tree.item(selected, "values")

            if values:
                self.set_inputs(*values)

    def _add(self):
        self.controller.add_student()

    def _update(self):
        self.controller.update_student()

    def _delete(self):
        self.controller.delete_student()

    def _refresh(self):
        self.controller.load_students()

    def show_info(self, title, message):
        messagebox.showinfo(title, message)

    def show_error(self, title, message):
        messagebox.showerror(title, message)

    def ask_confirmation(self, title, message):
        return messagebox.askyesno(title, message)
