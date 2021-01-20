import base64
import zlib

#Base64 Code
encoded = ""

#Decoding Process
decoded = base64.b64decode(encoded)
decompressed = zlib.decompress(decoded, -15) 

#Print Result | ShellCode
print(decompressed)
