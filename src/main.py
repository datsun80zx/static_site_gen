import os
from copystatic import prepare_destination_directory, directory_copy
from page_generation import generate_pages_recursively

def main ():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"\ncurrent directory is: {current_dir}\n")
    
    project_root = os.path.dirname(current_dir)
    print(f"projects root is: {project_root}\n")
    
    source = os.path.join(project_root, "static")
    print(f"src_path is: {source}\n")

    destination = os.path.join(project_root, "public")
    print(f"destination path is: {destination}\n")

    content = os.path.join(project_root, "content")
    print(f"content path is: {content}\n")

    template = os.path.join(project_root, "template.html")
    print(f"template path is: {template}\n")

    print(f"preparing to delete destination directory...\n")

    prepare_destination_directory(destination)
    directory_copy(source, destination)

    
    generate_pages_recursively(content, template, destination)


if __name__ == "__main__":
    main()