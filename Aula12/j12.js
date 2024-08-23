const themeToggleButton = document.querySelector('.theme-toggle');
const themeStylesheet = document.getElementById('theme-stylesheet');

themeToggleButton.addEventListener('click', () => {
    if (themeStylesheet.getAttribute('href') === 'light-theme.css') {
        themeStylesheet.setAttribute('href', 'dark-theme.css');
    } else {
        themeStylesheet.setAttribute('href', 'light-theme.css');
    }
});