"""
Generator CV ATS-Friendly Format Word (.docx) — Faqihudin Ghilbani Akhmad
Menggunakan python-docx untuk menghasilkan dokumen Word profesional standar ATS,
1 Halaman A4, tipografi Arial bersih, tab-stop kanan presisi, dan border heading elegan.
"""

import os
import docx
from docx.shared import Inches, Pt, Mm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def add_bottom_border(paragraph, color_hex="A6A6A6", size_eighth_pt="6"):
    """Menambahkan garis bawah tipis elegan pada heading (standar ATS Word)."""
    pPr = paragraph._element.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), size_eighth_pt)  # 6 = 0.75 pt
    bottom.set(qn('w:space'), '2')
    bottom.set(qn('w:color'), color_hex)
    pBdr.append(bottom)
    pPr.append(pBdr)

def generate_ats_docx(output_paths):
    doc = docx.Document()
    
    # Konfigurasi Halaman Standar A4 & Margin Presisi 1 Halaman
    section = doc.sections[0]
    section.page_width = Mm(210)    # 8.27 in
    section.page_height = Mm(297)   # 11.69 in
    
    section.top_margin = Inches(0.50)
    section.bottom_margin = Inches(0.50)
    section.left_margin = Inches(0.55)
    section.right_margin = Inches(0.55)
    
    content_width = section.page_width - section.left_margin - section.right_margin
    
    # Pengaturan Gaya Font Normal
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Arial'
    normal_style.font.size = Pt(9.0)
    normal_style.font.color.rgb = RGBColor(0x11, 0x11, 0x11)
    
    # Warna Aksara
    C_BLACK = RGBColor(0x11, 0x11, 0x11)
    C_MUTED = RGBColor(0x47, 0x47, 0x47)
    C_ACCENT = RGBColor(0x1B, 0x36, 0x5D)  # Dark Navy Slate
    
    # =========================================================================
    # 1. HEADER (Nama Lengkap & Kontak Terpusat)
    # =========================================================================
    p_name = doc.add_paragraph()
    p_name.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_name.paragraph_format.space_before = Pt(0)
    p_name.paragraph_format.space_after = Pt(2)
    p_name.paragraph_format.line_spacing = 1.05
    run_name = p_name.add_run("FAQIHUDIN GHILBANI AKHMAD")
    run_name.font.name = 'Arial'
    run_name.font.size = Pt(17.5)
    run_name.font.bold = True
    run_name.font.color.rgb = C_BLACK
    
    # Kontak
    p_contact = doc.add_paragraph()
    p_contact.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_contact.paragraph_format.space_before = Pt(0)
    p_contact.paragraph_format.space_after = Pt(1)
    p_contact.paragraph_format.line_spacing = 1.05
    run_contact = p_contact.add_run("Karawang, Jawa Barat   |   +62 858-8971-7020   |   gilbani907@gmail.com")
    run_contact.font.name = 'Arial'
    run_contact.font.size = Pt(9.0)
    run_contact.font.color.rgb = C_MUTED
    
    # Tautan LinkedIn & GitHub
    p_links = doc.add_paragraph()
    p_links.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_links.paragraph_format.space_before = Pt(0)
    p_links.paragraph_format.space_after = Pt(8)
    p_links.paragraph_format.line_spacing = 1.05
    run_links = p_links.add_run("linkedin.com/in/ghilbani   |   github.com/Gilban907")
    run_links.font.name = 'Arial'
    run_links.font.size = Pt(9.0)
    run_links.font.color.rgb = C_ACCENT
    
    # Helper: Heading Bagian dengan Garis Bawah
    def add_section_header(title_text):
        p_h = doc.add_paragraph()
        p_h.paragraph_format.space_before = Pt(7)
        p_h.paragraph_format.space_after = Pt(3)
        p_h.paragraph_format.line_spacing = 1.0
        p_h.paragraph_format.keep_with_next = True
        r = p_h.add_run(title_text)
        r.font.name = 'Arial'
        r.font.size = Pt(10.2)
        r.font.bold = True
        r.font.color.rgb = C_BLACK
        add_bottom_border(p_h)
        return p_h

    # Helper: Item Poin Peluru (List Bullet)
    def add_bullet_item(bold_title, desc_text):
        p_b = doc.add_paragraph(style='List Bullet')
        p_b.paragraph_format.space_before = Pt(0)
        p_b.paragraph_format.space_after = Pt(2.4)
        p_b.paragraph_format.line_spacing = 1.15
        
        r_b = p_b.add_run(bold_title + ": ")
        r_b.font.name = 'Arial'
        r_b.font.size = Pt(8.8)
        r_b.font.bold = True
        r_b.font.color.rgb = C_BLACK
        
        r_d = p_b.add_run(desc_text)
        r_d.font.name = 'Arial'
        r_d.font.size = Pt(8.8)
        r_d.font.color.rgb = C_BLACK
        return p_b

    # =========================================================================
    # 2. RINGKASAN PROFESIONAL (Professional Summary)
    # =========================================================================
    add_section_header("RINGKASAN PROFESIONAL")
    p_sum = doc.add_paragraph()
    p_sum.paragraph_format.space_before = Pt(2)
    p_sum.paragraph_format.space_after = Pt(4)
    p_sum.paragraph_format.line_spacing = 1.15
    r_sum = p_sum.add_run(
        "Fresh Graduate S1 Teknik Informatika dari Telkom University (IPK: 3.45) dengan fokus keahlian pada Web Development, "
        "Data Processing, dan Software Quality Assurance. Berpengalaman membangun aplikasi web terstruktur menggunakan ekosistem "
        "PHP/Laravel, mengolah dataset survei statistik di institusi pemerintah, serta menyusun dan mengeksekusi skenario pengujian "
        "perangkat lunak sistematis. Memiliki pemahaman kuat mengenai REST API, basis data relasional, pengujian fungsional/keamanan, "
        "serta perancangan antarmuka pengguna (UI/UX)."
    )
    r_sum.font.name = 'Arial'
    r_sum.font.size = Pt(8.8)
    r_sum.font.color.rgb = C_BLACK

    # =========================================================================
    # 3. PENDIDIKAN (Education)
    # =========================================================================
    add_section_header("PENDIDIKAN")
    
    # Univ + Tahun (Tab Stop Rata Kanan)
    p_edu1 = doc.add_paragraph()
    p_edu1.paragraph_format.space_before = Pt(2)
    p_edu1.paragraph_format.space_after = Pt(0)
    p_edu1.paragraph_format.line_spacing = 1.1
    p_edu1.paragraph_format.tab_stops.add_tab_stop(content_width, WD_TAB_ALIGNMENT.RIGHT)
    
    r_u1 = p_edu1.add_run("Telkom University")
    r_u1.font.bold = True
    r_u1.font.size = Pt(9.3)
    r_u2 = p_edu1.add_run(" — Bandung, Jawa Barat")
    r_u2.font.color.rgb = C_MUTED
    r_u2.font.size = Pt(8.8)
    r_u3 = p_edu1.add_run("\t2022 – 2026")
    r_u3.font.bold = True
    r_u3.font.size = Pt(8.8)
    
    # Jurusan + IPK
    p_edu2 = doc.add_paragraph()
    p_edu2.paragraph_format.space_before = Pt(0)
    p_edu2.paragraph_format.space_after = Pt(1)
    p_edu2.paragraph_format.line_spacing = 1.1
    p_edu2.paragraph_format.tab_stops.add_tab_stop(content_width, WD_TAB_ALIGNMENT.RIGHT)
    
    r_d1 = p_edu2.add_run("Sarjana Komputer (S1) Teknik Informatika")
    r_d1.font.italic = True
    r_d1.font.size = Pt(8.8)
    r_d2 = p_edu2.add_run("\tIPK: 3.45 / 4.00")
    r_d2.font.bold = True
    r_d2.font.size = Pt(8.8)
    
    # Mata Kuliah Relevan
    p_edu3 = doc.add_paragraph()
    p_edu3.paragraph_format.space_before = Pt(0)
    p_edu3.paragraph_format.space_after = Pt(4)
    p_edu3.paragraph_format.line_spacing = 1.1
    r_cw = p_edu3.add_run("Fokus Studi: Rekayasa Perangkat Lunak, Struktur Data & Algoritma, Basis Data Relasional, Pemrograman Web, Pengujian Perangkat Lunak.")
    r_cw.font.size = Pt(8.4)
    r_cw.font.color.rgb = C_MUTED

    # =========================================================================
    # 4. PENGALAMAN KERJA & MAGANG (Experience)
    # =========================================================================
    add_section_header("PENGALAMAN KERJA & MAGANG")
    
    # BPS Cilacap
    p_exp1 = doc.add_paragraph()
    p_exp1.paragraph_format.space_before = Pt(2)
    p_exp1.paragraph_format.space_after = Pt(0)
    p_exp1.paragraph_format.line_spacing = 1.1
    p_exp1.paragraph_format.tab_stops.add_tab_stop(content_width, WD_TAB_ALIGNMENT.RIGHT)
    
    r_e1 = p_exp1.add_run("Badan Pusat Statistik (BPS) Kabupaten Cilacap")
    r_e1.font.bold = True
    r_e1.font.size = Pt(9.3)
    r_e2 = p_exp1.add_run("\t2024")
    r_e2.font.bold = True
    r_e2.font.size = Pt(8.8)
    
    p_exp2 = doc.add_paragraph()
    p_exp2.paragraph_format.space_before = Pt(0)
    p_exp2.paragraph_format.space_after = Pt(2)
    p_exp2.paragraph_format.line_spacing = 1.1
    r_role = p_exp2.add_run("Magang IT & Pengolahan Data")
    r_role.font.italic = True
    r_role.font.color.rgb = C_ACCENT
    r_role.font.size = Pt(8.8)
    
    add_bullet_item(
        "Redesain Sistem Penilaian Pegawai",
        "Merancang ulang antarmuka dan alur evaluasi kinerja pegawai trisemester dan tahunan berbasis web menggunakan Laravel, Bootstrap, dan MySQL untuk menyederhanakan alur formulir panjang dan menggantikan rekapitulasi manual spreadsheet."
    )
    add_bullet_item(
        "Dashboard & Visualisasi Perangkingan",
        "Menyajikan dasbor analitik terstruktur, ringkasan statistik performa, dan visualisasi pemeringkatan otomatis guna mempercepat proses penilaian evaluasi berkala pimpinan secara objektif, transparan, dan efisien."
    )
    add_bullet_item(
        "Validasi & Pembersihan Data",
        "Melakukan verifikasi, pembersihan data mentah (data cleaning), dan digitalisasi rekapitulasi hasil survei lapangan untuk meminimalisir anomali data serta meningkatkan akurasi dan kecepatan pelaporan statistik sektoral."
    )

    # =========================================================================
    # 5. PROYEK PILIHAN (Key Projects)
    # =========================================================================
    add_section_header("PROYEK PILIHAN")
    
    # Proyek 1: Booket
    p_p1 = doc.add_paragraph()
    p_p1.paragraph_format.space_before = Pt(2)
    p_p1.paragraph_format.space_after = Pt(0)
    p_p1.paragraph_format.line_spacing = 1.1
    p_p1.paragraph_format.tab_stops.add_tab_stop(content_width, WD_TAB_ALIGNMENT.RIGHT)
    
    r_pr1 = p_p1.add_run("Sistem Informasi Manajemen Event & Pemesanan Tiket (Booket)")
    r_pr1.font.bold = True
    r_pr1.font.size = Pt(9.3)
    r_pr2 = p_p1.add_run("\t2024")
    r_pr2.font.bold = True
    r_pr2.font.size = Pt(8.8)
    
    p_p1_stack = doc.add_paragraph()
    p_p1_stack.paragraph_format.space_before = Pt(0)
    p_p1_stack.paragraph_format.space_after = Pt(2)
    p_p1_stack.paragraph_format.line_spacing = 1.1
    r_st1 = p_p1_stack.add_run("Tech Stack: Flutter, JavaScript, Node.js, Laravel, MySQL, REST API")
    r_st1.font.italic = True
    r_st1.font.size = Pt(8.5)
    r_st1.font.color.rgb = C_MUTED
    
    add_bullet_item(
        "Pengembangan Platform Web & Mobile",
        "Mengembangkan platform pemesanan dan penjualan tiket konser, workshop, dan festival dengan pencarian/filter event cerdas, integrasi pembayaran digital (e-wallet), notifikasi pengingat, dan penerbitan e-ticket ber-QR code."
    )
    add_bullet_item(
        "Sentralisasi & Arsitektur RESTful API",
        "Merancang arsitektur RESTful API untuk memusatkan pengelolaan kuota tiket real-time serta menyajikan dasbor analitik statistik penjualan komprehensif bagi pihak penyelenggara event."
    )
    
    # Proyek 2: El-Cloth
    p_p2 = doc.add_paragraph()
    p_p2.paragraph_format.space_before = Pt(3)
    p_p2.paragraph_format.space_after = Pt(0)
    p_p2.paragraph_format.line_spacing = 1.1
    p_p2.paragraph_format.tab_stops.add_tab_stop(content_width, WD_TAB_ALIGNMENT.RIGHT)
    
    r_pe1 = p_p2.add_run("Pengujian Aplikasi Mobile El-Cloth (QA & Usability Testing)")
    r_pe1.font.bold = True
    r_pe1.font.size = Pt(9.3)
    r_pe2 = p_p2.add_run("\t2024")
    r_pe2.font.bold = True
    r_pe2.font.size = Pt(8.8)
    
    p_p2_stack = doc.add_paragraph()
    p_p2_stack.paragraph_format.space_before = Pt(0)
    p_p2_stack.paragraph_format.space_after = Pt(2)
    p_p2_stack.paragraph_format.line_spacing = 1.1
    r_st2 = p_p2_stack.add_run("Tools & Metode: Blackbox Testing, Whitebox Testing, Usability Testing, Android/iOS Emulator, MobSF")
    r_st2.font.italic = True
    r_st2.font.size = Pt(8.5)
    r_st2.font.color.rgb = C_MUTED
    
    add_bullet_item(
        "Perancangan & Eksekusi Uji Fungsional",
        "Menyusun dan mengeksekusi 35+ skenario pengujian fungsional menyeluruh pada 7 modul kritis aplikasi: registrasi, login, katalog produk, keranjang belanja, checkout, transaksi pembayaran, dan pelacakan pesanan."
    )
    add_bullet_item(
        "Usability Testing & Security Analysis",
        "Menguji langsung efektivitas antarmuka bersama 19 responden uji coba serta menjalankan analisis keamanan statis menggunakan MobSF untuk mendeteksi potensi kerentanan data pada package Android sebelum rilis."
    )

    # =========================================================================
    # 6. KEAHLIAN TEKNIS (Technical Skills)
    # =========================================================================
    add_section_header("KEAHLIAN TEKNIS")
    
    skills = [
        ("Bahasa & Web", "PHP, Laravel, JavaScript, Python, HTML5, CSS3, RESTful API, Responsive Web Design"),
        ("Database & Tooling", "MySQL, Git, GitHub, Node.js, Bootstrap, Flutter, Postman, Android/iOS Emulator"),
        ("QA & Testing", "Blackbox Testing, Whitebox Testing, Usability Testing, MobSF, Desain Test Case"),
        ("Desain & Metodologi", "UI/UX Design, Figma, Wireframing, Alur Pengguna (User Flow), Agile / Scrum Basics")
    ]
    
    for category, details in skills:
        p_sk = doc.add_paragraph()
        p_sk.paragraph_format.space_before = Pt(0)
        p_sk.paragraph_format.space_after = Pt(2.0)
        p_sk.paragraph_format.line_spacing = 1.15
        
        r_c = p_sk.add_run(f"•  {category}: ")
        r_c.font.bold = True
        r_c.font.size = Pt(8.8)
        r_c.font.color.rgb = C_BLACK
        
        r_v = p_sk.add_run(details)
        r_v.font.size = Pt(8.8)
        r_v.font.color.rgb = C_BLACK
    
    # Metadata Dokumen Word
    core_props = doc.core_properties
    core_props.title = "CV - Faqihudin Ghilbani Akhmad"
    core_props.author = "Faqihudin Ghilbani Akhmad"
    core_props.subject = "Curriculum Vitae / Resume ATS-Friendly Word Version"
    core_props.keywords = "Teknik Informatika, Web Developer, Laravel, PHP, MySQL, QA Tester, BPS Cilacap, Telkom University, ATS Resume"
    
    for path in output_paths:
        os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
        doc.save(path)
        print(f"File Word (.docx) berhasil dibuat: {path}")

if __name__ == "__main__":
    targets = [
        r"D:\GILBAN\WEBSITE\cv\CV-Faqihudin-Ghilbani-Akhmad.docx",
        r"D:\GILBAN\WEBSITE\CV-Faqihudin-Ghilbani-Akhmad.docx"
    ]
    generate_ats_docx(targets)
