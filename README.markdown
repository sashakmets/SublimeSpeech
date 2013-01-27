SublimeSpeech
=============

English speech recognition plugin for Sublime Text 2.  
For Windows only.

Installation
------------
Install via Package Control. Or download from here, rename to "Speech" and put it in your "Packages" directory.

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
Full reference sheet is in file _reference.txt_  
You can say "What can i say" to open up this reference.

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

Not all functionality is available by speaking but simple application control and basic text editing is implemented.

Remember that you can train the recognizer to understand you better. This done in the control panel for speech recognition in Windows.

Note that status bar shows some info about speech recognition. For example it say "What was that?" if it can't understand you.

