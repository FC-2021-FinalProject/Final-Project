document.addEventListener("DOMContentLoaded", () => {
    console.log("login connected!")

// login pop up modal
    
    const bodyBlackout = document.querySelector('.body-blackout');
    const popupModal = document.querySelector('.auth-popup');

    //Event for popup modal window
    document.querySelector('.popup-button').addEventListener('click' , function(){
    
      popupModal.classList.add('modal-is-visible');
      bodyBlackout.classList.add('is-blacked-out');
  
    });
    //Event to close popup modal window
    popupModal.querySelector('.popup-modal__close').addEventListener('click', () => {
      
      popupModal.classList.remove('modal-is-visible');
      bodyBlackout.classList.remove('is-blacked-out');
    });

    //Event to close popup window when background is clicked
    bodyBlackout.addEventListener('click', () => {

      popupModal.classList.remove('modal-is-visible');
      bodyBlackout.classList.remove('is-blacked-out');
    })

// login validation
    
    const form = document.querySelector('.auth-form');
    const username = document.querySelector('.auth-items-username');
    const password = document.querySelector('.auth-items-password');
    
    form.addEventListener('submit', e => {
      e.preventDefault();

      checkInputs();
    });

    function checkInputs(){
      const usernameValue = username.Value.trim();
      const passwordValue = password.Value.trim();
      
      if (usernameValue === '') {
        setError(username, 'Username is a mandatory field.')
      } else {
        setSuccess(username);
      };
      if(password === '') {
        setError(passwrod, 'Password is a mandatory field.')
      } else {
        setSuccess(password);
      }
    }

    function setError(input, message) {
      const formControl = input.parentElement;
      const small = formControl.querySelector('small');
      formControl.className = 'form-control error';
	    small.innerText = message;
    }

    function setSuccess(input) {
      const formControl = input.parentElement;
      formControl.className = 'form-control success';
    }
      

  });  
  
