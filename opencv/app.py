import cv2
cam=cv2.VideoCapture(0)
cv2.namedWindow("Lun")
img_cnt=0
while True:
    ret,frame=cam.read()
    if not ret:
        print("Error")
        break
    cv2.imshow("testing",frame)  
    k=cv2.waitKey(1)
    if k%256==27:
        print("Closed")
        break
    elif k%256==32:
        img_name="Screen_shot_{}.png".format(img_cnt)
        cv2.imwrite(img_name,frame)

        # DISPLAY IMAGE TAKEN
        cv2.imshow(img_name,frame) 
        
        img_cnt+=1
        
cam.release()
cv2.destroyAllWindows()