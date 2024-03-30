document.addEventListener("DOMContentLoaded", function() {
    var usernameInput = document.getElementById("username");
    var passwordInput = document.getElementById("password");
    var loginButton = document.getElementById("login-button");
    var spanElements = document.querySelectorAll(".login-box button span");
    var eyesIcon = document.querySelector('.user-box .eyes');


    // 이전 페이지의 URL 파라미터 제거
    var urlWithoutNext = window.location.href.split('?')[0];
    window.history.replaceState({}, document.title, urlWithoutNext);


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

    checkInputs();
});