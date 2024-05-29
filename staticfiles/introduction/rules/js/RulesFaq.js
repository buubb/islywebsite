// RulesFaq.js

document.addEventListener("DOMContentLoaded", function() {
  var faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(function(item) {
    var iconShow = item.querySelector('.icon-show');
    var iconClose = item.querySelector('.icon-close');
    var answer = item.querySelector('.collapse');

    if (answer.classList.contains('show')) {
      iconShow.style.display = 'none';
      iconClose.style.display = 'inline-block';
    } else {
      iconShow.style.display = 'inline-block';
      iconClose.style.display = 'none';
    }

    item.addEventListener('click', function() {
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






