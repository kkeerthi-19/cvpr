import cv2
cap = cv2.VideoCapture('https://media.istockphoto.com/id/2164522908/video/low-flightof-a-sports-fpv-drone-at-high-speed-high-in-the-mountains-over-a-yellowautumn.mp4?s=mp4-640x640-is&k=20&c=KZjsjKSpCtz34k1m4hPcjaJpdBuHu7l0p-yLgcv7Law=')
while(cap.isOpened()):
ret, frame = cap.read()
cv2.putText(frame, 'Hello World!!', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,
255, 0), 2, cv2.LINE_AA)
if ret == True:
cv2.imshow('Frame', frame)
if cv2.waitKey(25) & 0xFF == ord('q'):
break
else:
break
cap.release()
cv2.destroyAllWindows()
