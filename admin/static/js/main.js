$(function() {
  "use strict";
  $("#adminform").submit(function () {
      $(".form_error").remove();
      $("#errordata").html(" ");

      var error='';
      var password=$("#id_password");
      var phone=$("#id_contact_no");
      var phonvalue=phone.val()
      var regex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?!.*\s).*$/;
      if(!regex.test(password.val())){
           password.after('<span class="text-danger form_error">Password must contains <small>UpperCase, LowerCase and Number</small></span>');
            error=true;

      }
      if(phonvalue.length != 10){
            phone.after('<span class="text-danger form_error">Please Enter A Valid Phone Number</span>');
            error=true;
      }
      var name=$('#id_name').val();
     var datasring={'name':name,"email": $('#id_email').val(),"password":$('#id_password').val(),"contact_no":$("#id_contact_no").val()};
    if(!error){
     var frm = $(this);
         $.ajax({
            type: frm.attr('method'),
            url: frm.attr('action'),
             data: datasring,
             dataType: 'Json',

            success: function (response) {
                 var error=response["error"];
                 if(response["error"]){
                     $("#errordata").append(error['email']);
                      $("#errordata").append("<span class='d-block'>");
                     $("#errordata").append(error['phone']);
                       $("#errordata").append("<span class='d-block'>");
                     $("#errordata").append(error['password']);

                 }else{
                    if(response['success']){
                         $("#errordata").append(response['success']);
                         frm[0].reset();
                    }
                 }

            },
             error: function (response) {
               alert(response);
            }
        });

    }
      return false;
  });
});