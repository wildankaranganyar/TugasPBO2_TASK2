
class StudentController:
    def __init__(self, usecase, view):
        self.usecase = usecase
        self.view = view
        self.view.set_controller(self)

    def load_students(self):
        try:
            students = self.usecase.list_students()
            self.view.display_students(students)

        except Exception as e:
            self.view.show_error("Database Error", str(e))

    def add_student(self):
        try:
            nim, nama, prodi, angkatan = self.view.get_inputs()

            success = self.usecase.create_student(
                nim, nama, prodi, angkatan
            )

            if success:
                self.view.show_info(
                    "Sukses",
                    "Data mahasiswa berhasil ditambahkan!"
                )
                self.view.clear_inputs()
                self.load_students()

        except Exception as e:
            self.view.show_error("Error", str(e))

    def update_student(self):
        try:
            nim, nama, prodi, angkatan = self.view.get_inputs()

            success = self.usecase.update_student(
                nim, nama, prodi, angkatan
            )

            if success:
                self.view.show_info(
                    "Sukses",
                    "Data mahasiswa berhasil diperbarui!"
                )
                self.view.clear_inputs()
                self.load_students()

        except Exception as e:
            self.view.show_error("Error", str(e))

    def delete_student(self):
        try:
            nim, _, _, _ = self.view.get_inputs()

            if not nim:
                raise ValueError(
                    "Pilih mahasiswa yang akan dihapus!"
                )

            confirmation = self.view.ask_confirmation(
                "Konfirmasi",
                f"Yakin ingin menghapus mahasiswa {nim}?"
            )

            if not confirmation:
                return

            success = self.usecase.delete_student(nim)

            if success:
                self.view.show_info(
                    "Sukses",
                    "Data mahasiswa berhasil dihapus!"
                )
                self.view.clear_inputs()
                self.load_students()

        except Exception as e:
            self.view.show_error("Error", str(e))
