function hoverHandler(){
    console.log('You Hover on The Element')
}

const log = document.getElementById("log");
const input = document.querySelector("input");

input.addEventListener("keypress", logKey);

function logKey(e) {
    console.log(e)
    // log.innerText += `${e.key}`
    log.textContent += ` ${e.key}`;
}
var header = document.getElementById('head2')
var btn = document.getElementById('btn')

// console.log(header)
btn.addEventListener('click', (e) => {
    console.log(e)
    header.innerText = 'Hello in Our Website'   
});

//removeEventListener()
const myDiv = document.getElementById("myDIV");
myDiv.addEventListener("mousemove", myFunction);

function removeHandler() {
    myDiv.removeEventListener("mousemove", myFunction);
}

function myFunction() {
    document.getElementById("demo").innerHTML = Math.random();
}