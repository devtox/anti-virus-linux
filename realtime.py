import os
import time
import requests 
import sys

# The Public API is limited to 500 requests per day and
# a rate of 4 requests per minute.
# Get one on virustotal.com
API_KEY = 'YOUR API KEY HERE'

# Set the path of the directory to monitor
path = os.path.join(os.path.expanduser('~'), 'Downloads')

scan_result = ""

def is_file_smaller_than_50mb(file_path):
    file_size = os.path.getsize(file_path)
    if file_size < 50 * 1024 * 1024:
        return True
    else:
        return False
    
def scan_file(file_path):
    global scan_result 
    scan_result = ''

    # Upload the file to VirusTotal
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': API_KEY}
    files = {'file': (file_path, open(file_path, 'rb'))}
    response = requests.post(url, files=files, params=params)

    # Get the resource ID for the uploaded file
    resource_id = response.json()['resource']

    # Check the scan report for the uploaded file
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {'apikey': API_KEY, 'resource': resource_id}
    response = requests.get(url, params=params)

    # Print the scan report
    if response.status_code == 200:
        json_response = response.json()
        if json_response['response_code'] == 1:
            positives = json_response['positives']
            total = json_response['total']
            if positives > 0:
                scan_result = f'{file_path} is malicious! ({positives}/{total} detections)'
                print(f'{file_path} is malicious! ({positives}/{total} detections)')
                return True,positives,total
            else:
                print(f'{file_path} is clean. ({total} scans performed)')
                return False
        else:
            print(f'Error: {json_response["verbose_msg"]}')
            return False
    else:
        print('Error: Could not retrieve scan report')
        return False


# Update the start time to the current time
start_time = time.time()

# Start the main loop
while True:
    # Sleep for 1 seconds before checking for new files
    time.sleep(1)

    # Get the list of files in the directory (recursively)
    new_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            new_files.append(os.path.join(root, file))

    # Check if there are any new files
    for new_file in new_files:
        if os.path.getctime(new_file) > start_time:
            print(f"New file detected: {new_file}")

            if is_file_smaller_than_50mb(new_file):
                if scan_file(new_file):
                    print('Malicious ' + new_file)
                    #os.system("notify-send 'MALWARE DETECTED!' " + new_file + " --expire-time=10000")
                    #os.system("notify-send 'MALWARE DETECTED!' '" + scan_result + "' --expire-time=60000")
                    os.system('zenity --error --text="' + scan_result + '" --no-wrap') 

                    # quarantine file, make not executable
                    os.chmod(new_file, 0o644) 


    # Update the start time to the current time
    start_time = time.time()

