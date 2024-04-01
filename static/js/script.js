// PUSH NAV

document.addEventListener("DOMContentLoaded", function () {
  const menuToggle = document.querySelector(".js-menuToggle");
  const mobileMenuLevelZero = document.querySelector(".js-pushmobileMenu");
  const navOverlay = document.querySelector(".js-navOverlay");
  const openLevel = document.querySelectorAll(".js-openLevel");
  const closeLevel = document.querySelectorAll(".js-closeLevel");

  menuToggle.addEventListener("click", function (e) {
    e.preventDefault();
    mobileMenuLevelZero.classList.toggle("isOpen");
    menuToggle.classList.toggle("cross");
    navOverlay.classList.toggle("active");

    // Remove isOpen class from all levels
    document
      .querySelectorAll(".js-pushNavLevelBack.isOpen")
      .forEach((navLevel) => navLevel.classList.remove("isOpen"));
  });

  openLevel.forEach((item) => {
    item.addEventListener("click", function () {
      const nextNavLevel = this.nextElementSibling;
      if (nextNavLevel) {
        nextNavLevel.classList.add("isOpen");
      }
    });
  });

  closeLevel.forEach((item) => {
    item.addEventListener("click", function () {
      const parentNavLevel = this.closest(".js-pushNavLevelBack");
      if (parentNavLevel) {
        parentNavLevel.classList.remove("isOpen");
        parentNavLevel
          .querySelectorAll(".isOpen")
          .forEach((childLevel) => childLevel.classList.remove("isOpen"));
      }
    });
  });
});

//////////////////////////////////////////////////////////////////

// SEARCH CLOSE BUTTON

const inputField = document.getElementById("search-input");
const closeBtn = document.querySelector(".close-btn");

inputField.addEventListener("click", showCloseBtn);

function showCloseBtn() {
  closeBtn.classList.add("active");
}

closeBtn.addEventListener("click", hideCloseBtn);

function hideCloseBtn() {
  closeBtn.classList.remove("active");
  inputField.value = "";
}

///////////////////////////////////////////////////////////////

// SLIDER

const initSlider = () => {
  const imageList = document.querySelector(".slider-wrapper .image-list");
  const slideButtons = document.querySelectorAll(".slider-wrapper .slide-button");
  const sliderScrollbar = document.querySelector(".slider-container .slider-scrollbar");
  const scrollbarThumb = sliderScrollbar.querySelector(".scrollbar-thumb");
  const maxScrollLeft = imageList.scrollWidth - imageList.clientWidth;
  const firstImage = imageList.firstElementChild;
  const computedStyle = getComputedStyle(imageList); // Get the computed style of the image list
  const imageWidth =
    firstImage.clientWidth + parseInt(computedStyle.gridColumnGap); // Include grid gap in image width

 scrollbarThumb.addEventListener("mousedown", (e) => {
  const startX = e.clientX;
  const thumbPosition = scrollbarThumb.offsetLeft;

  // Uodate thumb position on mouse move
  const handleMouseMove = (e) => {
    const deltaX = e.clientX - startX;
    const newThumbPosition = thumbPosition + deltaX;
    const maxThumbPosition = sliderScrollbar.getBoundingClientRect().width - scrollbarThumb.offsetWidth;

    const boundedPosition = Math.max(0, Math.min(maxThumbPosition, newThumbPosition));
    const scrollPosition = (boundedPosition / maxThumbPosition) * maxScrollLeft;

    scrollbarThumb.style.left = `${boundedPosition}px`;
    imageList.scrollLeft = scrollPosition;
  }
  // remove event listener on mouse up
  const handleMouseUp = () => {
    document.removeEventListener("mousemove", handleMouseMove);
  document.removeEventListener("mouseup", handleMouseUp);
  }
// add event listener for drag interaction
  document.addEventListener("mousemove", handleMouseMove);
  document.addEventListener("mouseup", handleMouseUp);
 });

  // Slide images according to the slide button clicks
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
    updateScrollThumbPosition(); // Update scrollbar thumb position when the slider is scrolled
  });

  const updateScrollThumbPosition = () => {
    const scrollPosition = imageList.scrollLeft;
    const thumbPosition =
      (scrollPosition / maxScrollLeft) *
      (sliderScrollbar.clientWidth - scrollbarThumb.offsetWidth);
    scrollbarThumb.style.left = `${thumbPosition}px`;
  };

  // Call handleSlideButtons initially to set initial button visibility
  handleSlideButtons();
  updateScrollThumbPosition();
};

window.addEventListener("load", initSlider);
