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
  
  document.querySelector('form').addEventListener('submit', (event) => {
    // Show the loader when the form is submitted
    showLoader();
  });