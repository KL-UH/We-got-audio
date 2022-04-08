import moviepy.editor as mp
import sys

video_fullpath = sys.argv[1]
video_name = sys.argv[2]

video_save_path = video_fullpath.replace(video_name,"temp.mp3")
# Insert Local Video File Path 
clip = mp.VideoFileClip(video_fullpath)
  
# Insert Local Audio File Path
clip.audio.write_audiofile(video_save_path)

print('Success')