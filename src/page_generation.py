from block_parser import markdown_to_html_node, extract_title
import os


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from 'from_path' to 'dest_path' using 'template_path'\n")

    markdown_content = None
    template = None

    with open(from_path, 'r') as file:
        markdown_content = file.read()
    
    with open(template_path, 'r') as file:
        template = file.read()
    
    html_string = markdown_to_html_node(markdown_content)
    title = extract_title(markdown_content)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_string)

    output_file = os.path.join(dest_path, "index.html")
    
    with open(output_file, 'w') as file:
        file.write(template)

def generate_pages_recursively(dir_path_content, template_path, dest_dir_path):
    for item in os.listdir(dir_path_content): 
        if os.path.isfile(os.path.join(dir_path_content, item)):
            generate_page(os.path.join(dir_path_content, item), template_path, dest_dir_path)
            continue
        else:
            new_dst = os.path.join(dest_dir_path, item)
            os.makedirs(new_dst, exist_ok=True)
            generate_pages_recursively(os.path.join(dir_path_content, item), template_path, new_dst)
