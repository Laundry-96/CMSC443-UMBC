import hashlib
hashStr = "delauney"
r = 0
while hashlib.sha256(hashStr + str(r)).hexdigest()[0:5] != "00000":
    r += 1
fid = open("delauney.txt", 'w')
fid.write((hashStr+str(r)))
fid.close()
