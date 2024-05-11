// // var swiperBottomScrollbarFull = new Swiper('.swiper', {
// //     allowTouchMove: true,
// //     slidesPerView: 'auto',
// //     grabCursor: true,
// //     preventClicks: true,
// //     spaceBetween: 30,
// //     keyboardControl: true,
// //     speed: 1000,
// //     pagination: {
// //         el: null
// //     },
// //     scrollbar: {
// //         el: '.swiper-scrollbar',
// //         draggable: true,
// //         hide: false,
// //         snapOnRelease: true
// //     },
// //     mousewheel: {
// //         enable: true
// //     },
// //     keyboard: {
// //         enabled: true
// //     },
// //     navigation: {
// //         nextEl: '.swiper-button-next',
// //         prevEl: '.swiper-button-prev'
// //     },
// //     breakpoints: {
// //         767: {
// //             scrollbar: {
// //                 hide: true
// //             },
// //             spaceBetween: 0,
// //             autoHeight: true,
// //             centeredSlides: false,
// //             slidesOffsetAfter: 85
// //         }
// //     },
// //     on: {
// //         resize: function () {
// //             var windowWidth = $(window).width();
// //             if(windowWidth <= 767){
// //                     swiperBottomScrollbarFull.direction('vertical');
// //                     swiperBottomScrollbarFull.detachEvents();
// //             }else{
// //                     swiperBottomScrollbarFull.direction('horizontal');
// //                     swiperBottomScrollbarFull.attachEvents();
// //             }
// //             swiperBottomScrollbarFull.update();
// //         }
// //     }
// // });

// // document.querySelectorAll(".js-horizontal-scroll").forEach(el => {
// //     el.addEventListener("wheel", e => {
// //       // 스크롤이 왼쪽 또는 오른쪽 끝에 도달했는지 확인
// //       const atLeftEnd = (el.scrollLeft === 0);
      
// //       // 논리상으로는 ===로 하는 게 맞겠지만, 브라우저에 따라 클 수도 있다고 하니 이렇게 둔다.
// //       const atRightEnd = (el.scrollLeft + el.offsetWidth >= el.scrollWidth);
  
// //       // 휠 이벤트가 위로 가는 것인지 아래로 가는 것인지 확인
// //       const scrollingUp = (e.deltaY < 0);
// //       const scrollingDown = (e.deltaY > 0);
  
// //       if ((atLeftEnd && scrollingUp) || (atRightEnd && scrollingDown)) {
// //         // 스크롤이 양 끝에 있고 사용자가 해당 방향으로 계속 스크롤하려고 하면,
// //         // 이벤트의 기본 동작을 수행하여 수직 스크론을 허용합니다.
// //         return;
// //       }
  
// //       // 그렇지 않으면, 가로 스크롤을 진행합니다.
// //       e.preventDefault();
// //       // noinspection JSSuspiciousNameCombination
// //       el.scrollLeft += e.deltaY * 2;
// //     })


// ;(function(){
  
//         // we need to set this here for now.
//         var marquee;
      
//         // first, let's grab the element we're going to move around
//         var marquee_el = document.querySelector( '.news-line.marquee' );
//         var children = marquee_el.querySelectorAll( '.news-box');
      
//         // the key here is not to animate all of the cells in the grid, which might be products or what have you; we have a grid constrained by a container, so we can just translate the entire grid and only the part of the grid that fits into the container will be visible anyway
//         function createMarquee(){
          
//           // just to be doubly sure there's an animation method...
//           if ('animate' in marquee_el && typeof marquee_el.animate === 'function') {
            
//             // we're going to recreate the marquee animation when the viewport is resized
//             // so get rid of any existing animation first
//             if( typeof marquee !== 'undefined' ) marquee.cancel();
      
//             // set this dynamically, so the thing will gracefully degrade to a typical grid of items
//             marquee_el.style.whiteSpace = 'nowrap';
      
//             // create a variable for the distance by which the grid element will be transformed
//             var displacement = 0;
      
//             // the width of all the elements in the marquee
//             // it's important to tot up the child element widths because if overflow is hidden,
//             // the clientWidth of the grid_to_animate element will be that of the parent element
//             for ( var j = 0; j < children.length; ++j ) displacement += children[j].clientWidth;
      
//             // crucial: subtract the width of the container
//             // take the opportunity to round the displacement value down to the nearest pixel
//             // the browser may thank you for this by not blurring the shit out of your text 
//             displacement = (displacement - marquee_el.clientWidth) << 0;
      
//             // by using the variable 'marquee' we created in the parent scope,
//             // we can easily use the reference to pause/cancel the animation later if necessary
//             marquee = marquee_el.animate([
//               // these are your keyframes, if you are familiar with the CSS syntax
//               // so your 'from' or '0%' keyframe translates to 'offset: 0'
//               // 'to'/'100%' translates to 'offset: 1'
//               // and anything in betwen like '54%' will be 'offset: .54'
//               { transform: 'matrix(1, 0.00, 0.00, 1, 0, 0)', offset: 0 },
//               { transform: 'matrix(1, 0.00, 0.00, 1,' + -displacement + ', 0)', offset: 1 }
//               // you don't have to use matrix, I just like it
//             ],
//             {
//               // animation-duration = 1 second for each element in marquee
//               // arbitrary decision
//               duration: children.length * 4e3,
      
//               // could be 'ease', 'cubic-bezier(.4,0,.2,1)', etc.
//               easing: 'linear',
      
//               // useful if you don't want the animation to start until your content has loaded from, say, a REST API and you want to speculate a reasonable time for that to take
//               delay: 0,
      
//               // kind of crucial for a marquee...
//               iterations: Infinity,
      
//               // invert animation after completion, so it scrolls backwards */
//               direction: 'alternate',
      
//               // you would use this if your animation is set to occur only a finite number of times, and you wanted the animated element to finish at the end keyframe, rather than the first keyframe
//               fill: 'forwards'
//             });
//           } 
//         }
      
      
//         // quick check for the WAAPI method
//         // you could also do if (typeof grid_to_animate.animate !== 'undefined')
//         // but this is cleaner in my opinion
//         if ('animate' in marquee_el && typeof marquee_el.animate === 'function') {
          
//           // okay, let's fire up the marquee!
//           createMarquee();
      
//           // now for the playing/pausing
//           marquee_el.addEventListener('mouseenter', pauseMarquee, false);
//           marquee_el.addEventListener('mouseleave', playMarquee, false);
          
//           // and resizing
//           window.addEventListener('resize', debounce( createMarquee ), false);
          
//         } else {
//             // let's say hello to those using Safari
//             // or indeed users of IE, not-recently-updated FF, very old Chrome, old Opera, etc.
//             document.querySelector('h1').innerHTML = 'Your browser does not appear to <br> support the Web Animation API';
//             document.querySelector('h2').innerHTML = 'So you see a grid of items like this';
//         }
      
//         // pretty self-explanatory
//         function playMarquee(){
//           if( marquee.playState === 'paused' ) marquee.play();
//         }
        
//         // pretty self-explanatory
//         function pauseMarquee(){
//           if( marquee.playState === 'running' ) marquee.pause();
//         }
      
//         // a debouncing function using requestAnimationFrame
//         // this is just an easy-to-use wrapper I like to use for event handlers
//         function debounce(func){
//           var scheduled, context, args;
//           return function(){
//             context = this; args = [];
//             for(var i = 0; i < arguments.length; ++i) args[i] = arguments[i];
//             !!scheduled && window.cancelAnimationFrame(scheduled);
//             scheduled = window.requestAnimationFrame(function(){
//               func.apply(context, args);
//               scheduled = null;
//             });
//           }
//         }
//       })();