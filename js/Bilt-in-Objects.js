// // String Object 
// let str1 = "Hello and Welcome in javascript course"
// // let str2 = new String('Hello again!')

// // just one property length 
// // console.log(str2.length) // 12
// console.log(str1[1]) // e 
// // 1. Array Methods manipulating the contents of the String
// console.log(str1.charAt(4)) // o 
// console.log(str1.indexOf('a')) // 6
// console.log(str1.lastIndexOf('a')) // 24
// console.log(str1.substring(0,4)) // Hell -> last one not included 
// console.log(str1.replace(/Hello/,"Hi")) // replace don't change the original string
// console.log(str1)
// // 2. Array Methods manipulating the appearance of the String
// document.writeln(str1)
// document.writeln(str1.bold())
// document.writeln('Hello'.fontcolor('red'))
// document.writeln('<h1>Hello Head 1</h1>')
// // ---------------------------------------------
// // Math Object 
// console.log(Math.random()) // -> Number between 0 and 1 
// console.log(Math.floor(2.9)) // 2 -> (2 - 3)
// console.log(Math.ceil(2.1)) // 3 -> (2 - 3)
// console.log(Math.round(2.7)) // 3 -> (2 - 3)
// console.log(Math.round(2.3)) // 2 -> (2 - 3)
// ---------------------------------------------
// Object 
// const person = {
//     firstName: "Ahmed",
//     lastName: "Adel",
//     age: 50,
//     eyeColor: "blue",
//     show: function(name) {
//         return 'Hello ' + name
//     }
// };

// console.log(person['firstName']) // Ahmed
// console.log(person.lastName) // Adel
// person.firstName = 'Basmala'
// console.log(person)
// console.log(person.show(person.firstName))
// console.log(person.show('Aya'))

// delete person.eyeColor
// console.log(person)

// -----------------------------------------------
// Date() Object 

// const months = ["January","February","March","April","May","June","July","August","September","October","November","December"];
// var date = new Date()
// // document.writeln(date)
// document.writeln(date.getFullYear())
// document.writeln(date.getMonth())
// var month = months[date.getMonth()] // getMonth() 0 - 11 
// console.log(month)


// var ul = document.getElementById('demo')
// const li = document.createElement("li");
// const li2 = document.createElement("li");
// const li3 = document.createElement("li");

// li.append(`The Full Year is: ${date.getFullYear()}`)
// li2.append(date.getMonth())
// li3.append(date.getHours())
// ul.append(li,li2,li3)
// document.writeln(`<br>${date.toLocaleString()}`)
// document.writeln(`<br>${date.toLocaleTimeString()}`)

