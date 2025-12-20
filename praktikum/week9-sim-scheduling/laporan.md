
# Laporan Praktikum Minggu 9
Topik: Simulasi Algoritma Penjadwalan CPU
---

## Identitas
- **Nama**  : Gradyaan Alannahda Shofari 
- **NIM**   : 250202940  
- **Kelas** : 1IKRB

---

## Tujuan
untuk mendapatkan pemahaman mendalam secara teori dan praktik mengenai cara kerja sistem operasi mengelola prosesor.

---

## Dasar Teori
a. Penjadwalan CPU

Merupakan mekanisme sistem operasi untuk menentukan urutan eksekusi proses yang ada di ready queue agar penggunaan CPU lebih efisien.

b. First Come First Serve (FCFS)

Proses dijalankan sesuai urutan kedatangan. Algoritma ini sederhana, tetapi dapat menyebabkan waiting time tinggi jika ada proses dengan burst time besar di awal (convoy effect).

c. Shortest Job First (SJF)

Proses dengan burst time paling pendek diprioritaskan. Algoritma ini lebih optimal dalam menurunkan rata-rata waiting time dan turnaround time, namun membutuhkan estimasi burst time yang akurat.

d. Waiting Time dan Turnaround Time

- Waiting Time = waktu tunggu proses di ready queue sebelum dieksekusi.
- Turnaround Time = total waktu dari kedatangan proses hingga selesai dieksekusi.
Kedua metrik ini digunakan untuk mengevaluasi performa algoritma penjadwalan.
e. Simulasi Penjadwalan
Digunakan untuk menguji algoritma secara otomatis dengan dataset tertentu, sehingga hasil lebih cepat, akurat, dan mudah dibandingkan dengan perhitungan manual.

---

## Langkah Praktikum
1. **Menyiapkan Dataset**

   Buat dataset proses minimal berisi:

   | Proses | Arrival Time | Burst Time |
   |:--:|:--:|:--:|
   | P1 | 0 | 6 |
   | P2 | 1 | 8 |
   | P3 | 2 | 7 |
   | P4 | 3 | 3 |

2. **Implementasi Algoritma**

   Program harus:
   - Menghitung *waiting time* dan *turnaround time*.  
   - Mendukung minimal **1 algoritma (FCFS atau SJF non-preemptive)**.  
   - Menampilkan hasil dalam tabel.

3. **Eksekusi & Validasi**

   - Jalankan program menggunakan dataset uji.  
   - Pastikan hasil sesuai dengan perhitungan manual minggu sebelumnya.  
   - Simpan hasil eksekusi (screenshot).

4. **Analisis**

   - Jelaskan alur program.  
   - Bandingkan hasil simulasi dengan perhitungan manual.  
   - Jelaskan kelebihan dan keterbatasan simulasi.

5. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 9 - Simulasi Scheduling CPU"
   git push origin main
   ```
---

## Kode / Perintah
FCFS
```bash
def fcfs(processes):
    procs = sorted(processes, key=lambda x: x["arrival"])
    time, results = 0, []
    for p in procs:
        if time < p["arrival"]:
            time = p["arrival"]
        waiting = time - p["arrival"]
        turnaround = waiting + p["burst"]
        results.append({"pid": p["pid"], "waiting": waiting, "turnaround": turnaround})
        time += p["burst"]
    return results
```
SJF Non-Preemptive
```bash
def sjf(processes):
    procs = sorted(processes, key=lambda x: x["arrival"])
    time, ready, results = 0, [], []
    while procs or ready:
        while procs and procs[0]["arrival"] <= time:
            ready.append(procs.pop(0))
        if ready:
            ready.sort(key=lambda x: x["burst"])
            p = ready.pop(0)
            waiting = time - p["arrival"]
            turnaround = waiting + p["burst"]
            results.append({"pid": p["pid"], "waiting": waiting, "turnaround": turnaround})
            time += p["burst"]
        else:
            time = procs[0]["arrival"]
    return results
```
OUTPUT TABEL
```bash
def print_table(title, results):
    print(f"\n=== {title} ===")
    print("PID | Waiting | Turnaround")
    print("---------------------------")
    total_waiting = total_turnaround = 0
    for r in results:
        print(f"{r['pid']:>3} | {r['waiting']:>7} | {r['turnaround']:>10}")
        total_waiting += r["waiting"]
        total_turnaround += r["turnaround"]
    n = len(results)
    print("---------------------------")
    print(f"Rata-rata Waiting   : {total_waiting/n:.2f}")
    print(f"Rata-rata Turnaround: {total_turnaround/n:.2f}")
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/hasil_simulasi.png.png)

---

## Analisis

### 1. jelaskan alur program

a. Input Dataset
- Program mulai dengan daftar proses berisi PID, Arrival Time, dan Burst Time.

a. Algoritma FCFS (First Come First Serve)

- Proses diurutkan berdasarkan waktu kedatangan.
- Setiap proses dijalankan sesuai urutan kedatangan.
- Hitung:
- Waiting Time = waktu mulai eksekusi − arrival time
- Turnaround Time = waiting time + burst time
c. Algoritma SJF (Shortest Job First – Non-Preemptive)
- Proses yang sudah datang dimasukkan ke ready queue.
- Dari antrian dipilih proses dengan burst time paling kecil.
- Hitung waiting time dan turnaround time sama seperti FCFS.
- Jika tidak ada proses di antrian, waktu loncat ke arrival time proses berikutnya.

d. Output Tabel

- Program menampilkan tabel berisi PID, Arrival, Burst, Waiting, dan Turnaround.
- Di akhir tabel dihitung rata-rata waiting time dan turnaround time.

e. Analisis Hasil

- FCFS lebih sederhana tapi rata-rata waktu tunggu lebih besar.
- SJF lebih optimal karena memilih proses dengan burst time pendek, sehingga rata-rata waktu tunggu lebih kecil.

### 2. Bandingkan hasil simulasi dengan perhitungan manual.

a. FCFS (First Come First Serve)
- Urutan eksekusi: P1 → P2 → P3 → P4
- Waiting time: 0, 5, 12, 18
- Turnaround time: 6, 13, 19, 21
- Rata-rata waiting = 8.75
- Rata-rata turnaround = 14.75

b. SJF (Shortest Job First – Non-Preemptive)
- Urutan eksekusi: P1 → P4 → P3 → P2
- Waiting time: 0, 3, 7, 13
- Turnaround time: 6, 6, 14, 21
- Rata-rata waiting = 5.75
- Rata-rata turnaround = 11.75



### 3. Jelaskan kelebihan dan keterbatasan simulasi.

Kelebihan Simulasi:

- Otomatis dan cepat → perhitungan dilakukan oleh program tanpa perlu manual.
- Mengurangi human error → hasil lebih konsisten dibanding hitung manual, terutama pada dataset besar.
- Mudah diuji ulang → dataset bisa diganti atau diperbesar tanpa mengubah logika program.
- Scalable → dapat menangani banyak proses sekaligus dengan hasil tetap akurat.
- Validasi teori → hasil simulasi bisa langsung dibandingkan dengan konsep algoritma yang dipelajari.

Keterbatasan Simulasi:

- Terbatas pada algoritma yang diimplementasikan → misalnya hanya FCFS dan SJF non-preemptive, belum mendukung algoritma lain (RR, Priority, SRTF).
- Tidak menampilkan visualisasi Gantt chart secara default → hanya berupa tabel, sehingga kurang intuitif untuk melihat urutan eksekusi.
- Tidak fleksibel untuk input interaktif → dataset harus disiapkan terlebih dahulu dalam file.
- Tidak mencerminkan kondisi nyata sistem operasi sepenuhnya → simulasi hanya meniru logika dasar, belum memperhitungkan faktor-faktor lain seperti I/O, interrupt, atau preemption.

---

## Kesimpulan
- Praktikum simulasi algoritma penjadwalan CPU memberikan pemahaman nyata tentang cara sistem operasi mengelola proses menggunakan algoritma FCFS dan SJF non-preemptive.
- Hasil simulasi menunjukkan bahwa algoritma SJF lebih optimal dibanding FCFS karena menghasilkan rata-rata waiting time dan turnaround time yang lebih kecil.
- Simulasi mempermudah perhitungan, mengurangi kesalahan manual, serta dapat digunakan untuk dataset besar dengan hasil konsisten.


---

## Quiz
1. Mengapa simulasi diperlukan untuk menguji algoritma scheduling?  
- Menghindari risiko pada sistem produksi
Algoritma yang belum teruji bisa menimbulkan keterlambatan atau kegagalan. Simulasi memberi ruang aman untuk eksperimen.
- Menguji berbagai skenario
Simulasi memungkinkan mencoba kondisi berbeda (beban tinggi, banyak proses, variasi prioritas) yang sulit direplikasi di dunia nyata.
- Evaluasi kinerja secara objektif
Metrik seperti waiting time, turnaround time, response time, dan CPU utilization dapat diukur dengan jelas.
- Efisiensi biaya dan waktu
Lebih murah dan cepat dibandingkan uji langsung pada perangkat keras atau sistem produksi.
- Validasi sebelum implementasi
Simulasi berfungsi sebagai tahap verifikasi agar algoritma benar-benar optimal sebelum diterapkan.

2. Apa perbedaan hasil simulasi dengan perhitungan manual jika dataset besar?   
   Perbedaan utama hasil simulasi dan perhitungan manual pada dataset besar terletak pada pendekatan dan kompleksitas, di mana simulasi (numerik/komputer) unggul dalam menangani skala dan kompleksitas tinggi melalui aproksimasi dan model, sementara perhitungan manual (analitik/rumus sederhana) menjadi tidak praktis atau mustahil karena waktu dan sumber daya, namun hasilnya idealnya mendekati nilai sebenarnya jika model simulasi akurat, meskipun simulasi memiliki potensi kesalahan pemodelan, diskritisasi, dan iteratif yang perlu dikelola untuk validitas. 

3. Algoritma mana yang lebih mudah diimplementasikan? Jelaskan. 
   - Logika sederhana → proses dijalankan sesuai urutan kedatangan, mirip antrean.
   - Tidak perlu parameter tambahan → tidak ada prioritas, kuantum waktu, atau perhitungan kompleks.
   - Implementasi mudah → cukup menggunakan struktur data queue (FIFO).
   - Perhitungan metrik sederhana → waktu tunggu dan turnaround dapat dihitung langsung dari urutan eksekusi.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
