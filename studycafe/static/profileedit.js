document.addEventListener("DOMContentLoaded", () => {
    console.log("connected!")
   
// profile edit form 
    const profileEditForm = document.querySelector('.profile-edit-form')

    console.log(profileEditForm)
    
    document.querySelector('.edit-profile-button').addEventListener('click', function(){

      profileEditForm.classList.add('show')
      });

    console.log(profileEditForm)
    
  });
