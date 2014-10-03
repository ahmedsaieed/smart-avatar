# run-avatar.py

# Python script that requests proximity sensor readings from Arduino, and decides
# whether to play the idle or the action video, based on the presence of humans
# around the avatar.


import serial
import time
import os


arduino = serial.Serial('/dev/ttyACM1', 9600)



def playIdle():
        # play idle video in loop
        print "Playing idle video in loop.\n\r"
        os.system("vlc --repeat --one-instance pause.mp4 &")


def playAction():
        # play action video in loop
        print "Playing action video in loop.\n\r"
        os.system("vlc --repeat --one-instance play.mp4 &")

try:
        playIdle()
        idle = True

        while True:

                print "Requesting sensor reading."

                arduino.write('A')
                
                if(arduino.inWaiting()):

                        # print "Got response from Arduino!" # DEBUG
                        
                        response = arduino.readline()

                        arduino.flushInput()
                        
                        # print "Response: " + str(response)  # DEBUG
                        # print "Idle State: " + str(idle) # DEBUG
                        
                        if "1" in response and idle == True:
                                # print "Got 1 in Respone and Idle is True" # DEBUG
                                idle = False                        
                                playAction()
                                
                                
                        elif "0" in response and idle == False:
                                # print "Got 0 in Respone and Idle is False" # DEBUG
                                idle = True                     
                                playIdle()
                                        
                        else:
                                # Do nothing!
                                
                                # print "No change in state.\n" # DEBUG
                                
                # print "Gotta sleep for 2 secs" # DEBUG
                time.sleep(2)
                        
except KeyboardInterrupt:
        print "Quit"
