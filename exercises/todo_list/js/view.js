/* jshint esversion: 6 */
/* jshint node: true */
/* jshint browser: true */
/* jshint jquery: true */
"use strict";

class ClowderView {
    constructor(model) {
        model.subscribe(this.redrawList.bind(this));
    }

    redrawList(roster, msg) {
        let tblBody = document.querySelector("#rosterTable > tbody");
        tblBody.innerHTML = "";
        let tblHead = document.querySelector("#rosterTable > thead");
        if (roster.size > 0) {
            tblHead.setAttribute("style", "visibility: visible");
        } else {
            tblHead.setAttribute("style", "visibility: collapse");
        }
        for (let item of roster) {
            this.addRow(item, tblBody);
        }
    }

    addRow(list, parent) {
        let row = document.createElement("tr");
        let cbCell = document.createElement("td");
        let cb = document.createElement("input");
        cb.type = "checkbox";
        cb.onclick = function() {
            list.removed = !list.removed;
        };
        cbCell.appendChild(cb);
        row.appendChild(cbCell);

        for (let val of ["name", "legs", "habitat", "diet"]) {
            let td = document.createElement("td");
            td.innerText = list[val];
            row.appendChild(td);
        }
        console.log(list);

        if(cbCell.priority=='Low') {
            row.className='btn-success';
        }
        if(cbCell.priority=='Critical') {
            row.className='btn-danger';
        }
        if(cbCell.priority=='Normal') {
            row.className='btn-success';
        }
        if(cbCell.priority=='Low') {
            row.className='btn-primary';
        }

        parent.appendChild(row);
    }

    removeRow() {
        
    }
}
