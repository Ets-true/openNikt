$(document).ready(function() {
    // $('.add-to-cart').click(function() {
    //     var prod=$(this).attr("data-product");
    //     var quan=$(this).attr("data-quantity");
    //     $.get('/add-to-cart', {product: prod, quantity: quan}, function(data){
    //        $("#quantity").attr('data-badge', data);
    //        // alert("Data" + data)
    //     });
    // });
    $('.send-message').click(function() {
        $.get('/send-message',{} , function(data){
            var name=$(document).getElementById("name_input")
            // $('td').remove();
            // $("#quantity").attr('data-badge', 0);
            $.get('/send-message/')
           alert(data);
        });
    });
});