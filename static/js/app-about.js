const list = document.querySelectorAll('.member-item');
const showMemButt = document.getElementById('icon-more')
const box = document.getElementById('box-l')
const memTab = document.getElementById('mem-tab')

function showMember(){
    showMemButt.classList.toggle('active')
    box.classList.toggle('active')
    memTab.classList.toggle('active')
    list.forEach((item) =>
            item.classList.toggle('active'));
}