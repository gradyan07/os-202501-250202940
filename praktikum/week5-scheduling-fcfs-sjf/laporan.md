
# Laporan Praktikum Minggu 5
Topik: Penjadwalan CPU – FCFS dan SJF

---

## Identitas
- **Nama**  : Gradyan Alannahda Shofari 
- **NIM**   : 250202940 
- **Kelas** : 1IKRB

---

## Tujuan
Tujuan mahasiswa melakukan praktikum tentang Penjadwalan CPU – FCFS dan SJF adalah untuk memahami, mengimplementasikan, dan menganalisis kinerja kedua algoritma penjadwalan CPU tersebut.
---

## Dasar Teori
1. Penjadwalan CPU: Proses pengelolaan dan pengalokasian waktu CPU untuk menjalankan proses-proses yang ada di sistem operasi.
2. FCFS (First Come First Served): Algoritma penjadwalan CPU yang melayani proses berdasarkan urutan kedatangan, yaitu proses yang datang pertama kali akan dilayani pertama kali.
3. SJF (Shortest Job First): Algoritma penjadwalan CPU yang melayani proses berdasarkan waktu eksekusi terpendek, yaitu proses dengan waktu eksekusi terpendek akan dilayani pertama kali.
4. Kriteria Penjadwalan CPU: Waktu tunggu (waiting time), waktu respons (response time), throughput sistem, dan efisiensi penggunaan CPU digunakan untuk mengevaluasi kinerja algoritma penjadwalan CPU.

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
uname -a
lsmod | head
dmesg | head
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

## Quiz
1. Apa perbedaan utama antara FCFS dan SJF?

   Perbedaan utama antara FCFS (First Come First Served) dan SJF (Shortest Job First) adalah FCFS memproses proses berdasarkan urutan kedatangannya, sementara SJF memproses proses dengan waktu eksekusi terpendek terlebih dahulu. Akibatnya, FCFS lebih sederhana tetapi bisa menyebabkan waktu tunggu yang lebih lama bagi proses yang tiba belakangan, sedangkan SJF bertujuan untuk meminimalkan waktu tunggu rata-rata, meskipun lebih kompleks untuk diimplementasikan.   

2. Mengapa SJF dapat menghasilkan rata-rata waktu tunggu minimum?

   Algoritma Shortest Job First (SJF) dapat menghasilkan rata-rata waktu tunggu minimum karena sifatnya yang greedy, yaitu selalu mengeksekusi proses dengan waktu eksekusi terpendek terlebih dahulu. Pendekatan ini memastikan bahwa proses-proses yang lebih pendek tidak harus menunggu lama di belakang proses-proses yang lebih panjang. 

3. Apa kelemahan SJF jika diterapkan pada sistem interaktif?  

   Kelemahan SJF pada sistem interaktif:

- Dapat menyebabkan starvation untuk proses panjang.

- Sulit memprediksi burst time secara akurat.

- Respons ke pengguna bisa lambat untuk proses panjang.

- Membutuhkan overhead untuk estimasi waktu eksekusi.  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
