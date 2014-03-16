/**
 * Created by dimitriy on 08.03.14.
 */

function Basket(store_name) {
    this.checkSupportHtml5Storage = function (){
        try {
            return 'localStorage' in window && window['localStorage'] !== null;
        } catch (e) {
            return false;
        }
    };

    this.prefix = store_name+'_pi_';

    this.handle_storage = function(e){
        if (!e) { e = window.event; }
        alert('Yaho');
    };

    if (window.addEventListener) {
      window.addEventListener("storage", this.handle_storage, false);
    } else {
      window.attachEvent("onstorage", this.handle_storage);
    }

    this.init = function(container){

    };

    this.setPurchaseItem = function(id, data){
        localStorage.set(this.prefix+id, JSON.stringify(data))
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
                console.log(key, value);
            }
        }
        return pis;
    };
}

//function PurchaseItem(id, name, additionalInfo, price){
//    this.id = id;
//    this.name = name;
//    this.additionalInfo = additionalInfo;
//    this.price = price;
//}
