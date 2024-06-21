/* jshint esversion: 6 */

// Ensure the DOM is fully loaded before executing
document.addEventListener('DOMContentLoaded', () => {
  const cardContentCartElements = document.querySelectorAll('.card-content-cart');

  cardContentCartElements.forEach(element => {
    element.addEventListener('click', () => {
      // Remove 'clicked' class from all elements
      cardContentCartElements.forEach(el => el.classList.remove('clicked'));
      // Add 'clicked' class to the clicked element
      element.classList.add('clicked');
      
      // Set a timeout to remove the 'clicked' class after 10 seconds
      const timeout = setTimeout(() => {
        cardContentCartElements.forEach(el => el.classList.remove('clicked'));
      }, 10000);

      // Clear the timeout if any element is clicked again
      cardContentCartElements.forEach(el => el.addEventListener('click', () => clearTimeout(timeout)));
    });
  });
});

// Ensure jQuery is included before using it
$(document).on('click', '.cart-update', function (e) {
  e.preventDefault();
  var product_id = $(this).data('index');

  $.ajax({
    type: 'POST',
    url: cartAddUrl, // cartAddUrl must be defined in the HTML or template
    data: {
      product_id: product_id,
      product_qty: $('#select' + product_id + ' option:selected').text(),
      csrfmiddlewaretoken: csrfToken, // csrfToken must be defined in the HTML or template
      action: 'post'
    },
    success: function (json) {
      location.reload();
    },
    error: function (xhr, errmsg, err) {
      console.error('Error:', errmsg);
    }
  });
});

$(document).on('click', '.cart-delete', function (e) {
  e.preventDefault();
  var product_id = $(this).data('index');

  $.ajax({
    type: 'POST',
    url: cartDeleteUrl, // cartDeleteUrl must be defined in the HTML or template
    data: {
      product_id: product_id,
      csrfmiddlewaretoken: csrfToken, // csrfToken must be defined in the HTML or template
      action: 'post'
    },
    success: function (json) {
      location.reload();
    },
    error: function (xhr, errmsg, err) {
      console.error('Error:', errmsg);
    }
  });
});
