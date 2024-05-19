$(function() {

    $('.btn-link[aria-expanded="true"]').closest('.accordion-item').addClass('active');
  $('.collapse').on('show.bs.collapse', function () {
	  $(this).closest('.accordion-item').addClass('active');
	});

  $('.collapse').on('hidden.bs.collapse', function () {
	  $(this).closest('.accordion-item').removeClass('active');
	});

});

const collectButton = document.getElementById('collect-button');
const checkboxes = document.querySelectorAll('input[type="checkbox"]');

collectButton.addEventListener('click', function() {
  const checkedElements = [];
  checkboxes.forEach(checkbox => {
    if (checkbox.checked) {
      // Use checkbox.name or checkbox.id depending on your preference
      checkedElements.push(checkbox.name || checkbox.id);
    }
  });

  // Create a downloadable text file
  const content = checkedElements.join("\n"); // Join elements with newline characters
  const blob = new Blob([content], { type: 'text/plain;charset=utf-8' });
  const url = window.URL.createObjectURL(blob);

  // Simulate a click on a temporary anchor element
  const link = document.createElement('a');
  link.href = url;
  link.download = 'checked_elements.txt'; // Set filename
  link.click();

  // Revoke the temporary URL object
  window.URL.revokeObjectURL(url);
});
