/* jshint esversion: 8 */
/* jshint node: true */
/* jshint browser: true */
/* jshint jquery: true */
'use strict';

// Greetings
var today = new Date();
var hourNow = today.getHours();
var greeting;

if (hourNow > 18) {
    greeting = 'Good evening!';
} else if (hourNow > 12) {
    greeting = 'Good afternoon!';
} else if (hourNow > 0) {
    greeting = 'Good morning!';
} else {
    greeting = 'Welcome!';
}
document.getElementById("greeting").innerHTML = greeting;

async function getData(url) {
    return fetch(url)
    .then(response => response.json())
    .catch(error => console.log(error));
}

async function getInfo() {

    // Assigning my own APIKEY to a String
    // Source: https://openweathermap.org/api
    var api = "44ee37cb145f80bd5ff333aaec7c6c57";
    let cityName = document.querySelector("#inputName").value;
    
    if (cityName != ""){

        // Fetching and getting a Json File
        let post = await fetch("https://api.openweathermap.org/data/2.5/weather?q="+cityName+"&appid="+ api+"&units=metric")
        .then(response => response.json())
        .catch(error => console.log(error,"The City Does not Exist"));

        // Adding information to the table
        let allPostsDiv = document.querySelector("#post > tbody");
        allPostsDiv.innerHTML = "";
        let row = document.createElement("tr");
        let city = document.createElement("td");

        // Adding cityname to the table
        city.innerHTML = cityName;
        row.appendChild(city);

        // Adding temperature to the table
        let temp = document.createElement("td");
        const temperature = post.main.temp;
        temp.innerHTML = temperature;
        row.appendChild(temp);
        allPostsDiv.appendChild(row);

        // Adding description to the table
        let descr = document.createElement("td");
        const weather = post.weather[0].description
        descr.innerHTML = weather;
        row.appendChild(descr);

        // Adding an Icon to the table
        let io = document.querySelector("#td");
        var x = document.createElement("IMG");
        const icon = post.weather[0].icon
        const imageURl = "http://openweathermap.org/img/wn/"+icon+"@2x.png"
        x.setAttribute("src", imageURl);
        row.appendChild(x);

        // Adding latitude and long to the paragraph for a later use
        let lat = document.createElement("td");
        let par = document.querySelector("#get2")
        var myArray = []
        const coordinator2 = post.coord.lon
        const coordinator = post.coord.lat
        myArray.push(coordinator);
        myArray.push(coordinator2)
        lat.innerHTML = myArray;
        par.innerHTML = myArray;
        row.appendChild(lat);

        
        // Let's Set up a LocalStorage
        // let menu = localStorage.getItem("post");
        // let myStore = {};
        // let names = ["cityName", "temperature", "weather", "x", "myArray"];
        // for (let i of names) {
        //     myStore[i] = document.getElementById(i).value;
        // }
        // menu.push(myStore);
        // console.log(menu);
        // console.log(cityName, temperature, weather, x , myArray)

        let getNumbers = document.querySelector("#get2").innerHTML;
        var array = JSON.parse("[" + getNumbers + "]");
        console.log(array[0]);
        var options = {
            zoom: 10,
            center: {lat:array[0], lng:array[1]}
        }
        //  map
        var map = new
        google.maps.Map(document.getElementById('map'),options);

        //  marker
        var marker = new google.maps.Marker({
            position:{lat:array[0], lng:array[1]},
            map:map
        });
    }
}
