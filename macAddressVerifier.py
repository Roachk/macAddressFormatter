def macAddressCleaner(macAddress):
    macAddressList = []
    macAddressList[:0] = macAddress
    if ':' # https://thispointer.com/python-how-to-check-if-an-item-exists-in-list-search-by-value-or-condition/
    macAddressList.remove(':')
    macAddressList.remove('.')
    macAddressList.remove('-')
    print(macAddressList)
    
            
print('Enter MAC Address: ')
macAddress = input()
macAddressCleaner(macAddress)
