// $(document).ready(function() {
//     $('.send-message').click(function () {
//         $.get('/send-message', {}, function (data) {
//             var name = $(document).getElementById("name_input");
//             // $('td').remove();
//             // $("#quantity").attr('data-badge', 0);
//             $.get('/send-message/');
//             alert(data);
//         });
//     });
// })
 grecaptcha.ready(function() {
      grecaptcha.execute('6LeLPqAUAAAAACA1yUnkWfmIQaNHlu6kPINcYk2l', {action: 'homepage'}).then(function(token) {
         $(function(){
            $(".snd-btn").on("click", function(){
                var params = {_method: 'POST'};
                var route = "/send-message/";
                var data = {
                    name: $('#name_input').val(),
                    phone: $('#phone_input').val(),
                    email: $('#e_mail_input').val(),
                    text: $('#text').val()
                }
        $.ajax({
             type: "POST",
             url: route,
             data: data,
             headers: {
                'X-CSRFToken': $('meta[name="csrf-token"]').attr('content')
             },
             success: function(response) {
                 alert(response);
             }
        });
        // alert("Your message was send")
   });
});
      });
  });

// $(function(){
//     $(".snd-btn").on("click", function(){
//         var params = {_method: 'POST'};
//         var route = "/send-message/";
//         var data = {
//             name: $('#name_input').val(),
//             email: $('#e_mail_input').val(),
//             text: $('#text').val()
//         }
//         $.ajax({
//              type: "POST",
//              url: route,
//              data: data,
//              headers: {
//                 'X-CSRFToken': $('meta[name="csrf-token"]').attr('content')
//              }
//
//         });
//         alert("Your message was send")
//    });
// });