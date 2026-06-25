
🚀 Dokumentasi API Endpoints
⚙️ Panduan Instalasi & Setup LokalIkuti langkah-langkah berikut untuk menjalankan proyek ini di komputer lokal kamu:
1. Clone RepositoryBashgit clone [https://github.com/USERNAME_GITHUB_KAMU/NAMA_REPOSITORY_KAMU.git](https://github.com/USERNAME_GITHUB_KAMU/NAMA_REPOSITORY_KAMU.git)
cd ecommerce_backend
2. Aktifkan Virtual Environment (Venv)Bash# Untuk Windows
python -m venv env
.\env\Scripts\activate

# Untuk macOS/Linux
python3 -m venv env
source env/bin/activate
3. Install DependenciesPastikan Django dan Django REST Framework sudah terinstall di dalam virtual environment kamu:Bashpip install django djangorestframework
4. Jalankan Migrasi DatabaseJalankan perintah migrasi untuk membentuk tabel-tabel relasional di database local:Bashpython manage.py makemigrations
python manage.py migrate
5. Buat Akun Superuser (Admin)Untuk masuk ke panel admin dan mengelola produk sampel, buat akun administrator baru:Bashpython manage.py createsuperuser
Ikuti petunjuk di terminal untuk mengisi Username dan Password kamu.6. Jalankan Server LokalBashpython manage.py runserver
Server akan aktif dan berjalan di alamat http://127.0.0.1:8000/.📊 
Cara Menguji AplikasiIsi Data Produk: Buka http://127.0.0.1:8000/admin, login dengan akun superuser, masuk ke menu Products, lalu tambahkan beberapa produk sampel (isi nama, harga, dan stok).
Cek JSON Produk: Buka http://127.0.0.1:8000/api/products/ di browser untuk melihat data produk yang sudah berhasil dikonversi menjadi format JSON.
Simulasi Tambah Keranjang: Buka http://127.0.0.1:8000/api/cart/add/. 
Gulir ke bawah ke bagian form Raw Data, pilih tipe application/json, lalu kirim data (POST) seperti ini:JSON{
    "product_id": 1,
    "quantity": 2
}
Proses Checkout: Buka http://127.0.0.1:8000/api/cart/checkout/ dan langsung klik tombol POST di bagian bawah. 
Stok barang di admin otomatis berkurang dan total harga otomatis terhitung.
Pantau Riwayat Transaksi: Buka http://127.0.0.1:8000/api/orders/ untuk melihat cetakan nota digital (invoice) permanen dari transaksi yang baru saja kamu lakukan.
📝 Nilai Jual Proyek Ini untuk Interviewer / HRDStandar Industri: Pemisahan struktur kode yang bersih memisahkan tanggung jawab antara Models, Views, Serializers, dan Routes.
Defensive Programming: Menangani potensi error objek kosong menggunakan blok try-except serta memvalidasi batasan stok sebelum database melakukan mutasi data.
Operational Control: Kustomisasi layout Django Admin menggunakan atribut list_display untuk mempermudah monitoring infrastruktur data secara internal.
---

### Cara Menaruhnya di Proyek Kamu:
1. Buka code editor kamu (VS Code atau yang lain).
2. Di folder utama proyek kamu (`D:\projek\ecommerce_backend\`), buat sebuah file baru bernama **`README.md`**.
3. Tempel (*paste*) semua teks yang kamu salin dari atas ke dalam file tersebut.
4. Simpan (*save*) filenya.

Setelah file itu disimpan, saat kamu melakukan perintah `git add .` dan `git push` seperti langkah