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
