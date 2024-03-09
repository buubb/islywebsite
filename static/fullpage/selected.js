$(function(){
    // this will get the full URL at the address bar
    var url = window.location.href; 

    // passes on every "a" tag 
    $(".nav .menu_name").each(function() {
            // checks if its the same on the address bar
        if(url == (this.href)) { 
            $(this).closest(".menu_li").addClass("active");
        }
    });
});