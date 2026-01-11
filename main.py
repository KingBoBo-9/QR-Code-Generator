import qrcode 

user_input = input('Enter the text or URL for the QR code: ')
file_name = input('Enter the filename: ')

img = qrcode.make(user_input)
type(img)
img.save(file_name)