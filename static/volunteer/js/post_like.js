// post_like.js

$(document).ready(function () {
    $(".like-btn").click(function (e) {
        e.preventDefault();

        // Post ID 가져오기
        var post_id = $(this).data("post-id");

        // Ajax 요청
        $.ajax({
            type: "POST",
            url: "/project/" + post_id + "/like/",
            data: {
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
                next: window.location.pathname
            },
            success: function (data) {
                // 하트 아이콘 업데이트
                if (data.liked) {
                    $(".like-btn i").removeClass("fa-regular fa-heart fa-beat").addClass("fa-solid fa-heart");
                } else {
                    $(".like-btn i").removeClass("fa-solid fa-heart").addClass("fa-regular fa-heart fa-beat");
                }

                // 좋아요 개수 업데이트
                var likeCount = data.like_count;
                $(".like-count").text(likeCount);


                // 로그인하지 않은 경우 로그인 페이지로 이동
                if (!data.logged_in) {
                    window.location.href = "/login/login/?next=" + encodeURIComponent(window.location.pathname);
                }
            },
            error: function (xhr, status, error) {
                console.error(xhr.responseText);
            }
        });
    });
});
