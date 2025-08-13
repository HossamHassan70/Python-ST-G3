// var x3;
// var x = 10 // global scope 
// let x2 = 15

// function funName() {
//     // Function body
//     x3 = 5
//     var y = 5;    // local scope / Function scope / block scope 
//     let y2 = 20;  // local scope / Function scope / block scope
//     console.log(x)  // 10 
//     console.log(x2) // 15 
//     console.log(x3) // undefined  
//     console.log(b) // undefined
//     {
//         let a = 10;
//         var b = 8;
//     }
//     // console.log(a) //ReferenceError: a is not defined 
//     console.log(b) // 8
//     // console.log(y3) // ReferenceError: Cannot access 'y3' before initialization
// }
// console.log(x3) // undefined
// console.log(y)  // undefined 
// // console.log(y2) // Error : ReferenceError: y2 is not defined 
// funName()
// console.log(x3) // 5
// console.log(y)  // undefined 

// console.log(x3) // undefined
// var x3 = 10; // Hoisting is happened 
// let y3 = 20; 
// let abc;
// console.log(abc) // undefined
// // console.log(abcd) // ReferenceError: Cannot access 'abcd' before initialization
// let abcd = 10;

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

// // parseInt , parseFloat , Number 
// console.log(parseInt('3'))
// console.log(parseFloat('3.2'))
// console.log(typeof(Number('40')))
// console.log(typeof(+('40')))


// anonymous function (a function without a name).
// const x = function (a, b) {return a * b};
// let z = x(4, 3);

// Arrow Function
// let myFunction = (a, b) => a * b;

// 1. No parameters No return
// function sum(){
//     var num1 = parseInt(prompt('Enter Number 1: '))
//     var num2 = parseInt(prompt('Enter Number 2: '))
//     var res = num1 + num2
//     document.write(res)
// }

// sum()

// 2. Parameters No return
// function sum(basmala,b) {
//     var res = parseInt(basmala) + parseInt(b)
//     document.write(res)
// }

// sum(prompt('Enter the First Number: '),prompt('Enter the Second Number: '))
// var str1 = 'Basmala'
// var str2 = 'Ahmed'

// console.log(str1 +' '+ str2)
// var x = 10
// var y = 5 
// document.write('<br>')
// sum(4,5)
// document.write('<br>')
// sum(x,y)
// document.write('<br>')
// sum('5','7') //12
// var num1 = parseInt(prompt('Enter Number 1: '))
// var num2 = parseInt(prompt('Enter Number 2: '))
// document.write('<br>')
// sum(num1,num2)

// 3. No parameters return
// function sum(){
//     var num1 = parseInt(prompt('Enter Number 1: '))
//     var num2 = parseInt(prompt('Enter Number 2: '))
//     var res = num1 + num2
//     return res
// }

// document.write(prompt('Enter Your Name: '))

// console.log(sum())

// function sum(x,y) {
//     return parseInt(x) + parseInt(y)
// }

// let num1 = 7
// let num2 = 5
// console.log(sum(4,5))
// console.log(sum(num1,num2))
