## Real-Time AV for Linux

This program monitors a specified directory for new files and scans them for malware using the VirusTotal API. The API key needs to be provided by the user. The program checks the size of the file before uploading it for scanning, as the API is limited to files smaller than 50 MB. 

If a malicious file is detected, the program sends a notification to the user using the Zenity application, and the file is quarantined by setting its permissions to not executable. The program runs continuously in a loop and checks for new files every second.

Click to watch video
[<img src="https://img.youtube.com/vi/ipyWj7IY5g8/maxresdefault.jpg" width="50%">](https://youtu.be/ipyWj7IY5g8)

## How many Virus Databases?

VirusTotal.com uses multiple virus databases to scan files for malware. Mar 2023, VirusTotal.com is using more than 70 different antivirus engines and malware scanners from various security companies and open-source projects to scan files for malware. However, the number of antivirus engines and malware scanners that VirusTotal.com uses may have changed since then.

## Why not use ClamAV?

One reason to use VirusTotal.com instead of ClamAV is that VirusTotal.com uses multiple antivirus engines and malware scanners to detect malware, which increases the likelihood of detecting malicious files. 

I created a malicious program that completely takes over the computer using Kali Linux (Reverse Shell, meterpreter). ClamAV was unable to detect it, but this program does. 

## But my Linux is secure and I can't get hacked!@

Like any other operating system, Linux is vulnerable to security threats such as viruses, malware, and hacking attempts. Here are some examples of how Linux systems can be compromised:

1. Malware: Malware is any software designed to harm a computer system, and it can infect Linux systems just as easily as it can infect Windows or macOS systems. Some common types of Linux malware include trojan horses, backdoors, and rootkits.

2. Phishing: Phishing is a social engineering attack where attackers trick users into divulging sensitive information or installing malware by posing as a trustworthy entity. Linux users can fall victim to phishing attacks just like any other users.

3. Remote access tools: Remote access tools like VNC, SSH, or RDP can be used by attackers to gain unauthorized access to a Linux system. Attackers can use these tools to execute commands, steal data, or install malware.

4. Reverse shells: A reverse shell is a type of shell that allows attackers to control a compromised system from a remote location. Attackers can use reverse shells to execute commands, download files, and exfiltrate data.

5. Exploits: Vulnerabilities in software or hardware can be exploited by attackers to gain access to a Linux system. Attackers can use exploits to execute arbitrary code, escalate privileges, or gain access to sensitive data.

6. Password attacks: Password attacks can be used to gain access to Linux systems by brute-forcing or guessing weak passwords. Attackers can also use stolen or leaked credentials to gain access to systems.

Learn: [Password Cracking: Brute Forcing](https://www.udemy.com/course/password-cracking-brute-forcing/)

These are just some examples of how Linux systems can be compromised. It's important to take steps to secure your Linux systems, such as keeping software up to date, using strong passwords, and using security tools like firewalls and antivirus software.

## Limitations

This program has some limitations

1. Only scans ~/Downloads directory (but you can change in code)
2. VirusTotal.com API allows maximal 4 files per second
3. No more than 500 checks a day (with free API)

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
