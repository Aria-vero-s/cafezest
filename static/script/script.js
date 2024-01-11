
function toggleNav() {
    var navLinks = document.querySelector('.nav-links');
    var burgerIcon = document.querySelector('.burger-icon');

    navLinks.classList.toggle('show');

    if (navLinks.classList.contains('show')) {
        burgerIcon.innerHTML = '✕';
        burgerIcon.style.color = '#fff';
    }
    else {
        burgerIcon.innerHTML = '☰';
        burgerIcon.style.color = '#000';
    }
}

function hideNav() {
    var navLinks = document.querySelector('.nav-links');
    var burgerIcon = document.querySelector('.burger-icon');

    navLinks.classList.remove('show');

    if (navLinks.classList.contains('show')) {
        burgerIcon.innerHTML = '✕';
    }
    else {
        burgerIcon.innerHTML = '☰';
    }
}

// JavaScript to set min-height based on image height
window.onload = function() {
    var hero = document.querySelector('.hero');
    var image = new Image();
    image.src = '../../media/hero.jpg';
  
    image.onload = function() {
      hero.style.minHeight = image.height + 'px';
    };
  };