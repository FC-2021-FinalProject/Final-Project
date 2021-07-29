document.addEventListener("DOMContentLoaded", () => {
  console.log("<<-----login.js----->> connected!")

  //final validation check array. Submit button to be enabled if all validation check passes and all elements of isValidLogin are true.
  const isValidLogin = [false, false, false];

  //Username validation
  const $username = document.getElementById('login-name')
  $username.onblur = () => {
    console.log('username test');
    // if check fails show error message and return
    if (lengthCheckValidation($username.value, 5)) {
      console.log("******username is too short!!1")
      // 에러메세지 보여주기
      isValidLogin[0] = false;
      return;
    }
    // if check passes override isValid to True 
    isValidLogin[0] = true;

    if (typeCheckValidation($username.value, String)){
      console.log("******username type error!!1")
      isValidLogin[1] = false;
      return;
    } 
    isValidLogin[1] = true;
  };

  //Password validation
  const $password = document.getElementById('login-password')
  $password.onblur = () => {
    console.log($password)
    console.log('password test');

    // if check fails show error message and return
    if (lengthCheckValidation($password.value, 8)) {
      console.log("******password is too short!!1")
      isValidLogin[2] = false;
      return;
    }
    isValidLogin[2] = true;
  };

  // Enable submit button after all validation check has passed (css and buttons disabled)

  
});

const retrieveUsername = async () => {
  try {
    const res = await fetch('http://example.com/getNickName');
    const data = res.json();
  
    if (data.nickname) {
      return true;
    }
    return false;
  } catch (error) {
    console.log(error);
    alert('')
  }

}
const lengthCheckValidation = (word, length) => {

  if (word.length > length) {
    return false;
  }
  return true;
}
const typeCheckValidation = (word, type) => {
  if (typeof word === type) {
    return true;
  }
  return false;
}