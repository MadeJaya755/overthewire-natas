# Natas 10 → 11

## 🎯 Tujuan
Mendapatkan password untuk level 11 di **OverTheWire Natas**.

## 🔑 Kredensial
- Username: `natas10`
- Password: `t7I5VHvpa14sJTUGV0cbEsbYfFP2dmOu`  # dari level 9
- URL: [http://natas10.natas.labs.overthewire.org](http://natas10.natas.labs.overthewire.org)

## 🛠️ Langkah
1. Input user dipakai langsung di command `grep`, tetapi karakter berbahaya `;`, `&`, `|` difilter.
2. Gunakan trik opsi bawaan `grep` untuk membaca file sensitif.
3. Payload:Payload:-a /etc/natas_webpass/natas11 
4. Output menampilkan password level 11:

## ✅ Flag / Password Level 11
`UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk`

## 💡 Catatan
- Fokus level ini: **command injection filter bypass** dengan **options abuse**.  
- `grep -a file` artinya treat file as text, sehingga isinya langsung keluar.  

