"""
Evernote doesn't allow mass exporting, or the exporting of stacks - but it does allow you to export whole notebooks containing groups of notes

This package converts these files to Markdown: https://github.com/wormi4ok/evernote2md

However, when exporting this package spits every single note into a separate markdown file into a single folder, with no structure at all

This script will preserve those notebooks (ENEX files) and run the script on each, putting them into a named folder.

Stacks will still need to be re-merged but this is far easier than grouping all the files.

To sync with your phone, you can use Google Drive and the Android App "Drive Sync" with a green/yellow/blue hollow circle, create a local folder on your phone and hook it up to sync. (works fast + as desired)
"""

import sys
import os
from pathlib import Path

def batch_enex_to_md(evernote2md_exe_path: str, enex_input_dir: str, md_output_dir: str, flags: str="")->None:
    """ The Evernote2md package converts evernote .enex files to MD. However, it doesn't retain folder structure for the notebooks.
        Therefore, this script will run the evernote2md command for each of the .enex files to its respective folder in the output dir

    Args:
        enex_input_dir (str): path of folder holding enex files (must exist with files)
        md_output_dir (str): path for output location (created if not exist)
        flags (str, optional): evernote2md flags. Defaults to "".

    Returns:
        None: Prints output and modifies files
    """
    EXE_PATH = Path(evernote2md_exe_path)
    ENEX_DIR = Path(enex_input_dir)
    MD_DIR = Path(md_output_dir)
    if not EXE_PATH.is_file(): return print(f"The evernote2md executable path, {evernote2md_exe_path} doesn\'t exist.")
    if not ENEX_DIR.is_dir(): return print(f"Enex input directory, {enex_input_dir} doesn\'t exist.")
    if not MD_DIR.is_dir(): MD_DIR.mkdir(parents=True)

    files_changed = 0
    incompatible_files = []

    for file in ENEX_DIR.iterdir():
        if file.suffix != '.enex':
            incompatible_files.append(file)
        else:
            executable = EXE_PATH.absolute().as_posix()
            file_to_change = file.absolute().as_posix()
            folder_to_write = MD_DIR.joinpath(file.stem).absolute().as_posix()
            os.system(f""" {executable} "{file_to_change}" "{folder_to_write}" """)
            files_changed+=1

    print(str(files_changed)+' files exported to '+md_output_dir)
    if incompatible_files: print(f"Ignored {len(incompatible_files)} files with incorrect formats: ", incompatible_files)

    return

evernote2md_path = r"C:\\Users\\USER\\Documents\\evernote2md.exe"
enex_dir = r"C:\\Users\\USER\\Documents\\EvernoteEnex"
md_dir = r"C:\\Users\\USER\\Documents\\EvernoteMarkdown"

batch_enex_to_md(evernote2md_path, enex_dir, md_dir)
