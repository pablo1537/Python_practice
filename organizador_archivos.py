import os
import shutil

folder_path = "C:\\Users\\Pablo\\Desktop\\Practice"



# ? supported image types
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".eps"]
# ? supported Video types
video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg", ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".flv", ".swf"]

# ? supported Audio types
audio_extensions = [".m4a", "mp3", ".wav", ".wma"]

# ? supported Document types
document_extensions = [".doc", ".docx", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]

video_folder = folder_path + "\\Videos"
if not os.path.exists(video_folder):
    os.mkdir(video_folder)

image_folder = folder_path + "\\Imagenes"
if not os.path.exists(image_folder):
    os.mkdir(image_folder)

music_folder = folder_path + "\\Musica"
if not os.path.exists(music_folder):
    os.mkdir(music_folder)

doc_folder = folder_path + "\\Documentos"
if not os.path.exists(doc_folder):
    os.mkdir(doc_folder)
    


def move_file(file,extensions,dest_folder):
    for extension in extensions:
        if file.lower().endswith(extension):
            #print(folder_path+"\\"+file)
            name= file
            while os.path.exists(dest_folder+"\\"+name):
                name="(1)"+name
            shutil.move(folder_path+"\\"+file,dest_folder+"\\"+name)

def main():
    files_paths = os.scandir(folder_path)
    for x in files_paths:
        move_file(x.name,video_extensions,video_folder)
        move_file(x.name,image_extensions,image_extensions)
        move_file(x.name,audio_extensions,music_folder)
        move_file(x.name,document_extensions,doc_folder)



if __name__ == '__main__':
    main()