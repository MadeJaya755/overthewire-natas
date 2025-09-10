Natas 16 → 17
🎯 Tujuan
Mendapatkan kata sandi untuk level 17 di OverTheWire Natas.

🔑 Kredensial
Username: natas16

Password: [kata sandi dari level 15]

URL: http://natas16.natas.labs.overthewire.org

🛠️ Langkah
Analisis Halaman: Halaman Natas 16 menyediakan kotak pencarian. Saat saya memasukkan sebuah kata (misalnya, groot), URL berubah menjadi ?needle=groot, dan halaman menampilkan "groot", menandakan bahwa input saya digunakan dalam beberapa cara. Kerentanan ini adalah Command Injection.

Identifikasi Kerentanan: Saya menggunakan karakter khusus untuk menguji apakah input saya dieksekusi sebagai perintah sistem.

Saya mencoba mencari test; ls.

Outputnya menunjukkan daftar file di direktori, yang mengonfirmasi bahwa perintah ls dieksekusi di server.

Melakukan Serangan Blind Command Injection: Tujuan utama saya adalah mendapatkan kata sandi dari file /etc/natas_webpass/natas17. Saya tidak bisa langsung mengeksekusi cat karena outputnya akan digabungkan dengan output grep dan kemungkinan tidak akan terlihat.

Solusinya adalah menggunakan teknik Blind Command Injection dengan grep. Saya akan menguji setiap karakter kata sandi, satu per satu, dengan membuat perintah yang menghasilkan output yang berbeda.

Saya akan mengotomatisasi proses ini menggunakan skrip Python yang membandingkan panjang output dari grep ketika output dari cat dimasukkan sebagai input.

Skrip Python:

Skrip akan mengirimkan permintaan dengan needle yang dimanipulasi. Payload yang digunakan adalah $(grep -E '^[karakter_yang_ditebak]' /etc/natas_webpass/natas17).

Jika grep menemukan kecocokan, cat akan menghasilkan output, dan panjang respons halaman akan lebih besar.

Skrip akan mengulang proses ini untuk setiap karakter hingga kata sandi lengkap ditemukan.

✅ Flag / Kata Sandi Level 17
[kata sandi untuk Natas 17]
