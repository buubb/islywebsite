/* main banner typing effect */
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


/* special activities svg(3) js*/
var morphTimeline = new TimelineMax({ 
  repeat:-1,
  repeatDelay:2
}); 

morphTimeline
  .to('#pathtuto1',2,{morphSVG:{shape:"#pathtuto2"}}) 
//path #pathtuto1 morph into #pathtuto2 during 2 seconds
  .to('#pathtuto1',2,{morphSVG:{shape:"#pathtuto3"}},"+=2")
//2 seconds later path #pathtuto1 morph into #pathtuto3 during 2 seconds
  .to('#pathtuto1',2,{morphSVG:{shape:"#pathtuto1"}},"+=2"); 
//2 seconds later path #pathtuto1 morph back into #pathtuto1 during 2 seconds
;


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

/* special activities svg(2) js*/
const count = 12;
const step = 180 / count;
const svg = document.getElementById('svg-container');

for (let i = 0; i < count; i++) {
    const start = step * i;
    const end = start + step;
    const meridian = document.createElementNS("http://www.w3.org/2000/svg", 'circle');
    meridian.setAttribute('r', '450');
    meridian.setAttribute('class', 'meridian');
    meridian.style.setProperty('--start', `${start}deg`);
    meridian.style.setProperty('--end', `${end}deg`);
    svg.appendChild(meridian);
}

/* special activities svg(1) js*/
const chunk_count = 100;
const anim_stack = 17;

let txt = document.querySelector(".flexible"),
    w = txt.getBoundingClientRect().width,
    h = txt.getBoundingClientRect().height,
    x_chunk = Math.ceil(w/chunk_count),
    y_chunk = h/chunk_count,
    remaining_pxs = w - x_chunk * 5;

txt.innerHTML = `<div class='mask'><div>${txt.innerHTML}</div></div>`;
let html = txt.innerHTML;

for(let i=0; i<chunk_count-1; i++) {
  txt.innerHTML += html;
}

let masks = document.querySelectorAll(".mask");
let inMasks = document.querySelectorAll(".mask div");

for(let i=0; i<masks.length; i++) {
  masks[i].style.width = x_chunk+"px";
  masks[i].style.overflow = "hidden";
  masks[i].style.animationDelay = `${-i*anim_stack}ms`;
  inMasks[i].style.left = -i*(x_chunk) + "px";
}

/* nav selected active effect js */
$(function(){
  // this will get the full URL at the address bar
  var url = window.location.href; 

  // passes on every "a" tag 
  $(".nav a").each(function() {
          // checks if its the same on the address bar
      if(url == (this.href)) { 
          $(this).closest(".menu_li").addClass("active");
      }
  });
});