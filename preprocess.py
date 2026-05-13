import cv2

def preprocess_image(image_path):

    
    image = cv2.imread(image_path)

   
    image = cv2.resize(image, (1400, 500))

    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    
    blur = cv2.GaussianBlur(gray, (3, 3), 0)

    return blur