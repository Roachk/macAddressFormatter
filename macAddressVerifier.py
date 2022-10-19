def macAddressCleaner(macAddress, delimiter, spaces):
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
            #print(char + ' is gucci!')
            if char.isalpha() == True: #nested if that activates if the char is ALPHA
                if ord(char) >= 97 and ord(char) <= 102: #checks if ALPHA is  between the letters lower case a - f
                    #print(char + ' is a valid character')
                    continue
                else:
                    print(char + ' is not a valid character')
                    return
        else:
            print(char + ' is not a valid MAC Address character')
            return
    if ord(delimiter) == 58 or ord(delimiter) == 46 or ord(delimiter) == 45: #This if statement checks if you're using a valid delimiter
        #print(delimiter +  ' is a valid delimiter')
        if spaces == "2": #This if will then insert users selecte3d delimitter into the MAC List every 2 spaces
            #print('You picked every 2 spaces')
            macAddressList.insert(2, delimiter)
            macAddressList.insert(5, delimiter)
            macAddressList.insert(8, delimiter)
            macAddressList.insert(11, delimiter)
            macAddressList.insert(14, delimiter)
            #print(macAddressList)
        elif spaces == "4":
            #print('You picked every 4 spaces')
            macAddressList.insert(4, delimiter)
            macAddressList.insert(9, delimiter)
            #print(macAddressList)
        else:
            print('Please choose either 2 or 4 characters')
            return
    else:
        print(delimiter + ' is not a valid delimiter')
        return
    return ''.join(macAddressList)

if __name__ == "__main__":
    while True:
        print('Enter MAC Address: ')
        macAddress = input()
        print('Please choose a delimiter (. or : or -)')
        delimiter = input()
        print('Place a delimitter every 2 or 4 characters?')
        spaces = input()
        cleanedMacAddress = macAddressCleaner(macAddress, delimiter, spaces)
        print(cleanedMacAddress)
