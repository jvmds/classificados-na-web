(function () {
    'use strict'

    const tipo_anuncio = document.getElementById('id_tipo_anuncio');
    const imagem = document.getElementById('id_imagem');

    tipo_anuncio.addEventListener('click', () => {
        // console.log(tipo_anuncio.value);
        if (tipo_anuncio.selectedIndex === 2) {
            imagem.style.display = 'block';
        } else {
            imagem.style.display = 'none';
        }
    });
})()