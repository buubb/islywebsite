// NoticeCarousel.js

(function ($) {
    "use strict";

    $(".notice-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        margin: 30,
        loop: true,
        dots: false,
        nav: true,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 2
            },
            1200: {
                items: 3
            },
            1800: {
                items: 3
            }
        }
    });

})(jQuery);