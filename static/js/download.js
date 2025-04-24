// Función para crear y descargar el archivo JSON
function downloadJSON(data) {
    const blob = new Blob([JSON.stringify(data, null, 4)], { type: "application/json" });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = 'resultadoNetCalc.json';  // Nombre del archivo JSON
    link.click();
}

// Redirigir al usuario a la página de resultados
function redirectToResultPage() {
    window.location.href = "/result";  // Redirige a result.html
}

// Ejecutar cuando la página cargue
window.onload = function() {
    const resultado = JSON.parse(document.getElementById("resultadoData").textContent);  // Obtener el resultado del cálculo
    downloadJSON(resultado);  // Descargar el archivo JSON
    setTimeout(redirectToResultPage, 1000);  // Redirigir después de 1 segundo para asegurar que se descargue
};
