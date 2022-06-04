import socket
from pymodbus.server.sync import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

import random

def run_server(server_ip_address,server_port,rand_dict):
    store = ModbusSlaveContext(
        ir=ModbusSequentialDataBlock(rand_dict["rand_start_adress"], rand_dict["rand_values"]), 
        # zero_mode=True
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


# --------- reate Random Block Of Memory To Fill Values ---------
rand_start_adress = 30001
rand_length = 100
rand_values = [random.randint(1,1024) for i in range(rand_length)]
rand_dict = {"rand_start_adress":rand_start_adress,"rand_length":rand_length,"rand_values":rand_values}
print(f"[+]Info : rand_start_adress:{rand_start_adress}")
print(f"[+]Info : rand_values:{rand_values}")

run_server(server_ip_address,server_port,rand_dict)


