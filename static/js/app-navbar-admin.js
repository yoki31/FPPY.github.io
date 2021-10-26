const openMenu = document.querySelector('#show-menu')
const hideMenuIcon = document.querySelector('#hide-menu')
const sideMenu = document.querySelector('#nav-menu')
const buttMore = document.querySelector('#show-more')
const moreTab = document.getElementById('more-options')

openMenu.addEventListener('click', function() {
    sideMenu.classList.add('active')
    moreTab.classList.remove('active')
    buttMore.classList.remove('active')
})

hideMenuIcon.addEventListener('click', function() {
    sideMenu.classList.remove('active')
})

function showMore(){
    moreTab.classList.toggle('active')
    buttMore.classList.toggle('active')
    sideMenu.classList.remove('active')
}
