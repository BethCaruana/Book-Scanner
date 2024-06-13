from PIL import Image

def display_image(image):
    #display the image
    image.show()

def convert_image_to_array(image):
    #load image data into an array
    return list(image.getdata())

def convert_array_to_image(array, width, height):
    #create gray scale image of same width and height
    image = Image.new("L", (width, height))
    image.putdata(array)
    return image

if __name__ == "__main__":
    #open the PNM file
    pnm_file = "auto.pnm"
    original_image = Image.open(pnm_file)

    #display the original image
    display_image(original_image)

    #convert the image to an array
    image_array = convert_image_to_array(original_image)

    #convert the array back to the original image
    width, height = original_image.size
    reconstructed_image = convert_array_to_image(image_array, width, height)

    #display the reconstructed image
    display_image(reconstructed_image)
