"""
Nama: Rayhan Abi Saputra Rambe
NIM: 12550112686
Matkul: Pemrograman Berbasis Objek
"""
# ini kelas untuk bukunya 
class Buku:
    # ini fungsi untuk bukunya        # ini fungsi untuk bukunya             
    def __init__(self, judul, penulis, status="Tersedia"):       #(__init__) Untuk menyiapkan data awal (atribut) pada objek.
        self.judul = judul
        self.penulis = penulis
        self.status = status 


     # ini fungsi untuk bukunya       
    def __str__(self):                       #(__str__) Mengembalikan string yang mudah dibaca manusia agar kita tahu isi dari objek tersebut.
        return f"{self.judul} - {self.penulis} ({self.status})"



#ini kelas untuk perpustakaannya
class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)

    def tampilkan_buku(self):
        print("\n--- DAFTAR BUKU ---")
        if not self.daftar_buku:
            print("Koleksi masih kosong.")
        for i, buku in enumerate(self.daftar_buku, start=1):
            print(f"{i}. {buku}")

    def cari_buku(self, judul):
        for buku in self.daftar_buku:
            if buku.judul.lower() == judul.lower():
                return buku
        return None

# pusat kodenya (ini yang ditampilkan pada user)
def main():
    perpus = Perpustakaan()
    
    # Data Awal untuk buku (contoh aja)
    perpus.tambah_buku(Buku("Rahasia Algoritma", "Budi Santoso"))
    perpus.tambah_buku(Buku("Senja di Kota Tua", "Citra Lestari"))
    perpus.tambah_buku(Buku("Rahasia Tuhan", "Ardi Situmorang"))
    perpus.tambah_buku(Buku("Dalam Dunia", "Fiska Arni"))

    # while di gunakan untuk menyatakan kebenaran (agar kalimat ini selalu di cetak)
    while True:
        print("\n=== MENU PERPUSTAKAAN ===")
        print("1. Lihat Buku\n2. Tambah Buku\n3. Pinjam Buku\n4. Kembalikan\n5. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            perpus.tampilkan_buku()

        elif pilihan == "2":
            j = input("Judul: ")
            p = input("Penulis: ")
            perpus.tambah_buku(Buku(j, p))
            print("Berhasil ditambah!")

        elif pilihan == "3":
            judul = input("Judul yang dipinjam: ")
            buku = perpus.cari_buku(judul)
            if buku and buku.status == "Tersedia":
                buku.status = "Dipinjam"
                print("Berhasil dipinjam!")
            else:
                print("Buku tidak tersedia atau tidak ditemukan.")

        elif pilihan == "4":
            judul = input("Judul yang dikembalikan: ")
            buku = perpus.cari_buku(judul)
            if buku and buku.status == "Dipinjam":
                buku.status = "Tersedia"
                print("Berhasil dikembalikan!")
            else:
                print("Data tidak cocok.")

        elif pilihan == "5":
            print("Sampai jumpa!")
            break

if __name__ == "__main__":
    main()
    # __name__ adalah variabel bawaan Python.
    #  ini Titik awal program dijalankan 