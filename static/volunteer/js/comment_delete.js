// comment_delete.js

$(document).ready(function() {
    $(".comment_delete").on("click", function(e) {
        e.preventDefault(); // 기본 동작 중지

        var $this = $(this);
        var url = $this.closest("form").attr("action");
        var csrf_token = $('input[name="csrfmiddlewaretoken"]').val(); // CSRF 토큰 가져오기

        // 확인 창을 띄움
        var confirmDelete = confirm("Are you sure you want to delete?");

        if (confirmDelete) {
            $.ajax({
                type: "POST",
                url: url,
                data: {
                    csrfmiddlewaretoken: csrf_token, // 가져온 CSRF 토큰 사용
                },
                success: function(response) {
                    if (response.success) {
                        // 삭제 권한이 있는 경우: comment_item 삭제
                        $this.closest(".comment_item").remove();
                        // 숫자와 아이콘 업데이트
                        var commentCount = response.comment_count;
                        $(".comment-btn").html('<i class="fa-regular fa-message"></i> ' + commentCount);
                        // 댓글이 0개인 경우: VltComment 삭제
                        if (commentCount == 0) {
                            $(".VltComment").remove();
                        }
                    } else {
                        // 삭제 권한이 없는 경우
                        alert("Only the author can delete this.");
                    }
                },
                error: function(xhr, errmsg, err) {
                    console.log(xhr.status + ": " + xhr.responseText); // 에러 메시지 출력
                }
            });
        }
    });
});
