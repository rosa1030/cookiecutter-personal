import os
import re
import sys
import shutil
from filecmp import clear_cache

project_slug = "{{ cookiecutter.project_slug }}"

REQUIRED_TOOLS = ["git", "conda"]

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

def check_system_requirements():
    for tool in REQUIRED_TOOLS:
        if shutil.which(tool) is None:
            print(f"{ERROR_COLOR}ERROR: {tool} is required but not found. Please install it before continuing.{RESET_ALL}")
            return False
    return True

# Verificar que el nombre del proyecto no contenga caracteres especiales
if not re.match(r'^[a-zA-Z0-9_]+$', project_slug):
    print(f"{ERROR_COLOR}ERROR: {project_slug} is not a valid name for this template. "
          f"Only letters, numbers, and underscores are allowed.{RESET_ALL}")
    sys.exit(1)

if not check_system_requirements():
    sys.exit(1)

print(f"{MESSAGE_COLOR}All system requirements are met. Let's continue with the project creation process!")
print(f"Creating project at {os.getcwd()}{RESET_ALL}")


