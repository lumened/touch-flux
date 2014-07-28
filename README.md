touch-flux
==========

Standalone application that provides an interface to control XBMC. GUI is rendered using `pygame`. 
To start the application, run `python touch-flux` from outside the repository or `python __main__.py` from the repository root.

This application is intended to run on the PiTFT touchscreen with Raspbmc or Raspbian + XBMC. 

The setup folder also contains an Upstart daemon that can automatically start this application on boot before XBMC.

###Application UI

This is the main control screen that provides navigation control.

<img src="https://raw.githubusercontent.com/lumened/touch-flux/master/screenshots/screen1.png">

Buttons in clockwise order starting from the top left are:

- Switch to Playback Control Menu (Only available when something is playing)
- Switch to Camera Control Menu (Camera support to be added)
- Back button
- Power Menu (To be added)
- The central button is the Select/Enter button with the surrounding keys being the navigation keys.

This is the playback control menu which is activated only when some media (audio/video) is playing.

<img src="https://raw.githubusercontent.com/lumened/touch-flux/master/screenshots/screen2.png">

Elements starting from top left are:
- Status information about the currently playing track
- Button to switch to navigation menu
- Progress bar for media
- Media keys (Stop, Forward, Rewind, Volume Down, Volume Up, Play/Pause)

Power Menu also present that has the ability to shutdown the system. Also, integrated with [BattMonitor](https://github.com/lumened/battmonitor), to show battery readings and state of the system.

