const openMenu = document.querySelector('#show-menu')
const hideMenuIcon = document.querySelector('#hide-menu')
const sideMenu = document.querySelector('#nav-menu')
const buttNoti = document.querySelector('#show-noti')
const noti = document.getElementById('noti')
const buttMore = document.querySelector('#show-more')
const moreTab = document.getElementById('more-options')

// ลอง swipe
// const buttSet = document.querySelector('#show-setting')
// const priTabMore = document.getElementById('pri-more-op')

openMenu.addEventListener('click', function() {
    sideMenu.classList.add('active')
    moreTab.classList.remove('active')
    buttMore.classList.remove('active')
    noti.classList.remove('active')
    buttNoti.classList.remove('active')
})

hideMenuIcon.addEventListener('click', function() {
    sideMenu.classList.remove('active')
})

function showNoti(){
    noti.classList.toggle('active')
    buttNoti.classList.toggle('active')
    moreTab.classList.remove('active')
    buttMore.classList.remove('active')
    sideMenu.classList.remove('active')
}

function showMore(){
    moreTab.classList.toggle('active')
    buttMore.classList.toggle('active')
    noti.classList.remove('active')
    buttNoti.classList.remove('active')
    sideMenu.classList.remove('active')
}

// buttSet.addEventListener('click', function() {
//     priTabMore.classList.add('active')
// })