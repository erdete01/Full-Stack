/* jshint esversion: 8 */
/* jshint node: true */
'use strict';

class shoppingList {
    constructor(Nnames, Nquantities, Nprices, Nstores, Nsections, Npriorities) {
        this._name = Nnames;
        this._quantity = Nquantities;
        this._price = Nprices;
        this._store = Nstores;
        this._section = Nsections;
        this._priority = Npriorities;

        this._removed = false;
    }

    get name() {
        return this._name;
    }

    get quantityType() {
        return this._quantity;
    }

    set quantityType(newValue) {
        this._quantity = newValue;
    }

    get price() {
        return this._price;
    }

    get storeType() {
        return this._store;
    }

    set storeType(newValue) {
        this._store = newValue;
    }

    get sectionType() {
        return this._section;
    }

    set sectionType(newValue) {
        this._section = newValue;
    }

    get priorityType() {
        return this._priority;
    }

    set priorityType(newValue) {
        this._priority = newValue;
    }

    get removed() {
        return this._removed;
    }

    set removed(newValue) {
        this._removed = newValue;
    }

    toString() {
        return `${this._priority} ${this._section} ${this._store} ${this._price} ${this._quantity} ${this._name}`;
    }
}

class Subject {
    constructor() {
        this.handlers = [];
    }

    subscribe(func) {
        this.handlers.push(func);
    }

    unsubscribe(func) {
        this.handlers = this.handlers.filter(item => item != func);
    }

    publish(msg, obj) {
        let scope = obj || window;
        for (let f of this.handlers) {
            f(scope, msg);
        }
    }
}

class Lab extends Subject 
{
    constructor() 
    {
        super();
        this._lab = [];
    }

    add(newList) 
        {
        this._lab.push(newList);
        this.publish("a new list added", this);
        }
    

    [Symbol.iterator]() {
        let idx = -1;
        return {
            next: () => ({value: this._lab[++idx], done: !(idx in this._lab)})
        };
    }

    
    cleanList() {
        this._lab = this._lab.filter(a => a.removed);
        this.publish("removed", this);
    }

    get size() {
        return this._lab.length;
    }
}

