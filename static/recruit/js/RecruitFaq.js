// RecruitFaq.js


document.addEventListener("DOMContentLoaded", function() {
  // 모든 FAQ 아이템을 선택
  var faqItems = document.querySelectorAll('.faq-item');

  // 각 FAQ 아이템에 대해 반복
  faqItems.forEach(function(item) {
    // 아이콘과 답변을 선택
    var iconShow = item.querySelector('.icon-show');
    var iconClose = item.querySelector('.icon-close');
    var answer = item.querySelector('.collapse');

    // 답변이 열려있는지 확인하고 아이콘을 설정
    if (answer.classList.contains('show')) {
      iconShow.style.display = 'none';
      iconClose.style.display = 'inline-block';
    } else {
      iconShow.style.display = 'inline-block';
      iconClose.style.display = 'none';
    }

    // FAQ 아이템을 클릭할 때의 이벤트를 추가
    item.addEventListener('click', function() {
      // 모든 답변을 가져오기
      var allAnswers = document.querySelectorAll('.faq-answer');

      // 다른 열린 답변이 있는 경우 닫기
      allAnswers.forEach(function(ans) {
        if (ans !== answer && ans.classList.contains('show')) {
          ans.classList.remove('show');
          ans.parentElement.querySelector('.icon-show').style.display = 'inline-block';
          ans.parentElement.querySelector('.icon-close').style.display = 'none';
        }
      });

      // 현재 클릭한 FAQ 아이템의 답변을 열거나 닫기
      if (answer.classList.contains('show')) {
        answer.classList.remove('show');
        iconShow.style.display = 'inline-block';
        iconClose.style.display = 'none';
      } else {
        answer.classList.add('show');
        iconShow.style.display = 'none';
        iconClose.style.display = 'inline-block';
      }
    });
  });
});







