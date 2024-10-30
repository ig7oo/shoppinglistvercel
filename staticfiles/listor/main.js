var m = document.getElementsByClassName("alert");  // Return an array

setTimeout(function(){
   if (m && m.length) {
       m[0].classList.add('hide');
   }
}, 3000);