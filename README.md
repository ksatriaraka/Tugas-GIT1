# Tugas-GIT1
Tugas Git mengupload tugas Python 5: OOP pada respository

# Python1.py (TASK 1)

Pada file Pyhton1.py akan dibuat class MarketingDataETL yang memiliki tiga metode:
1. extract(): akan membaca data dari sebuah file CSV (Misalkan, marketing_data.csv)
2. transform(): akan melakukan pembersihan dan transformasi sederhana pada data (seperti mengubah format tanggal atau membersihkan nilai yang kosong)
3. store(): akan menyimpan data yang telah ditransformasi ke dalam struktur data DataFramet.

## PENJELASAN CODING

Kode yang disediakan mengimplementasikan proses ETL (Extract, Transform, Load) untuk dataset pemasaran yang disimpan dalam file CSV - marketing_data.csv.

1. Langkah pertama adalah mengimpor modul-modul yang diperlukan : pandas adalah pustaka untuk manipulasi dan analisis data, sedangkan google.colab (juga dikenal sebagai colab) menyediakan akses ke Google Drive, sehingga kita dapat membaca dan menulis file di Drive.
2. Untuk terhubung dengan Google Drive: Baris kode harus memasang Google Drive pengguna sebagai sistem file lokal.
3. Kelas MarketingDataETL kemudian didefinisikan, yang bertanggung jawab untuk operasi ETL: Metode init menginisialisasi instance kelas dan menetapkan dua variabel instance: file_path: jalur file dari marketing_data.csv data: NULL
4. Metode pertama, extract(self): mengambil file marketing_data.csv dan menyimpannya dalam variabel data instance
5. Metode clean(self): menghapus nilai yang hilang dari DataFrame
6. Metode transform(self): mengubah kolom tanggal_pembelian menjadi objek datetime pandas
7. Terakhir, store(self, output): menulis DataFrame yang telah ditransformasi ke file CSV baru di Google Drive
lalu Kode akan memproses file marketing_data.csv dengan menghapus nilai yang hilang, mentransformasi kolom tanggal_pembelian, dan menyimpan hasil pemrosesan ke transformed_marketing_data_finish.csv.

# Python2.py (TASK 2)

Pada file Python2.py akan menggunakan metode Inheritance dan Polymorphism sesuai perintah berikut :
1. Gunakan inheritance untuk membuat class TargetedMarketingETL yang mewarisi dari MarketingDataETL
2. Tambahkan metode segment_customers() yang mengelompokkan pelanggan berdasarkan kriteria tertentu (misalnya, pengeluaran total atau kategori produk yang dibeli)
3. Demonstrasi polymorphism dengan meng-override metode transform() dalam TargetedMarketingETL untuk menambahkan logika segmentasi pelanggan ke dalam proses transformasi

## PENJELASAN CODING
Kode ini mendemonstrasikan proses ETL (Extract, Transform, Load) untuk data pemasaran yang ditargetkan dengan bantuan kelas Python.

Kode ini mencakup 2 kelas, MarketingDataETL dan TargetedMarketingETL, di mana TargetedMarketingETL mewarisi MarketingDataETL.
1. MarketingDataETL:
init : Menginisialisasi file_path dan variabel data
extract: Mengekstrak data CSV dari file yang diberikan
transform: Mengubah kolom "tanggal_pembelian" menjadi format datetime

2. Target PemasaranETL:
init : Menginisialisasi file_path dengan memanggil konstruktor induk
extract: Menimpa metode ekstrak induk untuk mengembalikan set data tetap untuk contoh ini
segment_customers: Mensegmentasi pelanggan berdasarkan total_pembelian dan kategori_produk mereka
total_pembelian: Mengembalikan total pembelian (jumlah) dari dataset

3. Sisa kode:
Pertama, kita memasang Google Drive menggunakan google.colab.drive.mount('/content/drive')
Kita membuat instance dari kelas TargetedMarketingETL, Ekstrak data menggunakan etl_process.extract(), panggil etl_process.segment_customers() untuk mensegmentasi pelanggan, lalu Tampilkan Total Pembelian dengan memanggil etl_process.total_pembelian()
