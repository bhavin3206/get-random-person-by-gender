from thispersondoesnotexist import Person
import os, cv2, random
from deepface import DeepFace
import shutil
import os, threading

def copy_img(img_name='',source_file ='',destination_folder='') :
    destination_path = destination_folder + img_name
    shutil.copy(source_file, destination_path)

def get_image_for_create_account(gender : str):
    gender = ['male','female']
    breakpoint()
    folder_path = os.path.join(os.getcwd(),f"profile_pic/{gender}")
    os.makedirs(folder_path)
    # Get a list of all files in the folder
    files_in_folder = os.listdir(folder_path)
    if len(files_in_folder) == 20 :
        threading.Thread(target=add_profile_img).start()
    return random.choice(os.path.join(os.getcwd(),f"profile_pic/{gender}/{random.choice(files_in_folder)}") )


def add_profile_img():
    for _ in range(100):
        person = Person(fetch_online=True)
        person.save(os.path.join(os.getcwd(),'profile_pic/checkimg.jpeg'))
        img = cv2.imread(os.path.join(os.getcwd(),'profile_pic/checkimg.jpeg'))
        result = DeepFace.analyze(img,actions=("gender"))
        destination_folder = ''
        if result[0]['dominant_gender'] == "Woman" :
            destination_folder = os.path.join(os.getcwd(),'profile_pic/female/')
        elif result[0]['dominant_gender'] == "Man" :
        # else :
            destination_folder = os.path.join(os.getcwd(),'profile_pic/male/')
        if destination_folder :
            print(result[0]['dominant_gender'])
            copy_img(img_name=f'{random.randint(1000,100000000)}.jpeg',source_file=os.path.join(os.getcwd(),'profile_pic/checkimg.jpeg'),destination_folder=destination_folder)

get_image_for_create_account('male')