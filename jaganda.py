crypted = "PHYJSLYDDQFDZXGASGZZQQEHXGKFNDRXUJUG"
mask = "432513432513432513432513432513432513432513432513432513"

message = ''.join([chr(ord(crypted[i])-int(mask[i]))
                   for i in range(len(crypted))])

print(message)

message = 'LEVERITABLEAUTEURDUVOLDEDIAMANTSEST'
crypted = ''.join([chr(ord(message[i])+int(mask[i]))
                   for i in range(len(message))])
print(crypted)

# activité 18 page 37
message = 'VOICILAPORTEOUSETROUVELACLE'
mask = 'KEY'*100
crypted = ''.join([
    chr(
        (
            ord(message[i]) - ord('A') +
            ord(mask[i]) - ord('A')
        ) % 26 + ord('A')
    ) for i in range(len(message))
])
print(message)
print(mask[0:len(message)])
print(crypted)

# activité 18 page 37
message = 'VOIRUNESEULEFOISVAUTMIEUXQUEDENTENDRECENTFOIS'
mask = 'CHINA'*100
crypted = ''.join([
    chr(
        (
            ord(message[i]) - ord('A') +
            ord(mask[i]) - ord('A')
        ) % 26 + ord('A')
    ) for i in range(len(message))
])
print(message)
print(mask[0:len(message)])
print(crypted)
