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

//Question 3
function printNPrimes() 
{
    getNPrimes(330);
    //console.log(toString())
}

//Greet By Name
function greetByName() {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const name = urlParams.get('name');
    //let name = urlParams.get('name');
    let greet = document.querySelector("h1");
    greet.innerHTML = 'Hello ${name}';
}

//Calling Function
window.onload = function() {
    this.printNPrimes();
    this.greetByName();
};

