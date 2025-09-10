Penyelesaian NATAS 12
Tantangan: Natas 12 adalah tantangan file upload vulnerability yang mengharuskan kita mengunggah file berbahaya untuk mendapatkan kata sandi level berikutnya.

Analisis Tantangan:

Halaman web Natas 12 menyediakan sebuah form untuk mengunggah file. Setelah menganalisis fitur ini, ditemukan bahwa server memvalidasi ekstensi file. Jika file yang diunggah tidak memiliki ekstensi yang diizinkan (misalnya, .jpg, .jpeg, .png), unggahan akan ditolak.

Metode Penyelesaian:

Solusi untuk tantangan ini adalah dengan mengakali validasi ekstensi server. Saya menggunakan metode menyipkan kode PHP ke dalam file gambar yang valid.

Membuat File Gambar Berisi Kode PHP:

Saya membuat file gambar bernama malicious.jpg.

Menggunakan editor teks, saya menambahkan kode PHP di akhir file gambar tersebut. Kode ini akan menjalankan perintah sistem untuk membaca file kata sandi (/etc/natas_webpass/natas13).

<?php system('cat /etc/natas_webpass/natas13'); ?>
Tindakan ini tidak merusak integritas file gambar, tetapi kode PHP tersebut tetap bisa dieksekusi oleh server web.

Mengunggah File:

Saya mengunggah file malicious.jpg yang sudah dimodifikasi melalui form yang disediakan. Karena file ini memiliki ekstensi .jpg dan merupakan file gambar yang valid, validasi server terlewati.

Setelah unggahan berhasil, server menyimpan file di direktori tertentu. Biasanya, direktori ini memiliki nama seperti /uploads/ atau /images/.

Mengeksekusi Kode PHP:

Saya menemukan bahwa file yang diunggah disimpan di direktori /uploads/.

Kemudian, saya mengakses file tersebut melalui URL: http://natas12.natas.labs.overthewire.org/uploads/malicious.jpg.

Ketika saya mengakses URL tersebut, server menjalankan kode PHP yang saya sisipkan. Outputnya adalah kata sandi untuk Natas 13.

Kata Sandi untuk Natas 13:

yZdkjAYZRd3R7tq7T5kXMjMJlOIkzDeB
