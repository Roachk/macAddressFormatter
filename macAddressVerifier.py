def macAddressCleaner(macAddress):
    macAddress = macAddress.lower() 
    macAddressList = []
    macAddressList[:0] = macAddress #Adds characters in macAddress to a list

    while ':' in macAddressList or '-' in macAddressList or '.' in macAddressList: #This loops while the delimiters are detected in the macAddressList. Once a delimitter is detected it is removed via the if/elif statement
        if ':' in macAddressList:
            macAddressList.remove(':')
        elif '-' in macAddressList:
            macAddressList.remove('-')
        elif '.' in macAddressList:
            macAddressList.remove('.')
    if len(macAddressList) != 12: #Checks the length of the MAC Address to make sure its 12 characters
        print('MAC Addresses must contain 12 Alpha Numeric characters')
        return
    for char in macAddressList:
        if char.isalnum(): #chacks if character in mac addresslist is alphanumer
            print(char + ' is gucci!')
            if char.isalpha() == True: #nested if that activates if the char is ALPHA
                if ord(char) >= 97 and ord(char) <= 102: #checks if ALPHA is  between the letters lower case a - f
                    print(char + ' is a valid character')
                else:
                    print(char + ' is not a valid character')
                    return
        else:
            print(char + ' is not a valid MAC Address character')
            return
while True:
    print('Enter MAC Address: ')
    macAddress = input()
    print('Please choose a delimiter (, or : or -)')
    delimiter = input()
    macAddressCleaner(macAddress)
