// for line

document.addEventListener("DOMContentLoaded", function () {

  // for adding profile changing functionality
  var fileInput = document.getElementById("fileinput");
  if (fileInput) {
    fileInput.addEventListener("change", function (event) {
      const file = event.target.file[0];
      if (file) {
        const validImageTypes = [
          "image/jpeg",
          "images/png",
          "images/gif",
          "image/ai",
        ];
        if (validImageTypes.includes(file.type)) {
          const reader = new FileReader();
          reader.onload = function (e) {
            document.getElementById("profileIcon").src = e.target.result;
          };
          reader.readAsDataURL(file);
        } else {
          alert(
            "Please Upload a valid image file from this format (JPEG<, PNG, GIF"
          );
        }
      }
    });
  } else {
    console.error("Element with ID 'fileinput' not found.");
  }

  // for showing entered data where user will be able to see and will redirect to submit page
  var form = document.getElementById("Form");
  if (form) {
    form.addEventListener("submit", function (event) {
      event.preventDefault();

      const countryCode = document.getElementById("countryCode").value;
      const number = document.getElementById("numberInput").value;
      const censoredNumber = maskMobileNumber(number);
      document.getElementById(
        "show"
      ).textContent = `Your Provided Mobile Number is :${countryCode}${censoredNumber}`;
       setTimeout(function () {
         window.location.href = "../submit/submit.html";
       }, 5000);
    });
  } else {
    console.error("Element with ID 'Form' not found.");
  }
  function maskMobileNumber(number) {
    number = number.toString();
    if (number.length < 10) {
      return number;
    }
    const prefix = number.substring(0, 2);
    const suffix = number.substring(number.length - 2);
    const masked = "*".repeat(number.length - 4);
    return `${prefix}${masked}${suffix}`;
  }
});
