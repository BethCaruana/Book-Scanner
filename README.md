# Book-Scanner

How to run the full program:

python text_scanner.py

Run the Segmentation (by itself):

python Segmentation.py

Run Sliding Window (by itself):

python sliding_window.py

Notes:
If you want to run your own image, take a photo of a book (textbook is likely to work) on a solid background with good lighting. Upload the image to the /Book-Scanner folder. Replace ACOMAF in the main function of text_scanner.py with the name of your file. Modify the window scale and stride length to fit your image (most scale values fall between .02 and .2 and stride values fall between .03 and .25). If your values are a good fit, it should pull up a search for the book. If this does not work, just run segmentation on the image to see if the words are making it through. If not, the image may not work for this program.
