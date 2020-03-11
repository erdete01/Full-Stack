/* jshint esversion: 6 */
/* jshint node: true */
/* jshint browser: true */
'use strict';
class Item {
    constructor(name, quantity, priority, store, section, price) {
        this.name = name;
        this.quantity = quantity;
        this.priority = priority;
        this.store = store;
        this.section = section;
        this.price = price;

        this._purchased = false;

    }

    get purchased() {
        return this._purchased;
    }

    set purchased(nv) {
        this._purchased = nv;
        alert(`${this.name} was purchased`)
    }
}

class Subject {

    constructor() {
        this.handlers = []
    }

    subscribe(fn) {
            this.handlers.push(fn);
        }

    unsubscribe(fn) {
        this.handlers = this.handlers.filter(
            function(item) {
                if (item !== fn) {
                    return item;
                }
            }
        );
    }

    publish(msg, someobj) {
        var scope = someobj || window;
        for (let fn of this.handlers) {
            fn(scope, msg)
        }
    }
}

class ShoppingList extends Subject {
    constructor() {
        super()
        this.newItems = []
        this.oldItems = [];
    }

    addItem(it) {
        this.newItems.push(it)
        this.publish('newitem', this)
    }
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