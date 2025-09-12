Natas 18 → 19
🎯 Tujuan
Mendapatkan password untuk level 19 dengan memanfaatkan SQL Injection pada ID sesi (session_id).

🔑 Kredensial
Username: natas18

Password: 6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ
URL: http://natas18.natas.labs.overthewire.org

🛠️ Langkah
Analisis Halaman: Halaman Natas 18 memiliki form login sederhana, tetapi tidak ada parameter yang terlihat di URL. Setelah menganalisis kode sumber, diketahui bahwa situs menggunakan session ID yang disimpan dalam cookie.

Identifikasi Kerentanan:

Saya menggunakan Burp Suite untuk mencegat permintaan HTTP.

Saya menemukan cookie bernama PHPSESSID yang nilainya adalah sebuah angka.

Dengan mengubah nilai PHPSESSID menjadi angka lain, saya bisa mendapatkan pesan "You are logged in as user natas[nomor_id]".

Ketika saya mencoba ID 1-640, server menunjukkan bahwa pengguna natas18 tidak ada, tetapi pengguna lain ada. Ini adalah petunjuk bahwa server memproses ID yang saya berikan dalam kueri SQL.

Melakukan SQL Injection:

Tujuannya adalah untuk membuat kueri SQL menganggap saya sebagai pengguna natas19, sehingga saya bisa mendapatkan kata sandi.

Saya mencoba menyuntikkan kueri SQL ke dalam cookie PHPSESSID.

Payload yang berhasil adalah 19 UNION SELECT "natas19".

Kueri ini akan menggabungkan hasil kueri asli (SELECT * FROM users WHERE session_id = '19') dengan hasil yang saya sisipkan, yaitu string "natas19".

Mendapatkan Kata Sandi:

Saya mengubah nilai cookie PHPSESSID menjadi 19 UNION SELECT "natas19".

Ketika saya merefresh halaman, server menampilkan pesan "You are logged in as user natas19" dan menampilkan kata sandi untuk level 19 di halaman tersebut.

✅ Flag / Kata Sandi Level 19
tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr

💡 Catatan
Fokus utama dari level ini adalah SQL Injection pada session ID.

Tantangan ini mengajarkan bahwa kerentanan dapat terjadi tidak hanya pada form input yang terlihat, tetapi juga pada data tersembunyi seperti cookie yang digunakan untuk otentikasi.

Penting untuk selalu memeriksa semua parameter yang dikirim ke server, baik melalui URL maupun header HTTP, untuk mencari potensi kerentanan.
