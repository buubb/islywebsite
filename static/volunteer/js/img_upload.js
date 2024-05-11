// img_upload.js

let fileInput = document.getElementById("file-input");
let imageContainer = document.getElementById("img-container");
let numOfFiles = document.getElementById("num-of-files");

function preview(){
    // Clear image container
    imageContainer.innerHTML = "";
    // Update numOfFiles
    numOfFiles.textContent = `${fileInput.files.length} Files Selected`;

    // Check file types
    for(let i of fileInput.files){
        if (!['image/jpg', 'image/jpeg', 'image/png'].includes(i.type)) {
            alert("Only JPG, JPEG, and PNG files are allowed.");
            // Clear file input
            fileInput.value = "";
            // Clear image container
            imageContainer.innerHTML = "";
            // Update numOfFiles
            numOfFiles.textContent = "No Files Chosen";
            // Stop further processing
            return;
        }

        let reader = new FileReader();
        let figure = document.createElement("figure");
        let figCap = document.createElement("figcaption");
        // Get the filename
        let filename = i.name;
        if (filename.length > 15) {
            let firstPart = filename.substring(0, 4);
            let lastPart = filename.substring(filename.length - 8, filename.length);
            figCap.innerText = firstPart + "..." + lastPart;
        } else {
            figCap.innerText = filename;
        }
        figCap.classList.add("image-caption");
        figure.appendChild(figCap);
        reader.onload = () => {
            let img = document.createElement("img");
            img.setAttribute("src", reader.result);
            figure.insertBefore(img, figCap);
        }
        imageContainer.appendChild(figure);
        reader.readAsDataURL(i);
    }
}
