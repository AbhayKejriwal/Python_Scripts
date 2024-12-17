import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)

# Drawing utilities to draw landmarks on hand
mp_drawing = mp.solutions.drawing_utils

# Initialize webcam
cap = cv2.VideoCapture(0)

# Define the virtual piano keys by splitting the screen width
def get_piano_key(x_pos, frame_width):
    key_width = frame_width // 7  # Assume 7 virtual keys (C, D, E, F, G, A, B)
    return x_pos // key_width

# Dictionary of notes for keys (replace these with actual sounds later)
piano_notes = {0: 'C', 1: 'D', 2: 'E', 3: 'F', 4: 'G', 5: 'A', 6: 'B'}

while True:
    success, frame = cap.read()
    if not success:
        break
    
    frame_height, frame_width, _ = frame.shape
    
    # Convert the image to RGB (OpenCV uses BGR by default)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame to detect hands
    results = hands.process(rgb_frame)
    
    # If hand landmarks are detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks on the frame
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Extract coordinates of the index finger tip (landmark 8)
            index_finger_tip = hand_landmarks.landmark[8]
            x_pos = int(index_finger_tip.x * frame_width)
            y_pos = int(index_finger_tip.y * frame_height)
            
            # Find the virtual piano key based on x position
            key = get_piano_key(x_pos, frame_width)
            note = piano_notes.get(key, None)
            
            if note:
                cv2.putText(frame, f'Playing: {note}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            
    # Display the frame with hand landmarks
    cv2.imshow("Piano Finger Tracking", frame)
    
    # Press 'q' to exit the video feed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
