document.addEventListener("DOMContentLoaded", () => {
  console.log("<<-----app.js----->> connected!")

  // header mobile menu drop down
  document.getElementById('mobile-menu').addEventListener('click', ()=> {
    const $mobileMenu = document.querySelector('.header-nav-menu-container');
    if ($mobileMenu.classList.contains('mobile-open')) {
      $mobileMenu.classList.remove('mobile-open');
      return;
    }
    $mobileMenu.classList.add('mobile-open');
  })
});