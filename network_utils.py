import ipaddress

def calcular_red(ip, mascara):
    try:
        if "/" in ip:
            red = ipaddress.IPv4Network(ip, strict=False)
        else:
            red = ipaddress.IPv4Network(f"{ip}/{mascara}", strict=False)

        hosts = list(red.hosts())

        clase = obtener_clase(red.network_address)
        tipo = "Privada" if red.network_address.is_private else "Pública"

        return {
            "ip": ip,
            "netmask": str(red.netmask),
            "cidr": f"/{red.prefixlen}",
            "network": str(red.network_address),
            "broadcast": str(red.broadcast_address),
            "first_host": str(hosts[0]) if hosts else "N/A",
            "last_host": str(hosts[-1]) if hosts else "N/A",
            "usable_hosts": len(hosts),
            "class": clase,
            "type": tipo
        }

    except Exception as e:
        return {"error": str(e)}

def obtener_clase(ip):
    first = int(str(ip).split(".")[0])
    if first < 128:
        return "A"
    elif first < 192:
        return "B"
    elif first < 224:
        return "C"
    elif first < 240:
        return "D"
    else:
        return "E"
