import pandas as pd

## Assign variable to file
folder = r'C:\Users\jelle\Documents\Python\IP-translation'
laptops = pd.read_excel(rf'{folder}\laptops.xlsx')
sites = [1, 2, 4, 5, 6, 7, 8, 16]
devices = []
ip = 5
ip_adressen_op = 'ip adressen zijn op!!!'


class Device:
    def __init__(self, scopeid, mac, host, ip_addresses):
        self.scopeid = scopeid
        self.mac = mac
        self.host = host
        self.ip_addresses = ip_addresses

    def __str__(self):
        output = ''
        for index, ip_address in enumerate(self.ip_addresses):
            output += f'{scopeid},{self.host},{self.mac},{ip_address}'
            if index != len(self.ip_addresses)-1:
                output += '\n'
        return output

    def __repr__(self):
        return str(self)


for index, row in laptops.iterrows():
    scopeid = row['ScopeID']
    mac = row['MAC']
    host = row['HOST']
    ip_addresses = []
    for site in sites:
        #ip_addresses.append(f'10.0.{site}.{ip}')
        ip_addresses.append(f'10.{scopeid}.{site}.{ip}')
    device = Device(scopeid, mac, host, ip_addresses)
    devices.append(device)
    ip += 5
    if ip == 255:
        output_path = rf'{folder}\ip_adressen_zijn_op!!!.csv'
        with open(output_path, 'w+') as file:
            file.write(ip_adressen_op)
        break

csv_output = 'ScopeID,Name,ClientId,IPAddress\n'

for index, device in enumerate(devices):
    csv_output += str(device)
    if index < len(devices)-1:
        csv_output += '\n'

output_path = rf'{folder}\import.csv'
with open(output_path, 'w+') as file:
    file.write(csv_output)
