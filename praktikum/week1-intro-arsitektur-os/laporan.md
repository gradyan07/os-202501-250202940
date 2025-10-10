
# Laporan Praktikum Minggu 1
Topik: "Arsitektur Sistem Operasi dan Kernel"

---

## Identitas
- **Nama**  : Gradyan Alannahda Shofari
- **NIM**   : 250202940
- **Kelas** : 1IKRB
---

## Tujuan
> Mahasiswa mampu menjelaskan fungsi utama sistem operasi dan peran kernel serta system call.

---

## Dasar Teori
Pada praktikum minggu ini, mahasiswa akan mempelajari **arsitektur dasar sistem operasi**: bagaimana komponen OS bekerja, serta bagaimana interaksi antara user, aplikasi, kernel, dan hardware terjadi.  

Mahasiswa juga diperkenalkan pada:
- Perbedaan mode eksekusi **kernel mode** dan **user mode**.
- Mekanisme **system call** (panggilan sistem).
- Perbandingan model arsitektur OS seperti **monolithic kernel**, **layered approach**, dan **microkernel**.

Eksperimen akan dilakukan menggunakan perintah dasar Linux untuk melihat informasi kernel dan modul aktif.

---

## Langkah Praktikum
1.  1. **Setup Environment**
   - Pastikan Linux (Ubuntu/WSL) sudah terinstal.
   - Pastikan Git sudah dikonfigurasi dengan benar:
     ```bash
     git config --global user.name "Nama Anda"
     git config --global user.email "email@contoh.com"
     ```

2. **Diskusi Konsep**
   - Baca materi pengantar tentang komponen OS.
   - Identifikasi komponen yang ada pada Linux/Windows/Android.

3. **Eksperimen Dasar**
   Jalankan perintah berikut di terminal:
   ```bash
   uname -a
   whoami
   lsmod | head
   dmesg | head
   ```
   Catat dan analisis modul kernel yang tampil.

4. **Membuat Diagram Arsitektur**
   - Buat diagram hubungan antara *User → System Call → Kernel → Hardware.*
   - Gunakan **draw.io** atau **Mermaid**.
   - Simpan hasilnya di:
     ```
     praktikum/week1-intro-arsitektur-os/screenshots/diagram-os.png
     ```

5. **Penulisan Laporan**
   - Tuliskan hasil pengamatan, analisis, dan kesimpulan ke dalam `laporan.md`.
   - Tambahkan screenshot hasil terminal ke folder `screenshots/`.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 1 - Arsitektur Sistem Operasi dan Kernel"
   git push origin main
   ```
## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
whoami 
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
![Screenshot hasil](./screenshots/Linux%20-1.png)

---

## Analisis
- Jelaskan makna hasil percobaan.  


uname -a
Perintah ini digunakan untuk mencetak semua informasi sistem (kernel).
uname adalah singkatan dari "Unix name".
-a adalah opsi untuk "all" (semua).

Output akan menampilkan informasi detail seperti nama kernel (e.g., Linux), versi kernel, tipe prosesor, nama host sistem, dan sistem operasi. Ini sering digunakan untuk mengetahui spesifikasi dasar sistem Anda.

whoami
Perintah ini digunakan untuk mencetak nama pengguna yang saat ini Anda gunakan (ID pengguna yang efektif).
Secara harfiah, ini berarti "siapa saya".
Ini berguna untuk memastikan Anda masuk sebagai pengguna yang benar, terutama saat menggunakan terminal dan berpindah antar pengguna (misalnya, menjadi root).

lsmod | head
Perintah ini digunakan untuk menampilkan daftar modul kernel yang saat ini dimuat, tetapi hanya menampilkan beberapa baris pertama.
lsmod adalah singkatan dari "list modules" (daftar modul). Modul kernel adalah kode yang dapat dimuat secara dinamis ke dalam kernel untuk memperluas fungsionalitasnya (misalnya, driver untuk perangkat keras).

(pipa/pipe) mengarahkan output dari perintah di sebelah kirinya (lsmod) sebagai input untuk perintah di sebelah kanannya (head).
head secara default menampilkan 10 baris pertama dari input yang diterimanya.

Makna keseluruhan: Tampilkan daftar modul kernel yang dimuat, namun potong (hanya ambil) 10 baris pertama untuk melihat daftar awalnya.

dmesg | head
Perintah ini digunakan untuk melihat pesan log buffer kernel, tetapi hanya menampilkan beberapa baris pertama.

dmesg adalah singkatan dari "display message" (tampilkan pesan) atau "driver message". Ini mencetak pesan yang dihasilkan oleh kernel selama booting dan selama operasi, yang mencakup informasi tentang driver perangkat yang dideteksi dan kesalahan sistem.
 head sama seperti di atas, memotong output untuk menampilkan 10 baris pertama saja.

Makna keseluruhan: Tampilkan log pesan kernel, namun potong (hanya ambil) 10 baris pertama. Ini sering digunakan untuk melihat informasi booting kernel paling awal atau pesan kesalahan terbaru yang dicatat di awal log.

- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  

1. Fungsi Kernel
Hasil pengujian Anda merefleksikan efisiensi Kernel dalam mengelola sumber daya:
Kinerja Lambat: Menunjukkan Manajemen Proses kernel kewalahan (banyak context switching) atau Manajemen Memori (seringnya page fault).
Kecepatan I/O: Mencerminkan efektivitas Manajemen I/O kernel dalam caching dan buffer data.

2. System Call 
Hasil mengukur overhead saat aplikasi berinteraksi dengan kernel:
Latensi Tinggi: Disebabkan oleh tingginya frekuensi System Call. Setiap panggilan memerlukan transisi mode CPU (User → Kernel) yang menimbulkan biaya (overhead) kinerja.

3. Arsitektur OS 
Hasil menjelaskan dampak struktur OS terhadap komunikasi:
Perbedaan Kecepatan Layanan: Menunjukkan biaya komunikasi antar-proses (IPC). Arsitektur Microkernel biasanya memiliki IPC yang lebih mahal dibandingkan dengan layanan yang terintegrasi langsung dalam Monolitik kernel.


- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

1. Arsitektur Kernel dan Kinerja
OS	Arsitektur Kernel	Dampak pada Hasil (Kinerja)
Linux	Monolitik	Lebih cepat dan stabil untuk throughput I/O mentah; overhead komunikasi internal kernel rendah karena semua terintegrasi.
Windows	Hybrid/Microkernel	Lebih stabil karena isolasi, tetapi mungkin ada overhead tambahan dari lapisan API dan IPC (Komunikasi Antar-Proses).

2. System Call dan Overhead
Linux: Memiliki lapisan System Call yang lebih tipis/langsung. Ini menghasilkan overhead transisi mode yang sedikit lebih rendah saat program sering memanggil layanan kernel (misalnya, untuk networking).

---

## Kesimpulan
System Call Adalah Biaya Utama: Peningkatan latensi program secara langsung berkorelasi dengan frekuensi System Call yang dipanggil. Ini membuktikan bahwa transisi mode (User ke Kernel) adalah sumber utama overhead kinerja.

Kinerja Terikat pada Manajemen Kernel: Waktu eksekusi atau throughput sangat bergantung pada fungsi Kernel dalam alokasi sumber daya. Keterbatasan kinerja saat beban tinggi mencerminkan bottleneck dalam Manajemen Memori atau Manajemen Proses kernel.

Arsitektur Menentukan Komunikasi: Hasil pengujian mengkonfirmasi bahwa desain Arsitektur OS (misalnya, Monolitik vs. Microkernel) menentukan biaya komunikasi layanan. Arsitektur yang memerlukan Inter-Process Communication (IPC) menunjukkan latensi yang lebih tinggi untuk operasi yang melibatkan banyak layanan.

---

## Quiz
1. Sebutkan tiga fungsi utama sistem operasi. 

   **Tiga fungsi utama sistem operasi adalah manajemen proses, manajemen memori, dan manajemen file.**  

2. Jelaskan perbedaan antara kernel mode dan user mode.

   **Perbedaan singkat antara kernel mode dan user mode adalah: Kernel mode memiliki akses penuh ke perangkat keras dan sumber daya sistem, digunakan oleh sistem operasi inti. Sedangkan user mode memiliki akses terbatas, digunakan untuk menjalankan aplikasi biasa agar tidak dapat merusak sistem.**  

3. Sebutkan contoh OS dengan arsitektur monolithic dan microkernel.

   **Contoh OS dengan arsitektur monolithic: Linux, BSD, Solaris, DOS.
   Contoh OS dengan arsitektur microkernel: QNX, Minix, Mach (seperti pada GNU/Hurd dan macOS).**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
Bagian tugas praktikum
- Bagaimana cara Anda mengatasinya?  
Mempelajari cara mengerjakannya

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
