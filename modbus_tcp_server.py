import socket
from pymodbus.server.sync import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext


def run_server(server_ip_address,server_port):
    store = ModbusSlaveContext(
        zero_mode=True
    )
    context = ModbusServerContext(slaves=store, single=True)
    StartTcpServer(context, address=(server_ip_address, server_port))

    
hostname = socket.gethostname()    
server_ip_address = socket.gethostbyname(hostname)
server_port = 502   # MTF default modbus tcp port

store = ModbusSlaveContext(zero_mode=True)
context = ModbusServerContext(slaves=store, single=True)


print(f"[+]Info : hostname:{hostname}")
print(f"[+]Info : server_ip_address:{server_ip_address}")
print(f"[+]Info : server_port:{server_port}")

run_server(server_ip_address,server_port)


