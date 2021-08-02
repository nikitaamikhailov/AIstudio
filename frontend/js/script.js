const swiperMain = new Swiper('.main-info_slider', {
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
    slidesPerView: 3,
    centeredSlides: true,
    pagination: {
        el: '.reviews-slider-pagination',
        clickable: true,
        type: 'bullets',
    },
    navigation: {
        nextEl: '.reviews-slider-button-next',
        prevEl: '.reviews-slider-button-prev',
    },
})
const mymap = L.map('blackMap').setView([59.98714, 30.1706], 15);
const attribution = 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>'
const tileUrl = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
const apiUrl = 0
const tiles = L.tileLayer(tileUrl, {attribution})
tiles.addTo(mymap)

const office = L.marker([59.98714, 30.1706]).addTo(mymap);

const offerPoint = document.querySelector('.point-1')
const offerLink = document.querySelector('.offer-page')
offerPoint.onclick = function () {
    offerLink.scrollIntoView({block: "start", behavior: "smooth"});
}