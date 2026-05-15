# File: item.py
from datetime import date, timedelta

class Item:
    def __init__(self, kode, nama, harga_satuan, jumlah_stok):
        self.kode = kode
        self.nama = nama
        self.harga_satuan = harga_satuan
        self.jumlah_stok = jumlah_stok

    def hitung_nilai_stok(self):
        return self.harga_satuan * self.jumlah_stok

    def tampilkan_info(self):
        return f"[{self.kode}] {self.nama} - Stok: {self.jumlah_stok} | Nilai: Rp{self.hitung_nilai_stok():,}"

class FoodItem(Item):
    def __init__(self, kode, nama, harga_satuan, jumlah_stok, tanggal_kadaluwarsa, suhu_penyimpanan):
        super().__init__(kode, nama, harga_satuan, jumlah_stok)
        self.tanggal_kadaluwarsa = tanggal_kadaluwarsa  # objek date
        self.suhu_penyimpanan = suhu_penyimpanan

    def cek_kadaluwarsa(self):
        selisih_hari = (self.tanggal_kadaluwarsa - date.today()).days
        return selisih_hari

    def hitung_nilai_stok(self):
        nilai = super().hitung_nilai_stok()
        if self.cek_kadaluwarsa() < 7:
            nilai *= 0.9  # diskon 10% karena mendekati kadaluwarsa
        return nilai

class ElectronicItem(Item):
    def __init__(self, kode, nama, harga_satuan, jumlah_stok, daya_watt, masa_garansi_bulan):
        super().__init__(kode, nama, harga_satuan, jumlah_stok)
        self.daya_watt = daya_watt
        self.masa_garansi_bulan = masa_garansi_bulan

    def hitung_nilai_stok(self):
        nilai = super().hitung_nilai_stok()
        nilai += nilai * 0.05  # tambahan biaya garansi 5%
        return nilai

class ClothingItem(Item):
    def __init__(self, kode, nama, harga_satuan, jumlah_stok, ukuran, bahan):
        super().__init__(kode, nama, harga_satuan, jumlah_stok)
        self.ukuran = ukuran
        self.bahan = bahan

    def tampilkan_info(self):
        info_dasar = super().tampilkan_info()
        return f"{info_dasar} | Ukuran: {self.ukuran} | Bahan: {self.bahan}"

# Contoh penggunaan dan subtyping
def cetak_detail_item(item: Item):
    print(item.tampilkan_info())

if __name__ == "__main__":
    makanan = FoodItem("F001", "Susu UHT", 15000, 100, date.today() + timedelta(days=5), "Dingin")
    elektronik = ElectronicItem("E001", "Kipas Angin", 200000, 20, 45, 12)
    pakaian = ClothingItem("C001", "Kemeja Polos", 120000, 50, "L", "Katun")

    cetak_detail_item(makanan)
    cetak_detail_item(elektronik)
    cetak_detail_item(pakaian)

    print(f"\nNilai stok makanan setelah diskon: Rp{makanan.hitung_nilai_stok():,}")