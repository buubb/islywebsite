// share.js

function copyURLToClipboard() {
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
}

// Share 버튼에 이벤트 리스너 추가
document.querySelector('.share-btn').addEventListener('click', copyURLToClipboard);
