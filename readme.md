# 🛒 Kopiko Store - Full-Stack E-Commerce API & Frontend

Proyek ini adalah aplikasi **Full-Stack E-Commerce** mini yang mengintegrasikan Backend berbasis **Python (Django & Django REST Framework)** dengan Frontend dinamis menggunakan **HTML5, Tailwind CSS, dan Vanilla JavaScript**. 

Aplikasi ini mengimplementasikan siklus data lengkap (*End-to-End*) mulai dari manajemen database produk, sistem keranjang belanja berbasis sesi, validasi stok *real-time*, hingga otomatisasi penerbitan nota transaksi (invoice/order history). Desain arsitekturnya mengikuti standar industri (separation of concerns) yang sangat cocok dijadikan portofolio berbobot untuk lowongan magang *Software Engineer* atau *Full-Stack Developer*.

---

## ✨ Fitur Utama Aplikasi

### 1. Robust Backend Architecture (Django & DRF)
* **Relational Schema & Dynamic Locking:** Menggunakan ORM Django untuk memetakan entitas `User`, `Product`, `Cart`, `OrderItem`, dan `Order`. Melalui relasi `OneToOneField`, keranjang belanja yang sukses di-checkout akan langsung "dikunci" menjadi nota transaksi permanen.
* **State Machine & Auto-Reset:** Begitu proses checkout selesai, status keranjang lama berubah menjadi `ordered=True` dan sistem backend secara otomatis membuatkan keranjang aktif baru yang kosong untuk sesi belanja berikutnya.
* **Defensive Stock Ledger:** Validasi kuantitas produk secara ketat. Jika user memesan melebihi stok yang tersedia, backend akan menolak request transaksi dan memberikan respon error demi menjaga konsistensi data.

### 2. Interactive Reactive Frontend (Tailwind & Vanilla JS)
* **Single Page Simulation:** Antarmuka katalog produk dan keranjang belanja dimuat secara dinamis dalam satu halaman menggunakan fungsi `fetch()` asynchronous JavaScript tanpa perlu *reload* halaman.
* **Real-time Inventory Synchronization:** Sinkronisasi data pintar yang mencocokkan ID produk dari API keranjang dengan katalog utama untuk menampilkan detail nama produk, kalkulasi sub-total, dan total harga secara akurat (mencegah error data `undefined` atau `NaN`).
* **CSRF Security Layer:** Mengamankan setiap mutasi data (`POST` request) saat tambah keranjang dan checkout dengan menyuntikkan token keamanan *Cross-Site Request Forgery* (CSRF) bawaan Django.

---

## 🛠️ Tech Stack & Spesifikasi

* **Backend:** Python & Django
* **API Engine:** Django REST Framework (DRF)
* **Frontend:** HTML5, Tailwind CSS (via Online Utility Engine), Vanilla JavaScript (ES6+ Asynchronous Fetch)
* **Database:** SQLite (Relasional lokal)

---

## 📂 Struktur Direktori Proyek

```text
ecommerce_backend/
│
├── core/
│   ├── settings.py          # Konfigurasi utama & aplikasi terdaftar (INSTALLED_APPS)
│   └── urls.py              # Routing utama (menghubungkan API dan halaman utama)
│
├── shop/
│   ├── templates/
│   │   └── shop/
│   │       └── index.html   # FILE UTAMA FRONTEND (HTML + JS Fetch)
│   ├── admin.py             # Kustomisasi visual list_display panel admin Django
│   ├── models.py            # Skema tabel database relasional (ORM)
│   ├── serializers.py       # Serializer objek ke format JSON array
│   ├── urls.py              # Endpoint lokal aplikasi (/products/, /cart/, dll)
│   └── views.py             # Controller logika bisnis & fungsi render template
│
└── manage.py                # Django administrative task manager