const showNav = document.querySelector("#show-nav")
const mobileNav = document.querySelector("#mobile-nav")
const closeNav = document.querySelector("#close-nav")
const mobileBtn = document.querySelector("#mobile-btn")


showNav.addEventListener("click",()=>{
    mobileBtn.style.display="none"
    mobileNav.style.display="block"
    
})

closeNav.addEventListener("click",()=>{
    mobileBtn.style.display="block"
    mobileNav.style.display="none"
    
})


