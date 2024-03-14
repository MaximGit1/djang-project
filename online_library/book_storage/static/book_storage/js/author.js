document.addEventListener('DOMContentLoaded', function() {
    const slider = document.querySelector('.books_list');
    const prevBtn = document.querySelector('.slider__btn_prev');
    const nextBtn = document.querySelector('.slider__btn_next');

    let currentIndex = 0;

    prevBtn.addEventListener('click', function() {
        currentIndex = Math.max(currentIndex - 1, 0);
        updateSlider();
    });

    nextBtn.addEventListener('click', function() {
        currentIndex = Math.min(currentIndex + 1, slider.children.length - 5);
        updateSlider();
    });

    function updateSlider() {
        const translateXValue = -currentIndex * 20 + '%';
        slider.style.transform = 'translateX(' + translateXValue + ')';
    }
});