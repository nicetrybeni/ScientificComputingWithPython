passwordFile = open('secretPasswordFile.txt', 'r')
secretPassword = passwordFile.read()
passwordFile.close()

print('Enter your assword.')
typedPassword = input().strip()
if typedPassword == secretPassword:
    print('Access Granted')
elif typedPassword == '12345':
    print('That password is for BOBO')
else:
    print('Access Denied')