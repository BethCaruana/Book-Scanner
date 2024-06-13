from PIL import Image
from Segmentation import Segmentation
import numpy as np
import low_level_processing as llp

def sliding_window(image, scale_factor, stride):
    #open image get width and height
    img = Image.open(image)
    width, height = img.size
    
    #get the segmented version of the image
    binary_array = Segmentation(image)
    binary_array = np.reshape(binary_array, (height, width))
    #initialize an array of the image size with 0
    temp_array = np.zeros_like(binary_array)

    #calculate the window size
    window_size = int(min(height, width) * scale_factor)
    size = window_size * window_size

    #calculate the stride
    stride = int(stride*window_size)
    
    #visit each window 
    for y in range(0, height - window_size+1, stride):
        for x in range(0, width - window_size+1, stride):
            window = binary_array[y:y+window_size, x:x+window_size]  
            #calculate ratio for the window
            white_space = extract_features(window)
            percentage = white_space / size
            #check if the window contains a character
            if 0.86 <= percentage and percentage <= .96:
                #set all values in the window to 1
                temp_array[y:y+window_size, x:x+window_size] = 1
                
    #keep image anywhere 1 and set to white if 0
    for z in range(height):
        for s in range(width):
            if(temp_array[z][s] == 1):
                temp_array[z][s] = binary_array[z][s]
            else:
                temp_array[z][s] = 255
    
    return temp_array.flatten()
            

#count white space in image
def extract_features(window):
    white_space = np.count_nonzero(window)
    return white_space

def main():
    image = "ACOMAF.jpg"
    binary_array = sliding_window(image,.11,.03)
    results = llp.get_image(binary_array, image)
    window = "sliding_window.pnm"
    llp.save_image(results, window)
    llp.display(window)
    
if __name__ == "__main__":
    main()
