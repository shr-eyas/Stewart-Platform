import cv2
import numpy as np
import pyrealsense2 as rs
import csv

# Function to apply moving average filter
def moving_average_filter(data, window_size):
    filtered_data = np.zeros_like(data)
    for i in range(len(data)):
        start = max(0, i - window_size)
        end = min(len(data), i + window_size + 1)
        filtered_data[i] = np.mean(data[start:end])
    return filtered_data

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

# Window size for moving average filter
window_size = 5

# Open CSV file for writing
with open('marker_data.csv', mode='w', newline='') as csv_file:
    fieldnames = ['Marker_ID', 'Distance (mm)', 'X-axis Distance (mm)', 'Y-axis Distance (mm)',
                  'Z-axis Distance (mm)', 'Yaw (degrees)', 'Pitch (degrees)', 'Roll (degrees)']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

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
                x_distance = tvecs[i][0][0]  # X-axis distance
                y_distance = tvecs[i][0][1]  # Y-axis distance
                z_distance = tvecs[i][0][2]  # Z-axis distance
                
                rotation_vector = rvecs[i][0]
                rotation_matrix, _ = cv2.Rodrigues(rotation_vector)

                yaw = np.arctan2(rotation_matrix[1, 0], rotation_matrix[0, 0])
                pitch = np.arctan2(-rotation_matrix[2, 0], np.sqrt(rotation_matrix[2, 1] ** 2 + rotation_matrix[2, 2] ** 2))
                roll = np.arctan2(rotation_matrix[2, 1], rotation_matrix[2, 2])

                yaw_deg = np.degrees(yaw)
                pitch_deg = np.degrees(pitch)
                roll_deg = np.degrees(roll)

                if roll_deg > 0:
                    roll_deg = 180-roll_deg
                else:
                    roll_deg = 180+roll_deg
                    roll_deg = -roll_deg

                # Apply moving average filter
                x_distance_filtered = moving_average_filter([x_distance], window_size)[0]
                y_distance_filtered = moving_average_filter([y_distance], window_size)[0]
                z_distance_filtered = moving_average_filter([z_distance], window_size)[0]
                roll_deg_filtered = moving_average_filter([roll_deg], window_size)[0]
                pitch_deg_filtered = moving_average_filter([pitch_deg], window_size)[0]
                yaw_deg_filtered = moving_average_filter([yaw_deg], window_size)[0]

                # Print data on terminal
                print("Marker ID:", ids[i][0])
                print("Distance:", (distance*1000))
                print("X-axis Distance:", x_distance_filtered*1000)
                print("Y-axis Distance:", y_distance_filtered*1000)
                print("Z-axis Distance:", z_distance_filtered*1000)
                print("Yaw (degrees):", yaw_deg_filtered)
                print("Pitch (degrees):", pitch_deg_filtered)
                print("Roll (degrees):", roll_deg_filtered)

                # Write data to CSV
                writer.writerow({'Marker_ID': ids[i][0],
                                 'Distance (mm)': distance*1000,
                                 'X-axis Distance (mm)': x_distance_filtered*1000,
                                 'Y-axis Distance (mm)': y_distance_filtered*1000,
                                 'Z-axis Distance (mm)': z_distance_filtered*1000,
                                 'Yaw (degrees)': yaw_deg_filtered,
                                 'Pitch (degrees)': pitch_deg_filtered,
                                 'Roll (degrees)': roll_deg_filtered})
      
        cv2.imshow('Video Feed', frame)

        key = cv2.waitKey(1)
        if key == 27:
            break

pipeline.stop()
cv2.destroyAllWindows()
