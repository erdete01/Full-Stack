/* jshint esversion: 8 */
/* jshint node: true */
/* jshint browser: true */
/* jshint jquery: true */
'user strict';

var quantities = [1, 2, 3, 4, 5, 6, 7, 8, 9];
var stores = ["Marty's", "Caf", "Oneote", "C-Store"];
var sections = ["Candy", "Food", "Drinks", "Snacks"];
var priorities = ["Critical", "Important", "Not Important"];


// Populating the list
function populateSelect(selectId, selectItems) {
    let sel = document.querySelector(selectId);
    for (let item of selectItems) {
        let opt = document.createElement("option");
        opt.value = item;
        opt.innerHTML = item;
        sel.appendChild(opt);
    }
}

var myShoppingModel = new Lab()
var myShoppingView = new View(myShoppingModel);

function addItem() {

    // Until a user enters a valid value, it won't add anything
    if (!document.querySelector("#item_list").checkValidity()) {
        return;
    }

    let names = document.querySelector("#item_name").value;
    let quantities = document.querySelector("#item_quantity").selectedOptions[0].value;
    let prices = document.querySelector("#item_price").value;
    let stores = document.querySelector("#item_store").selectedOptions[0].value;
    let sections = document.querySelector("#item_section").selectedOptions[0].value;
    let priorities = document.querySelector("#item_priority").selectedOptions[0].value;

    let newList = new shoppingList(names, quantities, prices, stores, sections, priorities);
    myShoppingModel.add(newList);

    // Adding it to localStorage
    let storage = localStorage.getItem("newList");
    storage = storage ? JSON.parse(storage) : [];
    let selNames = ["item_name", "item_quantity", "item_price", "item_store", "item_section", "item_priority"];
    let localStorageList = {};
    for (let i of selNames) {
        localStorageList[i] = document.getElementById(i).value;
    }
    console.log(localStorage);
    storage.push(localStorageList);
    localStorage.setItem("storage", JSON.stringify(storage));
}

// Removes everything from localstorage
function removeAllItem() {
    localStorage.removeItem("newList");
}

// Even when the page refreshes, the list does not go away
function saveList() {

    let vals = JSON.parse(localStorage.getItem('newList'));
    let tableList = document.querySelector('#tableList');

    // To Display a list here. incomplete
}

// When the button is clicked, it removes an item
function cleanList() {
    myShoppingModel.cleanList();
}

window.onload = function()  {
    populateSelect("#item_quantity", this.quantities);
    populateSelect("#item_store", this.stores);
    populateSelect("#item_section", this.sections);
    populateSelect("#item_priority", this.priorities)
    addItem();
}
