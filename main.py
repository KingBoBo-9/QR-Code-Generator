import qrcode

def get_user_choices():
    user_input = input('Enter the text or URL for the QR code: ')
    back_color = input('Background color? ')
    fill_color = input('Fill color? ')
    file_name = input('Enter the filename: ')
    return user_input, back_color, fill_color, file_name

def generate_qr_code(user_input, back_color, fill_color):
    qr = qrcode.QRCode(
        version=None,
        box_size=10,
        border=4,
    )

    qr.add_data(user_input)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    return img

def save_qr_code(image, file_name):
    image.save(file_name)
    print(f"QR code saved as {file_name}")

def main():
    user_input, back_color, fill_color, file_name = get_user_choices()
    generated_image = generate_qr_code(user_input, back_color, fill_color)
    save_qr_code(generated_image, file_name)

if __name__ == "__main__":
    main()
