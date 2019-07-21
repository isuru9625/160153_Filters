selection = input("1 - gaussian filter" + '\n' + "2 - median filter" +'\n' + "Enter your option number : "  )


import numpy as np
import cv2

if( selection == "1" or selection =="2"):
    print("processing")
    

    if(selection == "1"):
        import numpy as np
        import cv2
        img = cv2.imread('C:/Users/Isuru/Desktop/160153C_Filters/image.jpg', cv2.IMREAD_GRAYSCALE)
        
        img_out = img.copy()

        height = img.shape[0]
        width = img.shape[1]
        gauss = (1.0/57) * np.array([[0,1,2,1,0],[1,3,5,3,1],[2,5,9,5,2],[1,3,5,3,1],[0,1,2,1,0]])
        sum(sum(gauss))

        for i in np.arange(2, height-2):
            for j in np.arange(2, width-2):
                sum = 0
                for k in np.arange(-2,3):
                    for l in np.arange(-2,3):
                        a = img.item(i+k, j+l)
                        p = gauss[2+k, 2+l]
                        sum = sum + (p*a)
                b = sum
                img_out.itemset((i,j),b)
        cv2.imwrite('C:/Users/Isuru/Desktop/160153C_Filters/output.jpg', img_out)
        cv2.imshow('image', img_out)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
                
            
        
         
        
        


    if(selection == "2"):
        img = cv2.imread('C:/Users/Isuru/Desktop/Filters/image.jpg', cv2.IMREAD_GRAYSCALE)
       
        img_out = img.copy()
        height = img.shape[0]
        
        width = img.shape[1]
        

        for i in np.arange(3, height-3):
            for j in np.arange(3, width-3):
                neighbors = []
                for k in np.arange(-3,4):
                    for l in np.arange(-3,4):
                        a = img.item(i+k, j+l)
                        
                        neighbors.append(a)
                neighbors.sort()
                median = neighbors[24]
                b = median
                img_out.itemset((i,j), b)
        
        cv2.imwrite('C:/Users/Isuru/Desktop/Filters/output.jpg', img_out)
        cv2.imshow('image', img_out)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    print("processing completed")
    
else:
    print("Invalid input")
        
        
