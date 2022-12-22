import os
import math
from time import sleep

if __name__ == '__main__':
    counter = 0
    counter11 = 0
    root_folder = "D:\Hackaton-ransomeware"


    # get a list of all folders inside the root folder
    folder_list = [f for f in os.listdir(root_folder) if os.path.isdir(os.path.join(root_folder, f))]

    # iterate through the list of folders
    for folder in folder_list:
        # get a list of all sub-folders inside the current folder
        sub_folder_list = [f for f in os.listdir(os.path.join(root_folder, folder)) if
                           os.path.isdir(os.path.join(root_folder, folder, f))]

        # iterate through the list of sub-folders
        for sub_folder_name in sub_folder_list:
            # get the path to the current sub-folder
            sub_folder_path = os.path.join(root_folder, folder, sub_folder_name)

            # get a list of all sub-sub-folders inside the current sub-folder

            for dir_name in os.listdir(sub_folder_path):
                counter11+=1
                full_dir_path = os.path.join(sub_folder_path, dir_name)

                # first check if the file name contains the string ".htn"
                if full_dir_path.find(".htn") != -1:
                    print(full_dir_path)
                    
                # if it doesnt contain ".htn" calculate its entropy
                else:
                    if not full_dir_path.endswith(
                            ".mobi") and not full_dir_path.endswith(".rar") and not full_dir_path.endswith(
                            ".jpg") and not full_dir_path.endswith(".7z") and not full_dir_path.endswith(
                            ".pdf") and not full_dir_path.endswith(".png"):
                        with open(full_dir_path, 'rb') as f:
                            data = f.read()

                            # calculate the frequency of each byte value in the file
                        freq = {}
                        for byte in data:
                            if byte in freq:
                                freq[byte] += 1
                            else:
                                freq[byte] = 1

                        # calculate the entropy of the file
                        entropy = 0
                        for byte, count in freq.items():
                            p = count / len(data)
                            entropy -= p * math.log(p, 256)
                        if entropy > 0.9 and entropy < 1.1:
                            counter += 1
                            print(full_dir_path)
    
