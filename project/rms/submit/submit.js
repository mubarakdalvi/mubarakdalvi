// for submitting the form

document.addEventListener("DOMContentLoaded", function () {
  var countdownElement = document.getElementById("countdown");
  if (countdownElement) {
  let count = 5;
  function updateCountdown() {
    count--;
    countdownElement.textContent = count;
    if (count === 0) {
      clearInterval(countdownInterval);
      document.getElementById("countdown").textContent = "0";
      window.location.href = "../rms/rms.html";
      window.close();
    }
  }
  const countdownInterval = setInterval(updateCountdown, 1000);
} else {
  console.error("Element with ID 'countdown' not found.");
}
});
