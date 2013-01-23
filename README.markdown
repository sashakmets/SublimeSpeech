SublimeSpeech
=============

Speech recognition plugin for Sublime Text 2  
NOTE: Windows only since it uses Windows SAPI!  
Understands only english.  

Requirements
------------
You need to have the english language pack for Windows installed and enabled. If the UI you are seeing is in english, everything's set and you don't have to do anything.

The language pack can be downloaded from Windows Update if you need it.

Modes
-----
The recognizer can be in three modes:

* _Turned on_: self-explanatory
* _Turned off_: Totally turned off, doesn't even run in the background. You must manually turn it back on after this
* _Sleeping_: In sleep mode the recognizer still runs but doesn't respond to any other commands than "wake up" or "turn off".

Key bindings
------------
`ctrl+shift+o` Wakes up the recognizer if it's sleeping. Otherwise turns it on/off.

Speech Commands
---------------
There's no full reference available yet but you can look all the commands from _speech.py_ file. Syntax there is quite intuitive but you can also look the full syntax from [dragonfly](https://code.google.com/p/dragonfly/), the framework this plugin is built on.

Here are some example commands you can give:

* Command: _say &lt;text&gt;_  
  Example: _say write this down_  
  Result: prints _write this down_
* Command: _minimap_  
  Result: toggles minimap on/off
* Command: _translate to tabs_  
  Result: converts indentation to tabs
* Command: _turn off_  
  Result: turns the recognizer off
* Command: _new file_  
  Result: opens a new file
* Command: _set syntax &lt;language&gt;_  
  Example: _set syntax python_  
  Result: sets syntax to python for the current file

Not all functionality is available by speaking since there are so many commands in Sublime Text 2. However speech commands are great! Don't remember the shortcut for the action you want to do? Just speak it! Chances are you'll remember the speech command since they are intuitive and resemble their corresponding actions.

Remember that you can train the recognizer to understand you better. This done in the control panel for speech recognition in Windows.

Note that status bar shows some info about speech recognition. For example it say "What was that?" if it can't understand you.

