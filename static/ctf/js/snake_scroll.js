// snake_scroll.js


document.addEventListener("DOMContentLoaded", function() {
    const propsList = document.querySelector(".props");
    const listItem = `<li class="me-5"><a>USE ARROW KEYS TO PLAY</a></li>
                      <li class="me-5"><a>USE ARROW KEYS TO PLAY</a></li>`;

    for (let i = 0; i < 10; i++) {
        propsList.insertAdjacentHTML('beforeend', listItem);
    }
});













