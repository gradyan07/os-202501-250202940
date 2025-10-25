
# Laporan Praktikum Minggu 4
Topik: Manajemen Proses dan User di Linux

---

## Identitas
- **Nama**  : Gradyan Alannahda Shofari
- **NIM**   : 250202940 
- **Kelas** : 1IKRB

---

## Tujuan
- Memahami konsep manajemen proses dan user di Linux.
- Menguasai perintah-perintah Linux untuk mengelola proses dan user.
- Meningkatkan keterampilan teknis dalam mengelola sistem operasi Linux.
- Mempersiapkan mahasiswa untuk karir di bidang IT dan administrasi sistem Linux.

---

## Dasar Teori
1. Manajemen Proses:
    - Definisi proses dan jenis-jenis proses (foreground, background, daemon).
    - Perintah-perintah untuk mengelola proses (ps, top, kill, bg, fg).
    - Konsep PID (Process ID) dan PPID (Parent Process ID).

2. Manajemen User:
    - Konsep user dan group di Linux.
    - Perintah-perintah untuk mengelola user dan group (useradd, userdel, usermod, groupadd, groupdel).
    - Hak akses file dan direktori (permission) dengan sistem file berbasis Unix.

3. Keamanan Sistem:
    - Konsep keamanan dan kontrol akses di Linux.
    - Penggunaan sudo untuk memberikan hak akses istimewa kepada user.

4. Shell dan Perintah Dasar:
    - Penggunaan shell untuk menjalankan perintah dan mengelola sistem.
    - Perintah dasar Linux untuk navigasi direktori, manajemen file, dan pengelolaan proses.

Dasar teori ini menjadi landasan penting untuk memahami cara kerja sistem operasi Linux dan bagaimana mengelola proses serta user dengan efektif.

---

## Langkah Praktikum
Setup Environment

Gunakan Linux (Ubuntu/WSL).
Pastikan Anda sudah login sebagai user non-root.
Siapkan folder kerja:
praktikum/week4-proses-user/
Eksperimen 1 – Identitas User Jalankan perintah berikut:

whoami
id
groups
Jelaskan setiap output dan fungsinya.
Buat user baru (jika memiliki izin sudo):
```bash
sudo adduser praktikan
sudo passwd praktikan
```
Uji login ke user baru.
Eksperimen 2 – Monitoring Proses Jalankan:
```bash
ps aux | head -10
top -n 1
```
Jelaskan kolom penting seperti ``PID, USER, %CPU, %MEM, COMMAND.``
Simpan tangkapan layar top ke:
praktikum/week4-proses-user/screenshots/top.png
Eksperimen 3 – Kontrol Proses

Jalankan program latar belakang:
sleep 1000 &
ps aux | grep sleep
Catat PID proses sleep.
Hentikan proses:
```bash
kill <PID>
```
Pastikan proses telah berhenti dengan ps aux | grep sleep.
Eksperimen 4 – Analisis Hierarki Proses Jalankan:
```bash
pstree -p | head -20
```
Amati hierarki proses dan identifikasi proses induk (init/systemd).
Catat hasilnya dalam laporan.
Commit & Push
```bash
git add .
git commit -m "Minggu 4 - Manajemen Proses & User"
git push origin main
```
---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
whoami
id
groups
sudo adduser praktikan
sudo passwd praktikan
ps aux | head -10
top -n 1
sleep 1000 &
ps aux | grep sleep
kill <PID>
pstree -p | head -20
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
- Jelaskan makna hasil percobaan.  
Manajemen Proses:

1. Pengelolaan proses yang efektif: Hasil percobaan menunjukkan bahwa kita dapat mengelola proses dengan efektif menggunakan perintah-perintah seperti ps, kill, bg, dan fg.
2. Kontrol atas proses: Kita dapat mengontrol proses yang sedang berjalan, seperti menghentikan atau melanjutkan proses, serta memindahkannya ke latar belakang atau depan.
3. Peningkatan efisiensi sistem: Dengan mengelola proses yang efektif, kita dapat meningkatkan efisiensi sistem dan mengurangi penggunaan sumber daya yang tidak perlu.

Manajemen User:

1. Pengelolaan user yang efektif: Hasil percobaan menunjukkan bahwa kita dapat mengelola user dengan efektif menggunakan perintah-perintah seperti useradd, passwd, dan usermod.
2. Kontrol atas akses: Kita dapat mengontrol akses user ke sistem dan file dengan menggunakan hak akses dan kepemilikan file.
3. Peningkatan keamanan sistem: Dengan mengelola user dan hak akses yang efektif, kita dapat meningkatkan keamanan sistem dan mengurangi risiko akses tidak sah.

- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).
1. Fungsi Kernel: Kernel Linux berperan sebagai pengelola sumber daya sistem, termasuk proses dan user. Kernel memastikan bahwa proses berjalan dengan baik dan aman.
2. System Call: System call seperti fork(), exec(), kill(), dan wait() digunakan untuk berinteraksi dengan kernel dan mengelola proses. System call memungkinkan user space untuk meminta layanan dari kernel.
3. Arsitektur OS: Arsitektur Linux yang terdiri dari kernel space dan user space memungkinkan kernel untuk mengelola proses dan user secara efektif. Kernel memiliki kontrol penuh atas sumber daya sistem, sedangkan user space menjalankan aplikasi dan program.

- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. Apa fungsi dari proses init atau systemd dalam sistem Linux?  

   Fungsi utama dari proses init (kependekan dari initialization) atau systemd dalam sistem Linux adalah sebagai sistem inisialisasi dan pengelola sistem. Mereka adalah program pertama yang dijalankan oleh kernel Linux setelah kernel dimuat, dan bertanggung jawab untuk membawa sistem ke keadaan yang dapat digunakan.  

2. Apa perbedaan antara kill dan killall?  

   Perbedaan utama antara perintah kill dan killall di Linux terletak pada cara mereka mengidentifikasi proses target yang akan dihentikan:

- kill menargetkan proses berdasarkan Process ID (PID).
- killall menargetkan proses berdasarkan nama proses (nama perintah).  

3. Mengapa user root memiliki hak istimewa di sistem Linux?
  
   User root memiliki hak istimewa di sistem Linux karena mereka adalah Superuser atau Administrator sistem, yang secara filosofis dan teknis diperlukan untuk mengelola dan memelihara seluruh sistem operasi.
 

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? 
mengalami kesulitan pada saat mengulang perintah setelah membuat pasword 
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
