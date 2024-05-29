// name_counting.js

$(document).ready(function () {
    function updateNameCounter() {
        var content = $('#name').val();
        $('#name-counter').html("" + content.length + " / 10");
    }

    $('#name').on('input', function (e) {
        var content = $(this).val();
        $('#name-counter').html("" + content.length + " / 10");

        if (content.length > 10) {
            $(this).val(content.substring(0, 10));
            $('#name-counter').html("10 / 10");
        }
    });

    $('form').submit(function (e) {
        var nameContent = $('#name').val();

        if (nameContent.length > 10) {
            e.preventDefault();
            alert('Name exceeds 10 characters');
        }
    });

    updateNameCounter();
});

