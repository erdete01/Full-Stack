/* jshint esversion: 8 */
/* jshint node: true */
/* jshint browser: true */
/* jshint jquery: true */
'use strict';

async function getData(url) {
    return fetch(url)
    .then(response => response.json())
    .catch(error => console.log(error));
}

async function getInfo() {

    // This should empty everything before adding a new value
    document.getElementById("posts").innerHTML = "";

    let number = document.querySelector("#inputNumber").value;

    // Converting a string into a number and then assigning to a variable
    const count = Number(number);
    var n1 = count - 1;
    var n2 = count + 1;

    // converting number to a string
    var oneBelow = n1.toString();
    var oneAbove = n2.toString();
    var currentNumber = count.toString();

    let allPostsDiv = document.querySelector("#posts");

    // Fetching and getting a Json File
    let post1 = await fetch("http://numbersapi.com/"+oneBelow+"?json")
    .then(response => response.json())
    .catch(error => console.log(error));

    let postDiv = document.createElement("div");
    postDiv.innerHTML = post1["text"];
    allPostsDiv.appendChild(postDiv);
    console.log(postDiv);

    let post2 = await fetch("http://numbersapi.com/"+currentNumber+"?json")
    .then(response => response.json())
    .catch(error => console.log(error));

    let postDiv2 = document.createElement("div");
    postDiv2.innerHTML = post2["text"];
    allPostsDiv.appendChild(postDiv2);
    console.log(postDiv2);

    let post3 = await fetch("http://numbersapi.com/"+oneAbove+"?json")
    .then(response => response.json())
    .catch(error => console.log(error));

    let postDiv3 = document.createElement("div");
    postDiv3.innerHTML = post3["text"];
    allPostsDiv.appendChild(postDiv3); 
}

 async function getInfo2() {

    // This should empty everything before adding a new value
    document.getElementById("posts").innerHTML = "";
    
    let number = document.querySelector("#inputNumber").value;

    // Converting a string into a number and then assigning to a variable
    const count = Number(number);
    var n1 = count - 1;
    var n2 = count + 1;

    // converting number to a string
    var oneBelow = n1.toString();
    var oneAbove = n2.toString();
    var currentNumber = count.toString();

    // let allPostsDiv = document.querySelector("#posts");
    let allPostsDiv = document.querySelector("#posts");

    // Requesting all the data with one request
    let checkBox = await fetch("http://numbersapi.com/"+oneBelow+".."+oneAbove+"?json")
    .then(response => response.json())
    .catch(error => console.log(error));

    var firstDict = checkBox[oneBelow];
    var secondDict = checkBox[currentNumber];
    var thirdDict = checkBox[oneAbove];

    let postDiv = document.createElement("div");
    postDiv.innerHTML = firstDict["text"];
    allPostsDiv.appendChild(postDiv);
    let postDiv1 = document.createElement("div");
    postDiv1.innerHTML = secondDict["text"];
    allPostsDiv.appendChild(postDiv1);
    let postDiv2 = document.createElement("div");
    postDiv2.innerHTML = thirdDict["text"];
    allPostsDiv.appendChild(postDiv2);
 }



