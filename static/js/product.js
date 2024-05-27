$(document).on('click', '#add-cart', function(e) {
  e.preventDefault();
  $.ajax({
      type: 'POST',
      url: cartAddUrl,  // Use the JavaScript variable for the URL
      data: {
          product_id: $('#add-cart').val(),
          product_qty: $('#quantity-cart option:selected').text(),
          csrfmiddlewaretoken: csrfToken,  // Use the JavaScript variable for CSRF token
          action: 'post'
      },
      success: function(json) {
          // Update the cart quantity display
          document.getElementById("cart_quantity").textContent = json.qty;
          // Reload the page
          location.reload();
      },
      error: function(xhr, errmsg, err) {
          // Handle error
      }
  });
});