import cv2

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Choose the codec (XVID for .avi format)
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))  # Create the VideoWriter object

# Open the default camera (index 0)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret:
        # Write the frame to the output file
        out.write(frame)

        # Display the resulting frame
        cv2.imshow('frame', frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release the capture and writer objects and close any open windows
cap.release()
out.release()
cv2.destroyAllWindows()
