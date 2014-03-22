/**
 * Created by dimitriy on 08.03.14.
 */

function Basket() {
    this.checkSupportHtml5Storage = function (){
        try {
            return 'localStorage' in window && window['localStorage'] !== null;
        } catch (e) {
            return false;
        }
    };



    this.handle_storage = function(e){
        if (!e) { e = window.event; }
        alert('Yaho');
    };

    if (window.addEventListener) {
      window.addEventListener("storage", this.handle_storage, false);
    } else {
      window.attachEvent("onstorage", this.handle_storage);
    }

    this.init = function(store_name, container, counter){
        this.prefix = store_name+'_pi_';
        this.container = container;
        this.counter = counter;
    };

    this.setPurchaseItem = function(id, data){
        localStorage.setItem(this.prefix+id, JSON.stringify(data))
        this.updateContainer();
    };
    this.removePurchaseItem = function(id){
        localStorage.removeItem(this.prefix+id);
    };
    this.getPurchaseItem = function(id){
        var pi_jsondata = localStorage.getItem(this.prefix+id)
        if(typeof(pi_jsondata) != 'undefined' && pi_jsondata != null)
            return JSON.parse(pi_jsondata);
        return null;
    };

    this.getPIList = function(){
        var pis = [];
        for (var i=0,key,value; i < localStorage.length; i++) {
            key = localStorage.key(i);
            if(key.indexOf(this.prefix) != -1)
            {
                value = localStorage.getItem(key);
                pis.push(JSON.parse(value));
            }
        }
        return pis;
    };

    this.getPIListCount = function(){
        var count = 0;
        for (var i=0,key; i < localStorage.length; i++) {
            key = localStorage.key(i);
            if(key.indexOf(this.prefix) != -1){
                count+=1;
            }
        }
        return count;
    }

    this.updateContainer = function(){
      alert('updated');
    };
}

//function PurchaseItem(id, name, additionalInfo, price){
//    this.id = id;
//    this.name = name;
//    this.additionalInfo = additionalInfo;
//    this.price = price;
//}
