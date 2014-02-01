/**
 * Created by dimitriy on 29.01.14.
 */
function readImages(input, container) {
        if (input.files && input.files.length > 0) {
            for(var i = 0; i < input.files.length; i++)
            {
                if(input.files[i])
                {
                    var reader = new FileReader();

                    reader.onload = function (e) {
                        var box = Ext.create('Ext.Img', {
                            src: e.target.result,
                            height: 150
                            //width: 120

                        });
                        container.add(box);

                    }
                    reader.readAsDataURL(input.files[i]);
                }
            }
        }
    }