# Natas 6 → 7

## 🎯 Tujuan
Mendapatkan password untuk level 7 di **OverTheWire Natas**.

## 🔑 Kredensial
- Username: `natas6`
- Password: `0RoJwHdSKWFTYR5WuiAewauSuNaBXned`  # dari level 5
- URL: [http://natas6.natas.labs.overthewire.org](http://natas6.natas.labs.overthewire.org)

## 🛠️ Langkah
1. Buka halaman Natas 6 di browser.  
   Terlihat form untuk memasukkan **secret**.
2. Analisis halaman:
   - Ada file `includes/secret.inc` yang menyimpan password level 7.
   - Server memeriksa:
     - Apakah key `submit` ada di POST request
     - Apakah value dari variabel `secret` sama dengan isi `includes/secret.inc`
3. Cara menemukan password:
   - Coba akses file langsung:
     ```
     http://natas6.natas.labs.overthewire.org/includes/secret.inc
     ```
   - Yup, isi file bisa diakses → dapat secret.
4. Submit value dari file tersebut di form sebagai `secret` → password level 7 ditampilkan:

## ✅ Flag / Password Level 7
`bmg8SvU1LizuWjx3y7xkNERkHxGre0GS`

## 💡 Catatan
- Fokus level ini: **exposed secret file / insecure inclusion**.  
- Praktik buruk developer: menaruh file sensitif di direktori publik.  
- Pentester harus selalu cek:
- Direktori `includes/` atau file `.inc`, `.bak`, `.old`
- Parameter POST/GET untuk input validasi
- Tools: browser biasa atau script Python untuk otomatisasi POST.
