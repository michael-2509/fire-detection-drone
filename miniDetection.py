import airsim

# connect to the AirSim simulator
client = airsim.VehicleClient()
client.confirmConnection()

camera_name = "0"
image_type = airsim.ImageType.Scene

client = airsim.MultirotorClient()
client.confirmConnection()

client.simSetDetectionFilterRadius(
    camera_name, image_type, 80 * 100)  # in [cm]
client.simAddDetectionFilterMeshName(camera_name, image_type, "Car*")
client.simGetDetections(camera_name, image_type)
detections = client.simClearDetectionMeshNames(camera_name, image_type)
