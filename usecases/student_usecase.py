
from domain.entities import Mahasiswa


class StudentUseCase:
    def __init__(self, repository):
        self.repository = repository

    def list_students(self):
        return self.repository.get_all()

    def create_student(
        self,
        nim,
        nama,
        prodi,
        angkatan
    ):
        self._validate(
            nim, nama, prodi, angkatan
        )

        if self.repository.get_by_nim(nim):
            raise ValueError(
                "NIM sudah terdaftar!"
            )

        mhs = Mahasiswa(
            nim=nim,
            nama=nama,
            prodi=prodi,
            angkatan=angkatan
        )

        return self.repository.add(mhs)

    def update_student(
        self,
        nim,
        nama,
        prodi,
        angkatan
    ):
        self._validate(
            nim, nama, prodi, angkatan
        )

        if not self.repository.get_by_nim(nim):
            raise ValueError(
                "Data mahasiswa tidak ditemukan!"
            )

        mhs = Mahasiswa(
            nim=nim,
            nama=nama,
            prodi=prodi,
            angkatan=angkatan
        )

        return self.repository.update(mhs)

    def delete_student(self, nim):
        nim = nim.strip()

        if not nim:
            raise ValueError(
                "NIM tidak boleh kosong!"
            )

        if not self.repository.get_by_nim(nim):
            raise ValueError(
                "Data mahasiswa tidak ditemukan!"
            )

        return self.repository.delete(nim)

    def _validate(
        self,
        nim,
        nama,
        prodi,
        angkatan
    ):
        nim = nim.strip()
        nama = nama.strip()
        prodi = prodi.strip()

        if not nim or not nama or not prodi:
            raise ValueError(
                "Semua field wajib diisi!"
            )

        try:
            angkatan = int(angkatan)
        except (ValueError, TypeError):
            raise ValueError(
                "Angkatan harus berupa angka!"
            )

        if angkatan < 1900 or angkatan > 2100:
            raise ValueError(
                "Tahun angkatan tidak valid!"
            )

        if len(nim) > 20:
            raise ValueError(
                "NIM maksimal 20 karakter!"
            )

        if len(nama) > 100:
            raise ValueError(
                "Nama maksimal 100 karakter!"
            )

        if len(prodi) > 100:
            raise ValueError(
                "Prodi maksimal 100 karakter!"
            )
