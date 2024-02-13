$(function(){
    $('#fullpage').fullpage({
		//options here
        anchors:['s1','s2','s3','s4'],
		autoScrolling: false,
        scrollOverflow:true,
        sectionsColor:['#1f2122','aliceblue','#1f2122','#1f2122'],
        bigSectionsDestination: top,
	});
});

function toggleAnswer(answerID) {
    var answerDiv = document.getElementById(answerID);

    if (answerDiv.style.display === 'none') {
      answerDiv.style.display = 'block';
    } else {
      answerDiv.style.display = 'none';
    }
  }


  document.addEventListener("DOMContentLoaded", function() {
    const content1 = "Hello, We are\n";
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