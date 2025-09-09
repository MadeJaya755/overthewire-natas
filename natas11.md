# Natas 11 → 12

## 🎯 Tujuan
Mendapatkan password untuk level 12 di **OverTheWire Natas**.

## 🔑 Kredensial
- Username: `natas11`
- Password: `UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk`  # dari level 10
- URL: [http://natas11.natas.labs.overthewire.org](http://natas11.natas.labs.overthewire.org)

## 🛠️ Langkah
1. Halaman menggunakan cookie `data(HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg=)` yang terenkripsi dengan XOR + base64.
2. Source code menunjukkan ada key XOR rahasia = (eDWo).
3. Dengan membuat payload `{"showpassword":"yes","bgcolor":"#ffffff"}` lalu XOR dengan key, hasilnya bisa digunakan sebagai cookie baru.
4. Setelah set cookie, reload halaman → password level 12 ditampilkan:

## ✅ Flag / Password Level 12
`yZdkjAYZRd3R7tq7T5kXMjMJlOIkzDeB`

## 💡 Catatan
- Fokus level ini: **XOR encryption misuse**.  
- Kalau key XOR pendek dan plaintext bisa ditebak, key bisa direkonstruksi.  
- Teknik ini sering dipakai untuk bypass session handling lemah.
