import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
ptime = 0

mpdraw = mp.solutions.drawing_utils
mpFashMwsh = mp.solutions.face_mesh
faceMesh = mpFashMwsh.FaceMesh(max_num_faces=2)
drawSpec = mpdraw.DrawingSpec(thickness=1, circle_radius=2)

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)
    if results.multi_face_landmarks:
        for facelms in results.multi_face_landmarks:
            mpdraw.draw_landmarks(
                img, facelms, mpFashMwsh.FACEMESH_CONTOURS, drawSpec, drawSpec)
            for id, im in enumerate(facelms.landmark):
                ih, iw, ic = img.shape
    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime
    cv2.putText(img, str(int(fps)), (70, 50),
                cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
    cv2.imshow("image", img)
    cv2.waitKey(1)
