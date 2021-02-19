
import os
import glob
import speech_recognition as sr
import sys

# specify the location of ffmpeg for the project and grab all mp4s in the current folder and all folders below
ffmpeg_location = sys.argv[1] # send in the ffmpeg exe file through a command line arguement
video_files = glob.glob("./**/*.mp4", recursive=True) # grab all mp4s in the folder

# prep the speech recognizer for converting from audio to text
r = sr.Recognizer()

for video in video_files:
    
    # run the commands from ffmpeg to take the video and convert to an audio file
    sound_output = video.replace(".mp4", ".wav")
    command_for_converting = f" -i {video} {sound_output}"
    os.system(ffmpeg_location + " -y " + command_for_converting)

    audio = sr.AudioFile(sound_output)
    
    with audio as source:
        
        # get the audio into text format to write
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.record(source)
        text = r.recognize_google(audio)

        # modify the audio file name and path to create a name and file path for the text
        text_output = sound_output.replace(".wav", ".txt")

        # create a file and write the content out
        file = open(text_output, "w")
        file.write(text)




# output from recognize_google() =============================================================================
#   I don't know because of your weird specific job way more time than I would want on Facebook in 2019 in 
#   most response to the 2016 election Facebook released the ads Library feature which means you can see all 
#   of the ads that any sort of organization or Creator is running so in theory this every add a politician is 
#   running on Facebook which is helpful I always check anything because sometimes you'll find sales and other 
#   times you'll find exclusive promos that you weren't supposed to see