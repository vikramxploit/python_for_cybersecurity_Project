# ===== Port Risk Analyser =====

open_ports = [21, 22, 80, 443, 3306, 8080, 23]

services = {
    21: "FTP", 22: "SSH", 23: "Telnet",
    80: "HTTP", 443: "HTTPS",
    3306: "MySQL", 8080: "HTTP-Alt"
}
high_risk = [21, 23, 3306]

risk_ports = []  # collect risky ones

print("=" * 42)
print("     🔍 PORT RISK ANALYSER REPORT")
print("=" * 42)

for port in open_ports:
    svc = services.get(port, "Unknown")
    if port in high_risk:
        print(f"  ⚠️  {port:5} | {svc:10} | HIGH RISK")
        risk_ports.append(port)
    else:
        print(f"  ✅  {port:5} | {svc:10} | safe")

print("=" * 42)
print(f"  Total open  : {len(open_ports)}")
print(f"  High risk   : {len(risk_ports)} ports → {risk_ports}")
print("=" * 42)
