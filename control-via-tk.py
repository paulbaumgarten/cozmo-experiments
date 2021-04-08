import time, math, pycozmo
import tkinter

# 1X21C9ZP1CI9

# Start the program
app = tkinter.Tk()
app.title("My Cozmo!")
# Connect to Cozmo
cozmo = pycozmo.Client()
cozmo.start()
cozmo.connect()
cozmo.wait_for_robot()
time.sleep(1)

def left(e):
    print("Left")
    cozmo.drive_wheels(lwheel_speed=50.0, rwheel_speed=-50.0)

def right(e):
    print("Right")
    cozmo.drive_wheels(lwheel_speed=-50.0, rwheel_speed=50.0)

def forward(e):
    print("Forward")
    cozmo.drive_wheels(lwheel_speed=50.0, rwheel_speed=50.0)

def reverse(e):
    print("Reverse")
    cozmo.drive_wheels(lwheel_speed=-50.0, rwheel_speed=-50.0)

def stop(e):
    print("Stop")
    cozmo.stop_all_motors()

def terminate(e):
    print("Terminating")
    cozmo.disconnect()
    cozmo.stop()
    exit()


# Attach the keypresses to the functions above
app.bind("<Left>", left)
app.bind("<Right>", right)
app.bind("<Up>", forward)
app.bind("<Down>", reverse)
app.bind("<space>", stop)
app.bind("<Escape>", terminate)
# Run the program
app.mainloop()

