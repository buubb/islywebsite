$(document).ready(function(){
    // 서버에서 토큰을 가져오는 함수
    function getInstagramToken() {
        $.ajax({
            type: "GET",
            url: "/get-instagram-token/",  // Django에서 토큰을 가져오는 URL로 수정해야 함
            success: function(response) {
                var token = response.token;
                if (token) {
                    // 가져온 토큰을 사용하여 Instagram API에 요청
                    $.ajax({
                        type: "GET",
                        dataType: "jsonp",
                        cache: false,
                        url: "https://graph.instagram.com/me/media?access_token=" + token + "&fields=id,caption,media_type,media_url,thumbnail_url,permalink",
                        success: function(response) {
                            // console.log(response);
                            if (response.data != undefined && response.data.length > 0) {
                                for (i = 0; i < 12; i++) {
                                    if (response.data[i]) {
                                        var item = response.data[i];
                                        var image_url = "";
                                        var post = "";

                                        if (item.media_type === "VIDEO") {
                                            image_url = item.thumbnail_url;
                                        } else {
                                            image_url = item.media_url;
                                        }

                                        post += '<div class="news-box instagram_item' + i + '">';
                                        post += '<a href="' + item.permalink + '" target="_blank" rel="noopener noreferrer">';
                                        post += '<img src="' + image_url + '">';
                                        post += '</a>';
                                        post += '<div class="caption" OnClick="location.href =' + image_url + '" style="cursor:pointer;" >';
                                        post += '<a href="' + item.permalink + '">';
                                        post += '<h2>바로가기 <i class="bi bi-arrow-up-right"></i></h2>';
                                        post += '</a>';
                                        post += '</div>';
                                        post += '</div>';

                                        $('.carousel-primary').append(post);
                                    } else {
                                        // if no curent item
                                        show_fallback('#insta-item-' + i)
                                    }
                                }
                            } else {
                                // if api error
                                show_fallback('.news-box')
                            }
                        },
                        error: function() {
                            // if http error
                            show_fallback('.news-box')
                        }
                    });
                } else {
                    // 토큰이 없을 때 처리
                    console.log("Instagram 토큰을 가져오지 못했습니다.");
                }
            },
            error: function() {
                // 토큰 가져오기 실패 시 처리
                console.log("Instagram 토큰을 가져오는데 실패했습니다.");
            }
        });
    }

    // 토큰 가져오고 Instagram API 호출
    getInstagramToken();

    // Instagram 토큰을 주기적으로 갱신하기 위해 타이머 설정
    setInterval(function() {
        $.ajax({
            type: "GET",
            url: "/refresh-instagram-token/",  // Django에서 토큰을 갱신하는 URL로 수정해야 함
            success: function(response) {
                console.log("Instagram 토큰이 갱신되었습니다.");
                // 토큰 갱신 후 Instagram API 호출
                getInstagramToken();
            },
            error: function(error) {
                console.log("Instagram 토큰 갱신에 실패했습니다.");
            }
        });
    }, 50 * 24 * 60 * 60 * 1000); // 50일마다 실행
});

function show_fallback(el) {
    $(el).addClass('loaded fallback');
}