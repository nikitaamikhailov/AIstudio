const swiperMain = new Swiper('.main-info_slider', {
    loop: true,
    simulateTouch: true,
    spaceBetween: 100,
    pagination: {
        el: '.main-swiper-pagination',
        clickable: true,
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

const anchors = document.querySelectorAll('a[href*="#"]')

for (let anchor of anchors){
    anchor.addEventListener("click", function (event) {
        event.preventDefault()
        const blockID = anchor.getAttribute('href')
        document.querySelector('' + blockID).scrollIntoView({
            behavior: "smooth",
            block: "start"
        })
    })
}
const personalAreaButtons = document.querySelectorAll('.personal-area-button')
const hiddenElements = document.querySelectorAll('.can-be-hidden')
const personalArea = document.querySelector('.personal-area-form')
const registrationButton = document.querySelector('#registration')
const registration = document.querySelector('.registration-form')
const logo = document.querySelector('.logo')
const firstAnswer = document.querySelectorAll('.first-question_cards_card')
const firstQuestion = document.querySelector('.first-question')
const secondQuestion = document.querySelector('.second-question')
const secondAnswer = document.querySelectorAll('.second-question_cards_card')

for (let personalAreaButton of personalAreaButtons){
    personalAreaButton.addEventListener("click", function (event) {
        event.preventDefault()
        for (let block of hiddenElements){
            block.classList.add('hidden')
        }
        personalArea.classList.remove('hidden')
    })
}
registrationButton.addEventListener("click", function (event) {
    event.preventDefault()
    personalArea.classList.add('hidden')
    registration.classList.remove('hidden')
})

logo.addEventListener("click", function (event) {
    event.preventDefault()
    for (let block of hiddenElements){
        block.classList.remove('hidden')
    }
    personalArea.classList.add('hidden')
    registration.classList.add('hidden')
})

for (let answer of firstAnswer){
    answer.addEventListener("click", function (event) {
        event.preventDefault()
        firstQuestion.classList.add('hidden')
        secondQuestion.classList.remove('hidden')
    })}

for (let answer of secondAnswer){
    answer.addEventListener("click", function (event) {
        event.preventDefault()
        secondQuestion.classList.add('hidden')
        firstQuestion.classList.remove('hidden')
    })}