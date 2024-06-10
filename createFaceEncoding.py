import face_recognition
import os
import pickle

def update():
    photos = []
    names = []
    encodings = []

    for f in os.listdir("Images/"):
        if f.endswith('.jpg'):
            photos.append(f)

    for labels in photos:
        mname = labels[:-4]
        names.append(mname)

        mimage = mname + "_image"
        mencoding = mname + "_face_encoding"

        mimage = face_recognition.load_image_file("Images/{}".format(labels))
        mencoding = face_recognition.face_encodings(mimage)[0]

        encodings.append(mencoding)

    with open('faceEncodings', 'wb') as file1:
        pickle.dump(encodings, file1)
        print("Face Encodings Updated Successfully!!!")

    with open('faceNames', 'wb') as file2:
        pickle.dump(names, file2)
        print("Face Labels Updated Successfully!!!")