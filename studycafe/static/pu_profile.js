document.addEventListener("DOMContentLoaded", () => {
  console.log("personal profile page connected!")

//profile edit page -- submit button toggling

  //FORM ITEMS
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

// profile page tab event

  //TABS
  const $editProfileTab = document.querySelector('.pu-profile-header');
  const $changePasswordTab = document.querySelector('.pu-password-header');
  const $reservationsTab = document.querySelector('.pu-reservations-header');
  const $bookmarkedCafesTab = document.querySelector('.pu-bookmarked-header');

  //CONTENTS
  const $editProfile = document.querySelector('.pu-profile-contents');
  const $changePassword = document.querySelector('.pu-password-contents');
  const $reservations = document.querySelector('.pu-reservations-contents');
  const $bookmarkedCafes = document.querySelector('.pu-bookmarked-contents');

  //EVENTS
  $editProfileTab.addEventListener('click', () => {
    if ($editProfileTab.classList.contains('selected')) {
      console.log("already selected!")
    } else { 
        $editProfileTab.classList.add('selected')
        $editProfile.classList.remove('visually-hidden')
        
        if ($changePasswordTab.classList.contains('selected')){
          $changePasswordTab.classList.remove('selected')
          $changePassword.classList.add('visually-hidden')
        } else if ($reservationsTab.classList.contains('selected')){
          $reservationsTab.classList.remove('selected')
          $reservations.classList.add('visually-hidden')
        } else if ($bookmarkedCafesTab.classList.contains('selected')){
          $bookmarkedCafesTab.classList.remove('selected')
          $bookmarkedCafes.classList.add('visually-hidden')
        }
      }
  });

  $changePasswordTab.addEventListener('click', () => {
    if ($changePasswordTab.classList.contains('selected')) {
      console.log("already selected!")
    } else { 
        $changePasswordTab.classList.add('selected')
        $changePassword.classList.remove('visually-hidden')
        
        if ($editProfileTab.classList.contains('selected')){
          $editProfileTab.classList.remove('selected')
          $editProfile.classList.add('visually-hidden')
        } else if ($reservationsTab.classList.contains('selected')){
          $reservationsTab.classList.remove('selected')
          $reservations.classList.add('visually-hidden')
        } else if ($bookmarkedCafesTab.classList.contains('selected')){
          $bookmarkedCafesTab.classList.remove('selected')
          $bookmarkedCafes.classList.add('visually-hidden')
        }
      }
  });

  $reservationsTab.addEventListener('click', () => {
    if ($reservationsTab.classList.contains('selected')) {
      console.log("already selected!")
    } else { 
        $reservationsTab.classList.add('selected')
        $reservations.classList.remove('visually-hidden')
        
        if ($editProfileTab.classList.contains('selected')){
          $editProfileTab.classList.remove('selected')
          $editProfile.classList.add('visually-hidden')
        } else if ($changePasswordTab.classList.contains('selected')){
          $changePasswordTab.classList.remove('selected')
          $changePassword.classList.add('visually-hidden')
        } else if ($bookmarkedCafesTab.classList.contains('selected')){
          $bookmarkedCafesTab.classList.remove('selected')
          $bookmarkedCafes.classList.add('visually-hidden')
        }
      }
  });

  $bookmarkedCafesTab.addEventListener('click', () => {
    if ($bookmarkedCafesTab.classList.contains('selected')) {
      console.log("already selected!")
    } else { 
        $bookmarkedCafesTab.classList.add('selected')
        $bookmarkedCafes.classList.remove('visually-hidden')
        
        if ($editProfileTab.classList.contains('selected')){
          $editProfileTab.classList.remove('selected')
          $editProfile.classList.add('visually-hidden')
        } else if ($changePasswordTab.classList.contains('selected')){
          $changePasswordTab.classList.remove('selected')
          $changePasswordTab.classList.add('visually-hidden')
        } else if ($reservationsTab.classList.contains('selected')){
          $reservationsTab.classList.remove('selected')
          $reservations.classList.add('visually-hidden')
        }
      }
  });

});