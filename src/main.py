import os
from copystatic import prepare_destination_directory, directory_copy

def main ():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)

    source = os.path.join(project_root, "static")
    destination = os.path.join(project_root, "public")

    print(f"preparing to delete destination directory...")

    prepare_destination_directory(destination)
    directory_copy(source, destination)



if __name__ == "__main__":
    main()