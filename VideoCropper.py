# Import everything needed to edit video clips
from moviepy.editor import *
# import moviepy
import os
import logging


logging.basicConfig(filename = "LogFileTrimmer.log" , level = logging.INFO)

dir_path = input("Enter the path of the file:")
logging.info(f'pwd {dir_path}')


for root, dirs, files in os.walk(dir_path):
    logging.info(f'{root}{dirs}{files}')
   
    for file in files:
        logging.info(f'{files}')
       



        if file.endswith('.mp4'):


            print (dir_path+ '\\' +str(file))
            FilePath = dir_path+ '/' +str(file)
            logging.info(f'{file} is present is {FilePath}')
         
            file_name = os.path.basename(FilePath)
            print(file_name)
            
            vid = VideoFileClip(f'{file_name}')
  
  
            # getting duration of the video
            Duration = vid.duration
            logging.info(f'{vid} is has {Duration} in seconds')
            hours = int(vid.duration / 3600)
            logging.info(f'{vid} is has {hours} in hours')
            mins = int((vid.duration % 3600) / 60)
            logging.info(f'{vid} is has {mins} in minutes')
            secs =int((vid.duration % 60))
            logging.info(f'{vid} is has {secs} in seconds')
            
  
            # printing duration
            print(f"Duration : {hours}-{mins} min-{secs} sec")
            logging.info(f'{vid} is has {Duration} in minutes,seconds format')
        
        
            # Start point
            t_start = int(input('ENter the start:'))
            
            # End point
            t_end = int(input('ENter the end:'))

            # Converting in minutes
            Minutes = t_start*60
            logging.info(f'{vid} is has {Minutes}')
            # Converting in seconds
            Seconds = t_end*60
            logging.info(f'{vid} is has {Seconds}')


            # Trimming the Video
            Trim = vid.subclip(Minutes,Seconds)
        

            Trim.write_videofile("TrimmedVideo.mp4")
            logging.info(f'Video Trimmed Successfully ')
            exit()