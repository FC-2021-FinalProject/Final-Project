document.addEventListener("DOMContentLoaded", () => {
  console.log("<<-----login.js----->> connected!")

  const $username = document.getElementById('login-name');
  const $password = document.getElementById('login-password');
  const $errorUsername = document.querySelector('.username-input.error-msg');
  const $errorPassword = document.querySelector('.password-input.error-msg');
  const $submitButton = document.querySelector('.login-button');
  console.log($submitButton)
  
  const isValidLogin = [false, false];

  //USERNAME VALIDATION
  $username.addEventListener('blur', () => {
    if (lengthCheckValidation($username.value, 5)) {
      console.log("******username is too short!!1")
      // 에러메세지 보여주기
      $errorUsername.innerHTML = "Username must be greater than 5 characters."
      isValidLogin[0] = false;
      return;
    }
    $errorUsername.innerHTML = "";
    isValidLogin[0] = true;

    if ((isValidLogin[0] == true) && (isValidLogin[1] == true)){
      if ($submitButton.classList.contains('disabled')){
        toggleSubmit()
        console.log($submitButton)
      }
    }
  });
  
  //PASSWORD VALIDATION
  $password.addEventListener('blur', () => {
    if (lengthCheckValidation($password.value, 8)) {
      console.log("******password is too short!!1")
      $errorPassword.innerHTML = "Password must be greater than 8 characters."
      isValidLogin[1] = false;
      return;
    }
    $errorPassword.innerHTML = "";
    isValidLogin[1] = true;

    if ((isValidLogin[0] == true) && (isValidLogin[1] == true)){
      if ($submitButton.classList.contains('disabled')){
        toggleSubmit()
        console.log($submitButton)
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

  if (word.length > length) {
    return false;
  }
  return true;
}
// Check if username exists
// const retrieveUsername = async () => {
//   try {
//     const res = await fetch('http://127.0.0.1:8000/getUserName');
//     const data = res.json();
  
//     if (data.usernname) {
//       return true;
//     }
//     return false;
//   } catch (error) {
//     console.log(error);
//     alert('')
//   }

// }
