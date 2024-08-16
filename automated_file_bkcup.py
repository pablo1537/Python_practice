import os
import shutil
import datetime
import schedule 
import time

source_dir ="C:\\Users\\Pablo\\Desktop\\textos prueba"
bckup_dir= "C:\\Users\\Pablo\\Desktop\\bckup"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    bckup_folder_dir = os.path.join(dest,str(today))

    try:
        shutil.copytree(source,bckup_folder_dir)
        print(f"Carpeta copiada en: {bckup_folder_dir}")
    except FileExistsError:
        print(f"Carpeta ya existe en {bckup_dir}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    schedule.every().day.at("03:01").do(lambda: copy_folder_to_directory(source_dir,bckup_dir))
    #copy_folder_to_directory(source_dir,bckup_dir)
    while True:
        schedule.run_pending()
        time.sleep(60)