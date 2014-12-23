/**
 * Created by dimitriy on 27.01.14.
 */
Ext.define('Category',{
            extend: 'Ext.data.TreeModel',
            fields: ['id', 'name', 'description', 'slug', 'image', 'data', 'leaf'],
            idProperty: 'id'
        });
Ext.define('Store',{
            extend: 'Ext.data.Model',
            fields: ['id', 'name', 'phone', 'address'],
            idProperty: 'id'
        });
Ext.define('Product',{
            extend: 'Ext.data.Model',
            fields: ['id', 'name', 'image', 'slug', 'date_added', 'article', 'hidden'],
            idProperty: 'id'
        });
Ext.define('ProductItem',{
            extend: 'Ext.data.Model',
            fields: [
                {name:'id', type:'int'},
                {name:'color', type:'string'},
                {name:'size', type:'string'},
                {name:'rests', type:'auto'},
            ],
            idProperty: 'id'
        });
Ext.define('ProductItemRest',{
            extend: 'Ext.data.Model',
            fields: [
                {name:'id', type:'int'},
                {name:'item_id', type:'int'},
                {name:'store_id', type:'int'},
                {name:'store_name', type:'string'},
                {name:'count', type:'int'}
            ],
            idProperty: 'id'
        });
Ext.define('Image', {
    extend: 'Ext.data.Model',
    fields: [
        { name:'id', type:'int' },
        { name:'src', type:'string' },
        { name:'caption', type:'string' },
        { name:'order', type:'int' },
        { name:'deleted', type:'boolean' },
    ]
});

Ext.define('PageImage', {
    extend: 'Ext.data.Model',
    fields: [
        { name:'id', type:'int' },
        { name:'page_id', type:'int' },
        { name:'url', type:'string' },
        { name:'caption', type:'string' },
        { name:'order', type:'int' },
        { name:'deleted', type:'boolean' },
    ]
});

Ext.define('Page', {
    extend: 'Ext.data.Model',
    fields: [
        { name:'id', type:'int' },
        { name:'title', type:'string' },
        { name:'display_name', type:'string' },
        { name:'url', type:'string' },
        { name:'deletable', type:'boolean'},
        { name:'slug', type:'string' },
    ]
});


Ext.define('Order', {
    extend: 'Ext.data.Model',
    fields: [
        { name:'id', type:'int' },
        { name:'status_id', type:'int' },
        { name:'status_name', type:'string' },
        { name:'number', type:'string' },
        { name:'date', type:'string'},
        { name:'total_sum', type:'float'},
        { name:'customer_name', type:'string'},
        { name:'customer_email', type:'string'}
    ]
});

Ext.define('PurchaseItem', {
    extend: 'Ext.data.Model',
    fields: [
        { name:'id', type:'int' },
        { name:'name', type:'string' },
        { name:'size', type:'string' },
        { name:'color', type:'string' },
        { name:'count', type:'int' },
        { name:'price', type:'float' }
    ]
});
Ext.define('KeyNameItem', {
    extend: 'Ext.data.Model',
    fields: [
        { name:'key', type:'int' },
        { name:'name', type:'string' }
    ]
});

Ext.define('CallRequest',{
    extend: 'Ext.data.Model',
    fields: [
        { name:'id', type:'int' },
        { name:'date', type:'string' },
        { name:'phone', type:'string' },
        { name:'viewed', type:'boolean' }
    ]
});

Ext.define('ClientRequest',{
    extend: 'Ext.data.Model',
    fields: [
        { name:'id', type:'int' },
        { name:'date', type:'string' },
        { name:'viewed', type:'boolean' },
        { name:'email', type:'string' },
        { name:'message', type:'string' },
    ]
});