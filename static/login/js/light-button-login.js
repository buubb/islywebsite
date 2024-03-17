document.addEventListener("DOMContentLoaded", function() {
    var usernameInput = document.getElementById("username");
    var passwordInput = document.getElementById("password");
    var loginButton = document.getElementById("login-button");
    var spanElements = document.querySelectorAll(".login-box button span");
    var eyesIcon = document.querySelector('.user-box .eyes');

    function changePlaceholder(input, placeholderText) {
        input.setAttribute("placeholder", placeholderText);
    }

    usernameInput.addEventListener("click", function() {
        changePlaceholder(this, "아이디를 입력하세요");
        passwordInput.setAttribute("placeholder", "");
    });

    passwordInput.addEventListener("click", function() {
        changePlaceholder(this, "비밀번호를 입력하세요");
        usernameInput.setAttribute("placeholder", "");
    });

    document.addEventListener("click", function(event) {
        var target = event.target;
        if (target !== usernameInput && target !== passwordInput) {
            usernameInput.setAttribute("placeholder", "");
            passwordInput.setAttribute("placeholder", "");
        }
    });

    function checkInputs() {
        if (usernameInput.value.trim() !== "" && passwordInput.value.trim() !== "") {
            loginButton.disabled = false;
            loginButton.classList.add("active");
            spanElements.forEach(function(span) {
                span.style.display = "block";
            });
        } else {
            loginButton.disabled = true;
            loginButton.classList.remove("active");
            spanElements.forEach(function(span) {
                span.style.display = "none";
            });
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
            eyesIcon.classList.toggle('active');
            if (eyesIcon.classList.contains('active')) {
                eyesIcon.querySelector('i').classList.remove('fa-eye');
                eyesIcon.querySelector('i').classList.add('fa-eye-slash');
                passwordInput.setAttribute('type', 'text');
            } else {
                eyesIcon.querySelector('i').classList.remove('fa-eye-slash');
                eyesIcon.querySelector('i').classList.add('fa-eye');
                passwordInput.setAttribute('type', 'password');
            }
        }
    }
});
