Perjalanan Menaklukkan Natas: OverTheWire
Perjalanan saya menaklukkan Natas adalah serangkaian tantangan yang menguji pemahaman saya tentang keamanan web. Setiap level adalah sebuah puzzle yang mengasah kemampuan sebagai seorang pentester, mulai dari kerentanan dasar hingga trik eksploitasi yang lebih kompleks.

🔒 Level 0 → 1: View Source Code
Kerentanan: Kata sandi untuk level 1 disembunyikan dalam kode sumber halaman HTML.

Penyelesaian: Menggunakan fitur View Page Source pada peramban web atau curl untuk melihat kode HTML dan menemukan kata sandi yang disematkan dalam komentar.

🔒 Level 1 → 2: No Right Click
Kerentanan: Menu klik kanan dinonaktifkan untuk menyembunyikan kode sumber.

Penyelesaian: Menggunakan pintasan keyboard (misalnya, Ctrl + U atau ⌘ + U) atau developer tools peramban untuk melihat kode sumber, yang mengungkapkan kata sandi.

🔒 Level 2 → 3: Directory Traversal
Kerentanan: Halaman tidak menampilkan konten, tetapi ada petunjuk untuk file users.txt.

Penyelesaian: Menggunakan robots.txt untuk menemukan direktori yang diizinkan untuk diakses oleh web crawler. Direktori tersebut berisi file yang menyembunyikan kata sandi.

🔒 Level 3 → 4: Referer Header
Kerentanan: Akses ke halaman selanjutnya hanya diizinkan jika permintaan HTTP berasal dari sumber tertentu (dalam hal ini, dari situs Natas 3).

Penyelesaian: Menggunakan curl atau Burp Suite untuk memanipulasi HTTP header Referer, dengan menyetel nilainya ke http://natas3.natas.labs.overthewire.org/.

🔒 Level 4 → 5: Authentication with Cookies
Kerentanan: Situs menggunakan cookie untuk otentikasi. Nilai cookie yang benar akan memberikan akses.

Penyelesaian: Menggunakan developer tools peramban atau Burp Suite untuk memanipulasi nilai cookie loggedin dari 0 menjadi 1, sehingga situs menganggap saya sebagai pengguna yang terautentikasi.

🔒 Level 5 → 6: SQL Injection with Hidden Parameter
Kerentanan: Terdapat parameter tersembunyi yang rentan terhadap SQL Injection.

Penyelesaian: Menggunakan inspeksi elemen untuk menemukan parameter secret yang disembunyikan. Menyuntikkan kueri SQL seperti ' UNION SELECT 1 -- untuk melewati otentikasi dan mendapatkan kata sandi.

🔒 Level 6 → 7: File Inclusion
Kerentanan: Parameter page di URL rentan terhadap Local File Inclusion (LFI).

Penyelesaian: Menggunakan directory traversal (../) untuk mengakses file di luar direktori web, seperti ../../../../etc/natas_webpass/natas8, yang berisi kata sandi.

🔒 Level 7 → 8: Remote Code Execution
Kerentanan: Server memungkinkan Remote Code Execution (RCE) melalui input.

Penyelesaian: Menggunakan simbol | atau ; untuk menyuntikkan perintah baru, misalnya | ls -la untuk menampilkan daftar direktori dan menemukan lokasi file rahasia.

🔒 Level 8 → 9: Command Injection with Blacklisting
Kerentanan: Serupa dengan level 7, tetapi dengan filter kata-kata yang memblokir perintah umum.

Penyelesaian: Menggunakan metode bypass, seperti cat yang dienkode dalam heksadesimal atau ASCII, untuk melewati filter dan mengeksekusi perintah.

🔒 Level 9 → 10: Cross-Site Scripting (XSS)
Kerentanan: Input pengguna tidak disanitasi dengan benar, membuatnya rentan terhadap XSS.

Penyelesaian: Menyuntikkan skrip berbahaya seperti <script>alert('XSS');</script> untuk membuktikan kerentanan, lalu memanipulasinya untuk mendapatkan cookie yang berisi kata sandi.

🔒 Level 10 → 11: HTTP Parameter Pollution
Kerentanan: Server tidak menangani parameter HTTP duplikat dengan benar.

Penyelesaian: Mengirim dua parameter dengan nama yang sama, misalnya ?param=value1&param=value2. Server mungkin akan memproses keduanya, memungkinkan kita untuk memanipulasi logika aplikasi dan mendapatkan kata sandi.

🔒 Level 11 → 12: File Upload Vulnerability
Kerentanan: Server tidak memvalidasi jenis file yang diunggah dengan benar, memungkinkan unggahan file PHP berbahaya.

Penyelesaian: Mengunggah file dengan ekstensi ganda (misalnya, shell.php.jpg) atau menyisipkan kode PHP ke dalam file gambar yang valid untuk dieksekusi oleh server.

🔒 Level 12 → 13: Blind SQL Injection
Kerentanan: Situs rentan terhadap SQL Injection pada form login, tetapi respons server tidak menampilkan hasil kueri secara langsung (blind).

Penyelesaian: Menggunakan boolean-based blind SQL Injection dengan kueri seperti ' OR SUBSTRING(password, 1, 1) = 'a'-- dan mengotomatisasi prosesnya dengan skrip untuk menebak kata sandi, karakter per karakter.

🔒 Level 13 → 14: Command Injection
Kerentanan: Input pencarian rentan terhadap Command Injection dengan filter yang lemah.

Penyelesaian: Menyuntikkan perintah ke dalam string pencarian untuk dieksekusi oleh server, misalnya | cat /etc/natas_webpass/natas15.

🔒 Level 14 → 15: Command Injection with Blacklisting
Kerentanan: Mirip dengan level 13, tetapi dengan filter kata-kata yang lebih ketat.

Penyelesaian: Menggunakan trik bypass seperti cat yang dienkode dalam heksadesimal atau menggunakan karakter wildcard seperti * untuk melewati filter dan mengeksekusi perintah.

---

### 🔒 Level 15 → 16: Blind SQL Injection

* **Kerentanan:** Halaman ini rentan terhadap **Blind SQL Injection**. Respons server hanya memberikan pesan "user exists" atau "user does not exist" tanpa menampilkan data sensitif.
* **Penyelesaian:** Gunakan **skrip Python** untuk menebak kata sandi, karakter per karakter. Skrip akan mengirimkan kueri yang menguji setiap huruf dan angka. Respons `user exists` mengonfirmasi tebakan yang benar, memungkinkan kita untuk membangun kata sandi lengkap.

---

### 🔒 Level 16 → 17: Blind Command Injection

* **Kerentanan:** Input pencarian rentan terhadap **Command Injection** dengan filter yang memblokir karakter dan kata kunci tertentu.
* **Penyelesaian:** Gunakan trik *bypass* seperti `$(...)` atau *backticks* (``) untuk menyuntikkan perintah. Skrip dapat mengukur panjang respons atau mengecek pesan *error* untuk menebak kata sandi, karakter per karakter, hingga lengkap.

---

### 🔒 Level 17 → 18: Time-Based Blind SQL Injection

* **Kerentanan:** Kerentanan **SQL Injection** yang lebih canggih di mana tidak ada perbedaan pada respons server. Satu-satunya petunjuk adalah waktu responsnya.
* **Penyelesaian:** Gunakan **Blind SQL Injection** berbasis waktu. Skrip Python menyuntikkan fungsi `SLEEP()` atau `BENCHMARK()` yang hanya akan dieksekusi jika tebakan karakter kata sandi benar. Waktu respons yang lebih lama menandakan tebakan yang tepat.

---

### 🔒 Level 18 → 19: Session ID Manipulation

* **Kerentanan:** Halaman menggunakan **cookie** `PHPSESSID` untuk mengidentifikasi pengguna, dan nilainya digunakan dalam kueri SQL yang rentan.
* **Penyelesaian:** Ubah nilai *cookie* `PHPSESSID` secara manual (misalnya, melalui Burp Suite) menjadi `19` untuk berpura-pura menjadi pengguna berikutnya (`natas19`).

---

### 🔒 Level 19 → 20: Session ID with Hexadecimal

* **Kerentanan:** Mirip dengan level 18, tetapi nilai `PHPSESSID` dienkode dalam **heksadesimal**.
* **Penyelesaian:** Ubah nilai heksadesimal dari `PHPSESSID` untuk menyuntikkan `UNION SELECT` atau langsung ubah nilai ID pengguna menjadi `20` untuk mendapatkan akses ke akun `natas20`.
