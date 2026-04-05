import cv2
import mediapipe as mp
import random
import time

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

game_moves = ['rock', 'paper', 'scissors']

def is_finger_up(landmarks, tip_id, mcp_id):
    """Check if a finger is extended by comparing tip Y to MCP (base) joint Y."""
    return landmarks[tip_id].y < landmarks[mcp_id].y

def detect_hand_gesture(hand_landmarks):
    if not hand_landmarks:
        return None

    lm = hand_landmarks[0].landmark

    # Finger tip and MCP landmark IDs
    fingers = [
        (mp_hands.HandLandmark.INDEX_FINGER_TIP,  mp_hands.HandLandmark.INDEX_FINGER_MCP),
        (mp_hands.HandLandmark.MIDDLE_FINGER_TIP, mp_hands.HandLandmark.MIDDLE_FINGER_MCP),
        (mp_hands.HandLandmark.RING_FINGER_TIP,   mp_hands.HandLandmark.RING_FINGER_MCP),
        (mp_hands.HandLandmark.PINKY_TIP,         mp_hands.HandLandmark.PINKY_MCP),
    ]

    fingers_up = [is_finger_up(lm, tip, mcp) for tip, mcp in fingers]
    count = sum(fingers_up)

    if count == 0:
        return 'rock'      # All fingers curled
    elif count == 4:
        return 'paper'     # All fingers extended
    elif fingers_up[0] and fingers_up[1] and not fingers_up[2] and not fingers_up[3]:
        return 'scissors'  # Index + middle up only
    else:
        return None        # Unrecognized gesture

def get_winner(player_move, computer_move):
    if player_move == computer_move:
        return 'Draw'
    elif (player_move == 'rock'     and computer_move == 'scissors') or \
         (player_move == 'paper'    and computer_move == 'rock')     or \
         (player_move == 'scissors' and computer_move == 'paper'):
        return 'Player Wins!'
    else:
        return 'Computer Wins!'

cap = cv2.VideoCapture(0)

last_result = None
last_time = 0
COOLDOWN = 2  # seconds between rounds

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_rgb)

    if result.multi_hand_landmarks:
        for hand_lm in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_lm, mp_hands.HAND_CONNECTIONS)

        now = time.time()
        if now - last_time >= COOLDOWN:
            player_move = detect_hand_gesture(result.multi_hand_landmarks)

            if player_move:
                computer_move = random.choice(game_moves)
                last_result = {
                    'player': player_move,
                    'computer': computer_move,
                    'result': get_winner(player_move, computer_move)
                }
                last_time = now

    # Display last known result on screen (no freeze)
    if last_result:
        cv2.putText(frame, f"Player:   {last_result['player']}",   (10, 40),  cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 80,  80),  2)
        cv2.putText(frame, f"Computer: {last_result['computer']}", (10, 80),  cv2.FONT_HERSHEY_SIMPLEX, 1, (80,  200, 80),  2)
        cv2.putText(frame, last_result['result'],                  (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (80,  80,  255), 2)

    cv2.imshow('Rock Paper Scissors', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()