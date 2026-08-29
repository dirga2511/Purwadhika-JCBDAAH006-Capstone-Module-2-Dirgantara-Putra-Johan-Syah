# Koperasi Kampung – Sistem Manajemen Inventori Gudang

Sistem manajemen inventori sederhana berbasis Python yang digunakan untuk mengelola data stok barang melalui operasi CRUD (Create, Read, Update, Delete).

## Gambaran Project

Project ini dibuat sebagai bagian dari **Capstone Project Module 2 – Job Connector Business & Data Analyst Purwadhika**.

Project ini mensimulasikan sistem sederhana untuk pengelolaan data inventori gudang. Pengguna dapat melihat, menambahkan, memperbarui, dan menghapus data barang melalui menu interaktif berbasis terminal.

Data barang mencakup beberapa informasi seperti ID Barang, Nama Barang, Kategori, Stok, Harga, dan Supplier.

Program menggunakan **List of Dictionary** sebagai struktur data utama untuk menyimpan informasi inventori.

##  Tujuan Project

Project ini bertujuan untuk:

- Membuat sistem sederhana untuk mengelola data inventori.
- Mengimplementasikan operasi CRUD menggunakan Python.
- Mempermudah proses pencarian dan pengelolaan data barang.
- Menerapkan validasi untuk mengurangi kesalahan input.
- Menerapkan konsep dasar Python dalam sebuah studi kasus bisnis.

##  Fitur Utama

### 1. Menampilkan Data Stok

Pengguna dapat:

- Menampilkan seluruh data inventori.
- Mencari data barang berdasarkan ID Barang.

### 2. Menambahkan Barang Baru

Pengguna dapat menambahkan barang baru dengan memasukkan:

- ID Barang
- Nama Barang
- Kategori
- Stok
- Harga
- Supplier

Program juga melakukan validasi terhadap ID Barang untuk mencegah adanya ID yang sama serta menyediakan konfirmasi sebelum data disimpan.

### 3. Memperbarui Data Barang

Pengguna dapat memperbarui data barang yang sudah tersedia berdasarkan ID Barang.

Program terlebih dahulu memastikan data barang ditemukan sebelum proses pembaruan dilakukan.

### 4. Menghapus Data Barang

Pengguna dapat menghapus data barang berdasarkan ID Barang.

Sebelum data dihapus, program menampilkan informasi barang dan meminta konfirmasi dari pengguna untuk mengurangi risiko penghapusan yang tidak disengaja.

### 5. Menu Utama

Seluruh fitur dapat diakses melalui menu utama sehingga pengguna dapat berpindah antarfitur tanpa harus menjalankan program kembali.

##  Struktur Data

Program menggunakan **List of Dictionary** sebagai struktur data utama.

List digunakan untuk menyimpan banyak data barang, sedangkan Dictionary digunakan untuk menyimpan informasi dari masing-masing barang dalam bentuk pasangan key-value.

Contoh struktur data:

```python
{
    "id_barang": "BRG001",
    "nama_barang": "Indomie Goreng",
    "kategori": "Makanan",
    "stok": 120,
    "harga": 3500,
    "supplier": "PT Indofood CBP Sukses Makmur"
}
