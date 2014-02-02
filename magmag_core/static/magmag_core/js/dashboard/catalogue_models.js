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
Ext.define('ProductItems',{
            extend: 'Ext.data.Model',
            fields: ['id'],
            idProperty: 'id'
        });