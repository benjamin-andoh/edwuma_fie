// custom jquery scripts

$(document).ready(

    // the following scripts apply to the homepage




    //the following scripts are for the modals @ homepage
    function() {

        $("#forgotten").click(function() {
            $(".modal-footer-forgot").toggle().slideDown();
            $(".modal-footer").hide();

        });

        $("#signUpId").click(function() {
            $("#loginModal").hide();

        });

        // $("#category").onChange(function() {
        //     $("#skills").toggle().slideDown();
        //     // $(".modal-footer").hide();

        // });

        $('#category').on('change', function() {
            $('#skills').show().slideDown()

        });

        $("li").click(function() {
            // remove classes from all
            $("#v-pills-home-tab").removeClass("active");
            // add class to the one we clicked
            $("$v-pill-profile").addClass("active");
        });
        // $('#default').click(function() {
        //     $('#skills').hide().slideUp()

        // });



    });