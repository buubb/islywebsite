// topic_carousel.js

(function ($) {
    "use strict";

    $(".topic-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        margin: 25,
        loop: true,
        dots: false,
        nav: true,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 1
            },
            1200: {
                items: 1
            },
            1800: {
                items: 1
            }
        }
    });

})(jQuery);