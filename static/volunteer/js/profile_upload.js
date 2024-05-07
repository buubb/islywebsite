// profile_upload.js

function readURL(input) {
    if (input.files && input.files[0]) {
        var extension = input.files[0].name.split('.').pop().toLowerCase();
        if ($.inArray(extension, ['jpg', 'jpeg', 'png']) == -1) {
            alert("Only JPG, JPEG, and PNG files are allowed");
            $('#imageUpload').val('');
            return;
        }
        var reader = new FileReader();
        reader.onload = function(e) {
            $('#imagePreview').css('background-image', 'url('+e.target.result +')');
            $('#imagePreview').hide();
            $('#imagePreview').fadeIn(650);
        }
        reader.readAsDataURL(input.files[0]);
    }
}
$("#imageUpload").change(function() {
    readURL(this);
});

$("form").submit(function(event) {
    // If no image is uploaded and the image is not being modified
    if ($("#imageUpload").get(0).files.length === 0 && $("#imagePreview").css("background-image").indexOf("profile_bg.png") !== -1) {
        alert("Please upload a profile image");
        event.preventDefault(); // Prevent default submission behavior
    }
});

