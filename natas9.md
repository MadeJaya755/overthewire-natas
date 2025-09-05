# Natas 9 → 10

## 🎯 Tujuan
Mendapatkan password untuk level 10 di **OverTheWire Natas**.

## 🔑 Kredensial
- Username: `natas9`
- Password: `ZE1ck82lmdGIoErlhQgWND6j2Wzz6b6t`  # dari level 8
- URL: [http://natas9.natas.labs.overthewire.org](http://natas9.natas.labs.overthewire.org)

## 🛠️ Langkah
1. Masuk ke server Natas 9.
2. Gunakan **dictionary attack** untuk menemukan password level 10:
   ```bash
   grep -i foo dictionary.txt
   cat /etc/natas_webpass/natas10
✅ Flag / Password Level 10

t7I5VHvpa14sJTUGV0cbEsbYfFP2dmOu

💡 Catatan

Fokus level ini: brute force / dictionary enumeration.

Pentester sering menggunakan teknik ini untuk mengecek password sederhana atau common words.

Tools: grep, cat, script Python untuk automatisasi.
