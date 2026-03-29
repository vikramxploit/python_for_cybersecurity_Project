# ===== IP Address Analyser =====

ip = "  192.168.10.55  "   # messy input (spaces)

# Step 1: Clean the input
ip = ip.strip()

# Step 2: Split into octets
octets = ip.split(".")

# Step 3: Analyse
first  = octets[0]
last   = octets[-1]
total  = len(octets)
is_private = ip.startswith("192.168") or ip.startswith("10.")

# Step 4: Display the report
print("=" * 38)
print("     🔍  IP ADDRESS ANALYSER")
print("=" * 38)
print(f"  Full IP       : {ip}")
print(f"  All Octets    : {octets}")
print(f"  First Octet   : {first}")
print(f"  Last Octet    : {last}")
print(f"  Total Octets  : {total}")
print(f"  Private IP?   : {is_private}")
print(f"  Reversed IP   : {ip[::-1]}")
print("=" * 38)
