window.addEventListener('DOMContentLoaded', (event) => {
  // Code to be executed when the page finishes loading
  hideLoader(); // Hide the loader once the page is loaded
});

function showLoader() {
  const loader = document.querySelector('.loader');
  loader.classList.remove('hide');
}

function hideLoader() {
  const loader = document.querySelector('.loader');
  loader.classList.add('hide');
  
  const center = document.querySelector('.center');
  center.classList.remove('hide');
}

function goBack() {
  const loginForm = document.getElementById('login-form');
  
  loginForm.classList.remove('hide');
}
const toggleIcon = document.querySelector('.toggle-icon');
const passwordInput = document.querySelector('.password-toggle input[type="password"]');

toggleIcon.addEventListener('click', () => {
  if (passwordInput.type === 'password') {
    passwordInput.type = 'text';
    toggleIcon.innerHTML = '&#x1f441;'; // Change icon to open eye
  } else {
    passwordInput.type = 'password';
    toggleIcon.innerHTML = '&#x1f441;'; // Change icon to closed eye
  }
});
