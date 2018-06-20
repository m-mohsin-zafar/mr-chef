def checkCamera(recipeName,instruction_step):
    import cv2 
    import numpy as np
    import time
    from firebase import firebase
    from skimage.measure import compare_ssim as ssim
    import urllib
    template="template.jpg"
    success_img = cv2.imread("successTemplate.jpg")
    firebase = firebase.FirebaseApplication('https://mrchef-9eca9.firebaseio.com', None)
    result = firebase.get('/Image_Templates/testing/'+recipeName+instruction_step, None)
    urllib.request.urlretrieve(result, template)
    cam = cv2.VideoCapture(0)
    image=None
    img_counter=30
    for i in range(img_counter):
     ret,frame=cam.read()
    image=frame
    img_name = "acquired_image.jpg"
    cv2.imwrite(img_name, image)
    cam.release()
    img_rgb = cv2.imread(img_name)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(template,0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.6
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    s=ssim(success_img,img_rgb,multichannel=True)
    if s>-1.0 and s<0.2:
        ans=False
        print(s)
        print(ans)
    else:
        ans=True
        print(s)
        print(ans)
    cv2.imshow("result",img_rgb)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return ans

checkCamera("temp_loc","1")
