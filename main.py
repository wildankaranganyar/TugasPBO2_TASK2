
from infrastructure.database import Database
from infrastructure.student_repository import StudentRepository

from usecases.student_usecase import StudentUseCase

from presentation.views.student_view import StudentView
from presentation.controllers.student_controller import StudentController


def main():
    # Konfigurasi Laragon 6
    db = Database(
        host="127.0.0.1",
        user="root",
        password="",
        database="db_kampus",
        port=3306  # Ganti jika port MySQL Laragon berbeda
    )

    # Dependency Injection
    repository = StudentRepository(db)
    usecase = StudentUseCase(repository)
    view = StudentView()
    controller = StudentController(usecase, view)

    # Memuat data awal
    controller.load_students()

    # Menjalankan GUI
    view.mainloop()


if __name__ == "__main__":
    main()
