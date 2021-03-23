const offset = 500;
const scrollUp = document.querySelector('.home__scrollUp');



const getTop = () => window.pageYOffset || document.documentElement.scrollTop;
//onScroll
window.addEventListener('scroll', () => {

    if(getTop() > offset){
        scrollUp.classList.add('home__scrollUp_active');
    }
    else {
        scrollUp.classList.remove('home__scrollUp_active');
    }
})

//click 
scrollUp.addEventListener('click', ()=>{
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});