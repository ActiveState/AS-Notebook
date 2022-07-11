import hashlib


#enter a project location (path to YAML) and get its file location by sha1 hash
def getCachedRuntimeHash(pathToRuntimeYaml):
    bytes = str.encode(pathToRuntimeYaml) #convert to bytees
    #Only 4 LS bytes each hexadecimal charachter is 4 bits. 8x4 = 32 bit 
    return hashlib.sha1(bytes).hexdigest()[:8]


    