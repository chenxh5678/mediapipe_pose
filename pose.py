import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
myPose = mp.solutions.pose
poses = myPose.Pose()

cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = poses.process(frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    if results.pose_landmarks:  # 包含姿势地标的“姿势地标”字段。
        # get landmarks as numpy
        # landmarks = results.pose_landmarks.landmark
        # np_landmarks = np.array([(lm.x, lm.y, lm.z, lm.visibility) for lm in landmarks])
        # print(np_landmarks.shape)
        # print(np_landmarks)  # 获取坐标
        # 画图
        mp_drawing.draw_landmarks(frame,results.pose_landmarks,myPose.POSE_CONNECTIONS)
    # if results.pose_world_landmarks:  # “pose_world_landmarks”（姿势世界地标）字段，包含真实世界三维坐标中的姿势地标，以米为单位，原点位于臀部之间的中心。
    #     mp_drawing.draw_landmarks(frame,results.pose_world_landmarks,myPose.POSE_CONNECTIONS)
    cv2.imshow('MediaPipe Pose', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
