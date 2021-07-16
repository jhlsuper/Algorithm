
// cannot be a reserved keyword
// should be meaningful 
// Cannot start with a number (1name) 
// caanot contain a space or hypen (-)
//  ex) firstName 이런식으로 쓰자 
// are case-sensitive 대소문자 구분한다!!
// const는 못바뀐다. 

// js는 다이나믹 언어이다. 변수에따라 타입이 변함

//object  - class랑 비슷 key-value 
let person = {
    name: 'JeffLee',
    age: '25'
};
person['name'] = 'jeehyun'
person.name = 'jehyun'

//
console.log(person);

// Array  [] 다이나믹하다잉  
let selectedColors = ['red', 'blue'];
selectedColors[2] = 1 // type 달라도추가 

console.log(selectedColors.length);

// functions 함수 
function greet(name, lastName) { //여기서 name은 파라미터

    console.log('Hello ' + name + ' ' + lastName);
}

greet('JeffLee', 'lee');  //여기서 들어가는 jeff lee가 argument
greet("nononon") //인자 안주면 undefined로 나타난다. 

//calcuation a value
function square(number) {
    return number * number;
}
let number = square(2);
console.log(number);
