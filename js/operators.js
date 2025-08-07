// Unary operators: 
// ++ -- 
var x = 5 
// x++ // x = x + 1
// x-- // x = x - 1
// ++x //
console.log(x++) // 5 x will be 6 after printing 
console.log(x) // => 6
console.log(++x) // 7

// Binary operators:
// Arithmetic Operators: + - * / % 
var y = x + 2; // 7 + 2 => 9 
// Assignment Operators: = += -= *= /=  %= 
x += 2 // => x = x + 2 
console.log(x) // 9
// Comparison Operators: < > <= >= == != === !==
var j = 5;
if (j == "5"){ // true 
    console.log('Hello') 
}
else{
    console.log('Not Hello')
}


if (j === "5"){ // false 
    console.log('Hello')
}
else{
    console.log('Not Hello')
}

// Logical Operators: && || ! 

//  expression && expression && expression ... all of them true => true 
//      if any one of them false => false 
// expression || expression || expression ... one of them true => true
//  if all of them false => false 

//  String concatenation:
var str1 = 'Ahmed'
var str2 = 'Ali'
var num = 10 
console.log(str1 + ' ' + str2) // AhmedAli
console.log(str1 + num) // Ahmed10

// Ternary operators: 
// condition ? trueExpression : falseExpression => short hand if .. else statement 

// let PMarks = 50;
// // if (PMarks > 39){
// //     res = "Pass"
// // }
// // else{
// //     res = "Fail"
// // }
// let res = (PMarks > 39) ? "Pass" : "Fail";
// console.log(res);
// let userSalary = parseFloat(prompt('Enter Your Salary: '))

// alert((userSalary > 10000) ? 'You have valid range of salary': "Sorry, You don't have the required range")

