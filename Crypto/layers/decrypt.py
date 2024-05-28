from pwn import *

def get_encrypted_flag():
    # Kết nối đến server
    conn = remote('challs.actf.co', 31398)

    # Chọn mục 3 để lấy flag đã bị mã hóa
    conn.recvuntil(b'> ')
    conn.sendline(b'3')

    # Nhận flag đã mã hóa (in hex)
    encrypted_flag_hex = conn.recvline().strip().decode()
    conn.close()

    return encrypted_flag_hex

def get_decrypted_output(encrypted_flag_hex):
    # Kết nối lại đến server
    conn = remote('challs.actf.co', 31398)

    # Chọn mục 2
    conn.recvuntil(b'> ')
    conn.sendline(b'2')

    # Gửi flag đã mã hóa
    conn.recvuntil(b'> ')
    conn.sendline(encrypted_flag_hex.encode())

    # Nhận output
    decrypted_output_hex = conn.recvline().strip().decode()
    conn.close()

    return decrypted_output_hex

def main():
    # Bước 1: Lấy flag đã mã hóa
    encrypted_flag_hex = get_encrypted_flag()
    print(f"Encrypted flag (hex): {encrypted_flag_hex}")

    # Bước 2: Gửi flag đã mã hóa và nhận output
    decrypted_output_hex = get_decrypted_output(encrypted_flag_hex)
    print(f"Decrypted output (hex): {decrypted_output_hex}")

    # Bước 3: Chuyển đổi output thành bytes
    decrypted_output_bytes = bytes.fromhex(decrypted_output_hex)
    print(f"Decrypted output (bytes): {decrypted_output_bytes}")

if __name__ == '__main__':
    main()
