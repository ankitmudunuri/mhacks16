from pvrecorder import PvRecorder
import pandas as pd



devices = PvRecorder.get_available_devices()
print(devices)
x = input("choose a device")
device = devices[x]

recorder = PvRecorder(frame_length=512)
recorder.start()

while True:
    
    
    
    
    flag = input("Press b to stop recording")
    if flag == 'b':
        recorder.stop()
        recorder.delete()
        break
        
