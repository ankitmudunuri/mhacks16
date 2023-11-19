import Analyze.audio_in as a_in
import scripts.facialrecog as f_rec

# Thread 1
# Gets the audio, translates it to text, and translates the text
# Returns the text
phrase = a_in.main()


# Thread 2
# 

# Thread 3
# Gets the video and Finds the face
# Creates a grid alongside the video
# Prints the text at the location of the face
f_rec.video_stream()

print(phrase)
