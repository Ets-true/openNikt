const headerBurger = document.querySelector('.header__burger');
if (headerBurger) {
    const burgerBody = document.querySelector('.burger__body');
    const header = document.querySelector('.header');
    headerBurger.addEventListener("click", function (e) {
        headerBurger.classList.toggle('_active');
        burgerBody.classList.toggle('_active');
        header.classList.toggle('_active');
    })
}