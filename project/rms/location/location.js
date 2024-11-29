// geolocation for map
const m = document.getElementById("map");
function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    m.innerHTML = "Geolocation is not supported by this browser.";
  }
}
function showPosition(position) {
  m.innerHTML =
    "Latitude: " +
    position.coords.latitude +
    "<br> Longitude: " +
    position.coords.longitude;
}
