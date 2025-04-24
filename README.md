# 🌐 NetCalc - Calculadora de Redes IP

**NetCalc** es una herramienta para el cálculo de redes IP. Pensada para administradores de sistemas, estudiantes, y entusiastas de redes, permite trabajar tanto en una interfaz web intuitiva como en una potente línea de comandos (CLI).

> ⚠️ **NetCalc está en fase de prueba.** Esto significa que podrían realizarse cambios importantes en el futuro que modifiquen funcionalidades, sintaxis o resultados. ¡Gracias por tu comprensión!

Con **NetCalc**, puedes obtener de forma rápida y visual la dirección de red, broadcast, primer y último host, número de hosts disponibles y mucho más. Además, ofrece exportación de los resultados a archivos JSON.

---

## 📦 Características principales

- ✅ Cálculo completo de redes a partir de IP y máscara como argumentos de entrada.
- 🧠 Soporte para máscara decimal o CIDR (`192.168.1.1/24`).
- 💻 Interfaz web con Flask (frontend responsive y atractivo).
- 🖥️ Interfaz de línea de comandos (CLI).
- 📁 Exportación de resultados en formato JSON.
- 🎨 Estilos y scripts modularizados (CSS y JS externos).
- 🖱️  Código escalable.
- 🧪 Validación de entradas y manejo de errores.

---

## 🚀 Instalación

### Requisitos

- Python 3.6 o superior
- pip (gestor de paquetes de Python)

### Dependencias y librerias

- Flask 2.3.2
- Colorama 0.4.4

### Clonar el repositorio

```bash
git clone https://github.com/AdriSP16/NetCalc.git
cd NetCalc
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 🖥️ Uso de la interfaz web

### Iniciar el servidor Flask

```bash
python app.py
```

Esto iniciará la aplicación en:

```bash
http://127.0.0.1:5000
```

### ¿Qué puedes hacer desde la web?

- Introducir una dirección IP y máscara (ej: `192.168.1.10` y `255.255.255.0`)
- Visualizar los resultados en una tabla clara
- Descargar los resultados en un archivo JSON listo para usar

---

## ⚙️ Uso en línea de comandos (CLI)

### Sintaxis básica

```bash
python cli.py --ip Ip_para_analizar --mascara Mascara_red
```

### Con exportación a JSON

```bash
python cli.py --ip Ip_para_analizar --mascara mascara_red --json
```

### Opciones disponibles

| Opción      | Descripción                                      |
|-------------|--------------------------------------------------|
| `--ip`      | Dirección IP a analizar                          |
| `--mascara` | Máscara de subred (puede ser en CIDR o decimal)  |
| `--json`    | (Opcional) Exporta resultado como JSON           |

---

## 📁 Estructura del proyecto

```plaintext
netcalc/
│
├── app.py                # Servidor Flask
├── cli.py                # Modo línea de comandos
├── network_utils.py      # Lógica de cálculo
├── requirements.txt
│
├── templates/            # HTML5
│   ├── index.html
│   ├── result.html
│   └── download_redirect.html
│
├── static/
│   ├── css/              # CSS3
│   │   ├── base.css
│   │   ├── buttons.css
│   │   ├── download.css
│   │   ├── forms.css
│   │   ├── links.css
│   │   ├── reset.css
│   │   ├── style.css
│   │   └── tables.css
│   └── js/               # JS
│       └── download.js
```

---

## 🛠️ Tecnologías utilizadas

- Python 3
- Flask - Web framework
- Colorama - Formateo de salida en consola
- HTML5/CSS3 - Frontend estático
- JavaScript - Lógica de descarga en cliente

---

## 💡 Ejemplo de uso (CLI)

```bash
python cli.py --ip 192.168.0.1 --mascara 255.255.255.0
```

```bash
python cli.py --ip 10.0.0.1 --mascara 16 --json
```

📝 Esto mostrará en consola los detalles de red y generará el archivo `resultadoNetCalc.json`.

---

## 🧪 Ejemplo de uso (Web)

Accede a `http://localhost:5000`.

Introduce:

- **IP:** 192.168.0.100
- **Máscara:** 255.255.255.0

Marca la casilla si deseas exportar en JSON.

¡Calcula y visualiza el resultado!

---

## 🧑‍💻 Contribuciones

¿Te gustaría mejorar NetCalc? ¡Toda contribución es bienvenida!

1. Haz un fork del repositorio.
2. Crea tu rama de feature: `git checkout -b feature/nueva-funcion`
3. Haz commit de tus cambios: `git commit -m 'Agrega nueva función'`
4. Haz push a tu rama: `git push origin feature/nueva-funcion`
5. Abre un Pull Request ✨

---

## 📝 Licencia

Este proyecto está licenciado bajo la [Licencia Creative Commons Atribución-NoComercial-CompartirIgual 4.0 Internacional](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es).

---

## 📫 Contacto

¿Tienes dudas o sugerencias? Puedes contactarme vía GitHub o dejar una Issue en el repositorio.

¡Gracias por usar NetCalc! 🎉
