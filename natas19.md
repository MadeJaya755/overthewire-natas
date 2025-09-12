Natas 19 → 20
🎯 Tujuan
Mendapatkan kata sandi untuk level 20 dengan memanfaatkan SQL Injection pada ID sesi (session_id).

🔑 Kredensial
Username: natas19

Password: 6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ
URL: http://natas19.natas.labs.overthewire.org

🛠️ Langkah
Analisis Halaman: Halaman Natas 19 menampilkan sebuah form login yang rentan. Setelah masuk, saya menemukan bahwa situs ini menggunakan cookie PHPSESSID. Namun, kali ini nilainya bukan angka sederhana, melainkan string panjang yang terdiri dari karakter heksadesimal.

Mengidentifikasi Celah:

Dengan menggunakan Burp Suite, saya mengubah nilai PHPSESSID menjadi berbagai angka.

Ketika saya menyetel PHPSESSID ke 20, halaman menampilkan "You are logged in as user natas20" dan kata sandi untuk level 20. Ini mengonfirmasi bahwa ada kerentanan SQL Injection pada cookie.

Melakukan Eksploitasi:

Saya perlu mencari tahu bagaimana server memproses nilai heksadesimal dari PHPSESSID. Saya menyadari bahwa nilai heksadesimal tersebut digunakan dalam kueri SQL.

Saya menyuntikkan kueri SQL ke dalam cookie PHPSESSID. Payload yang berhasil adalah 20 UNION SELECT "natas20".

Kueri ini menggabungkan hasil kueri asli (SELECT * FROM users WHERE session_id = '20') dengan hasil yang saya sisipkan, yaitu string "natas20".

Mendapatkan Kata Sandi:

Saya mengubah nilai cookie PHPSESSID menjadi 20 UNION SELECT "natas20".

Ketika saya memuat ulang halaman, server menampilkan "You are logged in as user natas20" dan kata sandi untuk level 20 di halaman tersebut.

✅ Flag / Kata Sandi Level 20
tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr

💡 Catatan
Fokus utama dari level ini adalah SQL Injection pada session ID.

Tantangan ini mengajarkan bahwa kerentanan dapat terjadi tidak hanya pada form input yang terlihat, tetapi juga pada data tersembunyi seperti cookie yang digunakan untuk otentikasi.

Penting untuk selalu memeriksa semua parameter yang dikirim ke server, baik melalui URL maupun header HTTP, untuk mencari potensi kerentanan.
