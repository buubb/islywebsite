// title_counting.js

$(document).ready(function () {
    function updateTitleCounter() {
        var content = $('#title').val();
        $('#title-counter').html("" + content.length + " / 50");
    }

    $('#title').on('input', function (e) {
        var content = $(this).val();
        $('#title-counter').html("" + content.length + " / 50");

        if (content.length > 50) {
            $(this).val(content.substring(0, 50));
            $('#title-counter').html("50 / 50");
        }
    });

    $('form').submit(function (e) {
        var titleContent = $('#title').val();

        if (titleContent.length > 50) {
            e.preventDefault();
            alert('Title exceeds 50 characters');
        }
    });

    updateTitleCounter();
});

