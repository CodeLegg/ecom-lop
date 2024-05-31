////////////////////////////////////////////

// PRODUCT IMAGE SLIDER

const productinitSlider = () => {
    const imageList = document.querySelector(
      ".product-slider-wrapper .image-list"
    );
    const slideButtons = document.querySelectorAll(
      ".product-slider-wrapper .slide-button"
    );
    const thumbnailsContainer = document.querySelector(
      ".product-thumbnails-container"
    );
    const thumbnailItems =
      thumbnailsContainer.querySelectorAll(".thumbnail-item");
    const maxScrollLeft = imageList.scrollWidth - imageList.clientWidth;
    const firstImage = imageList.firstElementChild;
    const computedStyle = getComputedStyle(imageList);
    const imageWidth =
      firstImage.clientWidth + parseInt(computedStyle.gridColumnGap);
  
    slideButtons.forEach((button) => {
      button.addEventListener("click", () => {
        const direction = button.id === "prev-slide" ? -1 : 1;
        const scrollAmount = imageWidth * direction;
        imageList.scrollBy({ left: scrollAmount, behavior: "smooth" });
      });
    });
  
    const handleSlideButtons = () => {
      slideButtons[0].style.display =
        imageList.scrollLeft <= 0 ? "none" : "block";
      slideButtons[1].style.display =
        imageList.scrollLeft >= maxScrollLeft ? "none" : "block";
    };
  
    imageList.addEventListener("scroll", () => {
      handleSlideButtons();
      synchronizeThumbnails();
    });
  
    const synchronizeThumbnails = () => {
      const scrollPosition =
        (imageList.scrollLeft / maxScrollLeft) *
        (thumbnailsContainer.scrollWidth - thumbnailsContainer.clientWidth);
      thumbnailsContainer.scrollLeft = scrollPosition;
    };
  
    thumbnailItems.forEach((item, index) => {
      item.addEventListener("click", () => {
        const scrollAmount = index * imageWidth;
        imageList.scrollTo({ left: scrollAmount, behavior: "smooth" });
      });
    });
  
    handleSlideButtons();
  };
  
  window.addEventListener("load", productinitSlider);
  
  //////////////////////////
  
  // REVIEW TAB
  
  function openPage(pageName, elmnt) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tab-content");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].classList.remove("active");
    }
    document.getElementById(pageName).style.display = "block";
    elmnt.classList.add("active");
    if (pageName === "reviews" && elmnt.classList.contains("product-review-link")) {
      var productBorderTabs = document.querySelector('.border-product-tabs');
      console.log(productBorderTabs); // Check if the element is correctly selected
      console.log("Scrolling to reviews tab");
      productBorderTabs.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  }
  
  // Open the default tab
  document.getElementById("about").style.display = "block";
  document.getElementsByClassName("tablink")[0].classList.add("active");
  
  // Add event listener to the "Read Reviews" link
  document.querySelector(".product-review-link").addEventListener("click", function(event) {
    event.preventDefault(); // Prevent default link behavior
    openPage("reviews", this);
    openPage("reviews", document.querySelector(".tablink:nth-child(2)")); // Activate the reviews tab
  });
  
  
  ////////////////////////////////////////////////////////
  
  