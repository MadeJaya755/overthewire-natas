Natas 14 → 15
🎯 Tujuan
Mendapatkan kata sandi untuk level 15 di OverTheWire Natas.

🔑 Kredensial
Username: natas14

Password: trbs5pCjCrkuSknBBKHhaBxq6Wm1j3LC

URL: http://natas14.natas.labs.overthewire.org

🛠️ Langkah
Analisis Halaman: Halaman Natas 14 memiliki form login sederhana dengan dua kolom: username dan password. Tidak ada fitur unggah file. Ini menandakan bahwa kerentanannya bukanlah tentang file upload, melainkan SQL Injection.

Mengidentifikasi Kerentanan: Saya mencoba menguji kolom input username untuk kerentanan SQL Injection dengan memasukkan karakter khusus.

Input: ' OR 1=1 -- -

Tujuan dari input ini adalah untuk membuat kondisi SQL WHERE menjadi selalu benar, sehingga database mengembalikan semua baris data, termasuk informasi pengguna dan kata sandi.

Melakukan Eksploitasi:

Saya memasukkan ' OR 1=1 --  di kolom username dan kata sandi acak di kolom password.

Server menjalankan kueri SQL yang mirip dengan:

SQL

SELECT * FROM users WHERE username = '' OR 1=1 -- ' AND password = 'kata_sandi_acak';
Karakter -- (dua tanda hubung) pada SQL digunakan untuk membuat komentar. Ini menyebabkan sisa kueri (termasuk validasi kata sandi) diabaikan.

Karena kondisi 1=1 selalu benar, kueri berhasil dieksekusi dan mengembalikan data pengguna, yang mana menampilkan "You are logged in as a regular user." dan tidak memberikan kata sandi.

✅ Flag / Password Level 15
Karena tidak ada kata sandi yang terlihat di halaman, saya tahu bahwa saya harus memodifikasi kueri untuk mengekstrak data yang saya butuhkan.

Mengubah username menjadi kata sandi level 15:

Saya menggunakan metode blind SQL injection untuk mengekstrak data satu per satu.

Saya mengubah input username menjadi ' OR 1=1 UNION SELECT password, NULL FROM users -- 

Kueri ini menggabungkan hasil kueri asli dengan hasil dari SELECT password FROM users, yang seharusnya mengembalikan kata sandi level 15.

Mendapatkan kata sandi:

Setelah mencoba berbagai variasi, akhirnya saya berhasil menemukan kata sandi yang disembunyikan.

z3UYcr4v4uBpeX8f7EZbMHlzK4UR2XtQ
