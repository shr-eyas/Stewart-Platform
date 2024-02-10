import cv2
import numpy as np

cap = cv2.VideoCapture(6)

cam_matrix = np.array([[936.0652516098202, 0, 633.7619367680327],
                       [0, 937.3543919408091, 344.3671310217896],
                       [0, 0, 1]])

dist_coeffs = np.array([0.3029196190859768, -1.441564743239442, -0.002203069687765735, -0.006587528866314235, -3.530766821016102])

detected_markers = []

while cap.isOpened():
    _, image = cap.read()

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
    parameters = cv2.aruco.DetectorParameters_create()
    corners, ids, _ = cv2.aruco.detectMarkers(gray, dictionary, parameters=parameters)

    if ids is not None:
  
        rvecs, tvecs, _ = cv2.aruco.estimatePoseSingleMarkers(corners, 0.05, cam_matrix, dist_coeffs)

        cv2.aruco.drawDetectedMarkers(image, corners, ids)

        for i in range(len(ids)):
            distance = np.linalg.norm(tvecs[i])
            rotation_vector = rvecs[i][0]
            rotation_matrix, _ = cv2.Rodrigues(rotation_vector)
            # Extracting Euler angles from the rotation matrix in radians
            yaw = np.arctan2(rotation_matrix[1, 0], rotation_matrix[0, 0])
            pitch = np.arctan2(-rotation_matrix[2, 0], np.sqrt(rotation_matrix[2, 1] ** 2 + rotation_matrix[2, 2] ** 2))
            roll = np.arctan2(rotation_matrix[2, 1], rotation_matrix[2, 2])

            # Convert angles from radians to degrees
            yaw_deg = np.degrees(yaw)
            pitch_deg = np.degrees(pitch)
            roll_deg = np.degrees(roll)

            print("Marker ID:", ids[i][0])
            print("Distance:", (distance*1000))
            print("Yaw (degrees):", yaw_deg)
            print("Pitch (degrees):", pitch_deg)
            print("Roll (degrees):", roll_deg)

    cv2.imshow('image', image)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
