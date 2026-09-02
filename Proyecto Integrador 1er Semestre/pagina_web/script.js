
let imagenes = [
    "img/foto1Prov.svg",
    "img/foto2Ced.png",
    "img/foto3Prog.jpeg",
    "img/foto4Bas.jpeg",
    "img/foto5Err.jpeg"
];

let posicion = 0;

function imagenSiguiente() {

    posicion = posicion + 1;

    if (posicion == imagenes.length) {
        posicion = 0;
    }

    document.getElementById("imagenGaleria").src = imagenes[posicion];
}


function imagenAnterior() {

    posicion = posicion - 1;

    if (posicion < 0) {
        posicion = imagenes.length - 1;
    }

    document.getElementById("imagenGaleria").src = imagenes[posicion];
}




function irFuncionamiento() {
    const funcionamiento = document.getElementById('funcionamiento');

    funcionamiento.scrollIntoView();
}

function mostrarProvincias() {
    const provincias = document.getElementById('tablaProvincias');
    const boton = document.getElementById('botonProvincias');

    if (provincias.style.display == 'flex') {
        provincias.style.display = 'none';

        boton.textContent = 'Mostrar provincias';

    } else {
        provincias.style.display = 'flex';
        boton.textContent = 'Ocultar provincias'
    }

}
