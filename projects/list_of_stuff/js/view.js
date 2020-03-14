/* jshint esversion: 8 */
/* jshint node: true */
/* jshint browser: true */
'use strict';

class View {
    constructor(model) {
        model.subscribe(this.redrawList.bind(this));
    }

    redrawList(listofElements, msg) {
        let tblBody = document.querySelector("#tableList > tbody");
        tblBody.innerHTML = "";
        for (let alist of listofElements) {

            let row = document.createElement("tr");

            let cbCell = document.createElement("td");   
            let cb = document.createElement("input");
            cb.type = "checkbox";
            cb.onclick = function() {
                alist.removed = !alist.removed;
            }
            cbCell.appendChild(cb);
            row.appendChild(cbCell);

            let tdNames = document.createElement("td");
            tdNames.innerHTML = alist.name;
            row.appendChild(tdNames);

            let tdQuantities = document.createElement("td");
            tdQuantities.innerHTML = alist.quantityType;
            row.appendChild(tdQuantities);

            let tdPrices = document.createElement("td");
            tdPrices.innerHTML = alist.price;
            row.appendChild(tdPrices);

            let tdStores = document.createElement("td");
            tdStores.innerHTML = alist.storeType;
            row.appendChild(tdStores);

            let tdSections = document.createElement("td");
            tdSections.innerHTML = alist.sectionType;
            row.appendChild(tdSections);

            let tdPriorities = document.createElement("td");
            tdPriorities.innerHTML = alist.priorityType;
            row.appendChild(tdPriorities);

            tblBody.appendChild(row);
        }
    }
}