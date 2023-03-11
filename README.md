## Demo

[<img src="https://img.youtube.com/vi/ipyWj7IY5g8/maxresdefault.jpg" width="50%">](https://youtu.be/ipyWj7IY5g8)

This program monitors a specified directory for new files and scans them for malware using the VirusTotal API. The API key needs to be provided by the user. The program checks the size of the file before uploading it for scanning, as the API is limited to files smaller than 50 MB. If a malicious file is detected, the program sends a notification to the user using the Zenity application, and the file is quarantined by setting its permissions to not executable. The program runs continuously in a loop and checks for new files every second.

## Installation

Step 1: Change your API key realtime.py

Step 2: Create binary
```
pyinstaller realtime.py --onefile
cd dist
```

Test binary
```
./realtime
```

## Auto start

Create a file ~/.config/autostart/av.desktop 
Change YOURPATH to wherever the executable is
```
[Desktop Entry]
Name=AvScan
GenericName=avscan
Comment=avscan with virustotal
Exec=/YOURPATH/av/dist/realtime
Terminal=false
Type=Application
X-GNOME-Autostart-enabled=true
```
