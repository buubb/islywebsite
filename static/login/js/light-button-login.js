document.addEventListener("DOMContentLoaded", function() {
    var usernameInput = document.getElementById("username");
    var passwordInput = document.getElementById("password");
    var loginButton = document.getElementById("login-button");
    var spanElements = document.querySelectorAll(".login-box button span"); // 수정: 모든 span 요소 선택
    var toggleButton = document.getElementById("show-password");
    
    // 입력 상자를 클릭할 때 placeholder 텍스트를 변경하는 함수
    function changePlaceholder(input, placeholderText) {
        input.setAttribute("placeholder", placeholderText);
    }

    // username 입력 상자에 대한 클릭 이벤트 리스너
    usernameInput.addEventListener("click", function() {
        changePlaceholder(this, "아이디를 입력하세요");
        // password 입력 상자의 placeholder 초기화
        passwordInput.setAttribute("placeholder", "");
    });

    // password 입력 상자에 대한 클릭 이벤트 리스너
    passwordInput.addEventListener("click", function() {
        changePlaceholder(this, "비밀번호를 입력하세요");
        // username 입력 상자의 placeholder 초기화
        usernameInput.setAttribute("placeholder", "");
    });

    // 문서 전체에 대한 클릭 이벤트 리스너
    document.addEventListener("click", function(event) {
        var target = event.target;
        // 클릭된 요소가 username 또는 password 입력 상자가 아닌 경우 placeholder 텍스트를 초기화합니다.
        if (target !== usernameInput && target !== passwordInput) {
            usernameInput.setAttribute("placeholder", "");
            passwordInput.setAttribute("placeholder", "");
        }
    });

    // 입력 값 변화 이벤트 추가
    function checkInputs() {
        if (usernameInput.value.trim() !== "" && passwordInput.value.trim() !== "") {
            loginButton.disabled = false;
            loginButton.classList.add("active");
            // 모든 span 요소에 대해 display 속성을 block으로 설정
            spanElements.forEach(function(span) {
                span.style.display = "block";
            });
        } else {
            loginButton.disabled = true;
            loginButton.classList.remove("active");
            // 모든 span 요소에 대해 display 속성을 none으로 설정
            spanElements.forEach(function(span) {
                span.style.display = "none";
            });
        }
    }

    // 입력 값 변화 이벤트 추가
    usernameInput.addEventListener("input", checkInputs);
    passwordInput.addEventListener("input", checkInputs);

    // 페이지가 로드될 때 비밀번호 필드를 가림
    passwordInput.type = "password";

    // 비밀번호 보이기/가리기 버튼 클릭 이벤트 핸들러
    toggleButton.addEventListener("click", function() {
        if (passwordInput.type === "password") {
            // 현재 비밀번호가 가려져 있는 경우: 보이기
            passwordInput.type = "text";
        } else {
            // 현재 비밀번호가 보이는 경우: 가리기
            passwordInput.type = "password";
        }
    });
});
