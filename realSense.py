import cv2
import numpy as np
import pyrealsense2 as rs

pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
pipeline.start(config)

marker_length = 0.078
camera_matrix = np.array([[410.20468281, 0, 325.08951872],
                          [0, 411.09980003, 256.07790764],
                          [0, 0, 1]])
dist_coeffs = np.array([[0.01968542, -0.1836438, 0.00905011, 0.00086756, 0.35920412]])

detected_markers = []

while True:

    frames = pipeline.wait_for_frames()
    color_frame = frames.get_color_frame()
    if not color_frame:
        continue

    frame = np.asanyarray(color_frame.get_data())
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
    parameters = cv2.aruco.DetectorParameters_create()
    corners, ids, _ = cv2.aruco.detectMarkers(gray, dictionary, parameters=parameters)

    if ids is not None:
        rvecs, tvecs, _ = cv2.aruco.estimatePoseSingleMarkers(corners, marker_length, camera_matrix, dist_coeffs)
        cv2.aruco.drawDetectedMarkers(frame, corners, ids)

        for i in range(len(ids)):
            distance = np.linalg.norm(tvecs[i])
            rotation_vector = rvecs[i][0]
            rotation_matrix, _ = cv2.Rodrigues(rotation_vector)

            yaw = np.arctan2(rotation_matrix[1, 0], rotation_matrix[0, 0])
            pitch = np.arctan2(-rotation_matrix[2, 0], np.sqrt(rotation_matrix[2, 1] ** 2 + rotation_matrix[2, 2] ** 2))
            roll = np.arctan2(rotation_matrix[2, 1], rotation_matrix[2, 2])

            yaw_deg = np.degrees(yaw)
            pitch_deg = np.degrees(pitch)
            roll_deg = np.degrees(roll)

            print("Marker ID:", ids[i][0])
            print("Distance:", (distance*1000))
            print("Yaw (degrees):", yaw_deg)
            print("Pitch (degrees):", pitch_deg)
            print("Roll (degrees):", roll_deg)
  
    cv2.imshow('Video Feed', frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

pipeline.stop()
cv2.destroyAllWindows()
