import math
import PhotoScan



doc = PhotoScan.app.document
chunk = doc.chunk

point_cloud = chunk.point_cloud
points = point_cloud.points
npoints = len(points)
projections = chunk.point_cloud.projections
err_sum = 0
num = 0
photo_avg = {}

for camera in chunk.cameras:
	if not camera.transform:
		continue

	T = camera.transform.inv()
	calib = camera.sensor.calibration
	point_index = 0
	photo_num = 0
	photo_err = 0
	for proj in projections[camera]:
		track_id = proj.track_id
		while point_index < npoints and points[point_index].track_id < track_id:
			point_index += 1
		if point_index < npoints and points[point_index].track_id == track_id:
			if not points[point_index].valid: 
				continue

				#dist = calib.error(T.mulp(points[point_index].coord), proj.coord).norm() ** 2
			dist = camera.error(points[point_index].coord, proj.coord).norm() ** 2

			err_sum += dist
			num += 1
			photo_num += 1
			photo_err += dist

	photo_avg[camera.label] = (math.sqrt(photo_err / photo_num), photo_num)

sigma = math.sqrt(err_sum / num)
rep_avg = sigma

print(sigma)



