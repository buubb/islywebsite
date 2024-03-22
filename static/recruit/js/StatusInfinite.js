// StatusInfinite.js


document.addEventListener("DOMContentLoaded", function() {
    const propsList = document.querySelector(".props");
    const listItem = `<li class="me-5"><a>CHECK APPLICATION STATUS!</a></li>
                      <li class="me-5"><a>ARE YOU READY TO JOIN US?</a></li>`;

    for (let i = 0; i < 10; i++) {
        propsList.insertAdjacentHTML('beforeend', listItem);
    }
});













