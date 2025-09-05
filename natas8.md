# Natas 8 → 9

## 🎯 Tujuan
Mendapatkan password untuk level 9 di **OverTheWire Natas**.

## 🔑 Kredensial
- Username: `natas8`
- Password: `xcoXLmzMkoIP9D7hlgPlh9XD7OgLAe5Q`  # dari level 7
- URL: [http://natas8.natas.labs.overthewire.org](http://natas8.natas.labs.overthewire.org)

## 🛠️ Langkah
1. Lihat source code halaman Natas 8:
   ```php
   <?
   $encodedSecret = "3d3d516343746d4d6d6c315669563362";

   function encodeSecret($secret) {
       return bin2hex(strrev(base64_encode($secret)));
   }

   if(array_key_exists("submit", $_POST)) {
       if(encodeSecret($_POST['secret']) == $encodedSecret) {
           print "Access granted. The password for natas9 is <censored>";
       } else {
           print "Wrong secret";
       }
   }
   ?>
Analisis:

Server membandingkan encodeSecret($_POST['secret']) dengan $encodedSecret.

Fungsi PHP encodeSecret melakukan:

Base64 encode

Reverse string

Konversi ke hexadecimal

Solusi:

Kita bisa decode $encodedSecret untuk mendapatkan secret asli.

Gunakan Python untuk otomatisasi.

✅ Flag / Password Level 9

`ZE1ck82lmdGIoErlhQgWND6j2Wzz6b6t`

💡 Catatan

Fokus level ini: reverse engineer encoding scheme.

Teknik: pahami fungsi PHP, lalu balikkan proses encoding dengan Python.

Pentester sering menemukan mekanisme serupa untuk bypass login atau hidden validation.
