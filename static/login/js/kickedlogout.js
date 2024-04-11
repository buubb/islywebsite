function showKickedMessage() {
    var kickedMessageElement = document.getElementById('kicked-message');
    if (kickedMessageElement) {
        var kickedMessages = kickedMessageElement.querySelectorAll('p');
        if (kickedMessages.length > 0) {
            var message = kickedMessages[0].textContent.trim();
            var confirmed = window.confirm(message);
            if (confirmed) {
                // 확인 버튼을 클릭한 경우 추가 작업을 수행할 수 있습니다.
                // 예를 들어, 사용자를 로그아웃시키거나 다른 작업을 수행할 수 있습니다.
            }
        }
    }
}

// 페이지 로드 후에 알림창을 표시하는 이벤트 핸들러 등록
window.addEventListener('load', function() {
    showKickedMessage();
});
