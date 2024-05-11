// content_counting.js

$(document).ready(function () {
    function updateCounter() {
        var content = $('#content').val();
        $('#content-counter').html("" + content.length + " / 100");
    }

    $('#content').on('input', function (e) {
        var content = $(this).val();
        $('#content-counter').html("" + content.length + " / 100");

        if (content.length > 100) {
            $(this).val(content.substring(0, 100));
            $('#content-counter').html("100 / 100");
        }
    });

    $('form').submit(function (e) {
        var commentContent = $('#content').val();

        if (commentContent.length > 100) {
            e.preventDefault();
            alert('Comment exceeds 100 characters');
        }
    });

    updateCounter();
});

