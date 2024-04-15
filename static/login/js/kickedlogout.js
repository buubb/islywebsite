// 동시접속 제한
function showKickedMessage() {
    var kickedMessageElement = document.getElementById('kicked-message');
    if (kickedMessageElement) {
        var kickedMessages = kickedMessageElement.querySelectorAll('p');
        if (kickedMessages.length > 0) {
            var message = kickedMessages[0].textContent.trim();
            var confirmed = window.confirm(message);
            if (confirmed) {
                
            }
        }
    }
}

window.addEventListener('load', function() {
    showKickedMessage();
});
