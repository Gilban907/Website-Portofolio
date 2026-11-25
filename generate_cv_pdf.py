"""
Generator CV ATS-Friendly — Faqihudin Ghilbani Akhmad
Menggunakan PyMuPDF untuk menghasilkan file PDF 1 Halaman A4 Presisi Tinggi,
100% Text-Selectable, Standar Applicant Tracking System (ATS), dan Bersih.
"""

import os
import pymupdf

def generate_ats_cv(output_paths):
    doc = pymupdf.open()
    
    # Standar A4: 595.28 x 841.89 points
    page_w = 595.28
    page_h = 841.89
    page = doc.new_page(width=page_w, height=page_h)
    
    # Margin presisi (40pt kiri/kanan, 34pt atas)
    left = 42.0
    right = page_w - 42.0
    usable_w = right - left
    
    y = 34.0
    
    # Font Base-14 Standar ATS
    F_BOLD = "hebo"   # Helvetica-Bold
    F_REG = "helv"    # Helvetica-Regular
    F_ITAL = "heit"   # Helvetica-Oblique / Italic
    
    # Palet Warna ATS Minimalis & Kontras Tinggi
    C_BLACK = (0.07, 0.07, 0.07)   # #111111
    C_MUTED = (0.28, 0.28, 0.28)   # #474747
    C_LINE = (0.65, 0.65, 0.65)    # #A6A6A6
    C_ACCENT = (0.12, 0.24, 0.40)  # Dark Slate Navy (profesional, ramah ATS)
    
    # =========================================================================
    # 1. HEADER (Nama & Kontak Lengkap)
    # =========================================================================
    rect = pymupdf.Rect(left, y, right, y + 23)
    page.insert_textbox(
        rect,
        "FAQIHUDIN GHILBANI AKHMAD",
        fontname=F_BOLD,
        fontsize=18,
        color=C_BLACK,
        align=pymupdf.TEXT_ALIGN_CENTER
    )
    y += 23
    
    contact_line = "Karawang, Jawa Barat   |   +62 858-8971-7020   |   gilbani907@gmail.com"
    rect = pymupdf.Rect(left, y, right, y + 13)
    page.insert_textbox(
        rect,
        contact_line,
        fontname=F_REG,
        fontsize=9.2,
        color=C_MUTED,
        align=pymupdf.TEXT_ALIGN_CENTER
    )
    y += 13
    
    links_line = "linkedin.com/in/ghilbani   |   github.com/Gilban907"
    rect = pymupdf.Rect(left, y, right, y + 13)
    page.insert_textbox(
        rect,
        links_line,
        fontname=F_REG,
        fontsize=9.2,
        color=C_ACCENT,
        align=pymupdf.TEXT_ALIGN_CENTER
    )
    y += 17
    
    # Helper: Gambar Judul Bagian dengan Garis Pembatas
    def draw_section_heading(title, curr_y):
        rect_h = pymupdf.Rect(left, curr_y, right, curr_y + 14)
        page.insert_textbox(rect_h, title, fontname=F_BOLD, fontsize=10.2, color=C_BLACK)
        line_y = curr_y + 13.0
        page.draw_line(pymupdf.Point(left, line_y), pymupdf.Point(right, line_y), color=C_LINE, width=0.75)
        return curr_y + 18.0

    # Helper: Gambar Poin Peluru (Bullet Point) dengan Hanging Indent Rapi
    def draw_bullet(title_prefix, text_content, curr_y):
        # Titik peluru standar
        page.insert_text(pymupdf.Point(left + 6, curr_y + 8.5), chr(8226), fontname=F_REG, fontsize=10, color=C_BLACK)
        
        full_text = f"{title_prefix}: {text_content}" if title_prefix else text_content
        rect_b = pymupdf.Rect(left + 16, curr_y, right, curr_y + 120)
        rem = page.insert_textbox(rect_b, full_text, fontname=F_REG, fontsize=8.8, color=C_BLACK, lineheight=1.24)
        used_h = 120.0 - rem
        return curr_y + used_h + 3.2

    # =========================================================================
    # 2. RINGKASAN PROFESIONAL (Professional Summary)
    # =========================================================================
    y = draw_section_heading("RINGKASAN PROFESIONAL", y)
    summary_text = (
        "Fresh Graduate S1 Teknik Informatika dari Telkom University (IPK: 3.45) dengan fokus keahlian pada Web Development, "
        "Data Processing, dan Software Quality Assurance. Berpengalaman membangun aplikasi web terstruktur menggunakan ekosistem "
        "PHP/Laravel, mengolah dataset survei statistik di institusi pemerintah, serta menyusun dan mengeksekusi skenario pengujian "
        "perangkat lunak sistematis. Memiliki pemahaman kuat mengenai REST API, basis data relasional, pengujian fungsional/keamanan, "
        "serta perancangan antarmuka pengguna (UI/UX)."
    )
    rect_s = pymupdf.Rect(left, y, right, y + 100)
    rem_s = page.insert_textbox(rect_s, summary_text, fontname=F_REG, fontsize=8.8, color=C_BLACK, lineheight=1.24)
    y += (100.0 - rem_s) + 8.0

    # =========================================================================
    # 3. PENDIDIKAN (Education)
    # =========================================================================
    y = draw_section_heading("PENDIDIKAN", y)
    
    # Univ, Lokasi & Tahun
    page.insert_text(pymupdf.Point(left, y + 9), "Telkom University", fontname=F_BOLD, fontsize=9.5, color=C_BLACK)
    page.insert_text(pymupdf.Point(left + 95, y + 9), "—  Bandung, Jawa Barat", fontname=F_REG, fontsize=9.0, color=C_MUTED)
    page.insert_text(pymupdf.Point(right - 58, y + 9), "2022 – 2026", fontname=F_BOLD, fontsize=9.0, color=C_BLACK)
    y += 12
    
    # Gelar & IPK
    page.insert_text(pymupdf.Point(left, y + 8.5), "Sarjana Komputer (S1) Teknik Informatika", fontname=F_ITAL, fontsize=9.0, color=C_BLACK)
    page.insert_text(pymupdf.Point(right - 72, y + 8.5), "IPK: 3.45 / 4.00", fontname=F_BOLD, fontsize=9.0, color=C_BLACK)
    y += 11
    
    # Mata Kuliah / Fokus
    coursework = "Fokus Studi: Rekayasa Perangkat Lunak, Struktur Data & Algoritma, Basis Data Relasional, Pemrograman Web, Pengujian Perangkat Lunak."
    rect_c = pymupdf.Rect(left, y, right, y + 40)
    rem_c = page.insert_textbox(rect_c, coursework, fontname=F_REG, fontsize=8.5, color=C_MUTED)
    y += (40.0 - rem_c) + 8.0

    # =========================================================================
    # 4. PENGALAMAN KERJA & MAGANG (Work Experience)
    # =========================================================================
    y = draw_section_heading("PENGALAMAN KERJA & MAGANG", y)
    
    # BPS Cilacap
    page.insert_text(pymupdf.Point(left, y + 9), "Badan Pusat Statistik (BPS) Kabupaten Cilacap", fontname=F_BOLD, fontsize=9.5, color=C_BLACK)
    page.insert_text(pymupdf.Point(right - 28, y + 9), "2024", fontname=F_BOLD, fontsize=9.0, color=C_BLACK)
    y += 12
    
    page.insert_text(pymupdf.Point(left, y + 8.5), "Magang IT & Pengolahan Data", fontname=F_ITAL, fontsize=9.0, color=C_ACCENT)
    y += 11
    
    y = draw_bullet(
        "Redesain Sistem Penilaian Pegawai",
        "Merancang ulang antarmuka dan alur evaluasi kinerja pegawai trisemester dan tahunan berbasis web menggunakan Laravel, Bootstrap, dan MySQL untuk menyederhanakan alur formulir panjang dan menggantikan rekapitulasi manual spreadsheet.",
        y
    )
    y = draw_bullet(
        "Dashboard & Visualisasi Perangkingan",
        "Menyajikan dasbor analitik terstruktur, ringkasan statistik performa, dan visualisasi pemeringkatan otomatis guna mempercepat proses penilaian evaluasi berkala pimpinan secara objektif, transparan, dan efisien.",
        y
    )
    y = draw_bullet(
        "Validasi & Pembersihan Data",
        "Melakukan verifikasi, pembersihan data mentah (data cleaning), dan digitalisasi rekapitulasi hasil survei lapangan untuk meminimalisir anomali data serta meningkatkan akurasi dan kecepatan pelaporan statistik sektoral.",
        y
    )
    y += 4.5

    # =========================================================================
    # 5. PROYEK PILIHAN (Key Projects)
    # =========================================================================
    y = draw_section_heading("PROYEK PILIHAN", y)
    
    # Proyek 1: Booket
    page.insert_text(pymupdf.Point(left, y + 9), "Sistem Informasi Manajemen Event & Pemesanan Tiket (Booket)", fontname=F_BOLD, fontsize=9.5, color=C_BLACK)
    page.insert_text(pymupdf.Point(right - 28, y + 9), "2024", fontname=F_BOLD, fontsize=9.0, color=C_BLACK)
    y += 12
    
    tech_booket = "Tech Stack: Flutter, JavaScript, Node.js, Laravel, MySQL, REST API"
    page.insert_text(pymupdf.Point(left, y + 8.5), tech_booket, fontname=F_ITAL, fontsize=8.7, color=C_MUTED)
    y += 11
    
    y = draw_bullet(
        "Pengembangan Platform Web & Mobile",
        "Mengembangkan platform pemesanan dan penjualan tiket konser, workshop, dan festival dengan pencarian/filter event cerdas, integrasi pembayaran digital (e-wallet), notifikasi pengingat, dan penerbitan e-ticket ber-QR code.",
        y
    )
    y = draw_bullet(
        "Sentralisasi & Arsitektur RESTful API",
        "Merancang arsitektur RESTful API untuk memusatkan pengelolaan kuota tiket real-time serta menyajikan dasbor analitik statistik penjualan komprehensif bagi pihak penyelenggara event.",
        y
    )
    y += 4.0

    # Proyek 2: El-Cloth
    page.insert_text(pymupdf.Point(left, y + 9), "Pengujian Aplikasi Mobile El-Cloth (QA & Usability Testing)", fontname=F_BOLD, fontsize=9.5, color=C_BLACK)
    page.insert_text(pymupdf.Point(right - 28, y + 9), "2024", fontname=F_BOLD, fontsize=9.0, color=C_BLACK)
    y += 12
    
    tech_elcloth = "Tools & Metode: Blackbox Testing, Whitebox Testing, Usability Testing, Android/iOS Emulator, MobSF"
    page.insert_text(pymupdf.Point(left, y + 8.5), tech_elcloth, fontname=F_ITAL, fontsize=8.7, color=C_MUTED)
    y += 11
    
    y = draw_bullet(
        "Perancangan & Eksekusi Uji Fungsional",
        "Menyusun dan mengeksekusi 35+ skenario pengujian fungsional menyeluruh pada 7 modul kritis aplikasi: registrasi, login, katalog produk, keranjang belanja, checkout, transaksi pembayaran, dan pelacakan pesanan.",
        y
    )
    y = draw_bullet(
        "Usability Testing & Security Analysis",
        "Menguji langsung efektivitas antarmuka bersama 19 responden uji coba serta menjalankan analisis keamanan statis menggunakan MobSF untuk mendeteksi potensi kerentanan data pada package Android sebelum rilis.",
        y
    )
    y += 4.5

    # =========================================================================
    # 6. KEAHLIAN TEKNIS (Technical Skills)
    # =========================================================================
    y = draw_section_heading("KEAHLIAN TEKNIS", y)
    
    skills = [
        ("Bahasa & Web", "PHP, Laravel, JavaScript, Python, HTML5, CSS3, RESTful API, Responsive Web Design"),
        ("Database & Tooling", "MySQL, Git, GitHub, Node.js, Bootstrap, Flutter, Postman, Android/iOS Emulator"),
        ("QA & Testing", "Blackbox Testing, Whitebox Testing, Usability Testing, MobSF, Desain Test Case"),
        ("Desain & Metodologi", "UI/UX Design, Figma, Wireframing, Alur Pengguna (User Flow), Agile / Scrum Basics")
    ]
    
    for label, val in skills:
        page.insert_text(pymupdf.Point(left, y + 8.5), f"{label}:", fontname=F_BOLD, fontsize=8.8, color=C_BLACK)
        w_lbl = pymupdf.Font(F_BOLD).text_length(f"{label}:", 8.8)
        rect_sk = pymupdf.Rect(left + w_lbl + 5, y, right, y + 30)
        rem_sk = page.insert_textbox(rect_sk, val, fontname=F_REG, fontsize=8.8, color=C_BLACK)
        y += (30.0 - rem_sk) + 2.8
        
    print(f"Total tinggi dokumen terpakai: {y:.2f} pt dari {page_h:.2f} pt. Sisa ruang bawah: {page_h - y:.2f} pt.")
    
    # Metadata Dokumen PDF Standar ATS
    doc.set_metadata({
        "title": "CV - Faqihudin Ghilbani Akhmad",
        "author": "Faqihudin Ghilbani Akhmad",
        "subject": "Curriculum Vitae / Resume ATS-Friendly",
        "keywords": "Teknik Informatika, Web Developer, Laravel, PHP, MySQL, QA Tester, BPS Cilacap, Telkom University, ATS Resume",
        "creator": "PyMuPDF ATS Resume Engine"
    })
    
    # Simpan ke seluruh path target
    for out_path in output_paths:
        os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
        doc.save(out_path, deflate=True)
        print(f"File PDF berhasil dibuat: {out_path}")
        
    doc.close()

if __name__ == "__main__":
    targets = [
        r"D:\GILBAN\WEBSITE\cv\CV-Faqihudin-Ghilbani-Akhmad.pdf",
        r"D:\GILBAN\WEBSITE\CV-Faqihudin-Ghilbani-Akhmad.pdf"
    ]
    generate_ats_cv(targets)
