import qrcode

user_input = input('Enter the text or URL for the QR code: ')
user_back_color = input('Background color? ')
user_fill_color = input('Fill color? ')
file_name = input('Enter the filename: ')

qr = qrcode.QRCode(
    version = None,
    box_size = 10,
    border = 4,
)

qr.add_data(user_input)
qr.make(fit = True)

img = qr.make_image(fill_color = user_fill_color, back_color= user_back_color)
type(img)
img.save(file_name)

print(f'QR code saved as {file_name}')

