import cv2 as cv
import math
import imutils
import numpy as np

def crop_diagonal(x1,y1,x2,y2,x3,y3,x4,y4,img_path, img_save, scale_h = 1, scale_w = 1):
    ''' Initialize four coordinates to crop image, path to original image and path to save the cropped image
        x1,y1 is Top Left, x2,y2 is Top Right, x3,y3 is Bottom Right, x4,y4 is Bottom Left
        scale_h and sclae_w are used to scale up height and width of image
    '''
    # Load the origin image
    img = cv.imread(img_path)
    #Computing angle to rotate if needed
    vector_line = (10, 0)
    vector_width = (x2-x1, y2-y1)
    vector_height = (x4-x1, y4-y1)
    dot_product = vector_line[0]*vector_width[0] + vector_line[1]*vector_width[1]
    len_line = 10
    len_diagonal = math.sqrt(vector_width[0]**2 + vector_width[1]**2)
    origin_width = math.ceil(len_diagonal)
    origin_height = math.ceil(math.sqrt(vector_height[0]**2 + vector_height[1]**2))
    # print(origin_height)
    # print(origin_width)
    angle = (math.acos(dot_product/(len_line*len_diagonal))/math.pi)*180
    if y1 < y2:
        angle = -angle
    # print(angle)
    #first crop:
    top_left_x = min([x1,x2,x3,x4])
    top_left_y = min([y1,y2,y3,y4])
    bot_right_x = max([x1,x2,x3,x4])
    bot_right_y = max([y1,y2,y3,y4])
    crop = img[top_left_y:bot_right_y+1, top_left_x:bot_right_x+1]

    #Rotate the cropped image
    rotated_img = imutils.rotate_bound(crop, angle)
    shape = rotated_img.shape
    # cv.imwrite(img_save, rotated_img)
    # Recaculate the coordinates
    angle = (abs(angle)*math.pi)/180
    if y2 < y1:
        angle = (math.pi/2) - angle
    b = math.ceil(math.sin(angle)*math.cos(angle)*origin_height)
    a = math.ceil(math.sin(angle)*math.cos(angle)*origin_width)
    c = a + origin_height
    d = b + origin_width
    print(a,b,c,d)

    # Second crop:
    crop = rotated_img[a:c,b:d]
    if scale_h != 1 or scale_w != 1:
        crop = cv.resize(crop, (int(origin_width*scale_w), int(origin_height*scale_h)))
    cv.imwrite(img_save, crop)
    
def normal_crop(x1,y1,x3,y3,img_path, img_save,scale_h = 1, scale_w = 1):
    '''
    x1,y1 is Top Left; x3,y3 is Bottom Right; img_path and img_save are path to load and save image
    scale_h and sclae_w are used to scale up height and width of image
    '''
    img = cv.imread(img_path)
    img_num = np.array(img)
    y3 = min(y3,len(img))
    y1 = max(y1,0)
    x3 = min(x3,len(img[0]))
    x1 = max(x1,0)
    w = x3 - x1
    h = y3 - y1
    crop = img[y1:y3, x1:x3]
    if scale_h != 1 or scale_w != 1:
        crop = cv.resize(crop, (int(w*scale_w), int(h*scale_h)))
    try:
        cv.imwrite(img_save, crop)
    except:
        print("Save error")

img_path = "Path_to_original_image"
img_save = "Save_path_to_save_the_cropped_image"
# Example how to run: 
crop_diagonal(1457,1542,3235,1627,3229,1741,1452,1656,img_path, img_save)
# NOTE: Read the comment of the function to determine types of coordinate
