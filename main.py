import qrcode


def get_user_choices():
    user_input = input('Enter the text or URL for the QR code: ')
    user_back_color = input('Background color? ')
    user_fill_color = input('Fill color? ')
    file_name = input('Enter the filename: ')
    
    return (user_input, user_back_color, user_fill_color, file_name)

def generate_QR_code(user_input, user_back_color, user_fill_color):
    qr = qrcode.QRCode(
        version=None,
        box_size=10,
        border=4,
    )

    qr.add_data(user_input)
    qr.make(fit=True)
    img = qr.make_image(fill_color=user_fill_color, back_color=user_back_color)
    type(img)

    return img

def save_QR_code(image, file_name):
    image.save(file_name)
    print(f"QR code saved as {file_name}")

def main():
    user_choices = get_user_choices()
    generated_image = generate_QR_code(user_choices[0], user_choices[1], user_choices[2])
    save_QR_code(generated_image, user_choices[3])

if __name__ == "__main__":
    main()
