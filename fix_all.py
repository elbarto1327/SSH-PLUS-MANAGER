import os
import shutil
import re

base_dir = r"c:\Users\ruanr\Downloads\SSH-PLUS-MANAGER-main"

# 1. Delete duplicated folder and my temp scripts
nested_folder = os.path.join(base_dir, "SSH-PLUS-MANAGER-main")
if os.path.exists(nested_folder):
    shutil.rmtree(nested_folder)

for script in ["translate.py", "replace_urls.py", "replace_username.py"]:
    f = os.path.join(base_dir, script)
    if os.path.exists(f):
        os.remove(f)

# 2. Fix CRLF to LF in specific files, plus all bash scripts just to be safe
def to_lf(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'rb') as f:
        content = f.read()
    content = content.replace(b'\r\n', b'\n')
    with open(filepath, 'wb') as f:
        f.write(content)

for f in ["Plus", "Install/list", "Modules/menu", "Modules/conexao"]:
    to_lf(os.path.join(base_dir, f))

for root, _, files in os.walk(os.path.join(base_dir, "Modules")):
    for file in files:
        to_lf(os.path.join(root, file))

# 3. Fix syntax error in expcleaner
expcleaner_path = os.path.join(base_dir, "Modules", "expcleaner")
if os.path.exists(expcleaner_path):
    with open(expcleaner_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    content = content.replace('echo "EXPIRED WAS REMOVED""', 'echo "EXPIRED WAS REMOVED"')
    with open(expcleaner_path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)

# 4. Fix tab/space in open.py and proxy.py (replace tabs with 4 spaces)
for pyfile in ["open.py", "proxy.py"]:
    path = os.path.join(base_dir, "Modules", pyfile)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        content = content.replace('\t', '    ')
        with open(path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(content)

# 5. Fix Plus encoding / text
# The user mentioned broken encoding like (Ã—, â• etc.).
# These are ANSI borders like ════ and ≠×≠×≠×
# It happened because PowerShell's Set-Content or Out-File used a different encoding.
# I will download Plus fresh, apply translations and fixes, and save it in UTF-8 without BOM.
