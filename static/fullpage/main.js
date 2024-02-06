$(function(){
    $('#fullpage').fullpage({
		//options here
        anchors:['s1','s2','s3','s4','s5'],
		//autoScrolling:true,
		//scrollHorizontally: true,
        //navigation: true,
        //navigationPosition: 'bottom',
        sectionsColor:['#000','#1f2122','#1f2122','#1f2122', '#1f2122']
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