import cv2, face_recognition, os, time, pyautogui

def checkFaces():

    image_path1 = "base.jpg"
    camera = cv2.VideoCapture(0)
    check, frame = camera.read()

    imgName = f'unlockAttempt_{time.time()}.jpg'

    cv2.imwrite(imgName, frame)
    image_path2 = imgName
    image1 = face_recognition.load_image_file(image_path1)
    image2 = face_recognition.load_image_file(image_path2)
    face_encoding1 = face_recognition.face_encodings(image1)[0]
    face_encoding2 = face_recognition.face_encodings(image2)[0]
    results = face_recognition.compare_faces([face_encoding1], face_encoding2)
    match_percentage = face_recognition.face_distance([face_encoding1], face_encoding2)[0]
    match_percentage = round((1 - match_percentage) * 100, 2)

    if match_percentage >= 60:
        os.remove(imgName)
        try:
            os.remove(imgName)
        except:
            pass
        


    return match_percentage, results[0] #Returns a tuple of the match percentage and a boolean value of whether or not the faces match