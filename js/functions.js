// var x3;
var x = 10 // global scope 
let x2 = 15

function funName() {
    // Function body
    x3 = 5
    var y = 5;    // local scope / Function scope / block scope 
    let y2 = 20;  // local scope / Function scope / block scope
    console.log(x)  // 10 
    console.log(x2) // 15 
    console.log(x3) // undefined  
    console.log(b) // undefined
    {
        let a = 10;
        var b = 8;
    }
    // console.log(a) //ReferenceError: a is not defined 
    console.log(b) // 8
    // console.log(y3) // ReferenceError: Cannot access 'y3' before initialization
}
console.log(x3) // undefined
console.log(y)  // undefined 
// console.log(y2) // Error : ReferenceError: y2 is not defined 
funName()
console.log(x3) // 5
console.log(y)  // undefined 

console.log(x3) // undefined
var x3 = 10; // Hoisting is happened 
let y3 = 20; 
let abc;
console.log(abc) // undefined
// console.log(abcd) // ReferenceError: Cannot access 'abcd' before initialization
let abcd = 10;

// var userEmail = prompt('Enter your email: ')
// var score = 10;
// var conf = confirm('Do you want to make your score zero?')

// if (conf == true) {
//     score = 0
//     alert('Your score is zero!')
// }
// else {
//     alert('Your score is the same!')
// }