import time, math, pycozmo

# Connect to Cozmo
cozmo = pycozmo.Client()
cozmo.start()
cozmo.connect()
cozmo.wait_for_robot()
# Do something simple
cozmo.set_all_backpack_lights(pycozmo.lights.blue_light)
time.sleep(1)
cozmo.set_all_backpack_lights(pycozmo.lights.red_light)
time.sleep(1)
cozmo.set_all_backpack_lights(pycozmo.lights.off_light)

input("Press enter to continue")
cozmo.drive_wheels(lwheel_speed=50.0, rwheel_speed=50.0, duration=5.0)

# Disconnect from Cozmo
cozmo.disconnect()
cozmo.stop()
