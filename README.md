# EvernoteToMarkdownRetainFolders
Script for converting Evernote to Markdown using evernote2md, which preserves the structure of notebooks in folders

____

Evernote doesn't allow mass exporting, or the exporting of stacks - but it does allow you to export whole notebooks containing groups of notes

This package converts these files to Markdown: https://github.com/wormi4ok/evernote2md

However, when exporting this package spits every single note into a separate markdown file into a single folder, with no structure at all

This script will preserve those notebooks (ENEX files) and run the script on each, putting them into a named folder.

Stacks will still need to be re-merged but this is far easier than grouping all the files.

To sync with your phone, you can use Google Drive and the Android App "Drive Sync" with a green/yellow/blue hollow circle, create a local folder on your phone and hook it up to sync. (works fast + as desired)
