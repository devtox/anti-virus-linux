
<video src='https://www.youtube.com/watch?v=ipyWj7IY5g8' width=180/>

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
