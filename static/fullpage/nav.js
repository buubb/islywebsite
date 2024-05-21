$(".hamburger").click(function(){
    $(".res-nav-container").slideToggle();
  });

$(document).on("click", function(event) {
      // dropdown이 열려있을 때와 이벤트가 dropdown 내부에서 발생한 경우에는 아무 동작도 하지 않음
      if($(".depth_1").is(":visible") && !$(event.target).closest(".depth_1").length) {
          $(".depth_1").slideUp();
      }
  });

$(".aboutdrop").click(function(event){
    event.stopPropagation(); // 클릭 이벤트가 부모로 전파되지 않도록 함
    $(".depth_1").slideToggle();
  });
  
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