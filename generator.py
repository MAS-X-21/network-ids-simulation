import random
from datetime import datetime, timedelta
import pandas as pd
import numpy as np

def generate_synthetic_traffic(num_records=500):
    """
    Generates synthetic network flow records containing both normal traffic
    and simulated attack patterns (Port Scans, Brute Force, Data Exfiltration).
    """
    protocols = ['TCP', 'UDP', 'ICMP', 'HTTPS', 'HTTP']
    normal_services = [80, 443, 53, 22, 3306]
    attack_ports = [4444, 31337, 6667, 1337, 0]
    
    internal_ips = [f"192.168.1.{i}" for i in range(10, 50)]
    external_ips = [
        "203.0.113.45", "198.51.100.23", "45.33.32.156", 
        "185.199.108.153", "192.0.2.10", "104.244.42.1"
    ]
    
    records = []
    base_time = datetime.now() - timedelta(hours=2)
    
    for i in range(num_records):
        timestamp = base_time + timedelta(seconds=random.randint(1, 7200))
        src_ip = random.choice(internal_ips)
        dst_ip = random.choice(external_ips)
        proto = random.choice(protocols)
        
        attack_type = random.choices(
            ['Normal', 'Port_Scan', 'Brute_Force', 'Data_Exfiltration'],
            weights=[0.80, 0.07, 0.08, 0.05],
            k=1
        )[0]
        
        if attack_type == 'Port_Scan':
            dst_port = random.choice(attack_ports)
            packet_count = random.randint(500, 2000)
            byte_count = random.randint(10000, 50000)
            duration = round(random.uniform(0.1, 1.5), 2)
            flags = "SYN"
        elif attack_type == 'Brute_Force':
            dst_port = 22 if proto == 'TCP' else random.choice(normal_services)
            packet_count = random.randint(150, 400)
            byte_count = random.randint(8000, 25000)
            duration = round(random.uniform(10.0, 45.0), 2)
            flags = "RST/ACK"
        elif attack_type == 'Data_Exfiltration':
            dst_port = 443
            packet_count = random.randint(3000, 10000)
            byte_count = random.randint(500000, 5000000)
            duration = round(random.uniform(60.0, 300.0), 2)
            flags = "PSH/ACK"
        else:
            dst_port = random.choice(normal_services)
            packet_count = random.randint(5, 50)
            byte_count = random.randint(500, 8000)
            duration = round(random.uniform(0.5, 10.0), 2)
            flags = "ACK"
            
        records.append({
            'timestamp': timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'src_ip': src_ip,
            'dst_ip': dst_ip,
            'protocol': proto,
            'dst_port': dst_port,
            'packet_count': packet_count,
            'byte_count': byte_count,
            'duration': duration,
            'flags': flags,
            'label': attack_type
        })
        
    df = pd.DataFrame(records)
    return df
