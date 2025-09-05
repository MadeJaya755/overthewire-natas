# Natas 5 → 6

## 🎯 Tujuan
Mendapatkan password untuk level 6 di **OverTheWire Natas**.

## 🔑 Kredensial
- Username: `natas5`
- Password: `0n35PkggAPm2zbEpOU802c0x0Msn1ToK`
- URL: [http://natas5.natas.labs.overthewire.org](http://natas5.natas.labs.overthewire.org)

## 🛠️ Langkah
1. Buka halaman Natas 5 di browser.  
   Pesan muncul:
→ Server memakai **cookie** untuk kontrol login.
2. Buka **DevTools → Application → Cookies**.  
Temukan cookie bernama `loggedin` dengan nilai `0`.
3. Ubah nilai cookie `loggedin` dari `0` menjadi `1`.
4. Refresh halaman.  
Sekarang halaman menampilkan password untuk level 6.

## ✅ Flag / Password Level 6
`0RoJwHdSKWFTYR5WuiAewauSuNaBXned`

## 💡 Catatan
- Fokus level ini: **cookie manipulation**.  
- Server hanya mengecek nilai cookie, tanpa validasi di backend → jelas rawan.  
- Cara ini bisa dilakukan dengan:
- Browser DevTools (seperti yang gue pakai di sini).  
- `curl --cookie`.  
- Burp Suite.  
- Script Python `requests`.  
- Pentester harus selalu ngecek cookies/session karena sering jadi pintu bypass otentikasi.
