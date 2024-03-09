// InfiniteScroll.js


document.addEventListener("DOMContentLoaded", function() {
    const propsList = document.querySelector(".props");
    const listItem = `<li class="me-5"><a>JOIN OUR CHALLENGE</a></li>
                      <li class="me-5"><a>JOIN OUR VISION</a></li>
                      <li class="me-5"><a>JOIN OUR JOURNEY</a></li>
                      <li class="me-5"><a>JOIN OUR PROJECT</a></li>`;

    for (let i = 0; i < 10; i++) {
        propsList.insertAdjacentHTML('beforeend', listItem);
    }
});













