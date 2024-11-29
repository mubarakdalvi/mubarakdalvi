document.addEventListener('DOMContentLoaded', function() {
     var l = document.getElementById("line");
     if (l) {
       var ctx = l.getContext("2d");
       ctx.moveTo(0, 0);
       ctx.lineTo(200, 100);
       ctx.stroke();
     } else {
       console.error("Element with ID 'line' not found.");
     }

     // for circle

     var c = document.getElementById("circle");
     if (c) {
       var ctx = c.getContext("2d");
       ctx.beginPath();
       ctx.arc(95, 50, 40, 0, 2 * Math.PI);
       ctx.stroke();
     } else {
       console.error("Element with ID 'line' not found.");
     }

     //for line in circle

     var cl = document.getElementById("Line-over-circle");
     if (cl) {
       var col = cl.getContext("2d");
       col.beginPath();
       col.arc(95, 50, 40, 0, 2 * Math.PI);
       col.stroke();
       col.moveTo(0, 0);
       col.lineTo(200, 100);
       col.stroke();
     } else {
       console.error("Element with ID 'line' not found.");
     }
});