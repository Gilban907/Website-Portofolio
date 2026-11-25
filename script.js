/**
 * ============================================================================
 * SCRIPT.JS — PORTOFOLIO FAQIHUDIN GHILBANI AKHMAD
 * JavaScript Murni (Vanilla JS, Tanpa Framework / Library Eksternal)
 * Fitur:
 * 1. Mobile Hamburger Menu Toggle & Accessibility
 * 2. Navbar Styling & Shadow Saat Di-scroll
 * 3. Active Link Highlighting Berdasarkan Posisi Scroll
 * 4. Animasi Fade-in Halus Saat Section Muncul (IntersectionObserver)
 * 5. Smooth Scroll dengan Offset Navbar
 * 6. Form Kontak Terhubung Otomatis ke WhatsApp (+6285889717020)
 * ============================================================================
 */

document.addEventListener('DOMContentLoaded', () => {
  'use strict';

  // Inisialisasi Seluruh Modul
  initNavbarScroll();
  initMobileMenu();
  initSmoothScroll();
  initActiveNavOnScroll();
  initScrollReveal();
  initWhatsAppForm();
});

/**
 * ----------------------------------------------------------------------------
 * 1. NAVBAR SCROLL EFFECT
 * Menambahkan class .scrolled saat halaman digulir lebih dari 20px
 * ----------------------------------------------------------------------------
 */
function initNavbarScroll() {
  const navbar = document.getElementById('navbar');
  if (!navbar) return;

  const handleScroll = () => {
    if (window.scrollY > 20) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  };

  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll(); // Jalankan sekali saat inisialisasi
}

/**
 * ----------------------------------------------------------------------------
 * 2. MOBILE HAMBURGER MENU
 * Membuka & menutup menu navigasi di tampilan layar HP (responsif)
 * ----------------------------------------------------------------------------
 */
function initMobileMenu() {
  const hamburgerBtn = document.getElementById('hamburger-btn');
  const navMenu = document.getElementById('nav-menu');
  const navLinks = document.querySelectorAll('.nav-link');

  if (!hamburgerBtn || !navMenu) return;

  // Toggle status menu
  const toggleMenu = () => {
    const isExpanded = hamburgerBtn.getAttribute('aria-expanded') === 'true';
    hamburgerBtn.setAttribute('aria-expanded', !isExpanded);
    hamburgerBtn.classList.toggle('is-active');
    navMenu.classList.toggle('is-open');

    // Kunci scroll halaman saat menu terbuka di mobile
    document.body.style.overflow = !isExpanded ? 'hidden' : '';
  };

  // Tutup menu
  const closeMenu = () => {
    hamburgerBtn.setAttribute('aria-expanded', 'false');
    hamburgerBtn.classList.remove('is-active');
    navMenu.classList.remove('is-open');
    document.body.style.overflow = '';
  };

  hamburgerBtn.addEventListener('click', toggleMenu);

  // Tutup menu saat salah satu link diklik
  navLinks.forEach(link => {
    link.addEventListener('click', closeMenu);
  });

  // Tutup menu jika user menekan tombol ESC di keyboard
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && navMenu.classList.contains('is-open')) {
      closeMenu();
    }
  });

  // Tutup menu jika klik di luar area navbar
  document.addEventListener('click', (e) => {
    if (
      navMenu.classList.contains('is-open') &&
      !navMenu.contains(e.target) &&
      !hamburgerBtn.contains(e.target)
    ) {
      closeMenu();
    }
  });
}

/**
 * ----------------------------------------------------------------------------
 * 3. SMOOTH SCROLL DENGAN OFFSET NAVBAR
 * Memastikan posisi scroll tepat dan tidak tertutup navbar yang sticky
 * ----------------------------------------------------------------------------
 */
function initSmoothScroll() {
  const internalLinks = document.querySelectorAll('a[href^="#"]');

  internalLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#' || targetId === '') return;

      const targetElement = document.querySelector(targetId);
      if (targetElement) {
        e.preventDefault();
        const navbar = document.getElementById('navbar');
        const navHeight = navbar ? navbar.offsetHeight : 72;
        const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - navHeight;

        window.scrollTo({
          top: targetPosition,
          behavior: 'smooth'
        });
      }
    });
  });
}

/**
 * ----------------------------------------------------------------------------
 * 4. ACTIVE LINK HIGHLIGHTING
 * Mengubah indikator garis bawah menu aktif sesuai section yang terlihat
 * ----------------------------------------------------------------------------
 */
function initActiveNavOnScroll() {
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link');

  if (sections.length === 0 || navLinks.length === 0) return;

  const highlightNav = () => {
    const scrollY = window.pageYOffset;
    const navbar = document.getElementById('navbar');
    const navHeight = navbar ? navbar.offsetHeight : 72;

    sections.forEach(current => {
      const sectionHeight = current.offsetHeight;
      const sectionTop = current.offsetTop - navHeight - 60;
      const sectionId = current.getAttribute('id');

      if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
        navLinks.forEach(link => {
          link.classList.remove('active');
          if (link.getAttribute('href') === `#${sectionId}`) {
            link.classList.add('active');
          }
        });
      }
    });
  };

  window.addEventListener('scroll', highlightNav, { passive: true });
}

/**
 * ----------------------------------------------------------------------------
 * 5. SCROLL REVEAL (FADE-IN HALUS SAAT MUNCUL)
 * Menggunakan browser native IntersectionObserver tanpa library eksternal
 * ----------------------------------------------------------------------------
 */
function initScrollReveal() {
  // Elemen yang akan diberi efek muncul halus
  const revealTargets = document.querySelectorAll(
    '.hero-content, .hero-visual, .tentang-photo-col, .tentang-text-col, .project-card, .timeline-item, .kontak-info, .kontak-form-card'
  );

  if (!('IntersectionObserver' in window)) {
    // Fallback jika browser lawas tidak mendukung IntersectionObserver
    revealTargets.forEach(el => el.classList.add('is-visible'));
    return;
  }

  revealTargets.forEach(el => el.classList.add('reveal'));

  const observerOptions = {
    root: null,
    rootMargin: '0px 0px -40px 0px',
    threshold: 0.12
  };

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        obs.unobserve(entry.target); // Cukup animasi sekali saja agar tidak repetitif
      }
    });
  }, observerOptions);

  revealTargets.forEach(el => observer.observe(el));
}

/**
 * ----------------------------------------------------------------------------
 * 6. FORM KONTAK KE WHATSAPP OTOMATIS
 * Nomor WhatsApp tujuan: +62 858-8971-7020
 * Membuka obrolan WhatsApp dengan pesan terformat rapi
 * ----------------------------------------------------------------------------
 */
function initWhatsAppForm() {
  const form = document.getElementById('whatsapp-form');
  const feedback = document.getElementById('form-feedback');
  if (!form) return;

  const TARGET_WHATSAPP_NUMBER = '6285889717020';

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    const nameInput = document.getElementById('sender-name');
    const emailInput = document.getElementById('sender-email');
    const topicInput = document.getElementById('sender-topic');
    const messageInput = document.getElementById('sender-message');

    const name = nameInput ? nameInput.value.trim() : '';
    const email = emailInput ? emailInput.value.trim() : '';
    const topic = topicInput ? topicInput.value.trim() : '';
    const message = messageInput ? messageInput.value.trim() : '';

    // Validasi Sederhana
    if (!name || !email || !topic || !message) {
      if (feedback) {
        feedback.textContent = 'Harap isi semua kolom sebelum mengirim.';
        feedback.style.color = '#C24A2E'; // Notifikasi oranye/merah
      }
      return;
    }

    // Format Pesan WhatsApp yang Rapi dan Profesional
    const whatsappMessage = 
`Halo Faqihudin Ghilbani Akhmad,

Perkenalkan, saya: ${name}
Email: ${email}
Subjek / Keperluan: ${topic}

Pesan:
${message}

---
Dikirim melalui formulir kontak portofolio web.`;

    // Encode URL
    const encodedMessage = encodeURIComponent(whatsappMessage);
    const waUrl = `https://wa.me/${TARGET_WHATSAPP_NUMBER}?text=${encodedMessage}`;

    // Tampilkan Umpan Balik Positif
    if (feedback) {
      feedback.textContent = 'Membuka WhatsApp... Silakan lanjutkan pengiriman pesan di WhatsApp.';
      feedback.style.color = '#2F3E2E'; // Hijau Army
    }

    // Buka WhatsApp di Tab Baru
    window.open(waUrl, '_blank', 'noopener,noreferrer');

    // Opsional: Reset form setelah 2 detik
    setTimeout(() => {
      form.reset();
      if (feedback) {
        feedback.textContent = '';
      }
    }, 4000);
  });
}
