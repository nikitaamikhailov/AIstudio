const swiper1 = new Swiper('.main-info_slider', {
    loop: true,
    simulateTouch: true,
    spaceBetween: 100,
    pagination: {
        el: '.main-swiper-pagination',
        clickable: true
    },
})

const swiperReviews = new Swiper('.reviews_cards', {
    loop: true,
    spaceBetween: 75,
    pagination: {
        el: '.reviews-swiper-pagination',
        clickable: true
    },
    slidesPerView: 3,
    navigation: {
        nextEl: '.reviews-swiper-button-next',
        prevEl: '.reviews-swiper-button-prev',
    },
    centeredSlides: true,

})