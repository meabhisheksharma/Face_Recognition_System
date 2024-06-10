import face_recognition
import cv2
import pickle



def runCamera():
    count = 0
    gateOpen = False
    names = []
    encodings = []


    with open('faceEncodings', 'rb') as file1:
        encodings = pickle.load(file1)

    with open('faceNames', 'rb') as file2:
        names = pickle.load(file2)

    known_faces = encodings

    video_capture = cv2.VideoCapture(0)
    #video_capture = cv2.VideoCapture('http://192.168.1.105:4747/mjpegfeed')




    face_locations = []
    face_encodings = []
    process_this_frame = True

    print("Press 'Q' to close camera!!")

    while True:
        ret, frame = video_capture.read()
        if process_this_frame:

            face_locations = face_recognition.face_locations(frame)
            face_encodings = face_recognition.face_encodings(frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:

                match = face_recognition.compare_faces(known_faces, face_encoding)
                name = "Unknown"
                for itr in match:
                    if match[itr]:
                        name = names[itr]

                face_names.append(name)

        process_this_frame = not process_this_frame

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            if(name == "Unknown"):

                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                #print("\a Unknown!!!")

            else:

                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)

            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()