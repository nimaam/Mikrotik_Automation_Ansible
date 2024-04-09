import sys
import telnetlib

# Check for correct number of arguments
if len(sys.argv) != 4:
    print("Usage: python3 init_mikrotik.py <host> <username> <password>")
    sys.exit(1)

# Extract arguments
HOST = sys.argv[1]
user = sys.argv[2].encode('utf-8')  # Encoding to bytes as telnetlib expects bytes
password = sys.argv[3].encode('utf-8')
timeout = 20


# Commands to execute
commands = [
    b"/ip address add interface=ether1 address=192.168.12.254/24",
    b"/ip ssh set strong-crypto=yes host-key-size=2048 forwarding-enabled=both"
]

# Connect to the router
try:
    tn = telnetlib.Telnet(HOST, 23, timeout)
except Exception as e:
    print(f"Connection error: {e}")
    exit(1)

# Login
tn.read_until(b"Login: ")
tn.write(user + b"\r\n")

tn.read_until(b"Password: ")
tn.write(password + b"\r\n")

# Execute commands
for cmd in commands:
    tn.write(cmd + b"\r\n")
    # Wait for the command to execute; adjust sleep time as needed.
    tn.read_until(b">", timeout=timeout)

# Close the connection
tn.write(b"quit\r\n")
tn.close()

print("Commands executed successfully.")
