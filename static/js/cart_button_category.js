$(document).on('click', '.cart-btn', function (e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: cartAddUrl, // Use the variable defined in the template
        data: {
            product_id: $(this).val(), // Use $(this) to refer to the clicked button
            product_qty: 1, // Default quantity
            csrfmiddlewaretoken: csrfToken, // Use the variable defined in the template
            action: 'post'
        },
        success: function (json) {
            location.reload();
        },
        error: function (xhr, errmsg, err) {
            // Handle error
        }
    });
});
