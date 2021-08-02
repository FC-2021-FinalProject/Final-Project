document.addEventListener("DOMContentLoaded", () => {

  console.log('***bu-profile.js connected ***')

  
// profile page tab event

  //TABS
  const $businessProfileTab = document.querySelector('.bu-profile-header');
  const $manageCafeTab = document.querySelector('.bu-manage-header');
  const $reviewsFeedbackTab = document.querySelector('.bu-reviews-header');

  //CONTENTS
  const $businessProfile = document.querySelector('.bu-profile-content');
  const $manageCafe = document.querySelector('.bu-manage-content');
  const $reviewsFeedback = document.querySelector('.bu-reviews-content');

  //EVENTS
  $businessProfileTab.addEventListener('click', () => {
    if ($businessProfileTab.classList.contains('selected')) {
    } else { 
        $businessProfileTab.classList.add('selected')
        $businessProfile.classList.remove('visually-hidden')
        
        if ($manageCafeTab.classList.contains('selected')){
          $manageCafeTab.classList.remove('selected')
          $manageCafe.classList.add('visually-hidden')
        } else if ($reviewsFeedbackTab.classList.contains('selected')){
          $reviewsFeedbackTab.classList.remove('selected')
          $reviewsFeedback.classList.add('visually-hidden')
        }
      }
  });

  $manageCafeTab.addEventListener('click', () => {
    if ($manageCafeTab.classList.contains('selected')) {
    } else { 
        $manageCafeTab.classList.add('selected')
        $manageCafe.classList.remove('visually-hidden')
        
        if ($businessProfileTab.classList.contains('selected')){
          $businessProfileTab.classList.remove('selected')
          $businessProfile.classList.add('visually-hidden')
        } else if ($reviewsFeedbackTab.classList.contains('selected')){
          $reviewsFeedbackTab.classList.remove('selected')
          $reviewsFeedback.classList.add('visually-hidden')
        }
      }
  });

  $reviewsFeedbackTab.addEventListener('click', () => {
    if ($reviewsFeedbackTab.classList.contains('selected')) {
    } else { 
        $reviewsFeedbackTab.classList.add('selected')
        $reviewsFeedback.classList.remove('visually-hidden')
        
        if ($businessProfileTab.classList.contains('selected')){
          $businessProfileTab.classList.remove('selected')
          $businessProfile.classList.add('visually-hidden')
        } else if ($manageCafeTab.classList.contains('selected')){
          $manageCafeTab.classList.remove('selected')
          $manageCafe.classList.add('visually-hidden')
        }
      }
  });


});