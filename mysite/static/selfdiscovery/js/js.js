
const link = document.querySelector('#update-profile-link');
const form = document.querySelector('#update-profile-form');
const link2 = document.querySelector('#change-password-link');
const form2 = document.querySelector('#change-password-form');
const link3 = document.querySelector('#contact-admin-link');
const form3 = document.querySelector('#contact-admin-form');

link.addEventListener('click', (event) => {
  event.preventDefault();
  form.style.display = (form.style.display === 'none') ? 'block' : 'none';
});

link2.addEventListener('click', (event) => {
  event.preventDefault();
  form2.style.display = (form2.style.display === 'none') ? 'block' : 'none';
});

link3.addEventListener('click', (event) => {
  event.preventDefault();
  form3.style.display = (form3.style.display === 'none') ? 'block' : 'none';
});


