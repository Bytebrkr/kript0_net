#Kript0_net - Network Vulnerability Scanner
Kript0boi is a Python script designed to scan a target network for potential vulnerabilities and security risks. It provides a set of features to help identify open ports, perform reverse DNS lookup, validate SSL/TLS certificates, check for common misconfigurations, and perform network traceroute.

#Features
Port Scanning: The script scans a range of ports on the target host to identify open ports. It displays the open ports along with their associated services.

Reverse DNS Lookup: For each open port, the script performs a reverse DNS lookup to retrieve the hostnames associated with the IP address. This provides additional information about the target network.

SSL/TLS Certificate Validation: If an open port 443 (HTTPS) is detected, the script attempts to establish a secure connection and validate the SSL/TLS certificate. It performs basic validation checks and notifies if the certificate is invalid or self-signed.

Common Misconfigurations: The script includes checks for common misconfigurations on specific ports. It provides examples of checks for FTP, SSH, and web servers (HTTP/HTTPS). You can customize these checks or add additional checks based on your specific requirements.

Network Traceroute: After scanning the ports, the script performs a traceroute to the target host to analyze the network path. It displays the traceroute output, helping to identify network issues or bottlenecks.

#Usage
Run the script by executing the following command: python kript0_net.py.

Enter the target host IP address or hostname when prompted.

The script will perform a port scan and display the results, including open ports, reverse DNS lookup, SSL/TLS certificate information (if applicable), and common misconfigurations (if detected).

After the port scan, the script will perform a network traceroute and display the traceroute output.

#Requirements
Python 3.x
Socket module
SSL module
Subprocess module
Disclaimer
This script is intended for educational and security research purposes only. Use it responsibly and with proper authorization. The author and contributors are not responsible for any misuse or damage caused by this script. Always comply with all legal and ethical guidelines when conducting network security assessments.

#License
This project is licensed under the MIT License.

Feel free to customize and enhance the script based on your specific requirements and use case.

