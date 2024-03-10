// apply.js 파일에 checkRecruitment 함수를 정의합니다.
function checkRecruitment() {
    event.preventDefault();

    var currentDateTime = new Date();
    var recruitmentStart = new Date('2024-01-24'); // 모집 시작 날짜
    var recruitmentEnd = new Date('2024-02-07');   // 모집 종료 날짜

    if (currentDateTime >= recruitmentStart && currentDateTime <= recruitmentEnd) {
        window.location.href = "https://forms.gle/hGCiHURgAqV7LqVc6"; // 10기 지원 링크로 이동
    } else {
        alert("지금은 모집 기간이 아닙니다. 다음 10기 모집을 기다려주세요!");
    }
}
