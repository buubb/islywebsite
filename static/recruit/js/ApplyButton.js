// ApplyButton.js


document.addEventListener("DOMContentLoaded", function () {
    // apply 버튼에 대한 클릭 이벤트 핸들러 추가
    var applyButton = document.getElementById("CannotApply");
    if (applyButton) {
        applyButton.addEventListener("click", function (event) {
            event.preventDefault(); // 기본 동작 방지
            showAlert();
        });
    }
});

// showAlert 함수 정의
function showAlert() {
    alert("지금은 모집 기간이 아닙니다");
}