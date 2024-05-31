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

    // Toggle overflow hidden on body
    document.body.style.overflow = mobileMenuLevelZero.classList.contains(
      "isOpen"
    )
      ? "hidden"
      : "auto";

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

const inputField = document.getElementById("search-input");
const closeBtn = document.querySelector(".close-btn");

inputField.addEventListener("input", showCloseBtn);

function showCloseBtn() {
    if (inputField.value) {
        closeBtn.classList.add("active");
    } else {
        closeBtn.classList.remove("active");
    }
}

closeBtn.addEventListener("click", hideCloseBtn);

function hideCloseBtn() {
    closeBtn.classList.remove("active");
    inputField.value = "";
}

///////////////////////////////////////////////////////////////
document.addEventListener("DOMContentLoaded", function () {
  const dropdownToggle = document.querySelector(".dropdown-toggle");
  const chevronIcon = dropdownToggle.querySelector(".fa-chevron-down");
  dropdownToggle.addEventListener("click", function () {
    const dropdownMenu = this.nextElementSibling;

    // Toggle the visibility of the dropdown
    dropdownMenu.classList.toggle("show");

    // Toggle class to rotate the chevron icon based on the visibility state
    if (dropdownMenu.classList.contains("show")) {
      // If the dropdown is visible, rotate the chevron up
      chevronIcon.classList.add("rotate-up");
      chevronIcon.classList.remove("rotate-down");
    } else {
      // If the dropdown is hidden, rotate the chevron down
      chevronIcon.classList.add("rotate-down");
      chevronIcon.classList.remove("rotate-up");
    }
  });
});

