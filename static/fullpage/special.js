var swiperBottomScrollbarFull = new Swiper('.swiper', {
    allowTouchMove: true,
    slidesPerView: 'auto',
    grabCursor: true,
    preventClicks: true,
    spaceBetween: 30,
    keyboardControl: true,
    speed: 1000,
    pagination: {
        el: null
    },
    scrollbar: {
        el: '.swiper-scrollbar',
        draggable: true,
        hide: false,
        snapOnRelease: true
    },
    mousewheel: {
        enable: true
    },
    keyboard: {
        enabled: true
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev'
    },
    breakpoints: {
        767: {
            scrollbar: {
                hide: true
            },
            spaceBetween: 0,
            autoHeight: true,
            centeredSlides: false,
            slidesOffsetAfter: 85
        }
    },
    on: {
        resize: function () {
            var windowWidth = $(window).width();
            if(windowWidth <= 767){
                    swiperBottomScrollbarFull.direction('vertical');
                    swiperBottomScrollbarFull.detachEvents();
            }else{
                    swiperBottomScrollbarFull.direction('horizontal');
                    swiperBottomScrollbarFull.attachEvents();
            }
            swiperBottomScrollbarFull.update();
        }
    }
});

document.querySelectorAll(".js-horizontal-scroll").forEach(el => {
    el.addEventListener("wheel", e => {
      // 스크롤이 왼쪽 또는 오른쪽 끝에 도달했는지 확인
      const atLeftEnd = (el.scrollLeft === 0);
      
      // 논리상으로는 ===로 하는 게 맞겠지만, 브라우저에 따라 클 수도 있다고 하니 이렇게 둔다.
      const atRightEnd = (el.scrollLeft + el.offsetWidth >= el.scrollWidth);
  
      // 휠 이벤트가 위로 가는 것인지 아래로 가는 것인지 확인
      const scrollingUp = (e.deltaY < 0);
      const scrollingDown = (e.deltaY > 0);
  
      if ((atLeftEnd && scrollingUp) || (atRightEnd && scrollingDown)) {
        // 스크롤이 양 끝에 있고 사용자가 해당 방향으로 계속 스크롤하려고 하면,
        // 이벤트의 기본 동작을 수행하여 수직 스크론을 허용합니다.
        return;
      }
  
      // 그렇지 않으면, 가로 스크롤을 진행합니다.
      e.preventDefault();
      // noinspection JSSuspiciousNameCombination
      el.scrollLeft += e.deltaY * 2;
    })