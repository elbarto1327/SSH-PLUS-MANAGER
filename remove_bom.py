import os

base_dir = r"c:\Users\ruanr\Downloads\SSH-PLUS-MANAGER-main"

def remove_bom(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'rb') as f:
        content = f.read()
    if content.startswith(b'\xef\xbb\xbf'):
        content = content[3:]
        with open(filepath, 'wb') as f:
            f.write(content)
        print(f"Removed BOM from {filepath}")

remove_bom(os.path.join(base_dir, "Plus"))
remove_bom(os.path.join(base_dir, "README.md"))
remove_bom(os.path.join(base_dir, "Modules", "menu"))
remove_bom(os.path.join(base_dir, "Install", "list"))
