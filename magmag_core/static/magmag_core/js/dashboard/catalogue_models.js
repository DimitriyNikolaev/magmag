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
            fields: ['id', 'name', 'image', 'slug', 'date_added', 'article'],
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