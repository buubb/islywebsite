// post_share.js

function copyURLToClipboard(event) {
    // 현재 페이지의 URL 가져오기
    var url = window.location.href;

    // URL을 클립보드에 복사
    navigator.clipboard.writeText(url).then(function() {
        // 복사 성공 시 알림 띄우기
        alert('Link Copied!');
    }, function(err) {
        // 복사 실패 시 에러 메시지 출력
        console.error('Could not copy link: ', err);
    });

    // 기본 동작 방지
    event.preventDefault();
}

// Share 버튼에 이벤트 리스너 추가
document.querySelector('.post_share').addEventListener('click', function(event) {
    copyURLToClipboard(event);
});
