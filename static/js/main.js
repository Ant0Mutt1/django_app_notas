document.addEventListener('DOMContentLoaded', function() {
  
  var etiquetaLiList = document.querySelectorAll('.etiqueta-li');

  etiquetaLiList.forEach(function(etiquetaLi) {
    var miEnlaces = etiquetaLi.querySelectorAll('.miEnlace');

    etiquetaLi.addEventListener('mouseover', function(event) {
      miEnlaces.forEach(function(miEnlace) {
        if (event.target !== miEnlace) {
          miEnlace.removeAttribute('hidden');
        }
      });
    });

    document.addEventListener('mouseover', function(event) {
      var mouseDentroDelLi = etiquetaLi.contains(event.target);

      miEnlaces.forEach(function(miEnlace) {
        if (!mouseDentroDelLi) {
          miEnlace.setAttribute('hidden', 'true');
        }
      });
    });
  });
});

