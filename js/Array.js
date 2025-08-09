// Array 
//  Array Object has One Property (length)

let arr = [10, 'Ahmed', 'Aya', 20, true, 42.5] // support different types 
console.log(arr[0])  // Access aya member by index (Start from 0)
console.log(arr[2])

let arr2 = new Array(10, 'Mohamed', true)
console.log(arr2[1])
console.log(arr2[5]) // undefined

arr[0] = 20;
console.log(arr)
console.log(arr.length)
// Array Methods
// join() -> convert array items into string 
document.writeln(arr.join("<br>"))
document.writeln(typeof(arr.join())) // string

// reverse()
console.log(arr)
console.log(arr.reverse())

// push() Appends new elements to the end of an array, and returns the new length of the array.
arr.push(25)
console.log(arr)

// pop()
let x = arr.pop()
console.log(x)
console.log(arr)
console.log(arr.pop())
console.log(arr)

// shift() Removes the first element of an array, and returns that element
console.log(arr.shift())
console.log(arr)

// unshift()
console.log(arr.unshift(44.5))
console.log(arr)

// sort() 
const fruits = ["Banana", "Orange", "Lemon", "Apple", "Mango", "Cherries"];
fruits.sort();
console.log(fruits)
const numbers = [3, 1, 4, 7, 5, 9, 2, 6];
console.log(numbers.sort()) // Ascending 
console.log(numbers.sort().reverse()) // Descending 

// slice()
console.log(fruits.slice(1, 3)); // ['Banana', 'Cherries']

// splice()
const months = ["Jan", "March", "April", "June"];
months.splice(1, 0, "Feb", "new", 'NewAgain');
console.log(months) // ['Jan', 'Feb', 'new', 'NewAgain', 'March', 'April', 'June']
months.splice(2,2)
console.log(months) // ['Jan', 'Feb', 'March', 'April', 'June']

// find()
const array = [5, 12, 8, 130, 44];
const found = array.find((element) => element > 10);
console.log(found); // 12

// filter()
const words = ["spray", "elite", "exuberant", "destruction", "present"];
const result = words.filter((w) => w.length > 6);
console.log(result); // ['exuberant', 'destruction', 'present']
