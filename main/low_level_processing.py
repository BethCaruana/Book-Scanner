from PIL import Image
import pnm_file_actions

#retrieve the image as an array
def get_array(file_name):
    #open the pnm file
    original_image = Image.open(file_name)
    #convert color images to greyscale
    grayscale_image = original_image.convert("L")
    #convert the image to an array
    image_array = pnm_file_actions.convert_image_to_array(grayscale_image)
    #return the array
    return image_array

#displays the pnm file image
def display(file_name):
    #open the pnm file
    original_image = Image.open(file_name)
    #display image
    pnm_file_actions.display_image(original_image)

#convert array back to an image
def get_image(modified_array, original_file):
    original_image = Image.open(original_file)
    width, height = original_image.size
    reconstructed_image = pnm_file_actions.convert_array_to_image(modified_array, width, height)
    return reconstructed_image

def save_image(image, file_name):
    #save the image to a file
    image.save(file_name)