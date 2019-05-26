from math import atan2,degrees

def GetAngle(p1,p2):
	xDiff = p2.x - p1.x
	yDiff = p2.y - p1.y

	return degrees(atan2(yDiff,xDiff))
