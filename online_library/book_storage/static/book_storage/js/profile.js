function confirmLogout() {
    var logoutUrl = document.querySelector('.logout-link').getAttribute('data-logout-url');
    var isConfirmed = confirm("Вы уверены, что хотите выйти из аккаунта?");
    
    if (isConfirmed) {
        window.location.href = logoutUrl;
    } 
}
function initializeSlider() {
    const slider = document.querySelector(`.container_books .books_list`);
    const prevBtn = document.querySelector(`.container_books .slider__btn_prev`);
    const nextBtn = document.querySelector(`.container_books .slider__btn_next`);

    let currentIndex = 0;
    const slidesToShow = 5;
    const slideWidth = 20; // Здесь указывается ширина одного слайда в процентах

    prevBtn.addEventListener('click', function() {
        currentIndex = Math.max(currentIndex - 3, 0);
        updateSlider();
    });

    nextBtn.addEventListener('click', function() {
        currentIndex = Math.min(currentIndex + 3, slider.children.length - slidesToShow);
        updateSlider();
    });

    function updateSlider() {
        const translateXValue = -currentIndex * slideWidth + '%';
        slider.style.transform = 'translateX(' + translateXValue + ')';
    }
}
document.addEventListener('DOMContentLoaded', function() {
    let FormSup = document.querySelector('#showFormSup');
    FormSup.addEventListener('click', function() {
        var form = document.getElementById('contactForm');
        console.log(form);
        form.classList.toggle('hidden');
    });
    initializeSlider()
})



// function formSup() {
//     var form = document.getElementById('contactForm');
//     console.log(form);
//     form.classList.toggle('hidden');
// }