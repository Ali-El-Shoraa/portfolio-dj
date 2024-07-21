document.addEventListener("DOMContentLoaded", function () {
  const toggleMenu = document.getElementById("toggle-menu");
  const menuIcon = document.getElementById("menu-icon");
  const ulList = document.getElementById("list");
  const liList = document.querySelectorAll("li");

  toggleMenu.addEventListener("click", function () {
    menuIcon.classList.toggle("fa-bars");
    menuIcon.classList.toggle("fa-times");

    menuIcon.classList.contains("fa-bars")
      ? (ulList.style.right = "-100%")
      : (ulList.style.right = "0");
  });

  liList.forEach((li) => {
    li.addEventListener("click", function () {
      menuIcon.classList.toggle("fa-bars");
      menuIcon.classList.toggle("fa-times");

      menuIcon.classList.contains("fa-bars")
        ? (ulList.style.right = "-100%")
        : (ulList.style.right = "0");
    });
  });
});
