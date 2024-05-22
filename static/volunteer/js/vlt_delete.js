// vlt_delete.js

document.addEventListener('DOMContentLoaded', function() {
    document.body.addEventListener('click', function(event) {
        if (event.target.closest('.vlt_delete')) {
            event.preventDefault();

            const button = event.target.closest('.vlt_delete');
            const uri = button.getAttribute('data-uri');

            // Confirm deletion
            if (confirm("Are you sure you want to delete?")) {
                // If confirmed, redirect to delete endpoint
                window.location.href = uri;
            }
        }
    });
});
