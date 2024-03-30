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
      document.querySelectorAll(".js-pushNavLevelBack.isOpen")
        .forEach(navLevel => navLevel.classList.remove("isOpen"));
    });
  
    openLevel.forEach(item => {
      item.addEventListener("click", function () {
        const nextNavLevel = this.nextElementSibling;
        if (nextNavLevel) {
          nextNavLevel.classList.add("isOpen");
        }
      });
    });
  
    closeLevel.forEach(item => {
      item.addEventListener("click", function () {
        const parentNavLevel = this.closest(".js-pushNavLevelBack");
        if (parentNavLevel) {
          parentNavLevel.classList.remove("isOpen");
          parentNavLevel.querySelectorAll(".isOpen")
            .forEach(childLevel => childLevel.classList.remove("isOpen"));
        }
      });
    });
  });






























const inputField = document.getElementById("search-input");
const closeBtn = document.querySelector('.close-btn');

inputField.addEventListener("click", showCloseBtn);

function showCloseBtn() {
    closeBtn.classList.add('active');
}

closeBtn.addEventListener("click", hideCloseBtn);

function hideCloseBtn() {
    closeBtn.classList.remove('active');
    inputField.value = '';
}





