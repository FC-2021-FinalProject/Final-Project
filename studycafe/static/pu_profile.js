document.addEventListener("DOMContentLoaded", () => {
  console.log("personal profile page connected!")

  //activate submit button for input value changes for EDIT PROFILE TAB
  $nameInput = document.querySelector('#profile-name')
  $usernameInput = document.querySelector('#profile-username')
  $emailInput = document.querySelector('#profile-email')
  $submitButton = document.querySelector('.profile-edit-submit')

  $nameInput.addEventListener('change', toggleSubmit);
  $usernameInput.addEventListener('change', toggleSubmit);
  $emailInput.addEventListener('change', () => {
    toggleSubmit()
  });
  function toggleSubmit(){
    $submitButton.classList.remove('disabled');
    $submitButton.disabled = false;
  };

});
