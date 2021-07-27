
const $IdPwContainer = document.querySelector('.idpw-search-body');
const $searchList = document.querySelector('.search-list');

$searchList.onclick = ({ target }) => {
    if (target.classList.contains('search-list')) return;
    [...$searchList.children].forEach( $searchListItem => {
        $searchListItem.classList.toggle('active', $searchListItem === target);
        
        [...$IdPwContainer.children].forEach( $IdPwItem => {
            $IdPwItem.classList.toggle('active', $IdPwItem.classList.contains(target.id));
        });
    });
};
//     // tester text
//     if (target.id === "search-id" ){
//         $tester.textContent = "SEARCH USERNAME";
//          return;
//     } else if (target.id === "search-pw"){
//         $tester.textContent = "SEARCH PASSWORD";
//          return;
//     }
//   };
