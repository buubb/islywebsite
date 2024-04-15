// var checkSessionUrl = document.getElementById('checkSessionUrl').dataset.url;
// var loginUrl = document.getElementById('loginUrl').dataset.url;

// window.onload = function () {
//     checkSessionStatus();
//     setTimeout(checkSessionStatus, 20000);  // 10초마다 세션 상태 체크
// };

// function checkSessionStatus() {
//     console.log('Checking session status...');
//     fetch(checkSessionUrl)
//         .then(response => response.text())
//         .then(data => {
//             if (data.includes('세션이 만료되었습니다')) {
//                 if (window.confirm('세션이 만료되었습니다.')) {
//                     window.location.href='/login/?next=/';
//                 }
//             }
//         })
//         .catch(error => {
//             console.error('Error checking session status:', error);
//         });
// }