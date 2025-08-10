// SyntaxError 
// console.log('Error) // SyntaxError: Invalid or unexpected token
var myError = new Error()

// RangeError
function check(n) {
    if (!(n >= -500 && n <= 500)) {
        throw new RangeError("The argument must be between -500 and 500.");
    }
}

try {
    check(2000);
} catch (error) {
    if (error instanceof RangeError) {
        console.log('The range is invalid')
    }
}

// ReferenceError 
let x = 5;
try {
  x = y + 1;   // y cannot be used (referenced)
}
catch(err) {
    console.log(err.name); // ReferenceError
}

// TypeError 
let num = 1;
try {
  num.toUpperCase();   // You cannot convert a number to upper case
}
catch(er) {
    console.log(er.message)
}

// URIError 
try {
  decodeURI("%%%");   // You cannot URI decode percent signs
}
catch(err) {
    console.log(err.name)
}

var a = 10
if (a < 5){
    throw 'a variable is less than 10'
}

function myFunction() {
    const message = document.getElementById("message");
    message.style = "color:red";
    message.innerHTML = "";
    
    let x = document.getElementById("demo2").value;
    try { 
        if(x == "")  throw "is Empty";
        if(isNaN(x)) throw "not a number";
        if(x > 10)   throw "too high";
        if(x < 5)  throw "too low";
    }
    catch(err) {
        message.innerHTML = "Input " + err;
    }
}