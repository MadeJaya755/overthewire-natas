# Natas 3 → 4

## 🎯 Tujuan
Mendapatkan password untuk level 4 di **OverTheWire Natas**.

## 🔑 Kredensial
- Username: `3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH`
- Password: `<password_natas3>`  # ganti dengan password asli level 3
- URL: [http://natas3.natas.labs.overthewire.org](http://natas3.natas.labs.overthewire.org)

## 🛠️ Langkah
1. Buka halaman Natas 3 di browser.
2. Lihat **robots.txt** dengan menambahkan `/robots.txt` pada URL:
- Di dalamnya ditemukan lokasi rahasia: `/s3cr3t/`
3. Akses folder rahasia `/s3cr3t/`:
4. Temukan file `users.txt` di folder tersebut dan buka isinya.
5. Password untuk level 4 ada di file `users.txt`:

## ✅ Flag / Password Level 4
`QryZXc2e0zahULdHrtHxzyYkj59kUxLQ`

## 💡 Catatan
- Fokus level ini: **menemukan informasi tersembunyi menggunakan robots.txt**.  
- Teknik ini sering digunakan untuk **security testing**: server kadang menaruh folder sensitif tapi “dilarang” di robots.txt, yang bisa dimanfaatkan untuk menemukan data rahasia.  
- Tidak perlu tools tambahan, cukup browser atau script sederhana untuk otomatisasi.
