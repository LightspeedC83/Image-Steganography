
from PIL import Image

image_name = "tiger.jpg"
base = Image.open(image_name)
image_pixels = base.getdata()

secret_message = "hello world"

#converting the secret message to 1s and 0s by converting each char to unicode integer to binary representation
#each unicode character has a maximum of 21 bits (the binary number will be 21 digits)
to_encode = ""
for char in secret_message:
    uni = "0"*(8-len(bin(ord(char))[2:])) + bin(ord(char))[2:]
    if len(bin(ord(char))[2:]) > 8:
        print("character with too long encoding: " + char)
    to_encode += uni


if len(image_pixels)*3 < len(to_encode):
    print("The message is too long / the image is too small")

encoded = []
for pixel in image_pixels:
    to_append = []
    for val in pixel:
        try:
            if to_encode[0] == "0": # if we want to encode a 0 (the pixel value needs to be even)
                if val %2 == 1: # if the actual pixel value is odd we decrease it by 1
                    to_append.append(val-1)
                else: # if the actual pixel value is even we do nothing
                    to_append.append(val)
            else: # if we want to encode a 1 (the pixel value needs to be be odd)
                if val %2 == 0: # if the acual pixle value is even, we increase it by 1
                    to_append.append(val+1)
                else: # if the acutal pixel value is odd we do nothing
                    to_append.append(val)
            to_encode = to_encode[1:]
        except IndexError:
            to_append.append(val)
    encoded.append(tuple(to_append))

output = Image.new(mode="RGB", size=base.size)
output.putdata(encoded)
output.save("output\\secret_"+image_name)



# code that decodes an image

image_name = "output\\secret_tiger.jpg"
base = Image.open(image_name)
image_pixels = base.getdata()

to_decode = ""
for pixel in image_pixels:
    for val in pixel:
        if val %2 ==0: # if a pixel value is even, it is read as a 0
            to_decode += "0"
        else: # if a pixel value is odd, it is read as a 1
            to_decode += "1"
    
decoded = ""
print("decoding")
while len(to_decode) > 0:
    decoded += chr(int(to_decode[0:8], 2))
    to_decode = to_decode[8:]

print("writing")
with open("output\\decoded.txt", "w") as f:
    for x in decoded:
        try:
            f.write(x)
        except UnicodeEncodeError:
            pass
        
print('done')