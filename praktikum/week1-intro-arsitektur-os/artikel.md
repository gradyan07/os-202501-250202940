# 01 Pendahuluan
Sistem operasi (SO) merupakan perangkat lunak fundamental yang mengelola sumber daya perangkat keras komputer dan menyediakan layanan umum untuk program aplikasi. Salah satu aspek krusial dalam desain SO adalah arsitektur kernel, yang menentukan bagaimana berbagai komponen SO diorganisir. Secara garis besar, terdapat tiga arsitektur kernel utama: kernel monolitik (monolithic kernel), mikrokernel (microkernel), dan arsitektur berjenjang (layered architecture). Ketiganya menawarkan pendekatan yang berbeda dalam hal efisiensi, modularitas, keamanan, dan kompleksitas pengembangan.

1. Kernel Monolitik
Kernel monolitik adalah arsitektur SO tradisional di mana semua layanan SO—termasuk manajemen proses, manajemen memori, sistem file, dan device driver—berjalan dalam ruang alamat tunggal (single address space) di mode kernel (kernel mode).

Karakteristik Utama:
Integrasi Erat: Semua komponen SO terintegrasi dengan erat dan berkomunikasi melalui panggilan fungsi langsung, tanpa mekanisme Inter-Process Communication (IPC) yang kompleks.

Performa Tinggi: Karena tidak ada overhead perpindahan konteks (context switch) antara mode kernel dan mode pengguna untuk layanan SO, kernel monolitik umumnya menawarkan kecepatan eksekusi yang lebih cepat dan efisiensi tinggi.

Kekurangan Modularitas: Kerusakan pada satu komponen (device driver misalnya) dapat menyebabkan kegagalan seluruh sistem karena semuanya berbagi ruang memori. Selain itu, penambahan atau modifikasi layanan memerlukan kompilasi ulang seluruh kernel, membuatnya sulit diperluas dan dirawat.

Contoh: Linux, UNIX (tradisional), FreeBSD.

2. Mikrokernel
Arsitektur mikrokernel mengadopsi pendekatan minimalis dan modular. Hanya fungsi-fungsi paling dasar yang dipertahankan dalam kernel di mode kernel, seperti IPC, manajemen memori dasar, dan penjadwalan proses dasar.

Karakteristik Utama:
Minimalisme Inti: Sebagian besar layanan SO yang sebelumnya berada di kernel, seperti device driver, sistem file, dan network stack, dipindahkan ke mode pengguna (user mode) dan berjalan sebagai proses terpisah (server).

Komunikasi IPC: Komponen-komponen SO berkomunikasi melalui mekanisme IPC (seperti message passing). Meskipun meningkatkan modularitas dan keamanan, ini juga menambahkan overhead komunikasi yang dapat memperlambat eksekusi dibandingkan kernel monolitik.

Keamanan dan Ketahanan (Fault Tolerance): Kegagalan pada layanan di mode pengguna (misalnya driver) tidak akan menyebabkan seluruh sistem crash, karena layanan tersebut berjalan di ruang alamatnya sendiri. Hal ini meningkatkan keamanan dan ketahanan.

Contoh: Minix, QNX, Mach (yang menjadi dasar beberapa SO modern seperti macOS).

3. Arsitektur Berjenjang
Arsitektur berjenjang (layered architecture) adalah pendekatan struktural di mana SO dibagi menjadi beberapa lapisan (atau jenjang) yang berbeda. Setiap lapisan hanya dapat menggunakan layanan dari lapisan yang lebih rendah, dan menyediakan layanan ke lapisan yang lebih tinggi.

Karakteristik Utama:
Pemecahan Tugas: Setiap lapisan memiliki fungsi spesifik dan jelas yang dilakukan, memecah sistem yang kompleks menjadi bagian-bagian yang lebih mudah dikelola. Lapisan terendah berinteraksi langsung dengan perangkat keras, dan lapisan tertinggi berinteraksi dengan pengguna.

Kemudahan Implementasi dan Debugging: Karena pemisahan fungsi dan keterbatasan interaksi, arsitektur ini memudahkan implementasi, verifikasi, dan perbaikan bug. Perubahan pada satu lapisan idealnya hanya memengaruhi lapisan yang berdekatan.

Overhead Panggilan: Pengiriman permintaan dari lapisan atas ke lapisan bawah dapat melibatkan banyak panggilan fungsi, yang dapat menyebabkan overhead dan mengurangi performa dibandingkan kernel monolitik.

Contoh: SO THE oleh Dijkstra adalah contoh murni awal dari arsitektur berjenjang. Meskipun kernel monolitik modern (seperti Linux) sering menggunakan konsep modularitas dan lapisan, mereka umumnya tidak mengikuti struktur berjenjang yang ketat seperti model teoritis ini.

4. Model yang paling relevan untuk sistem modern adalah Monolitik Modular dan Hibrida (Hybrid).

Hampir semua SO modern utama (Linux, Windows, macOS) menggunakan variasi arsitektur yang menggabungkan performa tinggi kernel monolitik dengan modularitas dan stabilitas dari konsep mikrokernel.