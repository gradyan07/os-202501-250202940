
# Laporan Praktikum Minggu [X]
Topik: Penjadwalan CPU – Round Robin (RR) dan Priority Scheduling

---

## Identitas
- **Nama**  : Gradyan Alannahda Shofari  
- **NIM**   : 250202940
- **Kelas** : 1IKRB

---

## Tujuan

1. **Memahami konsep dasar** algoritma penjadwalan CPU, khususnya Round Robin dan Priority Scheduling.  
2. **Menganalisis perbedaan kinerja** kedua algoritma berdasarkan waktu tunggu, waktu respons, dan throughput.  
3. **Mengevaluasi kelebihan dan kekurangan** masing-masing algoritma dalam berbagai skenario sistem operasi.  
4. **Melatih kemampuan simulasi dan analisis**, baik secara manual maupun menggunakan perangkat lunak pendukung.

---

## Dasar Teori

1. **Round Robin (RR):**  
   Algoritma ini menggunakan time quantum untuk membagi waktu CPU secara bergiliran ke setiap proses, cocok untuk sistem time-sharing.

2. **Priority Scheduling:**  
   Proses dijalankan berdasarkan tingkat prioritas. Proses dengan prioritas lebih tinggi mendapat akses CPU lebih dulu.

3. **Time Quantum:**  
   Ukuran time quantum memengaruhi efisiensi dan responsivitas sistem. Terlalu kecil → overhead tinggi; terlalu besar → proses pendek tertunda.

4. **Starvation:**  
   Pada Priority Scheduling, proses prioritas rendah bisa tidak pernah dijalankan jika selalu ada proses prioritas tinggi.

5. **Pemilihan Algoritma:**  
   Harus disesuaikan dengan kebutuhan sistem, apakah lebih mementingkan keadilan, efisiensi, atau penanganan proses penting.


---

## Langkah Praktikum
1. **Siapkan Data Proses**
   Gunakan contoh data berikut (boleh dimodifikasi sesuai kebutuhan):
   | Proses | Burst Time | Arrival Time | Priority |
   |:--:|:--:|:--:|:--:|
   | P1 | 5 | 0 | 2 |
   | P2 | 3 | 1 | 1 |
   | P3 | 8 | 2 | 4 |
   | P4 | 6 | 3 | 3 |

2. **Eksperimen 1 – Round Robin (RR)**
   - Gunakan *time quantum (q)* = 3.  
   - Hitung *waiting time* dan *turnaround time* untuk tiap proses.  
   - Simulasikan eksekusi menggunakan Gantt Chart (manual atau spreadsheet).  
     ```
     | P1 | P2 | P3 | P4 | P1 | P3 | ...
     0    3    6    9   12   15   18  ...
     ```
   - Catat sisa *burst time* tiap putaran.

3. **Eksperimen 2 – Priority Scheduling (Non-Preemptive)**
   - Urutkan proses berdasarkan nilai prioritas (angka kecil = prioritas tinggi).  
   - Lakukan perhitungan manual untuk:
     ```
     WT[i] = waktu mulai eksekusi - Arrival[i]
     TAT[i] = WT[i] + Burst[i]
     ```
   - Buat tabel perbandingan hasil RR dan Priority.

4. **Eksperimen 3 – Analisis Variasi Time Quantum (Opsional)**
   - Ubah *quantum* menjadi 2 dan 5.  
   - Amati perubahan nilai rata-rata *waiting time* dan *turnaround time*.  
   - Buat tabel perbandingan efek *quantum*.

5. **Eksperimen 4 – Dokumentasi**
   - Simpan semua hasil tabel dan screenshot ke:
     ```
     praktikum/week6-scheduling-rr-priority/screenshots/
     ```
   - Buat tabel perbandingan seperti berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | RR | ... | ... | Adil terhadap semua proses | Tidak efisien jika quantum tidak tepat |
     | Priority | ... | ... | Efisien untuk proses penting | Potensi *starvation* pada prioritas rendah |

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 6 - CPU Scheduling RR & Priority"
   git push origin main
   ```

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
WT[i] = waktu mulai eksekusi - Arrival[i]
TAT[i] = WT[i] + Burst[i]
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

1. **Round Robin** memberikan keadilan waktu CPU untuk semua proses, namun performanya sangat dipengaruhi oleh ukuran time quantum.  
2. **Priority Scheduling** lebih efisien untuk proses penting, tetapi bisa menyebabkan starvation pada proses prioritas rendah.  
3. Pemilihan algoritma harus disesuaikan dengan kebutuhan sistem, apakah mengutamakan keadilan, efisiensi, atau responsivitas.

---

## Quiz
1. Apa perbedaan utama antara Round Robin dan Priority Scheduling?

   - Round Robin: Proses dijalankan bergiliran dengan jatah waktu tetap (time quantum). Adil, cocok untuk sistem time-sharing, tidak ada risiko starvation.
   - Priority Scheduling: Proses dengan prioritas tertinggi dijalankan lebih dulu. Tidak adil, bisa menyebabkan starvation, cocok untuk sistem real-time.


2. Apa pengaruh besar/kecilnya time quantum terhadap performa sistem?

   **Pengaruh besar/kecilnya time quantum terhadap performa sistem:**

- **Time quantum kecil:**  
  + Banyak context switching → overhead tinggi.  
  + Respons cepat, tapi efisiensi rendah.

- **Time quantum besar:**  
  + Proses pendek harus menunggu lama.  
  + Efisien, tapi respons lambat.

**Kesimpulan:**  
Time quantum harus seimbang agar sistem tetap responsif dan efisien.
  

3. Mengapa algoritma Priority dapat menyebabkan starvation?

Karena proses dengan prioritas rendah bisa terus-menerus tertunda jika selalu ada proses dengan prioritas lebih tinggi yang masuk. Akibatnya, proses prioritas rendah tidak pernah mendapat giliran CPU.
Solusi umum:

 

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
