let title = document.querySelector(".title");
// let namefield = document.querySelector(".namefield");
let signinbtn = document.getElementById("signinbtn")
let signupbtn = document.querySelector(".signupbtn");
// let password = document.querySelector('.password');

signinbtn.addEventListener('click',(e)=>{
    e.stopPropagation();
    title.innerHTML = "Sign In";

})

signupbtn.addEventListener('click',(e)=>{
    e.stopPropagation();
    title.innerHTML = "Sign Up";
})  