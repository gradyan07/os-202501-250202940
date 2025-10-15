
# Laporan Praktikum Minggu [X]
Topik: [Tuliskan judul topik, misalnya "Arsitektur Sistem Operasi dan Kernel"]

---

## Identitas
- **Nama**  : Gradyan Alannahda Shofari  
- **NIM**   : 250202940  
- **Kelas** : 1IKRB

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
> Mahasiswa mampu menjelaskan fungsi utama sistem operasi dan peran kernel serta system call.

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
pwd
ls -l
cd /tmp
ls -a
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---
Z
## Quiz
1. Apa fungsi dari perintah chmod?

   Fungsi dari perintah chmod adalah untuk mengubah izin akses (permission) pada file atau direktori di sistem operasi Unix/Linux. Dengan chmod, Anda dapat menentukan siapa yang dapat membaca, menulis, atau mengeksekusi file atau direktori tertentu, sehingga meningkatkan keamanan dan kontrol akses pada sistem. 

2. Apa arti dari kode permission rwxr-xr--?

   Kode permission rwxr-xr-- adalah representasi dari izin akses file atau direktori di sistem operasi Unix/Linux. Berikut adalah arti dari kode tersebut:

- rwx (Owner/User): Membaca (r), Menulis (w), dan Mengeksekusi (x)
- r-x (Group): Membaca (r) dan Mengeksekusi (x), tapi tidak dapat Menulis
- r-- (Other): Hanya dapat Membaca (r), tidak dapat Menulis atau Mengeksekusi

Jadi, kode rwxr-xr-- berarti:

- Pemilik file memiliki izin penuh (membaca, menulis, dan mengeksekusi)
- Anggota grup memiliki izin membaca dan mengeksekusi, tapi tidak dapat menulis
- Pengguna lain hanya dapat membaca file, tidak dapat menulis atau mengeksekusi.

3. Jelaskan perbedaan antara chown dan chmod.

   chown dan chmod adalah dua perintah yang berbeda dalam sistem operasi Unix/Linux.
chown digunakan untuk mengubah kepemilikan file atau direktori, yaitu mengubah siapa yang memiliki file atau direktori tersebut.
chmod digunakan untuk mengubah izin akses file atau direktori, yaitu menentukan siapa yang dapat membaca, menulis, atau mengeksekusi file atau direktori tersebut.

Jadi, chown berkaitan dengan kepemilikan, sedangkan chmod berkaitan dengan izin akses.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  

- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
