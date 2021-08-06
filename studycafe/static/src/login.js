document.addEventListener("DOMContentLoaded", () => {
  console.log("<<-----login.js----->> connected!")

  const $username = document.getElementById('login-name');
  const $password = document.getElementById('login-password');
  const $errorUsername = document.querySelector('.username-input.error-msg');
  const $errorPassword = document.querySelector('.password-input.error-msg');
  const $submitButton = document.querySelector('.login-button');
  
  const isValidLogin = [false, false];

  //USERNAME VALIDATION
  $username.addEventListener('blur', () => {
    if (lengthCheckValidation($username.value, 5)) {
      $errorUsername.innerHTML = "Username must be greater than 5 characters."
      isValidLogin[0] = false;
      return;
    }
    $errorUsername.innerHTML = "";
    isValidLogin[0] = true;

    if ((isValidLogin[0] == true) && (isValidLogin[1] == true)){
      if ($submitButton.classList.contains('disabled')){
        toggleSubmit()
      }
    }
  });
  
  //PASSWORD VALIDATION
  $password.addEventListener('blur', () => {
    if (lengthCheckValidation($password.value, 4)) {
      $errorPassword.innerHTML = "Password must be greater than 8 characters."
      isValidLogin[1] = false;
      return;
    }
    $errorPassword.innerHTML = "";
    isValidLogin[1] = true;

    if ((isValidLogin[0] == true) && (isValidLogin[1] == true)){
      if ($submitButton.classList.contains('disabled')){
        toggleSubmit()
      }
    }
  });

  //
  const toggleSubmit = () => {
    $submitButton.classList.remove('disabled');
    $submitButton.disabled = false;
  };  

});

const lengthCheckValidation = (word, length) => {

  if (word.length >= length) {
    return false;
  }
  return true;
}
// Check if username exists
// const retrieveUsername = async () => {
//   try {
//     const res = await fetch('http://127.0.0.1:8000/getUserName');
//     const data = res.json();
  
//     if (data.username) {
//       return true;
//     }
//     return false;
//   } catch (error) {
//     console.log(error);
// Show error on template 
//   }

// }
