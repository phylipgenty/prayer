// Helper alert
function showAlert(msg) {
  alert(msg);
}

document.addEventListener('DOMContentLoaded', () => {
  // Hero button
  document.getElementById('watchLiveNowBtn')?.addEventListener('click', () => 
    showAlert('🌐 LIVE STREAM: Join the worship now! Tune in via our YouTube channel.')
  );

  // Testimonies inside double column (with captions)
  const testimoniesList = [
    { text: "The Birmingham conference shifted my prayer life. I'll never be the same. Glory to God!", author: "— David K., Edinburgh" },
    { text: "After joining PPN prayers, my business turned around and my family received healing. God is faithful!", author: "— Sarah M., London" },
    { text: "My family found peace and breakthrough through their prayer requests. Highly recommend.", author: "— Lisa, Canada" }
  ];
  const testiContainer = document.getElementById('testimoniesContainer');
  if (testiContainer) {
    testiContainer.innerHTML = testimoniesList.map(t => `
      <div class="testimonial-text">
        “${t.text}”<div class="testimonial-author">${t.author}</div>
      </div>
    `).join('');
  }

  // Modal logic
  const socialModal = document.getElementById('socialModal');
  const prayerModal = document.getElementById('prayerModal');
  const closeBtns = document.querySelectorAll('.close-modal');

  function openModal(modal) { if (modal) modal.style.display = 'flex'; }
  function closeModal(modal) { if (modal) modal.style.display = 'none'; }

  const joinCard = document.getElementById('joinCard');
  const liveCard = document.getElementById('liveCard');
  const prayerCard = document.getElementById('prayerCard');

  if (joinCard) joinCard.addEventListener('click', () => openModal(socialModal));
  if (liveCard) liveCard.addEventListener('click', () => window.open('https://www.youtube.com/@henryonyirioha_ppn', '_blank'));
  if (prayerCard) prayerCard.addEventListener('click', () => openModal(prayerModal));

  closeBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      closeModal(socialModal);
      closeModal(prayerModal);
    });
  });
  window.addEventListener('click', (e) => {
    if (e.target === socialModal) closeModal(socialModal);
    if (e.target === prayerModal) closeModal(prayerModal);
  });

  // Slideshow logic – LONGER DURATION (6 seconds)
  let slideIndex = 0;
  const slides = document.querySelectorAll('.slide');
  if (slides.length > 0) {
    function showSlides() {
      slides.forEach(slide => slide.classList.remove('active'));
      slideIndex++;
      if (slideIndex > slides.length) slideIndex = 1;
      if (slides[slideIndex - 1]) slides[slideIndex - 1].classList.add('active');
      setTimeout(showSlides, 6000); // 6 seconds
    }
    showSlides();
  }

  // Gallery slideshow – also 6 seconds
  let galleryIndex = 0;
  const gallerySlides = document.querySelectorAll('.gallery-slide');
  function showGallerySlides() {
    if (!gallerySlides.length) return;
    gallerySlides.forEach(slide => slide.classList.remove('active'));
    galleryIndex++;
    if (galleryIndex > gallerySlides.length) galleryIndex = 1;
    if (gallerySlides[galleryIndex - 1]) gallerySlides[galleryIndex - 1].classList.add('active');
    setTimeout(showGallerySlides, 6000);
  }
  if (gallerySlides.length > 0) showGallerySlides();

  // Mobile menu toggle
  const toggleBtn = document.getElementById('menuToggle');
  const navLinks = document.getElementById('navLinks');
  if (toggleBtn && navLinks) {
    toggleBtn.addEventListener('click', () => navLinks.classList.toggle('show'));
    document.querySelectorAll('.nav-links a').forEach(link => {
      link.addEventListener('click', () => navLinks.classList.remove('show'));
    });
  }

  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const targetId = this.getAttribute('href');
      if (targetId === "#" || targetId === "") return;
      const targetElem = document.querySelector(targetId);
      if (targetElem) {
        e.preventDefault();
        targetElem.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });
});

// Manchester countdown
function startManchesterCountdown() {
  const countdownEl = document.getElementById('manchesterCountdown');
  if (!countdownEl) return;
  const eventDate = new Date("May 15, 2026 18:00:00").getTime(); // CHANGE to actual D-day
  const timer = setInterval(() => {
    const now = new Date().getTime();
    const distance = eventDate - now;
    if (distance < 0) {
      clearInterval(timer);
      countdownEl.innerHTML = "🔥 EVENT STARTED! 🔥";
    } else {
      const days = Math.floor(distance / (1000*60*60*24));
      const hours = Math.floor((distance % (86400000)) / (3600000));
      const mins = Math.floor((distance % 3600000) / 60000);
      const secs = Math.floor((distance % 60000) / 1000);
      countdownEl.innerHTML = `${days}d ${hours}h ${mins}m ${secs}s`;
    }
  }, 1000);
}
startManchesterCountdown();