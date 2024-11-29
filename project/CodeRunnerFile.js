// // getting div for below operations

// // getting the attribute
// let div = document.querySelector('div');
// console.log(div);

// let p = document.querySelector('p');
// console.log(p);

// let id = div.getAttribute('id');
// console.dir(id);
// let name = div.getAttribute('name');
// console.dir(name);

// //changing the attribute value

// console.log(p.setAttribute('name','kabat'));


// p.style.color = 'darkblue';

// // create element with document

// let btn = document.createElement('button');
// console.log(btn);

// btn.innerText = btn.innerText = 'Submit';
// console.log(btn);

// btn.setAttribute('type','submit');

// //adding created document in dom with append method
// div.append(btn);

// // adding created document in dom with prepend method so we can get element on top of each element in same parent element

// div.prepend(btn);

// // adding created document in dom with before method so we can element before div element

// div.before(btn);

// // adding created document in dom with after method so we can element after div element

// div.after(btn);

// // delete element with dom

// p.remove();


// // the change in state of an object is known as an event
// // Events are fired to notify code Of interesting code that may affect code execution

// // with element reference like element name,id,class

// let btn1 = document.querySelector('#btn1');

// btn1.onclick = () => {
//     console.log('button clicked');
//     let a = 25;
//     a++ 
//     console.log(a);
// }


// // with funtions 

// function mousein(event) {
//     console.log(event,'you are in');
// };


// function mouseout(event) {
//   console.log(event,"You are out");
// };

// // with element reference changing element behaviour

// let div1 = document.querySelector('div');

// //arrow function method

// div.onmouseenter = () => {
//     console.log('you are entered div')
// }

// // traditional function method

// function onmouseleave () {
//     console.log('You have leaved div')
// }

// div.onmouseleave = onmouseleave // with this we are assigning the event to a funtion , means the event will call


// //add event listners with arrow function

// let btn2 = document.querySelector('#btn2')

// btn2.addEventListener('click', () => {
//     console.log('Button Was Clicked');
// });


// // add event listners with arrow function

// let btn3 = document.querySelector('.btn3');

// btn3.addEventListener('click', function() {
//     console.log('Button 3 Was Clicked');
// });


// //remove event listner

// btn3.addEventListener("click", function () {
//   console.log("Button 3 Was Clicked 1");
// });
// const eventhandler2 = function () {  // if we want to remove this we have to provide it in a variable so we can pass it as variable so the memory of the same varible should be removed
//   console.log("Button 3 Was Clicked 2")};

// btn3.addEventListener("click", eventhandler2);
// btn3.addEventListener("click", function () {
//   console.log("Button 3 Was Clicked 3");
// });


// btn3.removeEventListener("click", eventhandler2);
