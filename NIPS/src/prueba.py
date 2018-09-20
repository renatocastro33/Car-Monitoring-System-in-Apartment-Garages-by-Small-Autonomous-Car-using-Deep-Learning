from openalpr import Alpr
import sys
import numpy as np
import cv2

cap = cv2.VideoCapture("/home/adminhpc/Escritorio/MultimediaALPR/PAPER/video3.mp4") # Video file url
cap.set(3, 500)
cap.set(4, 500)


def pipeline(foto):
	alpr = Alpr("us", "/etc/openalpr/openalpr.conf", "openalpr/runtime_data/")
	if not alpr.is_loaded():
		print("Error loading OpenALPR")
		sys.exit(1)
		
	alpr.set_top_n(7)
	alpr.set_default_region("md")

	results = alpr.recognize_ndarray(foto)

	i = 0
	for plate in results['results']:
		i += 1
		#print("Plate #%d" % i)
		#print("   %12s %12s" % ("Plate", "Confidence"))
		for candidate in plate['candidates']:
		#	prefix = "-"
		#	if candidate['matches_template']:
		#		prefix = "*"
			if len(candidate["plate"]) == 6 and candidate["confidence"] >= 50.0:
				print("Plate: " + str(candidate["plate"]) + " Confidence:" + str(candidate["confidence"]))
				
				
		#	print("  %s %12s%12f" % (prefix, candidate['plate'], candidate['confidence']))

	# Call when completely done to release memory
	alpr.unload()

while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()
	if ret == False:
		break
	# Our operations on the frame come here
	frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

	# Give frame to recognize
	pipeline(frame2)
	# Display the resulting frame
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
