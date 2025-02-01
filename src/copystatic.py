import os
import shutil

# so this function will delete everything from the public directory 
def prepare_destination_directory(path):
    if os.path.exists(path):
        print(f"now deleting...")
        shutil.rmtree(path)
        if os.path.exists(path):
            print(f"There was an error!")
        else:
            print(f"now remaking destination...")
            os.mkdir(path)
    else:
        print(f"Destination does not exist...")
        print(f"now creating destination...")
        os.mkdir(path)
        print(f"destination created successfully")

# this function will take the provided paths and recursively access each file and folder in the src_path and copy it to the dst_path. 
def directory_copy(src_path, dst_path):
    print(f" * source -> destination")
    for item in os.listdir(src_path): 
        if os.path.isfile(os.path.join(src_path, item)):
            shutil.copy(os.path.join(src_path, item), dst_path)
            continue
        else:
            new_dst = os.path.join(dst_path, item)
            os.makedirs(new_dst, exist_ok=True)
            directory_copy(os.path.join(src_path, item), new_dst)