document.addEventListener("DOMContentLoaded", () => {
    console.log("<<-----base.js----->> connected!")
  
    const $mobileMenu = document.querySelector('.header-nav-menu-container');
    const $bodyClick = document.querySelector('.body-background');

    // header mobile menu drop down
    document.getElementById('mobile-menu').addEventListener('click', ()=> {
      console.log('clicked')
      if ($mobileMenu.classList.contains('mobile-open')) {
        $mobileMenu.classList.remove('mobile-open');
        $bodyClick.classList.remove('mobile-open');
        return;
      }
      $mobileMenu.classList.add('mobile-open');
      $bodyClick.classList.add('mobile-open');

    });

    $bodyClick.addEventListener('click', () => {
      console.log('bodyclicked')
      $mobileMenu.classList.remove('mobile-open');
      $bodyClick.classList.remove('mobile-open');
    })
  });