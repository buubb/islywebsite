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
    const content1 = "열정만 있다면\n 누구나!\n";
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


const indexes = document.querySelectorAll('.indexes li');
const tabs = document.querySelectorAll('.tab');
const contents = document.querySelectorAll('.tab-content');

function reset() {
  for (let i = 0; i < tabs.length; i++) {
    indexes[i].style.borderColor = 'transparent';
    tabs[i].style.zIndex = 0;
    tabs[i].classList.remove('active2');
    contents[i].classList.remove('active2');
  }
}

function showTab(i) {
  indexes[i].style.borderColor = 'aliceblue';
  tabs[i].style.opacity = 1;
  tabs[i].style.zIndex = 5;
  tabs[i].classList.add('active2');
  contents[i].classList.add('active2');
}

function activate(e) {
  if (!e.target.matches('.indexes li')) return;
  reset();
  showTab(e.target.dataset.index);
}

const init = () => showTab(0);

window.addEventListener('load',init,false);
window.addEventListener('click',activate,false);