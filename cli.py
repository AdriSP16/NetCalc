import os
import json
import argparse
from colorama import Fore, Style, init # type: ignore
from network_utils import calcular_red

# Inicializamos colorama para que funcione en Windows
init(autoreset=True)

def get_download_path():
    """Devuelve la ruta a la carpeta de Descargas del usuario."""
    if os.name == 'nt':  # Windows
        return os.path.join(os.environ['USERPROFILE'], 'Downloads')
    else:  # Linux, macOS
        return os.path.join(os.path.expanduser('~'), 'Downloads')

def run_cli(ip, mascara, export_json):
    """Ejecuta el cálculo en la línea de comando con estilo"""
    try:
        if not ip:
            raise ValueError(f"{Fore.RED}La dirección IP es obligatoria.{Style.RESET_ALL}")

        print(f"{Fore.CYAN}Iniciando el cálculo para IP: {ip} y Máscara: {mascara}...{Style.RESET_ALL}")
        resultado = calcular_red(ip, mascara)

        if export_json:
            # Guardamos el resultado en la carpeta de Descargas
            download_path = get_download_path()
            json_path = os.path.join(download_path, 'resultadoNetCalc.json')

            with open(json_path, 'w') as f:
                json.dump(resultado, f, indent=4)

            print(f"{Fore.GREEN}Archivo JSON generado en: {json_path}{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}Resultado:{Style.RESET_ALL}")
            print(json.dumps(resultado, indent=4))

    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    # Configurar el argumento de la línea de comandos
    parser = argparse.ArgumentParser(description="Calculadora de redes IP")
    parser.add_argument("--ip", type=str, help="Dirección IP", required=False)
    parser.add_argument("--mascara", type=str, help="Máscara de subred", required=False)
    parser.add_argument("--json", action="store_true", help="Exportar el resultado como archivo JSON")

    args = parser.parse_args()

    # Ejecutamos la lógica de la CLI
    run_cli(args.ip, args.mascara, args.json)