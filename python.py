import ipaddress

# Ouvrir le fichier "subnet.txt" en mode lecture
with open("subnet.txt", "r") as f:
    subnets = f.readlines()

# Créer une liste pour stocker toutes les adresses IP
all_ips = []

# Boucle sur tous les blocs CIDR
for subnet in subnets:
    subnet = subnet.strip()  # supprimer les espaces blancs et les caractères de nouvelle ligne
    network = ipaddress.ip_network(subnet)
    
    # Ajouter toutes les adresses IP du bloc à la liste "all_ips"
    for ip in network.hosts():
        all_ips.append(str(ip))

# Ouvrir le fichier "ip.txt" en mode écriture et écrire toutes les adresses IP
with open("ip.txt", "w") as f:
    for ip in all_ips:
        f.write(ip + "\n")
