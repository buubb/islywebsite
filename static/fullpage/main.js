/*$(function(){
    $('#fullpage').fullpage({
		//options here
        anchors:['s1','s2','s3','s4'],
		autoScrolling: false,
        scrollBar:true,
        sectionsColor:['#1f2122','aliceblue','#1f2122','#1f2122'],
	});
});
*/
function toggleAnswer(answerID) {
    var answerDiv = document.getElementById(answerID);

    if (answerDiv.style.display === 'none') {
      answerDiv.style.display = 'block';
    } else {
      answerDiv.style.display = 'none';
    }
  }


  document.addEventListener("DOMContentLoaded", function() {
    const content1 = "Feel Your\n Passion in ";
    const content2 = "I.Sly()";
    const text = document.querySelector(".text");
    const cursor = document.querySelector(".cursor"); // 커서 요소 선택
    let i = 0;

    function typing() {
        let txt = i < content1.length ? content1[i] : content2[i - content1.length];
        if (i >= content1.length) {
            text.insertAdjacentHTML('beforeend', `<span class="green">${txt}</span>`);
        } else {
            text.innerHTML += txt === "\n" ? "<br/>" : txt;
        }
        i++;
        if (i < content1.length + content2.length) {
            setTimeout(typing, 200);
        } else {
            setTimeout(function() {
                cursor.style.display = 'none'; // 3초 후에 커서 숨김
            }, 3000); // 3초 후에 실행
        }
    }

    typing(); // 처음 한 번만 실행
});


// const indexes = document.querySelectorAll('.indexes li');
// const tabs = document.querySelectorAll('.tab');
// const contents = document.querySelectorAll('.tab-content');

// function reset() {
//   for (let i = 0; i < tabs.length; i++) {
//     indexes[i].style.borderColor = 'transparent';
//     tabs[i].style.zIndex = 0;
//     tabs[i].classList.remove('active2');
//     contents[i].classList.remove('active2');
//   }
// }

// function showTab(i) {
//   indexes[i].style.borderColor = 'aliceblue';
//   tabs[i].style.opacity = 1;
//   tabs[i].style.zIndex = 5;
//   tabs[i].classList.add('active2');
//   contents[i].classList.add('active2');
// }

// function activate(e) {
//   if (!e.target.matches('.indexes li')) return;
//   reset();
//   showTab(e.target.dataset.index);
// }

// const init = () => showTab(0);

// window.addEventListener('load',init,false);
// window.addEventListener('click',activate,false);


/* scroll 시 나타나는 animation */
$(document).ready(function() {
  // 클래스가 "scroll_on"인 모든 요소를 선택합니다.
  const $counters = $(".scroll_on");
  
  // 노출 비율(%)과 애니메이션 반복 여부(true/false)를 설정합니다.
  const exposurePercentage = 100; // ex) 스크롤 했을 때 $counters 컨텐츠가 화면에 100% 노출되면 숫자가 올라갑니다.
  const loop = true; // 애니메이션 반복 여부를 설정합니다. (true로 설정할 경우, 요소가 화면에서 사라질 때 다시 숨겨집니다.)

  // 윈도우의 스크롤 이벤트를 모니터링합니다.
  $(window).on('scroll', function() {
      // 각 "scroll_on" 클래스를 가진 요소에 대해 반복합니다.
      $counters.each(function() {
          const $el = $(this);
  
          // 요소의 위치 정보를 가져옵니다.
          const rect = $el[0].getBoundingClientRect();
          const winHeight = window.innerHeight; // 현재 브라우저 창의 높이
          const contentHeight = rect.bottom - rect.top; // 요소의 높이
          
          // 요소가 화면에 특정 비율만큼 노출될 때 처리합니다.
          if (rect.top <= winHeight - (contentHeight * exposurePercentage / 100) && rect.bottom >= (contentHeight * exposurePercentage / 100)) {
              $el.addClass('active');
          }
          // 요소가 화면에서 완전히 사라졌을 때 처리합니다.
          if (loop && (rect.bottom <= 0 || rect.top >= window.innerHeight)) {
              $el.removeClass('active');
          }
      });
  }).scroll();
});
