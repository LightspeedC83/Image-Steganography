
from PIL import Image

image_name = "image.jpg"
base = Image.open(image_name)
image_pixels = base.getdata()

secret_message = "hello world"

#converting the secret message to 1s and 0s by converting each char to unicode integer to binary representation
#each unicode character has a maximum of 21 bits (the binary number will be 21 digits)
to_encode = ""
for char in secret_message:
    uni = "0"*(8-len(bin(ord(char))[2:])) + bin(ord(char))[2:]
    print(uni)
    print(chr(int(uni)))
encoded = []


output = Image.new(mode="RGB", size=base.size)
output.putdata(encoded)
output.save("output\\"+image_name)

# canvas_x, canvas_y = base.size