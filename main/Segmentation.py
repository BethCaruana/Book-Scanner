import low_level_processing as llp
import numpy as np
#import matplotlib.pyplot as plt
from PIL import Image

def Segmentation(file_name):
    #get the array of pixels
    pixel_array = llp.get_array(file_name)

    #build the histogram
    histogram = [0] * 256
    for pixel_value in pixel_array:
        #increment each grey value in the histogram
        histogram[pixel_value] += 1
    #smooth the histogram
    histogram = smooth(histogram)
    #graph(histogram)
    #get global maxima and index value
    global_maxima,second_maxima = findMaxima(histogram)
    max_index = getIndex(histogram, global_maxima)

    #get second largest index value
    second_max_index = getIndex(histogram, second_maxima)

    #slice histogram to this range
    if(max_index < second_max_index):
        slice = histogram[max_index:second_max_index+1]
        #get the minimum value
        threshold = min(slice)
        threshold = thresholdIndex(histogram,max_index,second_max_index,threshold)
    else:
        slice = histogram[second_max_index:max_index+1]
        #get the minimum value
        threshold = min(slice)
        threshold = thresholdIndex(histogram, second_max_index, max_index, threshold)
    print("Threshold:" ,threshold)

    #if value above threshold set to white, otherwise set to black
    threshold_histogram = [0] * len(histogram)
    for z in range(len(histogram)):
        if (z > threshold):
            threshold_histogram[z] = 0
        else:
            threshold_histogram[z] = 255
    
    #convert histogram back to image
    for x in range(len(pixel_array)):
        temp = pixel_array[x]
        new_value = threshold_histogram[temp]
        pixel_array[x] = new_value
    
    pixel_array = np.array(pixel_array)

    return pixel_array

def findMaxima(histogram):
    temp = 0
    peaks = []
    
    maxima = max(histogram)
    minimum = min(histogram)
    threshold = (maxima - minimum) / 6
    #go through each value in half the histogram
    for x in range(len(histogram)):
        #if value gets larger replace
        if (histogram[x] >= temp):
            temp = histogram[x]
        #if smaller add previous to peaks
        else:
            peaks.append(temp)
            #reset temp
            temp = 0
    #get the max
    global_max = max(peaks)
    peaks.remove(global_max)
    #get the second peak
    second_peak = max(peaks)

    #choose a peak below certain threshold
    #prevent values from being too close
    while(second_peak > threshold):
        peaks.remove(second_peak)
        second_peak = max(peaks)

    return global_max, second_peak

def graph(histogram):
    plt.plot(histogram)
    plt.xlabel("gray level")
    plt.ylabel("frequency")
    plt.title("Histogram")
    plt.show()


def smooth(histogram):
    smooth_histogram = [0] * len(histogram)
    #go through eaach histogram value and apply mask
    for x in range(len(histogram)):
        indx_1 = x-2
        indx_2 = x-1
        indx_3 = x+1
        indx_4 = x+2
        total = histogram[x]
        if indx_1 >= 0 and indx_4 < len(histogram):
            total = 0
            total += histogram[indx_1] * (1/9)
            total += histogram[indx_2] * (2/9)
            total += histogram[x] * (3/9)
            total += histogram[indx_3] * (2/9)
            total += histogram[indx_4] * (1/9)
        smooth_histogram[x] = int(total)
    return smooth_histogram

def getIndex(histogram, value):
    #find the index for this value
    for i in range(len(histogram)):
        if(histogram[i] == value):
            return i
        
def thresholdIndex(histogram, start, end, value):
    #find index value in range of slice
    for i in range(start, end+1):
        if(histogram[i] == value):
            return i

def main():

    file_name = "potter.jpg"
    llp.display(file_name)
    final = Segmentation(file_name)
    results = llp.get_image(final, file_name)
    segment = "segmentation.pnm"
    llp.save_image(results, segment)
    llp.display(segment)
    
    with Image.open(segment) as img:
        img.convert("RGB").save("output.jpg")
    
if __name__ == "__main__":
    main()