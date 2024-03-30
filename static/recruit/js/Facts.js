// Recruit Template Javascript

(function ($) {
    "use strict";

    // Facts counter
    function startCounter() {
        $('[data-toggle="counter-up"]').counterUp({
            delay: 10,
            time: 2000
        });
    }

    // Call startCounter function to initialize counter
    startCounter();

})(jQuery);