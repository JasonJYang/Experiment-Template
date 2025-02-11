import sys
from pathlib import Path
from shutil import copytree, ignore_patterns

# This script initializes new pytorch project with the template files.
# Run `python3 new_project.py ../MyNewProject` then new project named 
# MyNewProject will be made
current_dir = Path()
assert (current_dir / 'new_project.py').is_file(), 'Script should be executed in the pytorch-template directory'
assert len(sys.argv) == 2, 'Specify a name for the new project. Example: python3 new_project.py MyNewProject'

project_name = Path(sys.argv[1])
target_dir = current_dir / project_name

def custom_ignore_patterns(path, names):
    ignore = [".git", "new_project.py", "LICENSE", ".flake8", "__pycache__"]
    if path == str(current_dir):
        ignore.append("README.md")
    return ignore

copytree(current_dir, target_dir, ignore=custom_ignore_patterns)
print('New project initialized at', target_dir.absolute().resolve())