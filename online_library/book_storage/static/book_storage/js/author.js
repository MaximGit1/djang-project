function initializeSlider(selector) {
    const slider = document.querySelector(selector + ` .books_list`);
    const prevBtn = document.querySelector(selector + ` .slider__btn_prev`);
    const nextBtn = document.querySelector(selector + ` .slider__btn_next`);

    let currentIndex = 0;
    const slidesToShow = 5;
    const slideWidth = 20;

    prevBtn.addEventListener('click', function() {
        currentIndex = Math.max(currentIndex - 1, 0);
        updateSlider();
    });

    nextBtn.addEventListener('click', function() {
        currentIndex = Math.min(currentIndex + 1, slider.children.length - slidesToShow);
        updateSlider();
    });

    function updateSlider() {
        const translateXValue = -currentIndex * slideWidth + '%';
        slider.style.transform = 'translateX(' + translateXValue + ')';
    }
}

document.addEventListener('DOMContentLoaded', function() {
    // Отдельные книги
    initializeSlider('#slider_other')

    // Инициализация всех слайдеров
    const slidersCount = document.querySelectorAll('.container_books').length;
    for (let i = 1; i <= slidersCount; i++) {
        initializeSlider(`#slider_${i}`);
    }
    
});
