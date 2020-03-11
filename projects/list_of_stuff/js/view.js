/* jshint esversion: 6 */
/* jshint node: true */
/* jshint browser: true */
/* jshint jquery: true */
class ShoppingView {
    constructor(model) {
        // The bind() method creates a new function that, when called, has its this keyword set to the provided value.
        model.subscribe(this.redrawList.bind(this))
    }

    redrawList(shoppingList, msg) {
        let tbl = document.getElementById("shoppinglist")
        tbl.innerHTML = ""
        for (let item of shoppingList.newItems) {
            this.addRow(item, tbl)
        }
    }

    addRow(item, parent) {
        let row = document.createElement("tr")
        row.classList.add(item.priority)
        let cb = document.createElement("input")
        cb.type = "checkbox"
        cb.classList.add("form-control")
        cb.onclick = function() { item.purchased = true; }
        row.appendChild(cb);

        for (let val of ['name', 'quantity', 'store', 'section', 'price']) {
            let td = document.createElement("td")        
            td.innerHTML = item[val]
            row.appendChild(td)
        }
        parent.appendChild(row)
    }

class LocalStorageSaver {

    constructor(model,lsname) {
        this.lsname = lsname;
        let self = this
        model.subscribe(function(slist, msg) {
            self.saveAll(slist)
        })
        // now restore from localstorage
        let restore_list = JSON.parse(localStorage.getItem(self.lsname))
        console.log(restore_list);
        for(let vals of restore_list) {
            let it = new Item(vals.name, vals.quantity, vals.priority, vals.store, vals.section, vals.price)
            //console.log(it);
            model.addItem(it)
        }
    }

    saveAll(slist) {
        let ls_list = JSON.stringify(slist.newItems)
        localStorage.setItem(this.lsname, ls_list)
    }
}