function sayHello() {
    let name = prompt("Как Вас зовут");
    alert(`Здравствуйте, ${name}, предлагаю воспользоваться калькулятором`)
    window.console.log(1+1);
}



function sum() {
    let a = parseInt(prompt("Enter number a"));
    let b = parseInt(prompt("Enter numbe b"));
    alert(sum(a,b));
    return a+b;
}

let calc = "";
let firstElem = "" ;
let secondElem = "" ;
let operandElem = "" ;
let archiveElem = "" ;
document.getElementById("result").innerHTML = "0"
document.getElementById("demo").innerHTML = ""

function resultTwo(elem1,operand,elem2){
    if (elem1=='') {elem1='0'; operand='+';}
    if (elem2=='') {elem2='0'; operand='+';}
    a =parseFloat(elem1)
    b =parseFloat(elem2)
    // window.console.log(a,b)
    if (operand=="+"){
        return a+b
    }
    else if (operand=="-"){
        return a-b
    }
    else if (operand=="*"){
        return a*b
    }
    else if (operand=="/"){
        return a/b
    }
}

function myFunction(x) {
    const numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.'];
    const operations = ['*', '/', '+', '-']
    document.getElementById("result").innerHTML = ""
    // document.getElementById("result").innerHTML = `start x=${x} a=${firstElem} ${operandElem} b=${secondElem}`
    if (numbers.includes(x,0)) {
        if ((operandElem=="")){
            firstElem += x
        }
        else {
            secondElem += x
        }
       document.getElementById("demo").innerHTML += x;

    }
    else if (operations.includes(x,0)) {
        if (secondElem==""){
            operandElem=x
        }
        else {
            firstElem = resultTwo(firstElem,operandElem,secondElem)
            secondElem = "" ;
            operandElem=x

        }
        document.getElementById("demo").innerHTML += x;
    }
    else if (x=="=") {
        result = resultTwo(firstElem,operandElem,secondElem);
        expression = document.getElementById("demo").innerHTML;
        document.getElementById("demo").innerHTML = "";
        document.getElementById("result").innerHTML = result;
        secondElem = "" ;
        firstElem = "" ;
        operandElem = "" ;


        document.getElementById("archive").innerHTML += `<p>${expression} = ${firstElem} ${result}</p>`
    }
    else if (x=="clear") {

        secondElem = "" ;
        firstElem = "" ;
        operandElem = "" ;
        document.getElementById("demo").innerHTML = "";
        document.getElementById("result").innerHTML = "0"
    }
    else {
        alert(`InputError! ${x} not supported.`)
    }

  }
