from pymodbus.client import ModbusTcpClient

# Adresa IP și portul serverului Modbus TCP/IP
SERVER_IP = '192.168.0.40'
SERVER_PORT = 502

# Creează un client Modbus TCP/IP
client = ModbusTcpClient(SERVER_IP, SERVER_PORT)

# Conectează-te la server
client.connect()

# Exemple de operații Modbus
# Citirea unei valori din registrul de intrare
result = client.read_input_registers(address=136, count=1, unit=1)
if result.isError():
    print('Eroare:', result)
else:
    print('Valoare citită:', result.registers)

# Scrierea unei valori în registrul de ieșire
result = client.write_registers(address= 134, values= 1, unit=1)
if result.isError():
    print('Eroare:', result)
else:
    print('Valori scrise cu succes.')

# Deconectează-te de la server
client.close()
