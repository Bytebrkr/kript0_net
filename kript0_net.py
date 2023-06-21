import socket
import ssl
import subprocess

target_host = input("Enter the target host: ")

# Check if the entered target_host is a valid IP address
try:
    socket.inet_aton(target_host)
except socket.error:
    print("Invalid IP address.")
    exit()

vulnerable_ports = {
    21: "FTP (File Transfer Protocol)",
    22: "SSH (Secure Shell)",
    23: "Telnet",
    25: "SMTP (Simple Mail Transfer Protocol)",
    53: "DNS (Domain Name System)",
    80: "HTTP (Hypertext Transfer Protocol)",
    110: "POP3 (Post Office Protocol version 3)",
    143: "IMAP (Internet Message Access Protocol)",
    443: "HTTPS (HTTP Secure)",
    3306: "MySQL Database",
    3389: "Remote Desktop Protocol (RDP)",
    5900: "Virtual Network Computing (VNC)"
}

def reverse_dns_lookup(ip_address):
    try:
        hostnames = socket.gethostbyaddr(ip_address)
        return hostnames[0]
    except socket.herror:
        return "N/A"

def validate_ssl_certificate(host, port):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((host, port)) as sock:
            with context.wrap_socket(sock, server_hostname=host) as secure_sock:
                cert = secure_sock.getpeercert()
                # Additional validation checks can be performed on the certificate
                return cert
    except ssl.SSLError:
        return None

def check_common_misconfigurations(port):
    if port == 21:
        # Check FTP misconfigurations
        try:
            with socket.create_connection((target_host, port)) as sock:
                sock.sendall(b"USER anonymous\r\n")
                response = sock.recv(1024).decode()
                if "230" in response:
                    print("Anonymous FTP access allowed.")
                else:
                    print("Anonymous FTP access not allowed.")
        except socket.error:
            print("Couldn't connect to FTP server.")

    elif port == 22:
        # Check SSH misconfigurations
        try:
            with socket.create_connection((target_host, port)) as sock:
                sock.sendall(b"SSH-2.0-OpenSSH_7.9p1 Debian-10+deb10u2\r\n")
                response = sock.recv(1024).decode()
                if "OpenSSH" in response:
                    print("OpenSSH banner detected.")
                else:
                    print("No OpenSSH banner detected.")
        except socket.error:
            print("Couldn't connect to SSH server.")

    elif port == 80 or port == 443:
        # Check web server misconfigurations
        try:
            with socket.create_connection((target_host, port)) as sock:
                sock.sendall(b"GET /robots.txt HTTP/1.1\r\nHost: example.com\r\n\r\n")
                response = sock.recv(1024).decode()
                if "Disallow:" in response:
                    print("Robots.txt file found. Directory listing might be disallowed.")
                else:
                    print("Robots.txt file not found.")
        except socket.error:
            print("Couldn't connect to web server.")

    else:
        # Add checks for other ports as needed
        pass

def perform_traceroute(target_host):
    try:
        traceroute_output = subprocess.check_output(['traceroute', target_host]).decode()
        print(f"\nTraceroute to {target_host}:")
        print(traceroute_output)
    except subprocess.CalledProcessError:
        print("Traceroute failed.")

def port_scanner(target_host):
    print("Kript0boi - Network Vulnerability Scanner")
    print("---------------------------------------")

    for port in vulnerable_ports:
        try:
            # Create a socket object
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Set a timeout value
            sock.settimeout(1)

            # Attempt to connect to the port
            result = sock.connect_ex((target_host, port))

            if result == 0:
                service_name = vulnerable_ports[port]
                reverse_dns = reverse_dns_lookup(target_host)
                print(f"Port {port} ({service_name}) is open. Potential vulnerability detected!")
                print(f"Reverse DNS lookup: {reverse_dns}")

                if port == 443:
                    cert = validate_ssl_certificate(target_host, port)
                    if cert:
                        print("SSL/TLS Certificate Information:")
                        print(cert)
                    else:
                        print("Invalid or self-signed certificate.")

                check_common_misconfigurations(port)

            # Close the socket
            sock.close()

        except KeyboardInterrupt:
            print("Port scanning stopped by user.")
            break

        except socket.error:
            print("Couldn't connect to server.")
            break

    # Perform traceroute
    perform_traceroute(target_host)

# Call the port_scanner function
port_scanner(target_host)
