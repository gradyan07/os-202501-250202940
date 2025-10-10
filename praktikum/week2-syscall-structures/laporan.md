
# Laporan Praktikum Minggu 2
Topik: "Struktur Sistem call dan Kernel Interaction"

---

## Identitas
- **Nama**  : Gradyan Alannahda Shofari
- **NIM**   : 250202940
- **Kelas** : 1IKRB

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:

Menjelaskan konsep dan fungsi system call dalam sistem operasi.
Mengidentifikasi jenis-jenis system call dan fungsinya.
Mengamati alur perpindahan mode user ke kernel saat system call terjadi.
Menggunakan perintah Linux untuk menampilkan dan menganalisis system call.

---

## Dasar Teori
Pada praktikum minggu ini, mahasiswa akan mempelajari mekanisme system call dan struktur sistem operasi.
System call adalah antarmuka antara program aplikasi dan kernel yang memungkinkan aplikasi berinteraksi dengan perangkat keras secara aman melalui layanan OS.

Mahasiswa akan melakukan eksplorasi terhadap:

Jenis-jenis system call yang umum digunakan (file, process, device, communication).
Alur eksekusi system call dari mode user menuju mode kernel.
Cara melihat daftar system call yang aktif di sistem Linux.

---

## Langkah Praktikum
1. Setup Environment

Gunakan Linux (Ubuntu/WSL).
Pastikan perintah strace dan man sudah terinstal.
Konfigurasikan Git (jika belum dilakukan di minggu sebelumnya).
Eksperimen 1 – Analisis System Call Jalankan perintah berikut:
```bash
strace ls
```
>Catat 5–10 system call pertama yang muncul dan jelaskan fungsinya.
Simpan hasil analisis ke results/syscall_ls.txt.

Eksperimen 2 – Menelusuri System Call File I/O Jalankan:
```bash
strace -e trace=open,read,write,close cat /etc/passwd
```
>Analisis bagaimana file dibuka, dibaca, dan ditutup oleh kernel.


Eksperimen 3 – Mode User vs Kernel Jalankan:
```bash
dmesg | tail -n 10
```
>Amati log kernel yang muncul. Apa bedanya output ini dengan output dari program biasa?


Diagram Alur System Call

Buat diagram yang menggambarkan alur eksekusi system call dari program user hingga kernel dan kembali lagi ke user mode.
Gunakan draw.io / mermaid.
Simpan di:
```bash
praktikum/week2-syscall-structure/screenshots/syscall-diagram.png
```
Commit & Push
```bash
git add .
git commit -m "Minggu 2 - Struktur System Call dan Kernel Interaction"
git push origin main
```
---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](./screenshots/syscall_Is.png)
![Screenshot hasil](./screenshots/syscall_ls%20(1).png)
![Screenshot hasil](./screenshots/syscall_Is%20(2).png)

---

## Analisis
- Jelaskan makna hasil percobaan.  
Percobaan ini juga menunjukkan bagaimana kernel mengelola akses ke sumber daya sistem dan memastikan keamanan serta stabilitas sistem. Dengan menggunakan perintah strace dan dmesg, kita dapat memantau system call dan log kernel untuk memahami bagaimana sistem operasi bekerja.

Hasil percobaan ini memberikan wawasan tentang:

1. Interaksi program-kernel
2. Manajemen sumber daya sistem
3. Keamanan dan stabilitas sistem
4. Penggunaan system call dalam program
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  

Percobaan Struktur System Call dan Kernel Interaction menunjukkan bahwa konsep sistem operasi tentang kernel, system call, dan arsitektur sistem operasi dapat diaplikasikan secara langsung dalam praktek. Hasil percobaan ini membuktikan bahwa:

1. Kernel berfungsi sebagai pengawas dan pengelola sumber daya sistem.
2. System call memungkinkan program untuk meminta layanan kernel.
3. Arsitektur sistem operasi yang terdiri dari mode pengguna dan mode kernel memungkinkan kontrol akses yang efektif.

Dengan demikian, percobaan ini memberikan bukti empiris tentang bagaimana sistem operasi bekerja dan bagaimana komponen-komponennya berinteraksi.

- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

Perbedaan antara Linux dan Windows dalam struktur sistem call dan kernel interaction adalah:

1. Linux menggunakan system call POSIX dan kernel monolitik, membuatnya lebih fleksibel dan dapat disesuaikan.
2. Windows menggunakan system call NT API dan kernel hibrid, membuatnya lebih fokus pada kemudahan penggunaan dan kompatibilitas.

Perbedaan ini mempengaruhi kinerja, keamanan, dan fleksibilitas kedua sistem operasi.

---

## Kesimpulan
Praktikum ini menunjukkan bagaimana system call digunakan oleh program untuk berinteraksi dengan kernel. Dengan menggunakan perintah strace, kita dapat memantau system call yang dilakukan oleh program, seperti open, read, write, dan close. Hasilnya membantu memahami cara kerja sistem operasi dalam mengelola sumber daya dan menangani permintaan dari program.

Perintah dmesg digunakan untuk memantau log kernel, yang dapat membantu dalam debugging dan memahami kejadian sistem. Dengan demikian, praktikum ini memberikan wawasan tentang interaksi antara program dan kernel, serta cara memantau dan menganalisis system call.

---

## Quiz
1. Apa fungsi utama system call dalam sistem operasi?

   Fungsi utama system call adalah memungkinkan program pengguna untuk berinteraksi dengan kernel sistem operasi, meminta layanan seperti manajemen proses, file, dan perangkat keras, sehingga memungkinkan akses terkendali dan aman ke sumber daya sistem.

2. Sebutkan 4 kategori system call yang umum digunakan.

   Empat kategori system call yang umum digunakan adalah:
- Manajemen Proses
- Manajemen File
- Manajemen Perangkat
- Manajemen Memori 


3. Mengapa system call tidak bisa dipanggil langsung oleh user program?

   System call tidak bisa dipanggil langsung oleh user program karena sistem operasi berjalan dalam mode kernel yang memiliki privilege lebih tinggi daripada mode pengguna. System call diperlukan sebagai perantara untuk memastikan keamanan, stabilitas, dan kontrol akses ke sumber daya sistem. Dengan demikian, sistem operasi dapat mengelola sumber daya secara efektif dan mencegah kerusakan sistem.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
Mendowload Linux 
- Bagaimana cara Anda mengatasinya?  
Menggunakan Cloud Shell
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
