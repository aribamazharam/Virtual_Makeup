from utils import *

# Features to add makeup
face_elements = [
    "LIP_LOWER",
    "LIP_UPPER",
    "EYEBROW_LEFT",
    "EYEBROW_RIGHT",
    "EYELINER_LEFT",
    "EYELINER_RIGHT",
    "EYESHADOW_LEFT",
    "EYESHADOW_RIGHT",
]

# Desired lipstick color in BGR
desired_lipstick_color = np.array([190, 68, 64], dtype=np.uint8)  # Example RGB value for a purple lipstick

face_connections = [face_points[idx] for idx in face_elements]

video_capture = cv2.VideoCapture(0)
while True:
    # Read image from camera
    success, image = video_capture.read()
    image = cv2.flip(image, 1)
    # If input from camera
    if success:
        # Create an empty mask like image
        mask = np.zeros_like(image)
        # Extract facial landmarks
        face_landmarks = read_landmarks(image=image)

        # Detect the original lip color
        upper_lip_color = detect_lip_color(image, face_points["LIP_UPPER"], face_landmarks)
        lower_lip_color = detect_lip_color(image, face_points["LIP_LOWER"], face_landmarks)

        # Mix the detected lip color with the desired lipstick color
        mixed_upper_lip_color = mix_colors(upper_lip_color, desired_lipstick_color, ratio=0.5)
        mixed_lower_lip_color = mix_colors(lower_lip_color, desired_lipstick_color, ratio=0.5)
        


        # Change the color of features
        colors_map = {
            "LIP_UPPER": mixed_upper_lip_color.tolist(),
            "LIP_LOWER": mixed_lower_lip_color.tolist(),
            "EYELINER_LEFT": [139, 0, 0],  # Dark Blue in BGR
            "EYELINER_RIGHT": [139, 0, 0],  # Dark Blue in BGR
            "EYESHADOW_LEFT": [0, 100, 0],  # Dark Green in BGR
            "EYESHADOW_RIGHT": [0, 100, 0],  # Dark Green in BGR
            "EYEBROW_LEFT": [19, 69, 139],  # Dark Brown in BGR
            "EYEBROW_RIGHT": [19, 69, 139],  # Dark Brown in BGR
        }

        colors = [colors_map[idx] for idx in face_elements]

        # Create mask for facial features with color
        mask = add_mask(
            mask,
            idx_to_coordinates=face_landmarks,
            face_connections=face_connections,
            colors=colors
        )

        # Combine the image and mask with respect to weights
        output = cv2.addWeighted(image, 1.0, mask, 0.2, 1.0)
        cv2.imshow("Feature", output)
        # Press q to exit the cv2 window
        if cv2.waitKey(100) & 0xFF == ord("q"):
            break
video_capture.release()
cv2.destroyAllWindows()

