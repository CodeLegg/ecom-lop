document.addEventListener('DOMContentLoaded', () => {
  const cardContentCartElements = document.querySelectorAll('.card-content-cart');

  cardContentCartElements.forEach(element => {
    element.addEventListener('click', () => {
      cardContentCartElements.forEach(el => el.classList.remove('clicked'));
      element.classList.add('clicked');
      const timeout = setTimeout(() => cardContentCartElements.forEach(el => el.classList.remove('clicked')), 10000);
      cardContentCartElements.forEach(el => el.addEventListener('click', () => clearTimeout(timeout)));
    });
  });
});

$(document).on('click', '.cart-update', function (e) {
  e.preventDefault();
  var product_id = $(this).data('index');
  $.ajax({
    type: 'POST',
    url: cartAddUrl, // Use the cartAddUrl variable defined in the template
    data: {
      product_id: product_id,
      product_qty: $('#select' + product_id + ' option:selected').text(),
      csrfmiddlewaretoken: csrfToken, // Use the csrfToken variable defined in the template
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

$(document).on('click', '.cart-delete', function (e) {
  e.preventDefault();
  $.ajax({
    type: 'POST',
    url: cartDeleteUrl, // Use the cartDeleteUrl variable defined in the template
    data: {
      product_id: $(this).data('index'),
      csrfmiddlewaretoken: csrfToken, // Use the csrfToken variable defined in the template
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