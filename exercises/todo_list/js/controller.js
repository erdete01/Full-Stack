/* jshint esversion: 6 */
/* jshint node: true */
/* jshint browser: true */
"use strict";

var team = ["Aardvark", "Beaver", "Cheetah", "Dolphin", "Elephant", "Flamingo", "Giraffe", "Hippo"];
var priority = ["Low", "Normal", "Important", "Critical"];

var myRosterModel = new Clowder();
var myClowderView = new ClowderView(myRosterModel);

function addTask() {
    if (!document.querySelector("#newList").checkValidity()) {
        document.querySelector("#listName").setAttribute("style", "background-color: pink;");
        document.querySelector("#listDate").setAttribute("style", "background-color: pink;");
        return;
    }
    document.querySelector("#listName").setAttribute("style", "background-color: white;");
    document.querySelector("#listDate").setAttribute("style", "background-color: white;");

    let name = document.querySelector("#listName").value;
    let assign = document.querySelector("#listAssign").selectedOptions[0].value;
    let priority = document.querySelector("#listPriority").selectedOptions[0].value;
    let date = document.querySelector("#listDate").value;

    let newList = new Task(name, assign, priority, date);
    myRosterModel.adopt(newList);

    if (myRosterModel.size === 1) {
        let cleanUpBtn = document.createElement("button");
        cleanUpBtn.setAttribute("type", "button");
        cleanUpBtn.setAttribute("id", "cleanBtn");
        cleanUpBtn.setAttribute("class", "btn btn-warning");
        cleanUpBtn.setAttribute("onclick", "cleanList()");
        cleanUpBtn.innerText = "Clean up the list";
        let body = document.querySelector("body");
        body.appendChild(cleanUpBtn);
    }
}

function cleanList() {
    myRosterModel.cleanList();
    if (myRosterModel.size == 0) {
        let cleanUpBtn = document.createElement("button");
        let body = document.querySelector("body");
        body.removeChild(cleanUpBtn)
    }
}

function populateSelectOption(elementId, optionsArray) {
    let menu = document.querySelector(elementId);
    for (let artist of optionsArray) {
        let newOption = document.createElement("option");
        newOption.setAttribute("value", artist);
        newOption.innerHTML = artist;
        menu.appendChild(newOption);
    }
}

window.onload = function () {
    populateSelectOption("#listAssign", team);
    populateSelectOption("#listPriority", priority);
};
