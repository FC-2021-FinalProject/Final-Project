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
    console.log(target.id)
}
