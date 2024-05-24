(function($){
    // Toggle menu
    $(".hamburger").click(function(){
        $(".res-nav-container").slideToggle();
    });

    // Document click event
    $(document).on("click", function(event) {
        // Do nothing if the dropdown is open and the event occurred inside the dropdown
        if ($(".depth_1").is(":visible") && !$(event.target).closest(".depth_1").length) {
            $(".depth_1").slideUp();
        }
    });

    // aboutdrop click event
    $(".aboutdrop").click(function(event){
        event.stopPropagation(); // Prevent the click event from propagating to the parent
        $(".depth_1").slideToggle();
    });

    // nav selected active effect
    $(function(){
        // This will get the full URL at the address bar
        var url = window.location.href; 

        // Passes on every "a" tag 
        $(".nav a").each(function() {
            // Checks if it's the same as the address bar
            if(url == (this.href)) { 
                $(this).closest(".menu_li").addClass("active");
            }
        });
    });

    // footer
    const nowUrl = "official.i.sly0@gmail.com";

    function copyUrl(){ 
        navigator.clipboard.writeText(nowUrl).then(res=>{
            alert("Mail Address copied!");
        });
    }

    // Add copyUrl function to the window object for global access
    window.copyUrl = copyUrl;

})(jQuery);