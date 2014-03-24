/**
 * Created by dimitriy on 08.03.14.
 */

function Basket() {

    var tmpl = '<div id="purchase_item_{0}" class="basket-item">' +
                '<a href="{1}">{2}</a>' +
                '<img src="{3}" />' +
                '<div><strong id="pi_count_{0}">{4}</strong> x <strong>{5}</strong></div>' +
                '</div>';

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

    this.init = function(store_name, container, counter, total_sum){
        this.prefix = store_name+'_pi_';
        this.container = container;
        this.counter = counter;
        this.total_sum = total_sum
        this.updateContainer();
    };

    this.setPurchaseItem = function(id, data){
        var existItem = this.getPurchaseItem(id);
        if(existItem != null)
        {
            data.count = existItem.count + 1;
        }
        else data.count = 1;
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
        var items = this.getPIList();
        var totalcount = 0;
        var totalsumm = 0;
        for(var i = 0; i < items.length; i++){
            var item = items[i];
            totalcount += item.count;
            totalsumm += item.count*item.price;
            if ($('#purchase_item_'+item.id).length > 0){
                if($('#pi_count_'+item.id).text() != item.count+'')
                    $('#pi_count_'+item.id).text(item.count);
            }
            else{
                var block = $(tmpl.format(item.id, '#',item.product, item.image, item.count, item.price));
                this.container.append(block);
            }
        }
        this.counter.text(totalcount);
        this.total_sum.text(totalsumm);

    };
}

//function PurchaseItem(id, name, additionalInfo, price){
//    this.id = id;
//    this.name = name;
//    this.additionalInfo = additionalInfo;
//    this.price = price;
//}
