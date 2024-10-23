""""
1. Define firewall rules using dictionary
2. Simulate traffic using random IP numbers
3. Evaluate IP with rules + act (allow/block)
4. Output result of each evaluation
"""

import random

# Generates random IP address
def generate_random_ip(): 
    return f"192.168.1.{random.randint(0,20)}"

# Given ip address and dictionary of rules, return corresponding action
def check_firewall_rules(ip, rules):
    for rule_ip, action in rules.items():
        if ip == rule_ip:
            return action
    return "allow"

def main(): 
    # Match IP to block with action to take
    firewall_rules = {
        "192.168.1.1": "block",
        "192.168.1.4": "block",
        "192.168.1.9": "block",
        "192.168.1.13": "block",
        "192.168.1.16": "block",
        "192.168.1.19": "block",
    }

    # Simulate network traffic by generating 12 ip addresses
    # and checking them against the firewall rules.
    for _ in range(12):
        ip_address = generate_random_ip()
        action = check_firewall_rules(ip_address, firewall_rules)
        random_number = random.randint(0, 9999)
        print(f"IP: {ip_address}, Action: {action}, Random: {random_number}")

# Ensure when script is executed, main function is called
if __name__ == "__main__":
    main()