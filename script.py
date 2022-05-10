from PIL import Image
import os
import pathlib
import time

#Characters used to build output text
#White to Black
# ASCII_Characters = ["@", "#", "%", "?", "*", "+", ";", ":", ",", ".", " "]
#Black to White
# ASCII_Characters = [" ", ".", ",", ":", ";", "+", "*", "?", "%", "#", "@"]

#Experimental (Limit Testing)
ASCII_Characters = [
" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
"'", "¨", "`", "´", "¸", ".", "·", "˜", "¯", "-", 
"’", "‘", "“", "”", ",", "„", "…", "•", "°", "¹",
"²", "³", "¬", "_", ":", ";", "‹", "›", "»", "~",
"=", "*", "^", "×", "+", "i", "l", 
"1", "!", "%", "#", "&", "$", "@"]

#Resizing image
# for full screen (new_width=200)
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

#Convert pixels into grayscale
def grayscaling(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)

#Convert pixels to a string of ASCII characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    # characters = "".join([ASCII_Characters[pixel//25] for pixel in pixels])
    #Experimental (Limit Testing)
    characters = "".join([ASCII_Characters[pixel//4] for pixel in pixels])
    return(characters)

def main(new_width=100):

    #Compare video
    # os.startfile(r'C:\Users\light\Desktop\ASCII Project\video.mp4')

    frame = 0
    for path in pathlib.Path("Bad Apple").iterdir():
    # for path in pathlib.Path("Hacking to the Gate").iterdir():
        if path.is_file():
            frame += 1
            #open image
            # path = input("Enter a valid pathname to an image:\n")
            path = "Bad Apple\BadApple" + str(frame) + ".jpg"
            # path = r"Hacking to the Gate\frame" + str(frame) + ".jpg"
            try:
                image = Image.open(path)
            except:
                print(path, "is not a valid pathname to an image.")

            #convert image to ASCII
            new_image_data = pixels_to_ascii(grayscaling(resize_image(image)))

            #format
            pixel_count = len(new_image_data)
            ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

            #print
            print(ascii_image)

            #save result to filename.txt
            with open("ascii.txt", "w+") as f:   
                f.write(ascii_image)
            #FPS cap
            time.sleep(1/6000)
main()
