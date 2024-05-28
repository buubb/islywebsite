$(document).ready(function() {
    // 서버에서 토큰을 가져오는 함수
    function getInstagramToken() {
        $.ajax({
            type: "GET",
            url: "/get-instagram-token/", // Django에서 토큰을 가져오는 URL로 수정해야 함
            success: function(response) {
                var token = response.token;
                if (token) {
                    // 가져온 토큰을 사용하여 Instagram API에 요청
                    fetchInstagramMedia(token);
                } else {
                    console.log("Instagram 토큰을 가져오지 못했습니다.");
                }
            },
            error: function() {
                console.log("Instagram 토큰을 가져오는데 실패했습니다.");
            }
        });
    }

    // Instagram 미디어를 가져오는 함수
    function fetchInstagramMedia(token) {
        $.ajax({
            type: "GET",
            url: "https://graph.instagram.com/me/media",
            data: {
                access_token: token,
                fields: "id,caption,media_type,media_url,thumbnail_url,permalink"
            },
            success: function(response) {
                if (response.data && response.data.length > 0) {
                    $('.carousel-primary, .carousel-secondary').empty(); // 이전 콘텐츠 제거

                    response.data.slice(0, 12).forEach((item, i) => {
                        var image_url = item.media_type === "VIDEO" ? item.thumbnail_url : item.media_url;
                        var post = `<div class="news-box instagram_item${i}">
                            <a href="${item.permalink}" target="_blank" rel="noopener noreferrer">
                                <img src="${image_url}">
                            </a>
                            <div class="caption" onClick="location.href='${item.permalink}'" style="cursor:pointer;">
                                <h2>바로가기 <i class="bi bi-arrow-up-right"></i></h2>
                            </div>
                        </div>`;
                        $('.carousel-primary, .carousel-secondary').append(post);
                    });
                    // 요소가 추가된 후에 애니메이션 시작
                    setTimeout(startAnimation, 100);
                } else {
                    show_fallback('.news-box');
                }
            },
            error: function() {
                show_fallback('.news-box');
            }
        });
    }

    // 애니메이션 시작 함수
    function startAnimation() {
        var primary = document.querySelector('.carousel-primary');
        var secondary = document.querySelector('.carousel-secondary');

        if (primary && secondary) {
            var containerWidth = primary.parentNode.clientWidth;

            primary.style.animation = `scroll-horizontal 25s linear infinite`;
            secondary.style.animation = `scroll-horizontal-2 25s linear infinite`;

            primary.style.transform = `translateX(0%)`;
            secondary.style.transform = `translateX(${containerWidth}px)`;

            // PC에서는 hover 이벤트를 사용하여 애니메이션 일시정지 및 재개
            if (!('ontouchstart' in window)) {
                $('.scroll-container').hover(
                    function() {
                        primary.style.animationPlayState = "paused";
                        secondary.style.animationPlayState = "paused";
                    },
                    function() {
                        primary.style.animationPlayState = "running";
                        secondary.style.animationPlayState = "running";
                    }
                );
            }
        } else {
            console.log("carousel-primary 또는 carousel-secondary 요소를 찾을 수 없습니다.");
        }
    }

    // 토큰 가져오고 Instagram API 호출
    getInstagramToken();

    // Instagram 토큰을 주기적으로 갱신하기 위해 타이머 설정
    setInterval(function() {
        $.ajax({
            type: "GET",
            url: "/refresh-instagram-token/", // Django에서 토큰을 갱신하는 URL로 수정해야 함
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
