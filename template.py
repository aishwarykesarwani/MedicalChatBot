import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

# / for mac/linux 
# \ for windows
list_of_files= [
    "src/_init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    #"requirements.txt",
    "setup.py",
    "app.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    ## / for mac and \ for windows problem will be solved by Path() Robust code


    filedir, filename = os.path.split(filepath)
    # convert src/__init__.py in tuple of filedir,filename
    # incase of tt.py tuple with ('',tt.py) filefir is ""

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
                                        # This check if anything is written or not in that file else don't delte
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")