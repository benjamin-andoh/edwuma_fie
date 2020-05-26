// custom jquery scripts

$(document).ready(

    // the following scripts apply to the homepage




    //the following scripts are for the modals @ homepage
    function(){

    $("#forgotten").click(function(){
      $(".modal-footer-forgot").toggle().slideDown();
      $(".modal-footer").hide();
        
    });
    
   $("#signUpId").click(function(){
    $("#loginModal").hide();

   });


  });