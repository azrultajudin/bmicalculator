# Kerja Kursus Asas Sains Komputer (ASK) Tingkatan 2
## Projek: Atur Cara Pengiraan Body Mass Index (BMI)

**Nama:** ______________  **Tingkatan:** 2 ______  **Sekolah:** ______________  **Guru:** ______________

---

## 1.0 Pendahuluan

Body Mass Index (BMI) ialah ukuran mudah yang membandingkan berat badan seseorang dengan ketinggiannya. Nilai BMI digunakan secara meluas untuk menyaring sama ada seseorang berada dalam kategori kurang berat, normal, lebih berat atau obes. Formula yang digunakan ialah:

> **BMI = berat (kg) ÷ [tinggi (m)]²**

Atur cara ini dibina berdasarkan pemerhatian dan kajian. Pemerhatian dibuat terhadap cara pengguna di gim, klinik dan hospital mengira BMI, serta kajian terhadap beberapa laman web kalkulator BMI di internet. Hasil pemerhatian mendapati pengiraan secara manual mengambil masa, mudah tersilap dan tidak disertakan nasihat kesihatan. Kajian terhadap laman web pula menunjukkan kalkulator yang baik perlu mudah digunakan, memaparkan status BMI dengan jelas dan memberi nasihat yang sesuai.

Oleh itu, atur cara ini dibangunkan dalam bahasa pengaturcaraan Python dengan ciri-ciri berikut:

1. Pilihan dua bahasa (Bahasa Malaysia dan English).
2. Menerima input nama, jantina, umur, berat (kg) dan tinggi (cm).
3. Mengira BMI, menentukan status dan memberi nasihat penjagaan kesihatan serta diet.
4. Membenarkan pengguna mengira BMI orang lain tanpa memulakan semula atur cara.

**Objektif projek:** membina atur cara yang mudah, pantas dan tepat untuk mengira BMI serta memberi nasihat kesihatan asas.

**Skop:** atur cara menggunakan kategori BMI dewasa Pertubuhan Kesihatan Sedunia (WHO) sebagai rujukan saringan awal sahaja dan bukan diagnosis perubatan.

| Status | Julat BMI |
|---|---|
| Kurang berat (Underweight) | kurang daripada 18.5 |
| Normal | 18.5 hingga 24.9 |
| Lebih berat (Overweight) | 25.0 hingga 29.9 |
| Obesiti (Obese) | 30.0 dan ke atas |

---

## 3.0 Pelaporan Penggunaan Teknik Pemikiran Komputasional

### Fasa 1: Analisis Masalah

| Teknik | Penerangan penggunaan |
|---|---|
| **Leraian** | Masalah besar "bina kalkulator BMI" dipecahkan kepada bahagian kecil: (a) pilih bahasa, (b) ambil input pengguna, (c) kira BMI, (d) tentukan status, (e) beri nasihat, (f) ulang untuk orang lain. |
| **Pengecaman Corak** | Semua kalkulator BMI yang dikaji mempunyai corak sama: input berat dan tinggi → formula → bandingkan dengan julat → papar status. Pengesahan input juga berulang: tanya, semak, tanya semula jika salah. |
| **Peniskalaan** | Hanya data penting diambil: nama, jantina, umur, berat dan tinggi. Butiran yang tidak perlu (seperti alamat dan nombor telefon) diabaikan. |
| **Pengitlakan** | Satu kaedah pengiraan yang sama boleh digunakan untuk semua orang. Kaedah ini juga boleh digunakan di gim, klinik dan hospital. |

### Fasa 2: Reka Bentuk Atur Cara

| Teknik | Penerangan penggunaan |
|---|---|
| **Leraian** | Setiap bahagian ditukar kepada satu fungsi: `pilih_bahasa`, `ambil_input`, `kira_bmi`, `tentukan_status`, `cetak_hasil_bmi`, `tanya_lagi` dan `main`. Pseudokod dan carta alir dilukis bagi setiap fungsi. |
| **Pengecaman Corak** | Corak gelung digunakan berulang kali: gelung `while True` untuk pengesahan input dan gelung utama untuk mengira BMI orang lain. Semua julat BMI mengikut corak syarat `jika ... lain jika ...`. |
| **Peniskalaan** | Paparan dibuat ringkas dalam bentuk teks (tanpa grafik) supaya mudah difahami dan berjalan pada komputer biasa. Hanya hasil penting dipaparkan: BMI, status dan nasihat. |
| **Pengitlakan** | Semua teks disimpan dalam satu kamus `TEKS` (bahasa `ms` dan `en`). Fungsi yang sama digunakan untuk kedua-dua bahasa, dan bahasa baharu boleh ditambah tanpa mengubah logik pengiraan. |

### Fasa 3: Pengekodan

| Teknik | Penerangan penggunaan |
|---|---|
| **Leraian** | Kod ditulis satu fungsi pada satu masa dan diuji sebelum fungsi seterusnya ditulis. Ini memudahkan pencarian kesilapan. |
| **Pengecaman Corak** | Fungsi `baca_nombor` ditulis sekali dan digunakan semula untuk umur, berat dan tinggi kerana ketiga-tiganya mempunyai corak sama (baca, tukar kepada nombor, semak julat). |
| **Peniskalaan** | Hanya modul standard Python digunakan. Tiada pemasangan tambahan diperlukan. Pemboleh ubah diberi nama jelas seperti `berat`, `tinggi` dan `bmi`. |
| **Pengitlakan** | Fungsi `kira_bmi(berat, tinggi_cm)` menerima sebarang nilai berat dan tinggi. Fungsi `cetak_hasil_bmi(t, ...)` menerima kamus bahasa `t` sebagai parameter supaya boleh memaparkan hasil dalam bahasa apa pun. |

### Fasa 4: Pengujian dan Penyahpepijatan

| Teknik | Penerangan penggunaan |
|---|---|
| **Leraian** | Setiap fungsi diuji secara berasingan (contoh: `kira_bmi(70, 175)` memberi 22.86), kemudian seluruh atur cara diuji bersama. |
| **Pengecaman Corak** | Ralat yang berulang dikenal pasti, contohnya input huruf menyebabkan `ValueError`, input kosong, nombor negatif dan koma perpuluhan (65,5). Semuanya diselesaikan dengan pengesahan input yang sama. |
| **Peniskalaan** | Ujian tertumpu pada kes penting: nilai sempadan 18.5, 25 dan 30, input tidak sah dan pengulangan atur cara. |
| **Pengitlakan** | Satu set kes ujian digunakan untuk kedua-dua bahasa dan semua jantina. Penyelesaian ralat dilakukan pada fungsi umum supaya penyelesaian itu terpakai untuk semua input. |

### Jadual Pengujian

| No. | Kes ujian | Input | Hasil dijangka | Hasil sebenar |
|---|---|---|---|---|
| 1 | Pilihan bahasa tidak sah | `9` kemudian `1` | Mesej ralat, minta semula | Lulus |
| 2 | Nama kosong | (tekan Enter) kemudian `Ali` | Mesej ralat, minta semula | Lulus |
| 3 | Jantina tidak sah | `x` kemudian `L` | Mesej ralat, minta semula | Lulus |
| 4 | Umur huruf | `abc` kemudian `14` | Mesej ralat, minta semula | Lulus |
| 5 | Berat negatif / sifar | `-5`, `0` kemudian `65,5` | Mesej ralat, koma diterima | Lulus (65.5 kg) |
| 6 | Tinggi di luar julat | `10` kemudian `170` | Mesej ralat, minta semula | Lulus |
| 7 | BMI 65.5 kg, 170 cm | - | 22.7, Normal | 22.7, Normal |
| 8 | BMI 40 kg, 160 cm | - | 15.6, Kurang berat | 15.6, Kurang berat |
| 9 | BMI 110 kg, 170 cm | - | 38.1, Obesiti | 38.1, Obese |
| 10 | Sempadan BMI 18.49 / 18.5 | - | Kurang / Normal | Kurang / Normal |
| 11 | Sempadan BMI 24.99 / 25 | - | Normal / Lebih berat | Normal / Lebih berat |
| 12 | Sempadan BMI 29.99 / 30 | - | Lebih berat / Obesiti | Lebih berat / Obesiti |
| 13 | Jawapan ulang tidak sah | `maybe`, `y`, kemudian `t` | Ralat, ulang, tamat | Lulus |
| 14 | Bahasa English | `2` | Semua mesej dalam English | Lulus |
| 15 | Umur kurang 19 tahun | `13` | Nota anggaran dipaparkan | Lulus |

---

## Pseudokod

```
FUNGSI pilih_bahasa()
    PAPAR "1. Bahasa Malaysia", "2. English"
    ULANG SELAMA BENAR
        BACA pilihan
        JIKA pilihan = "1" MAKA
            PULANG "ms"
        LAIN JIKA pilihan = "2" MAKA
            PULANG "en"
        LAIN
            PAPAR "Pilihan tidak sah"
        TAMAT JIKA
    TAMAT ULANG
TAMAT FUNGSI
```

```
FUNGSI baca_nombor(soalan, ralat, minimum, maksimum, bulat)
    ULANG SELAMA BENAR
        BACA nilai
        TUKAR koma (,) kepada titik (.)
        CUBA
            JIKA bulat MAKA nombor = BULAT(nilai) LAIN nombor = PERPULUHAN(nilai)
        JIKA GAGAL
            PAPAR ralat
            ULANG dari awal
        JIKA nombor < minimum ATAU nombor > maksimum MAKA
            PAPAR ralat
            ULANG dari awal
        PULANG nombor
    TAMAT ULANG
TAMAT FUNGSI
```

```
FUNGSI ambil_input(t)
    ULANG SELAMA BENAR
        BACA nama
        JIKA nama TIDAK kosong MAKA KELUAR gelung
        PAPAR "Nama tidak boleh kosong"
    TAMAT ULANG

    ULANG SELAMA BENAR
        BACA jantina
        JIKA jantina = "L" ATAU "M" MAKA jantina = "Lelaki", KELUAR gelung
        JIKA jantina = "P" ATAU "F" MAKA jantina = "Perempuan", KELUAR gelung
        PAPAR "Sila masukkan L atau P"
    TAMAT ULANG

    umur   = baca_nombor("Umur", ..., 1, 120, bulat = BENAR)
    berat  = baca_nombor("Berat (kg)", ..., 1, 500, bulat = PALSU)
    tinggi = baca_nombor("Tinggi (cm)", ..., 50, 272, bulat = PALSU)

    PULANG nama, jantina, umur, berat, tinggi
TAMAT FUNGSI
```

```
FUNGSI kira_bmi(berat, tinggi_cm)
    tinggi_m = tinggi_cm / 100
    bmi = berat / (tinggi_m * tinggi_m)
    PULANG bmi
TAMAT FUNGSI
```

```
FUNGSI tentukan_status(bmi)
    JIKA bmi < 18.5 MAKA
        PULANG "kurang"
    LAIN JIKA bmi < 25 MAKA
        PULANG "normal"
    LAIN JIKA bmi < 30 MAKA
        PULANG "lebih"
    LAIN
        PULANG "obes"
    TAMAT JIKA
TAMAT FUNGSI
```

```
FUNGSI cetak_hasil_bmi(t, nama, jantina, umur, berat, tinggi, bmi, status)
    PAPAR tajuk "HASIL PENGIRAAN BMI"
    PAPAR nama, jantina, umur, berat, tinggi
    PAPAR bmi (satu tempat perpuluhan)
    PAPAR nama status daripada t[status]
    PAPAR nasihat penjagaan kesihatan dan diet daripada t["nasihat_" + status]
    JIKA umur < 19 MAKA
        PAPAR nota "kategori ini hanyalah anggaran"
    TAMAT JIKA
TAMAT FUNGSI
```

```
FUNGSI tanya_lagi(t)
    ULANG SELAMA BENAR
        BACA jawapan
        JIKA jawapan = "y" ATAU "ya" MAKA PULANG BENAR
        JIKA jawapan = "t" ATAU "tidak" MAKA PULANG PALSU
        PAPAR "Sila jawab y atau t"
    TAMAT ULANG
TAMAT FUNGSI
```

```
FUNGSI main()
    bahasa = pilih_bahasa()
    t = TEKS[bahasa]
    ULANG
        nama, jantina, umur, berat, tinggi = ambil_input(t)
        bmi = kira_bmi(berat, tinggi)
        status = tentukan_status(bmi)
        cetak_hasil_bmi(t, nama, jantina, umur, berat, tinggi, bmi, status)
        lagi = tanya_lagi(t)
    SELAMA lagi = BENAR
    PAPAR mesej terima kasih
TAMAT FUNGSI

MULA
    main()
TAMAT
```

---

## 5.0 Penutup

Kesimpulannya, atur cara pengiraan BMI yang dibina berjaya mengira BMI, menentukan status dan memberi nasihat kesihatan dalam dua bahasa. Melalui empat teknik pemikiran komputasional (leraian, pengecaman corak, peniskalaan dan pengitlakan), masalah dapat diselesaikan secara tersusun daripada analisis hingga pengujian.

Teknologi pengiraan BMI di internet banyak memudahkan urusan pengguna di gim dan fasiliti kesihatan seperti klinik dan hospital. Pengguna tidak perlu mengira secara manual, jadi keputusan diperoleh dengan lebih cepat dan kesilapan pengiraan dapat dikurangkan. Jurulatih gim boleh menetapkan program latihan dan diet dengan lebih pantas. Pegawai di klinik dan hospital pula dapat membuat saringan awal pesakit dengan mudah sebelum pemeriksaan lanjut dan menjimatkan masa menunggu. Pengguna biasa juga boleh memantau berat badan sendiri di rumah pada bila-bila masa.

Walau bagaimanapun, BMI hanyalah alat saringan awal. Ia tidak mengambil kira otot, tulang dan umur (terutamanya bagi remaja), maka keputusan perlu dirujuk kepada doktor atau pegawai kesihatan. Pada masa depan, atur cara ini boleh ditambah baik dengan paparan grafik, penyimpanan rekod dan carta BMI mengikut umur.

---

## 6.0 Lampiran

### Lampiran A: Keperluan Sistem Pengendalian

- Windows 98
- Windows XP
- Windows Vista dan ke atas (Windows 7, 8, 10, 11)
- macOS
- Linux

*Catatan:* Atur cara Python dalam projek ini memerlukan Python 3. Python 3 versi terkini berjalan pada Windows 10/11, macOS dan Linux. Untuk sistem lama (Windows 98 dan XP), kalkulator BMI dalam talian yang diakses melalui penyemak imbas web yang disokong oleh sistem tersebut digunakan sebagai rujukan kajian.

### Lampiran B: Keperluan Perisian

- Penyemak imbas web: Google Chrome, Microsoft Edge, Opera dan lain-lain
- Python 3 (untuk menjalankan fail `bmi.py`)
- Penyunting kod: IDLE (disertakan bersama Python), Notepad atau Visual Studio Code

### Lampiran C: Keperluan Memori Minimum

- RAM minimum: **2GB**
- Memori tersedia (kosong) untuk menjalankan atur cara: **256MB**

### Lampiran D: Cara Menjalankan Atur Cara

1. Pasang Python 3 daripada python.org.
2. Simpan fail `bmi.py` dalam satu folder.
3. Buka terminal / Command Prompt dalam folder tersebut.
4. Taip: `python bmi.py` (atau `python3 bmi.py` pada macOS / Linux).
5. Pilih bahasa dan ikut arahan pada skrin.
