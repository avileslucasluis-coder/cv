'use strict';
const shareButton = document.getElementById('share-profile');
const toast = document.getElementById('toast');
let toastTimer;
shareButton.addEventListener('click', async () => {
  const url = new URL(window.location.href);
  url.hash = '';
  url.search = '';
  try {
    if (!navigator.clipboard || !window.isSecureContext) throw new Error('Clipboard unavailable');
    await navigator.clipboard.writeText(url.href);
    toast.textContent = 'Enlace copiado. Listo para compartir.';
    toast.classList.add('visible');
    window.clearTimeout(toastTimer);
    toastTimer = window.setTimeout(() => toast.classList.remove('visible'), 4000);
  } catch {
    const dialog = document.getElementById('share-dialog');
    const input = document.getElementById('profile-url');
    input.value = url.href;
    dialog.showModal();
    input.focus();
    input.select();
  }
});
if ('IntersectionObserver' in window) {
  const navLinks = [...document.querySelectorAll('.header nav a')];
  const observer = new IntersectionObserver(entries => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      for (const link of navLinks) {
        const active = link.hash === '#' + entry.target.id;
        link.classList.toggle('active', active);
        if (active) link.setAttribute('aria-current', 'location');
        else link.removeAttribute('aria-current');
      }
    }
  }, { rootMargin: '-10% 0px -65% 0px', threshold: 0 });
  for (const link of navLinks) {
    const section = document.querySelector(link.hash);
    if (section) observer.observe(section);
  }
}
