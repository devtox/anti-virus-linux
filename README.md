
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
