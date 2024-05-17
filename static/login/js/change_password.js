document.addEventListener("DOMContentLoaded", function() {
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
