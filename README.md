SoCoGa // Sonos Controller for Google Home
====

SoCoGa (Sonos Controller + Google Assistant) is a simple Python script that to allows you to
 control [Sonos speakers]() with simple voice commands from your [Google Home](). It is based on the open source [SoCo project]() and works in conjunction with [Google Assistant (Google Home)](), [IFTTT](), and [Dropbox]().


IFTTT applets
------------

Current working applets (Note: the word "set" is a GA override so alternative verbs must be used):
- [Volume: "turn Sonos volume to #"]()

Future:
- Toggle speech enhancement
- Toggle night Mode


Installation
------------

SoCoGa requires a Python script to run continuously on the same local network as the Sonos you would like to control. I recommend using a [Home Assistant]() automation running on an ethernet connected Raspberry Pi, but theoretically this will work on any device that can run Python.

This process takes about 20 minutes so buckle up!

First you will need to create a personal dropbox app by signing up at https://www.dropbox.com/developers/apps/. Sign up using the following steps:
1. Click "Create app"
2. Select "Dropbox Api"
3. Select "App Folder"
4. Enter a name your personal app - the name doesn't matter but will be used as the **[dropbox-app-name]** variable in the IFTTT applet.


Next, generate a personal token by following the instructions [here](https://blogs.dropbox.com/developers/2014/05/generate-an-access-token-for-your-own-account/) which will you will need to paste in for the **[dropbox-token]** in socoga.py.

Now add one of the applets listed [above]() to your IFTTT account. Once you have connected your dropbox account, edit the applet so that the file path matches your **[dropbox-app-name]**. E.g. "Apps/SoCoGa"

![alt dropbox](dropbox-folderpath.png)


Once your apps are setup, its time to setup your device that will run the script.

 On your unix device, install [SoCo]():

``pip install soco``

``pip install requests``

Install dropbox on the device (you may need to reboot at this point):

``pip install dropbox``

Finally, setup the socoga.py script:

Create your dropbox environment variable:

``export SOCOGA_DROPBOX_TOKEN=[dropbox-token]``

Using your preferred method, setup the socoga.py script to run continuously at a set interval on your device, I've found 3 seconds works just fine.

If you choose to use [Home Assistant](), you can do this by following the [install instructions](), then clone this repo into your /.homeassisant directory, and lastly add the following automation to your configuration.yaml file:

```
shell_command:
  alias: "Sonos volume setter script"
  socoga: "python /home/homeassistant/.homeassistant/socoga/socoga.py"

automation:
  alias: "Control Sonos from Google Home"
  initial_state: True
  hide_entity: False
  trigger:
    platform: time
    seconds: /3
  action:
    service: shell_command.socoga
```

If everything worked correctly it should look like this:

![alt homeassistant](homeassistant-example.png)

Congratulations, you should now have the script up and running on your local network. Try saying "Hey Google, turn the Sonos volume to 50" to test it out.


Contributing
------------

This project was put together after about a day of hacking, if there is a feature you would like, something you think might be more efficient, or if you just have an edit for this readme - pull requests are very welcomed.


License
-------

SoCoGa is released under the [MIT license](http://www.opensource.org/licenses/mit-license.php).

SoCoGa includes code from [SoCo](https://github.com/SoCo/SoCo), which is licensed under the [MIT license](http://www.opensource.org/licenses/mit-license.php).
