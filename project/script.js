//import promptsync
// import promptSync from "prompt-sync";
// import { isMethodSignature } from "typescript";

// // Initialize prompt
// const prompt = promptSync();

/* learning the js */
/*
console.log('Hello, World');

let a = 10;
let b = 15;

// arithmatic operators 
console.log('a = ', a, 'b = ',b,'a + b = ' , a + b, 'a - b', a - b, 'a * b', a * b, 'a / b', a / b);

// modulus 

console.log('a % b = ' , a % b);

// exponentiation 

console.log('a ** b =' ,a ** b);

// unary operato
// inceament 
a ++; // this will changes effect in next line , this is post increament
a --; // same for this as above , this is post decreament 
++a; // this changes the value on the same line , this is pre increamnet
--a; // same as above , this is pre decreament
console.log('increament of a by b = ',a); 

// assignment operators

a += 1;
console.log('a +=  = ',a);
b -= 1;
console.log('a -=  =', b);
a *= 2;
console.log('a *=  = ',a );
a/= 5;
console.log('a /=  =',a);
a %= 5;
console.log('a % 5 = ',a);
a **= 4;
console.log('a **  4  =',a);

// comparison operator

console.log('a == b',a == b);
console.log('a != b',a != b);
console.log('a > b',a > b);
console.log('a < b',a < b);
console.log('a <= b',a <= b);
console.log('a >= b',a >= b);
a = '14';
console.log('this will compare string with a number',a == b); // this will compare string with a number as js code is so fast in compiling 
// stricter version of equal to 

console.log('this is strict it doesnt allow to compare string with number : ',a === b);

console.log('This is strict not equal to allow to compare number with number , will not compare string with number : ', a !== b);

// logical operator 
a = 14;


let condi1 = a > b; //false
let condi2 = a === b; //true , before that i was getting false cause of declaring variable after 
/* new varible creation as a = 14 after condi2 as a variable was declared 
as i had a varible a with value '14' as a = '14' so in the comparision operator i was getting error due to strict comparison operator that
is === */

//console.log('condition 2',condi2);

// and operator

//console.log('condi1 && condi2 :', condi1 && condi2);
// in above both statement have to be true otherwise will get result false

// or operator

//console.log('condi1 || condi2 :', condi1 || condi2);
// in the above statement one condition have to be true then result will be true
// if both condtions are false then result will be false

// not
// this will give opposite result of coditions
// as condi1 will give true and condi2 will false

//console.log('condi1 is false but true with not operator', !condi1);
//console.log('condi2 is true but will be false as above : ',!condi2 );

// conditional statements
// if statement
/*
let age = 17;
if (age >= 18){
    console.log('You Can Now DRIVE');
}

if (age < 18){
    console.log('You Are Nor Ready For DRIVE');
}


let mode = 'light';
let color;

if (mode === 'light'){
    color === 'white';
    console.log('Light Mode Is Enabled');
}
if (mode === 'dark'){
    color === 'black';
    console.log('Dark Mode Is Enabled');
}

// if-else statement

if(mode === 'dark'){
    color = 'black';
    console.log('Dark Mode Is Enabled');
} else {
    color = 'white';
    console.log('Light Mode Is Enabled');
}

let my_age = 18;
if(my_age >= 18){
    console.log('You Are Adult');
}else {
  console.log('You Are Not Adult');
}

// odd even with conditional statement
let x = 15175515984563;
if (x % 2 === 0){ // must use === for strictly for number only for  checking
    console.log('Even');
}else{
    console.log('Odd');
}
// else if statement 

age = 55;
if (age < 18){
    console.log('You Are Not Adult');
} else if (age >= 55){ 
    console.log('You Are Old');
}else {
    console.log("Your Are Adult");
}

// ternary operator

syntax

//condition ? true output : false output

1st method

with storing in variable 

let result = age > 18 ? 'adult' : 'not adult';
console.log(result);

without storing in variable 

age = 17;
age >= 18 ? console.log('adult') : console.log('not adult');
// above is simpler and compact if else statement in js


let expr1 = 'papayas';
let expr2 = 'oranges';
switch (expr1,expr2) { // switch statement
    
    case 'oranges' :
        console.log('oranges are 964$');
        break
    case 'mangoes' :
        console.log('mangoes are 5458$');
        break;
    case 'bananas':
        console.log('bananas are 65477$');
        break;
    default:
        console.log(`Sorry, we are out of ${expr1,expr2}.`);
}
// escape character 
let name = 'Mubarak Dalvi';
console.log(name.length); // this will give length
console.log('Mubarak\nDalvi','Mubarak\tDalvi','Mubarak\rDalvi'); // these are esscape characters
console.log(name.toUpperCase()); // this will convert string to uppercase , it is a function cause it is with paranthesis ()
console.log(name.toLowerCase()); // thsi convert string to lowercase
console.log(name.slice(0,7)); // this is to slice a string
console.log(name.replace('Dalvi','Bhai')); // this will repace 
console.log(name.trim('Bhai')); // this will trim the string



var albumu = 'shadi';
let album = 'shadi';
const albuma = 'shadi';


function EvenOdd(num) {
    if (num % 2 === 0){
        console.log('Even');
    } else {
        console.log('Odd');
    }
}

const num = 257;
EvenOdd(num);

let a = 10;  
let b = 54;

console.assert(a === 0,"failed"); // if value is not as defined then this will give 
// assertion error , and in '' qoutes we can type error message

let con1 = a > b;
let con2 = a !== b;
let con3 = a < b;
let con4 = a === b;

console.log(a + b,a - b,a * b, a / b, a % b, a ** b, a ++,b ++,a --,b --, ++ a,-- a , 
    a += b,a -= b, a *= b, a /= b, a %= b, a **= b,++ b, -- b, a == b , a === b ,a != b, 
    a !==b, a < b , a > b, a <= b,a >=b, con1 && con4,con2 && con3, con1 || con3, con4 || con2,
    !con1,!con2,!con3,!con4,!(con1,con2,con3,con4),con1 && con2 && con3, con2 || con3 || con4  
)

let result = a > b ? 'yes' :'no';
console.log(result,a,b);

function divible(num) {
    if (num % 5 === 0) {
        console.log('Number is multiple of 5');
    } else {
        console.log('Number is not multipl of 5');
    }
}
divible(3);

// grade system for student

function grade(score){
    if (score <= 100 && score >= 90) {
        console.log('Grade A');
    } else if(score <= 89 && score >= 70) {
        console.log('Grade B');
    } else if (score <= 69 && score >= 60) {
        console.log('Grade C');
    } else if (score <= 59 && score >= 50) {
        console.log('Grade D');
    } else if (score <= 0 && score >= 49) {
        console.log('F');
    }
}
grade(98);


// loops and string concepts

// for loop

for (i = 1; i <= 5 ; i ++ ){
    console.log('anpan');
}

// with repeat method we can repeat a number many times we want

for (i = 0; i <= 5; ++i){
    console.log('*'.repeat(i));
}

// eg of repeat
// regex , regular expression in js

let ab = 'anpan';
let rs = ab.repeat(5);
console.log(rs.match(/anpan/g));



let age = Number;
age = 25;
age = 15;
age = 'hi';
console.log(age);


// if we assign our og string with new string then it will be update to the new string with method only not by direct assign
//as in javaascipt strings are immutable

// split methoss
let str1 = 'i have this string abc but i have a number too which is ';
let str2 =  str1.split(' ');
console.log(str2); //output [ 'i', 'have', 'this', 'string', 'abc' ]
console.log(str1);
str1 = str1.toUpperCase(); //output  I HAVE THIS STRING ABC
console.log(str1);
//uppercase and lower case
str1 = str1.toLowerCase();
console.log(str1); //output i have this string abc
// str1 = str1.toUpperCase();
// trim method

let str3 = '              i have this string abc                     ';

let str_trim = str3.trim(); //removes white spaces from start and end not from middle
console.log(str_trim); // output i have this string abc

// slice method
//return part of string syntax str.slice(start,end?); non inclusive ending value
// if we provide slice value like our string 'myname' and we provide sting.slice(1,3) then output will be my not myn

//eg 1 as str1 is updated as uppercase , as we mutated the or string
let str4 = str1.slice(5,10);
console.log(str4);

// eg 2 
let str5 = '0123456789'
let str6 = str5.slice(0,2); 
// it will give same index but the last index provided it excluded 
// indexing start from 0
console.log(str6); // output 45678 

// concatination
let concat1 = str1.concat(str6); // wihout space it will join wil other string
let concat2 = str1.concat(" ",str6); // with space or other things in between two strings
console.log(concat1);
console.log(concat2);
console.log(str1 + ' ' + str6); // with givin hardcode values without using concat

// replace method

let str7 = str1.replace('i','you'); // just remerber the case of the string else it wont work
console.log(str7);

let str8 = str1.replaceAll('i','you'); //this will replce all the string character matching the provided characters
console.log(str8); // but not recommended as for one character it will change all other charwacter meaning

let str9 = str1.indexOf('a'); // this will give index of character at fist instance
console.log(str9);

let str10 = str1.charAt(3); //with this we will be able to see on which index which character is in string
console.log(str10);


// Prompt for age
let age = prompt('What is your age: ');

// Convert the age to a number
age = Number(age);
// Example usage of `sync` (searching for files)
// Check if age is greater than 18
if (age > 18) {
    console.log('You are ready');
} else {
    console.log('You are not ready');
}


// username creation with java script
let username = prompt('Please Enter Username:- ');

username = String(username); // redefining the variable for usage without error

if(username) {
    console.log(`@${username.toLowerCase()}${username.length}`);
}else {
    console.log('Please Provide Name For Your User Name');
}

// array is inforamtion starer linear method

let student1 = 97;
let student2 = 85;
let student3 = 97;
let student4 = 85;
let student5 = 97;

console.log(student2.valueOf()); // vaueof is property which is giving information about student2
// primitive aproach for storing key value pairs

let marks = {
  student1: 91,
  student2: 54,
  student3: 97,
  student4: 54,
  student5: 65,
};

// diff between property and methods for variables of data types
// methods do work for the variable  like upperCase  in string made all string value to capital
// property provide usefull information , in numbers valueof property which gives information about number data type
// array is special type of object
// array used index to locate values
// in object we use key to locate value
// like in marks

console.log(marks.student1); // in this we are getting value of student 1

let arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1];

console.log(typeof marks, typeof student1, typeof arr1);

console.log(arr1.indexOf(1)); //this will give first instance of 1 which is present at index 0

// array indices

console.log(arr1[2]); // in this we are getting output with index number which is 3 present on index 2

// if we try to get the index not present in array we get undefined

console.log(arr1[11]);

// if we want to change the value of an index then we can just assign it to it

arr1[9] = 10; // we have assigned index 9 value 10

// we can add new value with index method
// in this we are adding 1000 value in 999 index
// as we get answer [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, <989 empty items>, 1000 ]

arr1[999] = 1000;

console.log(arr1);

// this function creates an array of numbers
function thousandnumbers(start, end, steps) {
  const arr = [];
  if (!steps || steps <= 0) {
    console.log("Please enter a valid step value greater than 0.");
    return arr;
  }
  if (start < end) {
    for (let i = start; i <= end; i += steps) {
      arr.push(i);
    }
  } else {
    for (let i = start; i >= end; i -= steps) {
      arr.push(i);
    }
  }
  return arr;
}

const result = thousandnumbers(1, 10, 2);
console.log(result);




//primitive data types
// they are immutable
// they cannot be changed after creation

let str1 = 'Hello JavaScript';
console.log(str1, typeof str1);
// str1[0] = 'i'; immutable
// console.log(str1);

let num = 25;
console.log(num, typeof num);
// num[0] = 2;
// console.log(num);

let float = 3.14;
console.log(float, typeof float);
// float[0] = 2; 
// console.log(float);

let bool = true;
console.log(bool, typeof bool);

let Undef = undefined;
console.log(Undef, typeof Undef);

let Null = null;
console.log(Null, typeof Null);

let sym = Symbol('description');
console.log(sym, typeof sym);

let bnum = 1564516485156444877148974894;
console.log(num,typeof(bnum));

// mutable data types in js

let obj = { name: "Alice", age: 25 };
console.log(obj,typeof(obj));

let arr = [1, 2, 3, 4];
console.log(arr,typeof(arr));

function greet() {
  console.log("Hello!");
}

console.log(typeof(greet))

let date = new Date();
console.log(date,typeof(date));

let regex = /ab+c/i;
console.log(regex,typeof(regex));

let map = new Map();
console.log(map,typeof(map));

let set = new Set([1, 2, 3, 1]);
console.log(set,typeof(set));



function thousandnumbers(start, end, steps) {
  const arr = [];
  if (!steps || steps <= 0) {
    console.log("Please enter a valid step value greater than 0.");
    return arr;
  }
  if (start < end) {
    for (let i = start; i <= end; i += steps) {
      arr.push(i);
    }
  } else {
    for (let i = start; i >= end; i -= steps) {
      arr.push(i);
    }
  }
  return arr;
}

const result = thousandnumbers(1, 100, 1);
console.log(result);

for (let r of result){
    console.log(r);
}


for (let i=0; i < result.length; i++){
    console.log(result[i]);
}


// for of loop
// for is used to access the value of the variable 
// for in used to access the index for the variable
let fruits = ["apple","banana","cherry","dragon fruit","egg fruit", "Fig", "Guava", "ice apple", "jack fruit", "kiwi", "lemon", "mango", "nance"]

for (let fruit of fruits){
    console.log(fruit);
}

// for in loop
console.log('-----------------------------------------')
let cities = ['delhi','mumbai','noida','bangalore','pune','chennai','kochi'];

for (let city of cities){
    console.log(city.toUpperCase());
}



let sum = 0; // remmber to intialize the value with zero // if dont wan to change variable value then we can use const
let marks = [85,97,44,37,76,60];
for (let mark of marks) {
    sum += mark;
}
let result = sum / marks.length;
console.log(sum,result);


// generate otp 

function generatorotp(length) {
  let otp = "";
  const digits = '1234567890';
  for (let i = 0; i < length; i++) {
    otp += digits.charAt(Math.floor(Math.random() * digits.length));
  }
  return otp;
}
 
const otp = generatorotp(6);
console.log(otp);


// user validation with otp
function userValidation(otp = generatorotp(6)) {
    console.log(otp);
  let attempt = 0;
  let maximum_attempt = 3;
  let isAuthenticated = false
  while (attempt < maximum_attempt && !isAuthenticated) {
    let userInput = prompt("Please Enter OTP : ");
    if (userInput == otp) {
      console.log("You Have Entered Correct OTP");
      isAuthenticated = true;
    } else {
      console.log("Please Enter Valid Ouput");
    }
    attempt += 1;
  }
  if (!isAuthenticated) {
    console.log("Maximum attempts reached. Please try again later.");
  }
}
 
userValidation()


// minus 10% of every element in array

let item = [250,645,300,900,50];

for(let i = 0; i < item.length; i++){
    item[i] -= item[i] * 0.10
}
console.log(item);



// array method
// push , its add new value
let vegitables = ['potato','tomato','cabbage','lady finger'];
console.log(vegitables);
console.log(vegitables.push('cauli flower')) // this method returns updated lenght if we use console.log 
console.log(vegitables); // as in this method no length is returning
vegitables.push('coriander','onion','garlic');
console.log(vegitables);

console.log(vegitables);
// pop it deletes last  value 
 
let deletedItem = vegitables.pop();
console.log(vegitables);
console.log("deleted Item",deletedItem);

// to string it converts an array to string
// this method does not made changes in original array
let tostring = vegitables.toString();
console.log(typeof(tostring));
console.log(typeof(vegitables));

// concat methods this join multiple array and does not changes original array it gives new result

let marvel = ['Thor','Ironman','Spiderman'];
let dc = ['Suparman','Batman','Flash'];

let heroes = marvel.concat(dc);
console.log(heroes);

// unshift it is used to add new value in start


heroes.unshift('Antman');
console.log(heroes);

// shift it use to delete from start
// it return and make changes in original string
heroes.shift();
console.log(heroes); // it


// slice returns piece of array
// it returns new result and does not make changes in original array
console.log(heroes.slice(1,3));

//splice method changes original array
// add, remove , replace these 3 operations done by this splice method


let arr = [1,2,3,4,5,6,7];
let arr2 = [45,4,6,4,54,7,4,5,89,4,89]
arr.splice(2, 0, arr2); // 2 is index ,0 is how many value i want to delete , how many element i want to add 10 and 15 i have added
console.log(arr);



// functions ate block of code that performs a specfc taks can be invoked
// we can call function as many as time
// function minizes redundency , repeatations
// the function defianation have paramete which are used to input
// function call have the argument which in we provide value
// the code never run after return statement in a block of function
// the function parameter will acts as a local variable which are accessible only in function block
// simple functions
function sum(num1,num2) { // these are parameter they are accessible on functions block level
    let result = num1 + num2;
    return result
}
let result = sum(1,5); // these are argument when calling function means sum(1,5) and we are assingning it to result variable
console.log(result);
// arrow funtions

const arrowSum = (num1,num2) => {
    result = num1 + num2;
    console.log(result);
};

arrowSum(5,5);

 
// call back funtion it is a function to excute for each element in array
// a call back is a function is passed to another function as an argument

// for each loop in arrays
let arr = [0,1,2,3,4,5,6,7,8,9];
arr.forEach(function printVal(val){ //each value at each index
    console.log(val);
});

// arrow funtions as callbacl

arr.forEach((val,i, arr) => {
    console.log(val, i, arr);
})


// map method of array
// create a new array with results of some operations the value its callback returns are use to form new array
// map used when creating new array

let newarr = arr.map((val) => {
    return val ** 2;
});
console.log(newarr);


// filter method array
let Evenarr = arr.filter( (val) => {
    return val % 2 === 0;
});
console.log(Evenarr);

let Oddarr = arr.filter( (val) => {
    return val % 2 === 1;
});
console.log(Oddarr);

// reduce method
// it reduces the array to single value and returns that single value
//for summing the array
const output = arr.reduce((res, curr) => {
    return res + curr;
});

console.log(output);
// for getting bigger value we can use this method

const max = arr.reduce((res, curr) => {
  return res > curr ? res: curr;
});

console.log(max);

// for getting smallest value we can use this method

const min = arr.reduce((res, curr) => {
  return res < curr ? res: curr;
});

console.log(min);




// binary search algorithm

//dom document object model

// readability
//modular
//browser caching
//Html struct
// CSS style
// Js Logic
// window object

// given this file as script for logical understanding connected to index.html
// when we add js file in head of document then the dom element are not accessible or the js cannot find element
//as  they are not loaded yet so its a better approach to always add js file in bottom before end body tag

//dom notes in js notes available

// the change in state of an object is known as an event
// Events are fired to notify code Of interesting code that may affect code execution

//events in note of js notes

// classes and onject oops
// object

// A javascript object is an entity having state means property and behaviour means functions property and methods
// Js object has special property called prototype which is also object which have properties and methods
// We can set prototype using __proto__

const student = {
  name: "michael",
  surname: "schumacher",
  marks: 95.2,
  getMarks: function () {
    console.log(`your marks ${this.marks}  ${student.marks}`); // like this we can access but
  }, // student.marks we cannot accces the marks before initialization od student object
};

const employee = {
    calcTax() {
        console.log('Tax rate is 100%')
    }
}

function calcTax() { // outside object we will get error
        console.log('Tax rate is 100%')
    };

let newEmployee1 = {
    name: 'karan',
    salary: 500000
}

// with the prototype we will be able to use other object inside the same object
// now we will use employee in  newemployee 
// __proto__ is use to se prototype whixh mean 
// the prototype we are making of object we can use it property ,method
// prototype property is actually a null and in mostly cases it is a reference to an object


newEmployee1.__proto__ = employee; // here we are setting newEmployee proto to employee

// now we are adding tax rate the object , and with proto we have also another object method 
// and if we call calcTax then newEmployee calcTax will be called not from employee calcTax
// cause it is defined in the same object,the object dont need to use other object method if it have the
// method in the same object


let newEmployee2 = {
  name: "karan",
  salary: 500000,
  calcTax () {
    console.log("Tax rate is 100%");
  }
};

let emp = {
    emp1 : {
        id: 1,
        name: 'myname',
    },
    emp2 : {
        id: 2,
        name: 'yourname'
    }
}

console.log(emp.emp1);
*/


//Class


//Class in a programme code template for creating object
// Those objects will have some state (variable) and some behaviour (function) inside it

// when we want to create a similar object in bulk or on bigger level then we dont want to create 
// same rule and repeat it for all the items , that why we use class, 
// classes are blueprint of js


class toyotaCar {
    start () {
        console.log('Car Started');
    }
    stop () {
        console.log('Stop');
    }
}

let fortuner = new toyotaCar();

