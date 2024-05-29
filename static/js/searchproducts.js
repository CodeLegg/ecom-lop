function initializeAutocomplete() {
    console.log("Initializing autocomplete");
    $.ajax({
        method: "POST",
        url: productList,  // Assuming productListAjaxUrl is the URL mapped to productlistAjax view
        data: {
            csrfmiddlewaretoken: csrfToken  // Include CSRF token in data
        },
        success: function (response) {
            console.log("AJAX request successful", response);
            var products = [];
            $.each(response, function(index, product) {
                products.push({
                    label: product.name,
                    value: product.name,
                    // Include the first image URL, if available
                    // You can modify this part to include multiple images if needed
                    image: product.images.length > 0 ? product.images[0] : null
                });
            });
            $(".searchproducts").autocomplete({
                source: products,
                // Custom rendering for autocomplete items
                // You can modify this to display images alongside names
                select: function(event, ui) {
                    if (ui.item.image) {
                        // Handle selection with image
                        console.log("Selected product:", ui.item.label, "Image URL:", ui.item.image);
                    } else {
                        // Handle selection without image
                        console.log("Selected product:", ui.item.label);
                    }
                }
            }).data("ui-autocomplete")._renderItem = function(ul, item) {
                var listItem = $("<li>");
                if (item.image) {
                    listItem.append("<img src='" + item.image + "' alt='Product Image' class='autocomplete-image'>");
                }
                listItem.append("<span>" + item.label + "</span>");
                return listItem.appendTo(ul);
            };
            console.log("Autocomplete initialized");
        },
        error: function (xhr, status, error) {
            console.error("Error fetching product data:", error);
        }
    });
}

// Ensure the document is ready before initializing autocomplete
$(document).ready(function() {
    initializeAutocomplete();
});

