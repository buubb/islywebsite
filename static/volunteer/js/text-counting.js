// text-counting.js

$(document).ready(function () {
    $('form').submit(function (e) {
        var titleContent = $('#title').val();

        if (titleContent.length > 50) {
            e.preventDefault(); // 폼 제출 방지
            alert('Title exceeds 50 characters.'); // alert 창 띄우기
        }
    });

    $('#title').on('input', function (e) {
        var content = $(this).val();
        $('#title-counter').html("" + content.length + " / 50"); // 글자수 카운팅

        if (content.length > 50) {
            // 타이핑 되지 않도록
            $(this).val(content.substring(0, 51));
            $('#title-counter').html("51 / 50");
            // 글자 수가 50을 초과하면 feedback을 나타나게 함
            $('#title-feedback').show();
        } else {
            // 글자 수가 50 이하이면 feedback을 숨김
            $('#title-feedback').hide();
        }
    });
});
