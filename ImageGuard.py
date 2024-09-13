# python code for encryption 
# take path of image as a input 

path = r'C:\Users\91813\OneDrive\Desktop\code\IMAGE.jpg'
key = int(input('Enter Key for encryption of image: '))

print("The path of file : ", path)
print("key for encryption : ", key)

fin = open(path, 'rb')

image = fin.read()

fin.close()

image = bytearray(image)

for index, value in enumerate(image):
    image[index] = value ^ key

fin = open(path, 'wb')

fin.write(image)
fin.close()
print('Encryption completed successfully')

