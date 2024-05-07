// name_counting.js

$(document).ready(function () {
    function updateCounter() {
        var content = $('#name').val();
        $('#name-counter').html("" + content.length + " / 10");
    }

    $('#name').on('input', function (e) {
        var content = $(this).val();

        // 글자수 카운팅
        $('#name-counter').html("" + content.length + " / 10");

        if (content.length > 10) {
            // 타이핑 되지 않도록
            $(this).val(content.substring(0, 10));
            $('#name-counter').html("10 / 10");
        }
    });

    updateCounter();
});

