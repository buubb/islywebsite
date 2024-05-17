$(".hamburger").click(function(){
    $(".res-nav-container").slideToggle();
  });

$(document).on("click", function(event) {
      // dropdown이 열려있을 때와 이벤트가 dropdown 내부에서 발생한 경우에는 아무 동작도 하지 않음
      if($(".depth_1").is(":visible") && !$(event.target).closest(".depth_1").length) {
          $(".depth_1").slideUp();
      }
      if($(".depth_2").is(":visible") && !$(event.target).closest(".depth_2").length) {
        $(".depth_2").slideUp();
    }
  });

$(".aboutdrop").click(function(event){
    event.stopPropagation(); // 클릭 이벤트가 부모로 전파되지 않도록 함
    $(".depth_1").slideToggle();
  });

$(".aboutdrop2").click(function(event){
    event.stopPropagation(); // 클릭 이벤트가 부모로 전파되지 않도록 함
    $(".depth_2").slideToggle();
});