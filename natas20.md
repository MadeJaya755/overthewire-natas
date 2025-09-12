Natas 20 → 21
🎯 Tujuan
Mendapatkan kata sandi untuk level 21 dengan mengeksploitasi kerentanan pada file sesi.

🔑 Kredensial
Username: natas20

Password: tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr

URL: http://natas20.natas.labs.overthewire.org

🛠️ Langkah
Analisis Halaman: Halaman Natas 20 memiliki form sederhana untuk mengatur nama (name). Setelah saya memasukkan nama, halaman menampilkan nama saya dan tombol "View". Ketika saya melihat kode sumber, saya menemukan bahwa nama disimpan dalam file sesi.

Identifikasi Kerentanan:

Kerentanan di sini adalah Local File Inclusion (LFI), yang terkait dengan cara server menyimpan dan memuat file sesi.

Server membaca nama file sesi dari cookie, dan kemudian memuat kontennya. Namun, ada celah di mana kita bisa memanipulasi path file tersebut.

Saya menggunakan Burp Suite untuk mencegat permintaan. Di sana saya melihat cookie PHPSESSID dan parameter name.

Melakukan Eksploitasi:

Saya mengubah nilai PHPSESSID menjadi nama file yang ingin saya baca.

Saya juga menyadari bahwa saya bisa menyuntikkan karakter khusus untuk memanipulasi path.

Payload yang berhasil adalah: PHPSESSID = ../../etc/natas_webpass/natas21

Saya memasukkan name=natas21 di form dan mengirimkan permintaan.

Server kemudian menyimpan natas21 di file sesi dengan nama yang saya suntikkan. Ketika saya mengklik "View", server akan membaca file yang saya tentukan (../../etc/natas_webpass/natas21) dan menampilkan isinya, yang merupakan kata sandi untuk level 21.

✅ Flag / Kata Sandi Level 21
p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw

💡 Catatan
Fokus utama dari level ini adalah eksploitasi file sesi dan LFI.

Tantangan ini menunjukkan bagaimana data sesi yang tidak ditangani dengan benar dapat mengarah pada kerentanan yang serius.

Penting untuk selalu memvalidasi input pengguna, bahkan ketika itu digunakan untuk mengelola sesi, untuk mencegah serangan traversal direktori dan LFI.
