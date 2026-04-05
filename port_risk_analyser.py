# ===== Service Scanner =====

SERVICES = {
    21:"FTP", 22:"SSH", 23:"Telnet",
    25:"SMTP", 53:"DNS", 80:"HTTP",
    443:"HTTPS", 3306:"MySQL", 8080:"HTTP-Alt"
}
RISKY = [21, 23, 3306]

def identify(port):
    return SERVICES.get(port, "Unknown")

def risk_level(port):
    return "HIGH" if port in RISKY else "LOW"

def scan(ip, open_ports):
    print(f"\n{'='*45}")
    print(f"  🔍 TARGET: {ip}")
    print(f"{'='*45}")
    for port in open_ports:
        svc  = identify(port)
        risk = risk_level(port)
        icon = "⚠️ " if risk=="HIGH" else "✅"
        print(f"  {icon} {port:5} | {svc:10} | {risk}")
    print(f"{'='*45}\n")

# Run the scanner
scan("192.168.1.1", [22, 80, 21, 443, 3306])
