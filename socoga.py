#!/usr/bin/env python
import time
import datetime
import os
SOCOGA_DROPBOX_TOKEN = os.environ['SOCOGA_DROPBOX_TOKEN']

# Include the Dropbox SDK
import dropbox
from dropbox.client import DropboxClient

#Include Sonos Controller
from soco import SoCo
from soco import SonosDiscovery

platform = 'sonos'

def handleVolume(volume):
    # print "Handling Sonos Volume: Set to " + volume + "%"
    if platform == 'sonos':
        sonos_devices = SonosDiscovery()
        for ip in sonos_devices.get_speaker_ips():
            device = SoCo(ip)
            zone_name = device.get_speaker_info()['zone_name']
            # print "IP of %s is %s" % (zone_name, ip)

            # Set volume - divide final volume by 2 since 50% is the most natural listening volume
            device.volume(int(volume) / 2.0)
    return

def cleanup(path):
    print "Moving file to executed folder " + path
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H:%M:%S_')
    response = client.file_move(path, "/executed_commands/" + st + path[1:])
    return

# Create dropbox client object
client = DropboxClient(SOCOGA_DROPBOX_TOKEN)

# Check all the files in the app directory
folder_metadata = client.metadata("/")

# Handle SoCoGa Commands
if 'contents' in folder_metadata.keys():
    for files in folder_metadata['contents']:
        if "volume" in files['path']:
            # print files['path']
            for s in files['path'].split('.'):
                if s.isdigit():
                    # found the file we want
                    # print s
                    handleVolume(s)

            cleanup(files['path'])
