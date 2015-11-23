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
    };

    if (window.addEventListener) {
      window.addEventListener("storage", this.handle_storage, false);
    } else {
      window.attachEvent("onstorage", this.handle_storage);
    }

    this.init = function(store_name, container, counter, total_sum, item_template){
        this.prefix = store_name+'_pi_';
        this.container = container;
        this.counter = counter;
        this.total_sum = total_sum;
        this.tmpl = item_template;
        this.updateContainer();
    };

    this.setPurchaseItem = function(id, data){
        var existItem = this.getPurchaseItem(id);
        if(existItem != null)
        {
            data.count = existItem.count + 1;
        }
        else data.count = 1;
        localStorage.setItem(this.prefix+id, JSON.stringify(data));
        this.setToCookie();
        this.updateContainer();
    };
    this.removePurchaseItem = function(id){
        localStorage.removeItem(this.prefix+id);
        this.setToCookie();
        this.updateContainer();
    };
    this.getPurchaseItem = function(id){
        var pi_jsondata = localStorage.getItem(this.prefix+id);
        if(typeof(pi_jsondata) != 'undefined' && pi_jsondata != null)
            return JSON.parse(pi_jsondata);
        return null;
    };

    this.setPurchaseItemCount = function(id, count){
        var existItem = this.getPurchaseItem(id);
        if(existItem != null){
            existItem.count = count;
            localStorage.setItem(this.prefix+id, JSON.stringify(existItem));
            this.updateContainer();
        }
        this.setToCookie();
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
    };
    this.getTotalSum = function(){
        var items = this.getPIList();
        var total_sum = 0;
        for(var i = 0; i < items.length; i++){
            var item = items[i];
            total_sum += item.count*item.price;
        }
        return total_sum;
    };

    this.updateContainer = function(){
        var items = this.getPIList();
        var total_count = 0;
        var total_sum = 0;

        for(var i = 0; i < items.length; i++){
            var item = items[i];
            total_count += item.count;
            total_sum += item.count*item.price;
            if ($('#purchase_item_'+item.id).length > 0){
                var el_count =  $('#pi_count_'+item.id);
                if(el_count.text() != item.count+'')
                    el_count.text(item.count);
            }
            else{
                var block = $(this.tmpl.format(item.id, '#',item.product, item.image, item.count, item.price));
                this.container.append(block);
            }
        }
        var blocks = this.container.children();
        for(var j = 0; j < blocks.length; j++){
            var id = blocks[j].id.replace('purchase_item_', '');
            if(this.getPurchaseItem(id) == null){
                $(blocks[j]).remove();
            }
        }
        this.counter.text(total_count);
        this.total_sum.text(total_sum);

    };
    this.setToCookie = function()
    {
        $.cookie.json = true;
        $.cookie('purchase_items', this.getIdsCountArray(), { path: '/' })

    };
    this.getIdsCountArray = function()
    {
        var items = this.getPIList();
        var cookie_val = [];
        for(var i = 0; i < items.length; i++){
            var purchase_item = {id: items[i].id, count: items[i].count};
            cookie_val.push(purchase_item);
        }
        return cookie_val;
    };

    this.clear = function()
    {
        localStorage.clear();
        this.setToCookie();
        this.updateContainer();
    };
}

//function PurchaseItem(id, name, additionalInfo, price){
//    this.id = id;
//    this.name = name;
//    this.additionalInfo = additionalInfo;
//    this.price = price;
//}
