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

        // Cloning education form
        var id_count = 1;
        $('.addEducation').on('click', function() {
            var source = $('.eduForm-holder:first'),
                clone = source.clone();
            // clone.find(':input').attr('id', function(i, val) {
            //     return val + id_count;
            // });
            clone.appendTo('.form-holder-append');
            id_count++;
        });

        // Removing added education/certificate
        $('body').on('click', '.removeEducation', function() {
            var closest = $(this).closest('.eduForm-holder').remove();
        });

        $("#profileImage").click(function(e) {
            $("#imageUpload").click();
        });

        function fasterPreview(uploader) {
            if (uploader.files && uploader.files[0]) {
                $('#profileImage').attr('src',
                    window.URL.createObjectURL(uploader.files[0]));
            }
        }

        $("#imageUpload").change(function() {
            fasterPreview(this);
        });

    });