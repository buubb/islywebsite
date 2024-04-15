// document.addEventListener("DOMContentLoaded", function() {
//     // 비밀번호 변경 알림 메시지 확인
    
//     var resetMessageElement = document.getElementById('reset-message');
//     if (resetMessageElement) {
//         var resetMessages = resetMessageElement.querySelectorAll('p');
//         if (resetMessages.length > 0) {
//             var message = resetMessages[0].textContent.trim();
//             var confirmed = window.confirm(message);
//             if (confirmed) {
//                 // 확인 버튼을 클릭한 경우 로그아웃 및 리디렉션 수행
//                 logoutAndRedirect();
//             }
//         }
//     }
// });
    
//     // 로그아웃 및 리디렉션 함수
//     function logoutAndRedirect() {
//         fetch('/logout')  // 로그아웃 URL로 변경
//             .then(response => {
//                 // 로그아웃이 성공하면 로그인 페이지로 리디렉션
//                 if (response.ok) {
//                     window.location.replace('/login');  // 로그인 페이지 URL로 변경
//                 }
//             })
//             .catch(error => console.error('로그아웃 중 오류 발생:', error));
//     }
    

// document.addEventListener("DOMContentLoaded", function() {
//     // 비밀번호 변경 알림 메시지 확인
//     var resetConfirmation = document.getElementById('reset-confirmation').dataset.reset;
    
//     // 로그인되어 있을 때만 처리
//     if (resetConfirmation === 'true') {
//         // 경고 메시지 출력
//         var confirmation = confirm("관리자가 비밀번호를 변경했습니다. 다른 기기에서 로그아웃됩니다.");
//         if (confirmation) {
//             // 사용자가 확인을 클릭하면 로그아웃 및 리디렉션 수행
//             logoutAndRedirect();  
//         } else {
//             // 사용자가 취소를 클릭하면 이전 페이지로 이동
//             window.history.back();
//         }
//     }
// });

// // 로그아웃 및 리디렉션 함수
// function logoutAndRedirect() {
//     fetch('/logout')  // 로그아웃 URL로 변경
//         .then(response => {
//             // 로그아웃이 성공하면 로그인 페이지로 리디렉션
//             if (response.ok) {
//                 window.location.replace('/login');  // 로그인 페이지 URL로 변경
//             }
//         })
//         .catch(error => console.error('로그아웃 중 오류 발생:', error));
//}
