document.addEventListener("DOMContentLoaded", function() {
    var usernameInput = document.getElementById("username");
    var passwordInput = document.getElementById("password");
    var loginButton = document.getElementById("login-button");
    var eyesIcon = document.querySelector('.showHidePw');
    var errorMessage = document.getElementById("error-message");

    var currentUrl = window.location.href;
    var baseUrl = currentUrl.split('/login')[0]; // "/login" 이전의 부분을 가져옴
    var newUrl = baseUrl + '/login';
    window.history.replaceState({}, document.title, newUrl);

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
    

    var LOGIN_TRY_LIMIT = 5;
    var loginAttempts = 0;

    function loginFailed() {
        loginAttempts++;
        if (loginAttempts >= LOGIN_TRY_LIMIT) {
            loginButton.disabled = true;
            loginButton.classList.remove("active");
        } 
    }



    // 에러 메시지가 존재하는 경우
    if (errorMessage) {
        var message = errorMessage.innerText.trim();
        showAlert(message);
    }

    function showAlert(message) {
        alert(message);
    }
});
