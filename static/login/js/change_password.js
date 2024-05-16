document.addEventListener("DOMContentLoaded", function() {
    var usernameInput = document.getElementById("old_password");
    var passwordInput = document.getElementById("new_password1");
    var password1Input = document.getElementById("new_password2");
    var loginButton = document.getElementById("login-button");

    function checkInputs() {
        if (usernameInput.value.trim() !== "" && passwordInput.value.trim() !== "" && password1Input.value.trim() !== "") {
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

    password1Input.addEventListener("input", function() {
        checkInputs();
    });

    var errorMessage = document.getElementById("error-message");
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
