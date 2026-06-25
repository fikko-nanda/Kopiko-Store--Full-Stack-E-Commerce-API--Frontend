# 🛒 E-Commerce Backend API

Sebuah RESTful API untuk platform e-commerce yang dibangun menggunakan **Python**, **Django**, dan **Django REST Framework (DRF)**. Proyek ini mengimplementasikan relasi database yang bersih, serialisasi data (serialization), validasi stok secara real-time, otomatisasi pencatatan transaksi, serta kustomisasi panel admin untuk monitoring data secara visual.

Proyek ini dikembangkan dengan standar arsitektur profesional (MVT/MVC pattern) yang dirancang khusus untuk mendemonstrasikan kompetensi inti logika bisnis dan backend engineering untuk persiapan magang (Software Engineering Internship).

---

## ✨ Fitur & Fungsionalitas Utama

### 1. Arsitektur Database & ORM
* **Skema Relasional:** Implementasi relasi database yang bersih yang menghubungkan entitas `User`, `Product`, `Cart`, `OrderItem`, dan `Order`.
* **Penguncian Data Transaksi:** Menggunakan relasi `OneToOneField` dari `Cart` yang sudah selesai ke sebuah `Order` (Nota/Invoice) untuk mengunci riwayat snapshot belanjaan secara permanen.

### 2. Logika Bisnis & API Endpoints
* **Validasi Stok Real-Time:** Mencegah pembelian berlebih dengan melakukan pengecekan ketat pada nilai `product.stock` sebelum barang masuk ke keranjang maupun saat checkout.
* **Buku Besar Stok Otomatis:** Memotong jumlah stok produk di database secara permanen begitu transaksi checkout berhasil dilakukan.
* **State Machine Berbasis Sesi:** Secara otomatis mengosongkan keranjang aktif lama dan membuatkan `Cart` aktif baru (`ordered=False`) untuk pengguna segera setelah checkout berhasil, sehingga pengguna bisa langsung belanja kembali.

### 3. Serialisasi & Keamanan API
* **Nested Serialization:** Menyajikan representasi data yang kaya dengan menyarangkan (nesting) struktur produk dan item di dalam respon JSON nota riwayat transaksi.
* **Kontrol Akses Endpoint:** Mengamankan integritas data dengan membatasi akses endpoint manajemen keranjang dan checkout hanya untuk user yang sudah login (`IsAuthenticated`).

---

## 🛠️ Tech Stack

* **Bahasa Pemrograman:** Python
* **Framework:** Django
* **API Toolkit:** Django REST Framework (DRF)
* **Database:** SQLite (Default bawaan / Mudah dimigrasikan ke PostgreSQL)

---

## 📂 Struktur Proyek

```text
ecommerce_backend/
│
├── core/
│   ├── settings.py          # Pengaturan & konfigurasi pusat proyek
│   └── urls.py              # Definisi rute URL utama
│
├── shop/
│   ├── admin.py             # Kustomisasi visual panel admin Django
│   ├── models.py            # Skema dan relasi database ORM
│   ├── serializers.py       # Skema konversi data ke format JSON
│   ├── urls.py              # Definisi rute API khusus aplikasi shop
│   └── views.py             # Logika bisnis utama penanganan request (API Views)
│
└── manage.py                # Manager tugas administratif Django