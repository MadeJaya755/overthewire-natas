# Natas 12 → 13

## 🎯 Tujuan
Mendapatkan password untuk level 13 di **OverTheWire Natas**.

## 🔑 Kredensial
- Username: `natas12`
- Password: `yZdkjAYZRd3R7tq7T5kXMjMJlOIkzDeB`  # dari level 11
- URL: [http://natas12.natas.labs.overthewire.org](http://natas12.natas.labs.overthewire.org)

## 🛠️ Langkah
1. Halaman menyediakan form upload file.
2. Filter membatasi ekstensi, misal hanya `.txt`.
3. Teknik bypass:
   - Upload **file PHP** yang diberi ekstensi `.php5` atau `.phtml`.
   - File berisi kode PHP sederhana untuk mengeksekusi perintah atau membaca file `/etc/natas_webpass/natas13`.
4. Akses file yang diupload lewat URL → server mengeksekusi PHP → password level 13 ditampilkan:

## ✅ Flag / Password Level 13
`yZdkjAYZRd3R7tq7T5kXMjMJlOIkzDeB`

## 💡 Catatan
- Fokus level ini: **file upload exploit**.  
- Pentester harus selalu cek:
- Filter ekstensi file
- Direktori upload
- Eksekusi file server-side
- Teknik ini biasa untuk **Remote Code Execution (RCE)**.
