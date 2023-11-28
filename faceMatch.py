import face_recognition, cv2, os

def checkFaces():


    image_path1 = "base.jpg"

    camera = cv2.VideoCapture(0)
    check, frame = camera.read()

    # Save the captured image to a file
    cv2.imwrite("captured_img.jpg", frame)
    image_path2 = "captured_img.jpg"

    # Compare the faces and get the match percentage and result
    # match_percentage, is_match = checkFaces(image_path1, image_path2)

    # Load the images and convert them to face encodings
    image1 = face_recognition.load_image_file(image_path1)
    image2 = face_recognition.load_image_file(image_path2)
    
    face_encoding1 = face_recognition.face_encodings(image1)[0]
    face_encoding2 = face_recognition.face_encodings(image2)[0]
    
    # Compare the face encodings
    results = face_recognition.compare_faces([face_encoding1], face_encoding2)
    
    # Calculate the match percentage
    match_percentage = face_recognition.face_distance([face_encoding1], face_encoding2)[0]
    match_percentage = round((1 - match_percentage) * 100, 2)

    os.remove("captured_img.jpg")
    
    return match_percentage, results[0]

# Provide the paths to the two images you want to compare

print(checkFaces())