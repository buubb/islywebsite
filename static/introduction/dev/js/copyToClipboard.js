// Dev Template Javascript

function copyToClipboard(event, text) {
    event.preventDefault(); // 페이지 이동 방지
    var textarea = document.createElement("textarea");
    textarea.value = text;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand("copy");
    document.body.removeChild(textarea);
    alert("Username Copied!"); // 알림 창 표시
}
