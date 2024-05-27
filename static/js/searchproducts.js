
function initializeAutocomplete() {
    console.log("Initializing autocomplete");
    $.ajax({
        method: "POST",
        url: productList,
        data: {
            csrfmiddlewaretoken: csrfToken  // Include CSRF token in data
        },
        success: function (response) {
            console.log("AJAX request successful", response);
            $(".searchproducts").autocomplete({
                source: response
            });
            console.log("Autocomplete initialized");
        },
        error: function (xhr, status, error) {
            console.error("Error fetching product names:", error);
        }
    });
}

// Ensure the document is ready before initializing autocomplete
$(document).ready(function() {
    initializeAutocomplete();
});