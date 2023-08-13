import cv2 as cv
import math
import imutils

def crop_diagonal(x1,y1,x2,y2,x3,y3,x4,y4,img_path, img_save):
    ''' Initialize four coordinates to crop image, path to original image and path to save the cropped image
        x1,y1 is Top Left, x2,y2 is Top Right, x3,y3 is Bottom Right, x4,y4 is Bottom Left
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
    img = img[top_left_y:bot_right_y+1, top_left_x:bot_right_x+1]

    #Rotate the cropped image
    rotated_img = imutils.rotate_bound(img, angle)
    shape = rotated_img.shape

    # Recaculate the coordinates
    angle = (-angle*math.pi)/180
    b = math.ceil(origin_height/math.tan(math.pi/2-angle))
    a = math.ceil(math.sin(angle)*math.cos(angle)*origin_width)
    c = a + origin_height
    d = b + origin_width
    print(a,b,c,d)

    # Second crop:
    img = rotated_img[a:c,b:d]
    cv.imwrite(img_save, img)


img_path = "Path_to_original_image"
img_save = "Save_path_to_save_the_cropped_image"
# Example how to run: 
crop_diagonal(1457,1542,3235,1627,3229,1741,1452,1656,img_path, img_save)
# NOTE: Read the comment of the function to determine types of coordinate
