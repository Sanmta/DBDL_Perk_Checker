import cv2
import os
import numpy as np
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

# resize image to target shape (used to resize reference image to match ROI)
def resizeImage(image, target_image):
        return cv2.resize(image, (target_shape[1], target_shape[0]))

# search function
def search():
    main_image=cv2.imread('assets/test2.png') # for now loads static image, will add functionality to load image from user clipboard
    main_image_gray=cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY) # convert to grayscale

    rois = [
        (441, 312, 34, 34) # (x, y, width, height)
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


    for i, (x, y, w, h) in enumerate(rois):
        roi = main_image_gray[y:y+h, x:x+w]
        mse_result = 0
        ssim_result = 0
        for j, reference_image in enumerate(resized_reference_images):
            m, s = compareImages(roi, reference_image)
            print(f'ROI {i+1} vs Reference {reference_files[j]}: MSE={m}, SSIM={s}')
            if s > ssim_result:
                mse_result = m
                ssim_result = s
                best_match = j
        print(f'Best match for ROI {i+1}: Reference {reference_files[best_match]}')
        cv2.imwrite('assets/result.png', roi, [cv2.IMWRITE_PNG_COMPRESSION, 0])
        cv2.imwrite('assets/HighQualResult.png', reference_images[best_match], [cv2.IMWRITE_PNG_COMPRESSION, 0])
        cv2.imwrite('assets/lowQualResult.png', resized_reference_images[best_match], [cv2.IMWRITE_PNG_COMPRESSION, 0])
        
if __name__ == '__main__':
    search()