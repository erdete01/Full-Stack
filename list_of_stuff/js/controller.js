/* jshint esversion: 6 */
/* jshint node: true */
/* jshint browser: true */
"use strict";

var stores = ['Fareway', 'Ace Hardware', 'Caseys', 'The Hatchery', 'Amundsens']
var sections = ['Produce', 'Meats', 'Cereal', 'Canned Goods', 'Frozen Foods', 'Dairy', 'Liquor', 'Tools', 'Clothing']

var shoppingModel = new ShoppingList()
var myView = new ShoppingView(shoppingModel)

// add Button
function clickedon() {
    let rowcolids = ['itemname', 'qty', 'store', 'category', 'price', 'priority']
    let vals = {}
    for (let cid of rowcolids) {
        vals[cid] = document.getElementById(cid).value;
        //console.log(vals);
    }
    let it = new Item(vals.itemname, vals.qty, vals.priority, vals.store, vals.category, vals.price)
    //console.log(it);
    shoppingModel.addItem(it)
}

// function addMeal() {
//     let menu = localStorage.getItem("menu");
//     menu = menu ? JSON.parse(menu) : [];
//     let selNames = ["quantity", "name", "meal"];
//     let newMeal = {};
//     for (let cid of selNames) {
//         newMeal[cid] = document.getElementById("sel_" + cid).value;
//     }
//     menu.push(newMeal);
//     localStorage.setItem("menu", JSON.stringify(menu));
// }


// Populating a list
function populateSelect(selectId, sList) {
    let sel = document.getElementById(selectId, sList)
    for (let s of sList) {
        let opt = document.createElement("option")
        opt.value = s
        opt.innerHTML = s
        sel.appendChild(opt)
    } 
}

$(document).ready(function () {
    populateSelect('store', stores)
    populateSelect('category', sections)
})