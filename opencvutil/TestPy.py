import face_recognition
known_image = face_recognition.load_image_file("C:\\Users\\ZDF64\\Desktop\\Demo\\imgAndcache\\1inch2.jpg");
unknown_image = face_recognition.load_image_file("C:\\Users\\ZDF64\\Desktop\\Demo\\imgAndcache\\picHead.png");

lyfCode = face_recognition.face_encodings(known_image)
print(lyfCode)