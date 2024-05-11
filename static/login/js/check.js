document.addEventListener("DOMContentLoaded", function() {
    var usernameInput = document.getElementById("username");
    var passwordInput = document.getElementById("password");
    var loginButton = document.getElementById("login-button");
    var eyesIcon = document.querySelector('.showHidePw');
    var errorMessage = document.getElementById("error-message");
    var currentUrl = window.location.href;
    
    function checkInputs() {
        if (usernameInput.value.trim() !== "" && passwordInput.value.trim() !== "") {
            loginButton.disabled = false;
            loginButton.classList.add("active");
        } else {
            loginButton.disabled = true;
            loginButton.classList.remove("active");
        }
    }
    usernameInput.addEventListener("input", function() {
        checkInputs();
    });
    passwordInput.addEventListener("input", function() {
        checkInputs();
    });
    eyesIcon.addEventListener('click', function() {
        togglePasswordVisibility();
    });
    function togglePasswordVisibility() {
        if (passwordInput.value.trim() !== "") {
            if (passwordInput.type === "password") {
                passwordInput.type = "text";
                eyesIcon.classList.add('active');
                eyesIcon.classList.remove('uil-eye-slash');
                eyesIcon.classList.add('uil-eye');
            } else {
                passwordInput.type = "password";
                eyesIcon.classList.remove('active');
                eyesIcon.classList.remove('uil-eye');
                eyesIcon.classList.add('uil-eye-slash');
            }
        }
    }

    // 에러 메시지가 존재하는 경우
    if (errorMessage) {
        var message = errorMessage.innerText.trim();
        showAlert(message);
    }

    checkInputs();
});
function showAlert(message) {
    alert(message);
}