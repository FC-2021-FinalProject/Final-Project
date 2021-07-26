document.addEventListener("DOMContentLoaded", () => {
    console.log("<<-----login.js----->> connected!")
  
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
  
    // login validation
    const isValidLogin = [false, false, false, false];
  
    document.getElementById('loginName').onblur = () => {
      console.log('test');
      // 검사 실패시
      if (lengthCheckValidation()) {
        // 에러메세지 보여주기
        isValid[0] = false;
        return;
      }
      isValid[0] = true;
    };
    // Enable submit button after all validation check has passed (css and buttons disabled)
  
  });