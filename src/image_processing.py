import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim




# compute mean squared error (MSE) between two images (average squared difference per pixel)
def mse(imageA, imageB):
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err

# compare two images using MSE and SSIM
def compareImages(imageA, imageB):
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB)
    return m, s

# search function
def search(end_screen):
    # convert the image to grayscale
    end_screen_gray=cv2.cvtColor(end_screen, cv2.COLOR_BGR2GRAY)

    # define the list of ROIs using nested loops
    rois = [
        ((37 * j) + 441, (79 * i) + 312, 34, 34) if j == 1 else ((37 * j) + 442, (79 * i) + 312, 34, 34)  # (x, y, width, height)
        for i in range(4)  # Loop for survivors
        for j in range(4)  # Loop for perks
    ]

    # performed testing with standard pngs, then with pngs along with perk backgrounds, however the accuracy was low
    reference_files = os.listdir('assets/jpgPerks') # get list of reference jpegs (pngs seem to have a lower accuracy)
    reference_images = [
        cv2.imread(os.path.join('assets/jpgPerks', file_name), cv2.IMREAD_GRAYSCALE) # load reference images in grayscale
        for file_name in reference_files
    ]
    
    #  resize reference images so they match the size of the ROIs (34x34)
    resized_reference_images = [
        cv2.resize(cv2.imread(os.path.join('assets/jpgPerks', file_name), cv2.IMREAD_GRAYSCALE), (34, 34))
        for file_name in reference_files
    ]

    recognisedPerks = [] # list to store recognised perks
    
    for i, (x, y, w, h) in enumerate(rois):
        # get the region of interest (ROI) from the main image
        roi = end_screen_gray[y:y+h, x:x+w]

        # apply thresholding to make black colors blacker
        _, thresholded_roi = cv2.threshold(roi, 106, 255, cv2.THRESH_BINARY) 

        # default values for best mse and best ssim
        mse_result = 0 # CURRENTLY UNUSED FOR COPARISON BUT HERE IN CASE NEEDED LATER
        ssim_result = 0

        # compare all images in the reference list to the current ROI
        for j, reference_image in enumerate(resized_reference_images):
            threshold_needed = False # flag to indicate if thresholding is needed (essentially, "is it an eye perk?")
            m, s = compareImages(roi, reference_image)

            if s > ssim_result: # if the ssim value is greater than the current best ssim value, set new best match
                mse_result = m
                ssim_result = s
                best_match = j
                # print(f'MSE: {mse_result}, SSIM: {ssim_result} for {reference_files[j]}')

        # if the best match is an eye perk, apply thresholding to the ROI and compare again as they are harder to match
        if "DejaVu" in reference_files[best_match] or "ObjectOfObsession" in reference_files[best_match] or "DarkSense" in reference_files[best_match] or "Kindred" in reference_files[best_match]:
            threshold_needed = True # flag to indicate that thresholding is needed
            cv2.imwrite('testing/test5/threshold.png', thresholded_roi, [cv2.IMWRITE_PNG_COMPRESSION, 0]) # save thresholded ROI for debugging
            
            # new default values for best mse and best ssim for thresholded image
            ssim_result_threshold = 0
            mse_result_threshold = 0
            for k, reference_image in enumerate(resized_reference_images):
                n, r = compareImages(thresholded_roi, reference_image) # compare thresholded ROI to reference image

                if r > ssim_result_threshold:
                    mse_result_threshold = n
                    ssim_result_threshold = r
                    best_match_threshold = k
                    #print(reference_files[best_match_threshold])
                    
        # write to files for debugging, will be removed in final version
        file_name = 'testing/test5/test5Perk'+ str(i) +'.png'
        cv2.imwrite(file_name, roi, [cv2.IMWRITE_PNG_COMPRESSION, 0])
        cv2.imwrite('testing/test5/test5HighQualRef.png', reference_images[best_match], [cv2.IMWRITE_PNG_COMPRESSION, 0])
        cv2.imwrite('testing/test5/test5LowQualRef.png', resized_reference_images[best_match], [cv2.IMWRITE_PNG_COMPRESSION, 0])
        if threshold_needed == True:
           print(f'Best match for ROI {i+1}: Reference {reference_files[best_match_threshold]}')
           recognisedPerks.insert(i, reference_files[best_match_threshold])
        else: 
            print(f'Best match for ROI {i+1}: Reference {reference_files[best_match]}')
            recognisedPerks.insert(i, reference_files[best_match])    
    return recognisedPerks
        
        
if __name__ == '__main__':
    search()