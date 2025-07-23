const openUpdate = document.querySelector("#open-update")
const profileUpdate = document.querySelector("#profile-update")
const closeUpdate = document.querySelector("#close-update")

console.log(profileUpdate);
console.log(openUpdate);

openUpdate.addEventListener("click",()=>{
    profileUpdate.style.display="block"
    
})

closeUpdate.addEventListener("click",()=>{
    profileUpdate.style.display="none"
    
})