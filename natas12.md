Natas 12 → 13
🎯 Tujuan
Mendapatkan password untuk level 13 di OverTheWire Natas.

🔑 Kredensial
Username: natas12

Password: yZdkjAYZRd3R7tq7T5kXMjMJlOIkzDeB

URL: http://natas12.natas.labs.overthewire.org

🛠️ Langkah
Analisis Halaman: Halaman web menyediakan sebuah form untuk mengunggah file.

Identifikasi Celah: Setelah mencoba mengunggah beberapa jenis file, diketahui bahwa server melakukan validasi ekstensi file untuk membatasi unggahan hanya pada format gambar.

Membuat Payload: Saya membuat file gambar JPEG bernama shell.jpg dan menyisipkan kode PHP sederhana di dalamnya. Kode ini dirancang untuk membaca file kata sandi (/etc/natas_webpass/natas13) dan menampilkannya.

PHP

<?php system('cat /etc/natas_webpass/natas13'); ?>
Eksploitasi:

Saya mengunggah file shell.jpg tersebut melalui form yang disediakan.

Server, yang menganggap file ini sebagai gambar yang valid, menerima unggahan tersebut.

File tersebut disimpan di direktori uploads/.

Eksekusi Kode: Saya mengakses file yang telah diunggah melalui URL http://natas12.natas.labs.overthewire.org/uploads/shell.jpg. Karena server mengaktifkan eksekusi PHP pada file gambar di direktori tersebut, kode yang saya sisipkan dieksekusi, dan kata sandi level 13 pun ditampilkan.

✅ Flag / Password Level 13
yZdkjAYZRd3R7tq7T5kXMjMJlOIkzDeB
