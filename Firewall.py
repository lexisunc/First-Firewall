import socket

def basic_firewall():
    # Create a socket to listen to incoming packets
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', 8888))  # Replace with your desired port and IP

    print("Basic Firewall is running...")

    while True:
        data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes, adjust as needed
        print("Received packet from:", addr)

        # Check if the packet is on port 80 (http) and drop if it is
        if addr[1] == 80:
            print("Blocking packet on port 80")
            coninue # Drop packets on port 80

        # Process the packet if it doesn't match the rule
        print("Packet allowed:", data.decode())

if __name__ == "__main__":
    basic_firewall()

from collections import defaultdict

# Simulated failed login attempts (IP addresses)
failed_logins = [
    '192.168.1.100',
    '192.168.1.101',
    '192.168.1.102',
    '192.168.1.100',
    '192.168.1.103',
    '192.168.1.101',
    '192.168.1.104',
    '192.168.1.100',
    '192.168.1.101',
    '192.168.1.105',
]

def print_color_text(text, color):
    colors = {
        'cyan': '\033[96m',
        'bold': '\033[1m',
        'underline': '\033[4m',
        'end': '\033[0m'
    }
    
    color_code = colors.get(color.lower())
    if color_code:
        print(f"{color_code}{text}{colors['end']}")
    else:
        print(f"Invalid color: {color}. Supported colors: {', '.join(colors.keys())}")

        # Check for failed login attempts exceeding a threshold of 2 and print the alert in cyan
def check_failed_logins(threshold):3
login_attempts = defaultdict(int)

for ip in failed_logins:
        login_attempts[ip] += 1

    suspicious_ips = [ip for ip, count in login_attempts.items() if
    count > threshold]

    if suspicious_ips:
        print_color_text("Alert - Suspicious activity detected:", "cyan")
        for ip in suspicious_ips:
            print_color_text(f"IP: {ip} - Failed login attempts: {login_attempts[ip]}", "cyan")

import random
import time

def print_color_text(text, color):
    colors = {
        'bright_yellow': '\033[93m',
        'bold': '\033[1m',
        'underline': '\033[4m',
        'end': '\033[0m'
    }
    
    color_code = colors.get(color.lower())
    if color_code:
        print(f"{color_code}{text}{colors['end']}")
    else:
        print(f"Invalid color: {color}. Supported colors: {', '.join(colors.keys())}")
        
def check_cpu_threshold(threshold):
    while True:
        # Simulate CPU usage (random values between 0 and 100)
        cpu_usage = random.randint(0, 100)

        if cpu_usage > threshold:
            print_color_text(f"Alert - High CPU Usage: {cpu_usage}%", "bright_yellow")
            # Add any action to take when the threshold is breached (e.g., send notification/email)
        
        # Simulate a delay between checks (in seconds)
        time.sleep(5)  # Adjust the interval as needed

        # Check for CPU usage exceeding a threshold of 90%
        check_cpu_threshold(threshold=90)

import logging
from logging.handlers import RotatingFileHandler

def print_color_text(text, color):
    colors = {
        'bright_blue': '\033[94m',
        'bold': '\033[1m',
        'underline': '\033[4m',
        'end': '\033[0m'
    }
    
    color_code = colors.get(color.lower())
    if color_code:
        print(f"{color_code}{text}{colors['end']}")
    else:
        print(f"Invalid color: {color}. Supported colors: {', '.join(colors.keys())}")

def configure_logging(log_file):
    # Create a logger
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)

    # Create a rotating file handler
    handler = RotatingFileHandler(log_file, maxBytes=10000, backupCount=5)
    handler.setLevel(logging.INFO)

    # Create a formatter and set it for the handler
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    return logger

def simulate_events(logger):
    # Simulating some events
    for i in range(5):
        logger.debug(f"Debug message {i}")
        logger.info(f"Info message {i}")
        logger.warning(f"Warning message {i}")
        logger.error(f"Error message {i}")
        logger.critical(f"Critical message {i}")

    # Configure logging and simulate events
    log_file = 'Lexis.log'
    logger = configure_logging(log_file)
    print_color_text("Logging and Reporting Configuration:", "bright_blue")
    simulate_events(logger)

def print_color_text(text, color):
    colors = {
        'bright_purple': '\033[95m',
        'bold': '\033[1m',
        'underline': '\033[4m',
        'end': '\033[0m'
    }
    
    color_code = colors.get(color.lower())
    if color_code:
        print(f"{color_code}{text}{colors['end']}")
    else:
        print(f"Invalid color: {color}. Supported colors: {', '.join(colors.keys())}")

def simulate_network_scan():
    # Simulating a network scan or probe
    for i in range(5):
        print_color_text(f"Probing network segment {i}", "bright_purple")

        # Simulate actions like sending network packets, scanning IP ranges, or checking ports
        time.sleep(3)  # Simulate a delay between probes (in seconds)

    # Simulate network scans or probes, printing alerts in bright purple
    print_color_text("Regular Network Scans or Probes:", "bright_purple")
    simulate_network_scan()
        
    # if addr[0] == '192.168.1.100':
    #     print("Blocking packet from IP:", addr[0])
    #     continue  # Drop packets from this IP
    # Process the packet if it doesn't match any rules
        print("Packet allowed:", data.decode())
