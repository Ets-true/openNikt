const offset = 500;
// const scrollFooter = 100;
const scrollUp = document.querySelector('.home__scrollUp');



const getTop = () => window.pageYOffset || document.documentElement.scrollTop;
// const scrollHeight = Math.max(
//     document.body.scrollHeight, document.documentElement.scrollHeight,
//     document.body.offsetHeight, document.documentElement.offsetHeight,
//     document.body.clientHeight, document.documentElement.clientHeight
//   );
//onScroll
window.addEventListener('scroll', () => {

    if(getTop() > offset){
        scrollUp.classList.add('home__scrollUp_active');
    }
    // if(scrollFooter > (scrollHeight-(getTop()))) {
    //     scrollUp.classList.add('home__scrollUp_footer');
    // }
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