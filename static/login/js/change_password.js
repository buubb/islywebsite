document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById("change-password-form");

    form.addEventListener("submit", function(event) {
        var newPasswordInput = document.getElementById("new_password");
        var confirmPasswordInput = document.getElementById("confirm_password");

        // 비밀번호 유효성 검사를 수행합니다.
        var errorMessage = validatePassword(newPasswordInput.value, confirmPasswordInput.value);

        // 에러 메시지가 있을 경우
        if (errorMessage) {
            event.preventDefault(); // 폼 제출을 막습니다.

            // 에러 메시지를 사용자에게 표시합니다.
            showAlert(errorMessage);
        }
    });

    // 비밀번호 유효성을 검사하는 함수입니다.
    function validatePassword(newPassword, confirmPassword) {
        // 패스워드 변경 규칙을 정의합니다.
        var rules = [
            "Your password must contain at least 8 characters.",
            "Your password can’t be too similar to your other personal information.",
            "Your password can’t be a commonly used password.",
            "Your password can’t be entirely numeric."
        ];

        var errorMessages = [];

        if (origin_password != user.password){
            errorMessages.push('Current password is incorrect.')
        }

        // 각 규칙을 검사합니다.
        if (newPassword.length < 8) {
            errorMessages.push("Your password must contain at least 8 characters.");
        }

        // 비밀번호 확인
        if (newPassword !== confirmPassword) {
            errorMessages.push("Password confirmation doesn't match.");
        }

        // 모든 조건을 만족하는 경우
        if (errorMessages.length === 0) {
            return null;
        }

        // 에러 메시지를 반환합니다.
        return errorMessages.join("<br>"); // HTML 줄바꿈 추가
    }

    // 에러 메시지를 보여주는 함수입니다.
    function showAlert(message) {
        var errorContainer = document.getElementById("error-container");
        if (errorContainer) {
            errorContainer.innerHTML = '<div class="alert alert-danger" role="alert">' + message + '</div>';
        } else {
            alert(message); // 요소를 찾지 못한 경우, 경고창으로 메시지 표시
        }
    }
});
