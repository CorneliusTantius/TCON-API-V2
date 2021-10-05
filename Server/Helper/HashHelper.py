### Package Import ###
import base64
### AppCode Import ###


###############################################################################

def Encode(string):
    message_bytes = string.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    del message_bytes, base64_bytes
    return base64_message

###############################################################################

def Decode(string):
    base64_bytes = string.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    del base64_bytes, message_bytes
    return message

###############################################################################