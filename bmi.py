"""Atur cara Pengiraan Body Mass Index (BMI) / BMI Calculator Program.

Kerja Kursus Asas Sains Komputer (ASK) Tingkatan 2.
Dwibahasa: Bahasa Malaysia dan English.
"""

TEKS = {
    "ms": {
        "tajuk": "KALKULATOR BMI",
        "ralat_pilihan": "Pilihan tidak sah. Sila masukkan 1 atau 2.",
        "nama": "Nama                : ",
        "jantina": "Jantina (L/P)       : ",
        "umur": "Umur (tahun)        : ",
        "berat": "Berat (kg)          : ",
        "tinggi": "Tinggi (cm)         : ",
        "ralat_nama": "Nama tidak boleh kosong.",
        "ralat_jantina": "Sila masukkan L (lelaki) atau P (perempuan).",
        "ralat_umur": "Umur mesti nombor bulat antara 1 hingga 120.",
        "ralat_berat": "Berat mesti nombor antara 1 hingga 500 kg.",
        "ralat_tinggi": "Tinggi mesti nombor antara 50 hingga 272 cm.",
        "lelaki": "Lelaki",
        "perempuan": "Perempuan",
        "hasil": "HASIL PENGIRAAN BMI",
        "l_nama": "Nama",
        "l_jantina": "Jantina",
        "l_umur": "Umur",
        "l_berat": "Berat",
        "l_tinggi": "Tinggi",
        "l_bmi": "BMI",
        "l_status": "Status",
        "l_nasihat": "Nasihat",
        "tahun": "tahun",
        "nota_remaja": (
            "Nota: Anda berumur kurang daripada 19 tahun. Kategori di atas "
            "hanyalah anggaran. Doktor menggunakan carta BMI mengikut umur."
        ),
        "kurang": "Kurang berat (Underweight)",
        "normal": "Normal",
        "lebih": "Lebih berat (Overweight)",
        "obes": "Obesiti (Obese)",
        "nasihat_kurang": (
            "Tambah pengambilan makanan berkhasiat seperti protein (telur, "
            "ikan, ayam, kekacang), karbohidrat kompleks dan susu. Makan "
            "lebih kerap dalam kuantiti sederhana dan lakukan senaman "
            "kekuatan ringan."
        ),
        "nasihat_normal": (
            "Tahniah! Kekalkan pemakanan seimbang mengikut Pinggan "
            "Sihat Malaysia, minum air secukupnya, bersenam sekurang-"
            "kurangnya 150 minit seminggu dan tidur yang cukup."
        ),
        "nasihat_lebih": (
            "Kurangkan makanan bergoreng, minuman bergula dan makanan "
            "segera. Perbanyakkan sayur dan buah, pilih nasi dalam kuantiti "
            "sederhana, dan bersenam (berjalan pantas, berbasikal, "
            "berenang) setiap hari."
        ),
        "nasihat_obes": (
            "Dapatkan nasihat doktor atau pegawai dietetik. Kawal kalori "
            "harian, elakkan makanan berlemak dan bergula, dan mulakan "
            "senaman ringan secara berperingkat. Pemeriksaan kesihatan "
            "berkala disyorkan."
        ),
        "lagi": "Kira BMI orang lain? (y/t): ",
        "ya": ("y", "ya"),
        "tidak": ("t", "tidak"),
        "ralat_lagi": "Sila jawab y (ya) atau t (tidak).",
        "tamat": "Terima kasih kerana menggunakan Kalkulator BMI. Jaga kesihatan anda!",
    },
    "en": {
        "tajuk": "BMI CALCULATOR",
        "ralat_pilihan": "Invalid choice. Please enter 1 or 2.",
        "nama": "Name                : ",
        "jantina": "Gender (M/F)        : ",
        "umur": "Age (years)         : ",
        "berat": "Weight (kg)         : ",
        "tinggi": "Height (cm)         : ",
        "ralat_nama": "Name cannot be empty.",
        "ralat_jantina": "Please enter M (male) or F (female).",
        "ralat_umur": "Age must be a whole number between 1 and 120.",
        "ralat_berat": "Weight must be a number between 1 and 500 kg.",
        "ralat_tinggi": "Height must be a number between 50 and 272 cm.",
        "lelaki": "Male",
        "perempuan": "Female",
        "hasil": "BMI RESULT",
        "l_nama": "Name",
        "l_jantina": "Gender",
        "l_umur": "Age",
        "l_berat": "Weight",
        "l_tinggi": "Height",
        "l_bmi": "BMI",
        "l_status": "Status",
        "l_nasihat": "Advice",
        "tahun": "years",
        "nota_remaja": (
            "Note: You are under 19 years old. The category above is only "
            "an estimate. Doctors use BMI-for-age charts instead."
        ),
        "kurang": "Underweight",
        "normal": "Normal",
        "lebih": "Overweight",
        "obes": "Obese",
        "nasihat_kurang": (
            "Eat more nutritious food such as protein (eggs, fish, chicken, "
            "legumes), complex carbohydrates and milk. Eat more often in "
            "moderate portions and do light strength exercises."
        ),
        "nasihat_normal": (
            "Well done! Keep a balanced diet following the Malaysian Healthy "
            "Plate, drink enough water, exercise at least 150 minutes a "
            "week and get enough sleep."
        ),
        "nasihat_lebih": (
            "Cut down on fried food, sugary drinks and fast food. Eat more "
            "vegetables and fruit, take moderate portions of rice, and "
            "exercise (brisk walking, cycling, swimming) every day."
        ),
        "nasihat_obes": (
            "Seek advice from a doctor or dietitian. Control your daily "
            "calories, avoid fatty and sugary food, and start light "
            "exercise gradually. Regular health check-ups are recommended."
        ),
        "lagi": "Calculate BMI for another person? (y/n): ",
        "ya": ("y", "yes"),
        "tidak": ("n", "no"),
        "ralat_lagi": "Please answer y (yes) or n (no).",
        "tamat": "Thank you for using the BMI Calculator. Stay healthy!",
    },
}

GARIS = "=" * 60


def pilih_bahasa():
    """Minta pengguna memilih bahasa; ulang sehingga pilihan sah."""
    print(GARIS)
    print("   BMI CALCULATOR / KALKULATOR BMI")
    print(GARIS)
    print("1. Bahasa Malaysia")
    print("2. English")
    while True:
        pilihan = input("Pilih / Choose (1/2): ").strip()
        if pilihan == "1":
            return "ms"
        if pilihan == "2":
            return "en"
        print(TEKS["ms"]["ralat_pilihan"], "/", TEKS["en"]["ralat_pilihan"])


def baca_nombor(soalan, ralat, minimum, maksimum, bulat=False):
    """Baca nombor dalam julat [minimum, maksimum]; ulang jika tidak sah."""
    while True:
        nilai = input(soalan).strip().replace(",", ".")
        try:
            nombor = int(nilai) if bulat else float(nilai)
        except ValueError:
            print(ralat)
            continue
        if not minimum <= nombor <= maksimum:
            print(ralat)
            continue
        return nombor


def ambil_input(t):
    """Ambil nama, jantina, umur, berat (kg) dan tinggi (cm) dengan pengesahan."""
    while True:
        nama = input(t["nama"]).strip()
        if nama:
            break
        print(t["ralat_nama"])

    while True:
        jantina = input(t["jantina"]).strip().lower()
        if jantina in ("l", "m"):
            jantina = t["lelaki"]
            break
        if jantina in ("p", "f"):
            jantina = t["perempuan"]
            break
        print(t["ralat_jantina"])

    umur = baca_nombor(t["umur"], t["ralat_umur"], 1, 120, bulat=True)
    berat = baca_nombor(t["berat"], t["ralat_berat"], 1, 500)
    tinggi = baca_nombor(t["tinggi"], t["ralat_tinggi"], 50, 272)
    return nama, jantina, umur, berat, tinggi


def kira_bmi(berat, tinggi_cm):
    """BMI = berat (kg) / tinggi (m) kuasa dua."""
    tinggi_m = tinggi_cm / 100
    return berat / (tinggi_m ** 2)


def tentukan_status(bmi):
    """Kembalikan kunci kategori BMI mengikut piawai WHO."""
    if bmi < 18.5:
        return "kurang"
    if bmi < 25:
        return "normal"
    if bmi < 30:
        return "lebih"
    return "obes"


def cetak_hasil_bmi(t, nama, jantina, umur, berat, tinggi, bmi, status):
    """Paparkan maklumat pengguna, BMI, status dan nasihat."""
    print()
    print(GARIS)
    print(t["hasil"].center(60))
    print(GARIS)
    print(f"{t['l_nama']:<10}: {nama}")
    print(f"{t['l_jantina']:<10}: {jantina}")
    print(f"{t['l_umur']:<10}: {umur} {t['tahun']}")
    print(f"{t['l_berat']:<10}: {berat:g} kg")
    print(f"{t['l_tinggi']:<10}: {tinggi:g} cm")
    print(f"{t['l_bmi']:<10}: {bmi:.1f}")
    print(f"{t['l_status']:<10}: {t[status]}")
    print(f"{t['l_nasihat']:<10}: {t['nasihat_' + status]}")
    if umur < 19:
        print()
        print(t["nota_remaja"])
    print(GARIS)
    print()


def tanya_lagi(t):
    """Tanya sama ada pengguna mahu mengira BMI orang lain."""
    while True:
        jawapan = input(t["lagi"]).strip().lower()
        if jawapan in t["ya"]:
            return True
        if jawapan in t["tidak"]:
            return False
        print(t["ralat_lagi"])


def main():
    try:
        bahasa = pilih_bahasa()
        t = TEKS[bahasa]
        print()
        print(t["tajuk"].center(60))
        while True:
            print()
            nama, jantina, umur, berat, tinggi = ambil_input(t)
            bmi = kira_bmi(berat, tinggi)
            status = tentukan_status(bmi)
            cetak_hasil_bmi(t, nama, jantina, umur, berat, tinggi, bmi, status)
            if not tanya_lagi(t):
                break
        print(t["tamat"])
    except (KeyboardInterrupt, EOFError):
        print("\nTamat / Goodbye.")


if __name__ == "__main__":
    main()
