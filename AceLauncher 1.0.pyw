import subprocess;
from os import path;
import tkinter as tk
from tkinter import simpledialog

acepath = '%APPDATA%\\ACEStream\\engine\\ace_engine.exe'
if '%' in acepath:
    acepath = path.expandvars(acepath)

subprocess.Popen(acepath, shell=True);

root = tk.Tk()
root.withdraw()

aceID = simpledialog.askstring(prompt="\tPaste AceStream ID here:\t\t", title="AceLauncher")

if aceID is not None:
    aceURL = ' http://127.0.0.1:6878/ace/getstream?id=';
    aceURL += aceID;
    subprocess.run('"C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"' + aceURL, shell=True);
