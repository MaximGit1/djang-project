function show_seria(){
    let book = document.querySelector('.sh_books')
    book.style.display = 'block'
    let show = document.querySelector('.seriya button')
    show.style.display = 'none'
}
function showModal() {
    document.getElementById('copyForm').style.display = 'flex';
}


function closeForm() {
    document.getElementById('copyForm').style.display = 'none';
}
function Copy() {
    var Url = document.getElementById("url");
    Url.innerHTML = window.location.href;
    console.log(Url.innerHTML)
    Url.select();
    document.execCommand("copy");
  }
  