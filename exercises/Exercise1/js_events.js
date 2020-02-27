/* jshint esversion: 8 */
/* jshint node: true */
'use strict';

console.log("Hello from the console");

// Question 1
function isPrime(n)
{
  if (n < 2)
  {
    return false;
  }else
  {
    for(var i = 2; i < n; i++)
    {
      if(n % i === 0)
      {
        return false;
      }
    }
    return true;  
  }
}

// Question 2
function getNPrimes(n)
{

    if (isPrime(n) == true) {
      var myList  = [], primes = [];
      for (var i = 2; i <= n; ++i) 
      {        
          if (!myList [i]) 
            {
              primes.push(i);        
              for (var j = i << 1; j <= n; j += i) 
              {
                  myList[j] = true;
              }
          }
      }
      return primes;
    } 
}

//Question 3
function printNPrimes(n){ 

  const queryString = window.location.search;
  const urlParams = new URLSearchParams(queryString);
  let number = urlParams.get('n')
  // let printing = document.querySelector("th");
  // printing.innerHTML = `${number}`;
  
  //console.log(primes.toString())
}
//Greet By Name
function greetByName() {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    if (name = urlParams.get('name')) {
    let name = urlParams.get('name');
    let greet = document.querySelector("h1");
    greet.innerHTML = `Hello ${name}`;
      }
    else 
      greet.innerHTML = `Hello Student`;
}

//Print Numbers in a List


//Calling Function
window.onload = function() {
  this.greetByName();
  this.printNPrimes();
};