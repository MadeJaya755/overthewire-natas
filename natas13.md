Tentu, saya akan buatkan dokumentasi untuk penyelesaian Natas 13 dalam format yang sama.

Natas 13 → 14
🎯 Tujuan
Mendapatkan password untuk level 14 di OverTheWire Natas.

🔑 Kredensial
Username: natas13

Password: yZdkjAYZRd3R7tq7T5kXMjMJlOIkzDeB

URL: http://natas13.natas.labs.overthewire.org

🛠️ Langkah
Analisis Celah: Halaman ini memiliki form unggah file yang serupa dengan Natas 12. Namun, kali ini filter validasinya jauh lebih ketat. Server menggunakan fungsi exif_imagetype() yang memeriksa beberapa byte pertama file (magic bytes) untuk memastikan file yang diunggah benar-benar sebuah gambar (seperti JPEG atau GIF).

Membuat Payload Khusus: Saya tidak bisa langsung mengunggah file PHP. Oleh karena itu, saya membuat file yang memiliki magic bytes valid di awal, diikuti dengan kode PHP.

Saya membuat file bernama shell.gif dengan konten berikut. GIF87a adalah magic bytes untuk file GIF.

GIF87a
<?php system('cat /etc/natas_webpass/natas14'); ?>
Kode PHP system('cat /etc/natas_webpass/natas14') berfungsi untuk membaca kata sandi level berikutnya.

Unggah dan Eksploitasi:

Saya mengunggah file shell.gif yang sudah saya siapkan. Karena file ini memiliki magic bytes yang valid, validasi exif_imagetype() berhasil dilewati.

Setelah unggahan berhasil, file disimpan di direktori /uploads/.

Saya mengakses file tersebut melalui URL: http://natas13.natas.labs.overthewire.org/uploads/shell.gif.

Server mengeksekusi kode PHP di dalam file GIF, dan kata sandi untuk level 14 pun ditampilkan.

✅ Flag / Password Level 14
trbs5pCjCrkuSknBBKHhaBxq6Wm1j3LC
