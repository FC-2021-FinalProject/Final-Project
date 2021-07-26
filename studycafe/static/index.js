document.addEventListener("DOMContentLoaded", () => {
  console.log("<<-----index.js----->> connected!")

  // header mobile menu drop down
  document.getElementById('mobile-menu').addEventListener('click', ()=> {
    console.log("mobile menu")
    const $mobileMenu = document.querySelector('.header-nav-menu-container');
    if ($mobileMenu.classList.contains('mobile-open')) {
      $mobileMenu.classList.remove('mobile-open');
      return;
    }
    $mobileMenu.classList.add('mobile-open');
  });
});