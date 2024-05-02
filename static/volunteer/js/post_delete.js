// post_delete.js

document.addEventListener('DOMContentLoaded', function() {
    const deleteButtons = document.querySelectorAll('.post_delete');

    deleteButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            event.preventDefault();

            const uri = this.getAttribute('data-uri');

            // Confirm deletion
            if (confirm("Are you sure you want to delete?")) {
                // If confirmed, redirect to delete endpoint
                window.location.href = uri;
            }
        });
    });
});
