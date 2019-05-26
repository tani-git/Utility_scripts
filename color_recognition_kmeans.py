import numpy as np
import cv2
import webcolors
import matplotlib.pyplot as plt


def Color_Recognition_Kmeans(image_cropped):
        '''
        recognize the main color of the given box, input is box coordinate(x,y,w,h),return is color
        using kemans to cluster domianant color of a given box

        ''' 

        print('Color Recognition.....')
        print(image_cropped.shape)
        
       # tic = time.time()

        #reshape image from [X][Y][3] to [X*Y,3]


        print(image_cropped.shape)
        # img_reshape = np.array([img.reshape((-1,3)) for img in image_cropped])
        img_reshape = image_cropped.reshape((-1,3))
        print(img_reshape.shape)

        #reshape numpy 2D array to 1D array
        # pixels_flat = np.concatenate(img_reshape)
        # pixels_flat = img_reshape.ravel()
        #change to float
        # pixels_flat = np.float32(pixels_flat)
        pixels_flat = np.float32(img_reshape)
        
        # define criteria, number of clusters(K) and apply kmeans()
        # Define criteria = ( type, max_iter = 10 , epsilon = 1.0 )
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        K = 3
        ret,label,center=cv2.kmeans(pixels_flat,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

        #change to unit center
        center = np.uint8(center)

        #a list
        center = [tuple([int(c) for c in color]) for color in center]

        #return unique class label of an array and its coming counts
        l,c = np.unique(label,return_counts=True)

        #sorting list (l, c),reverse it from high to low
        order = sorted(zip(c,l),reverse=True)

        #just show class label in order
        order = [l for c,l in order]

        #convert list to array in order, then to list
        center = np.asarray(center)[order].tolist()


        for index, RGB_value in enumerate(center):

            print (index, RGB_value)

            requested_colour =RGB_value

            try:

                closest_name = webcolors.rgb_to_name(requested_colour)

            except ValueError:

                min_colours = {}

                for key, name in webcolors.css3_hex_to_names.items():
                    r_c, g_c, b_c = webcolors.hex_to_rgb(key)
                    rd = (r_c - requested_colour[0]) ** 2
                    gd = (g_c - requested_colour[1]) ** 2
                    bd = (b_c - requested_colour[2]) ** 2
                    min_colours[(rd + gd + bd)] = name

                #actual_name = None
                closest_name = min_colours[min(min_colours.keys())]
                #closest_name = None

            print ( 'closest colour name:', closest_name)

            return closest_name


def predict(imagepath):
	image = cv2.imread(imagepath)
    image = image[:,:,::-1]
    print(image.shape)
    rows, cols = image.shape[:2]

    top_offset = (1.0/6) * rows - (1.0/7) * cols
    side_offset = (1.0/2) * cols - (1.0/4) * cols 


    crop_width = 3*(1.0/7)*cols
    crop_height = 4*(1.0/6)*rows

    top_left = [int(top_offset), int(side_offset)]
    bottom_right = [int(top_offset + crop_height), int(side_offset + crop_width)]

    name = Color_Recognition_Kmeans(image[ top_left[0]: bottom_right[0], top_left[1]: bottom_right[1]])

    return name

# # print(top_left, bottom_right)
# plt.imshow(image[ top_left[0]: bottom_right[0], top_left[1]: bottom_right[1]])
# # # plt.imshow(image)
# plt.show()
# p = "/home/quantiphi/Documents/px/testing/darkflow/aa.jpg"
# print(predict(cv2.imread(p)))


# print(name)
# plt.imshow(image[:,:,::-1])
# plt.show()
# cv2.putText(image,name,(15, 15), 2, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
# cv2.imshow("images", image)
# cv2.waitKey(0)
#
# cv2.destroyAllWindows()
