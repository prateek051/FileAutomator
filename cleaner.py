import os

# Ask the user for the target folder
target_folder = input("Enter the full path of the folder to clean\n")

# Teleport there
try:
    os.chdir(target_folder)
    print(f"cleaning : {os.getcwd()}")
except FileNotFoundError:
    print(f"That floder does not exist!")
    exit() # stop the script if the folder is bad

extension_map = {
    ".png" : "Images",
    ".txt" : "Documents",
    ".pdf" : "Documents",
    ".mp3" : "Audio",
    ".csv" : "Data"
}

files = os.listdir()

for file in files :
    extensions = os.path.splitext(file)

# if condition check if a keypair exist in the dictionary or not,
    if extensions[1] in extension_map : # without this line it will be KeyErro

        # print(f"File {extensions[0]}{extensions[1]} should go to {extension_map[extensions[1]]}")
        folder_name = extension_map[extensions[1]]
        os.makedirs(folder_name, exist_ok=True)

        new_path = os.path.join(folder_name, file)
        os.rename(file, new_path)
# print(type(os.path.splitext("image.png")))
# C:\Users\prate\Downloads