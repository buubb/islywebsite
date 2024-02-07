document.addEventListener("DOMContentLoaded", function () {
    // 페이지 로딩이 완료되면 실행될 JavaScript 코드
    checkSessionStatus();
});

function checkSessionStatus() {
    // 서버에서 세션 상태 확인하는 Ajax 요청
    fetch('/check_session_status/')
        .then(response => response.json())
        .then(data => {
            if (data.session_expired) {
                // 세션이 만료된 경우 알림을 표시 (부트스트랩 모달 사용 예제)
                var myModal = new bootstrap.Modal(document.getElementById('sessionExpiredModal'));
                myModal.show();
            }
        })
        .catch(error => console.error('Error checking session status:', error));
}