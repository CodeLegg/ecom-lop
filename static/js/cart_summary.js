document.addEventListener('DOMContentLoaded', () => {
    const cardContentCartElements = document.querySelectorAll('.card-content-cart');
  
    cardContentCartElements.forEach(element => {
      element.addEventListener('click', () => {
        // Remove 'clicked' class from all elements
        cardContentCartElements.forEach(el => {
          el.classList.remove('clicked');
        });
  
        // Add 'clicked' class to the clicked element
        element.classList.add('clicked');
  
        // After ten seconds, remove the 'clicked' class if not clicked again
        const timeout = setTimeout(() => {
          cardContentCartElements.forEach(el => {
            el.classList.remove('clicked');
          });
        }, 10000); // 10 seconds in milliseconds
  
        // If another item is clicked within 10 seconds, clear the timeout
        cardContentCartElements.forEach(el => {
          el.addEventListener('click', () => {
            clearTimeout(timeout);
          });
        });
      });
    });
  });
  
// cart delete

$(document).on('click', '.cart-update', function (e) {
    e.preventDefault();
    var product_id = $(this).data('index');
    $.ajax({
      type: 'POST',
      url: cartAddUrl, // Use the cartAddUrl variable defined in the template
      data: {
        product_id: $(this).data('index'),
        product_qty: $('#select' + product_id + ' option:selected').text(), // Corrected variable name
        csrfmiddlewaretoken: csrfToken, // Use the csrfToken variable defined in the template
        action: 'post'
      },
  
      success: function (json) {
        //console.log(json)
        location.reload();
      },
  
      error: function (xhr, errmsg, err) {
        // Handle error
      }
    });
  });
  
  // cart delete
  
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
        //console.log(json)
        location.reload();
      },
  
      error: function (xhr, errmsg, err) {
        // Handle error
      }
    });
  });
  