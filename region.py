import cv2
import numpy as np

# List to store points and ROIs
points = []
rois = []
roi_counter = 1

# Mouse callback function
def mouse_callback(event, x, y, flags, param):
    global points
    if event == cv2.EVENT_LBUTTONDOWN:
        # Store the point coordinates
        points.append((x, y))
        print(f"Point selected: {(x, y)}")

def vid_roi(video, save_file='rois.txt'):
    global points, rois, roi_counter
    
    # Open video capture
    cap = cv2.VideoCapture(video)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    cv2.namedWindow('Frame')
    cv2.setMouseCallback('Frame', mouse_callback)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Draw the current points being selected
        for point in points:
            cv2.circle(frame, point, 5, (0, 255, 0), -1)
        if len(points) >= 2:
            cv2.line(frame, points[0], points[1], (0, 255, 0), 2)
        if len(points) >= 3:
            cv2.line(frame, points[1], points[2], (0, 255, 0), 2)
        if len(points) == 4:
            cv2.line(frame, points[2], points[3], (0, 255, 0), 2)
            cv2.line(frame, points[3], points[0], (0, 255, 0), 2)
            print(f"Rectangle coordinates: {points}")

        # Draw all saved ROIs
        for roi in rois:
            roi_array = np.array(roi['coordinates'], dtype=np.int32)
            roi_array = roi_array.reshape((-1, 1, 2))
            cv2.polylines(frame, [roi_array], isClosed=True, color=(255, 0, 0), thickness=2)
            cv2.putText(frame, roi['name'], tuple(roi['coordinates'][0]), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

        cv2.imshow('Frame', frame)

        # Check for key presses
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('c'):
            points = []  # Reset points
            print("Points reset.")
        elif key == ord('s') and len(points) == 4:
            # Prompt the user to enter a name for the ROI
            roi_name = input(f"Enter a name for ROI {roi_counter}: ")
            
            # Save the current ROI with its name
            rois.append({'name': roi_name, 'coordinates': points.copy()})
            
            # Save the ROI to the text file
            with open(save_file, 'a') as f:
                f.write(f"ROI {roi_counter}: {roi_name} - {points}\n")
            
            print(f"ROI {roi_counter} saved as '{roi_name}' to {save_file}")
            roi_counter += 1
            points = []  # Reset points for the next ROI

    # Release video capture and close windows
    cap.release()
    cv2.destroyAllWindows()

    # If any ROI was saved, print a summary
    if rois:
        print(f"Total ROIs saved: {len(rois)}")
    else:
        print("No ROI was saved.")
