document.addEventListener('DOMContentLoaded', function(){
    let rate = this.querySelectorAll('.rate')
    for(let i = 0; i <=rate.length; i++){
        let img = this.querySelectorAll('.card a img');
        let styles = window.getComputedStyle(img[i]);
        rate[i].style.width = styles.width;
    }
})