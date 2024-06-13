from PIL import Image
import pytesseract
import numpy as np
import low_level_processing as llp
import webbrowser
import sliding_window as sw

#OCR takes image and converts text to a string
def text_scanner(filename, psm):
    img1 = np.array(Image.open(filename))
    text = pytesseract.image_to_string(img1, config=f' --psm {psm}') 
    return text 

#searches title in google
def search(title):
    search_url = "https://www.google.com/search?q="
    final_url = search_url + title.replace(' ', '+')
    webbrowser.open(final_url)
 

def main():
    #put file name here
    file_name = "ACOMAF.jpg"
    #file_name = "crown.jpg"
    llp.display(file_name)
    #send file name with scale factor and stride
    binary_array = sw.sliding_window(file_name, .11, .03)
    #binary_array = sw.sliding_window(file_name, .02, .03)
    results = llp.get_image(binary_array, file_name)
    window = "sliding_window.pnm"
    llp.save_image(results, window)
    llp.display(window)
    #PSM=11 find as much text as possible no particular order
    title = text_scanner(window, psm=11)
    #search the title on google
    search(title)
    print(title)

if __name__ == "__main__":
    main()