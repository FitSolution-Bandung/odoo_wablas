odoo.define('send_whatsapp.QRCodeWidget', function(require) {
    'use strict';

    var fieldRegistry = require('web.field_registry');
    var FieldChar = require('web.basic_fields').FieldChar;

    var QRCodeWidget = FieldChar.extend({
        _renderReadonly: function() {
            this._super();
            var url = this.value;
            if (url) {
                var iframe = $('<iframe>', {
                    src: url,
                    style: 'width:100%; height:400px; border:none;',
                });
                this.$el.html(iframe);
            }
        },
    });

    fieldRegistry.add('qr_code_widget', QRCodeWidget);

    return QRCodeWidget;
});
