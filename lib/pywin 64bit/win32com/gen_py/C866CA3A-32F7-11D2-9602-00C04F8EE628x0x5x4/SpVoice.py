# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 2.6.5 (r265:79096, Mar 19 2010, 18:02:59) [MSC v.1500 64 bit (AMD64)]
# From type library '{C866CA3A-32F7-11D2-9602-00C04F8EE628}'
# On Wed Jan 23 16:28:35 2013
'Microsoft Speech Object Library'
makepy_version = '0.5.01'
python_version = 0x20605f0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{C866CA3A-32F7-11D2-9602-00C04F8EE628}')
MajorVersion = 5
MinorVersion = 4
LibraryFlags = 8
LCID = 0x0

from win32com.client import CoClassBaseClass
import sys
__import__('win32com.gen_py.C866CA3A-32F7-11D2-9602-00C04F8EE628x0x5x4._ISpeechVoiceEvents')
_ISpeechVoiceEvents = sys.modules['win32com.gen_py.C866CA3A-32F7-11D2-9602-00C04F8EE628x0x5x4._ISpeechVoiceEvents']._ISpeechVoiceEvents
__import__('win32com.gen_py.C866CA3A-32F7-11D2-9602-00C04F8EE628x0x5x4.ISpeechVoice')
ISpeechVoice = sys.modules['win32com.gen_py.C866CA3A-32F7-11D2-9602-00C04F8EE628x0x5x4.ISpeechVoice'].ISpeechVoice
# This CoClass is known by the name 'SAPI.SpVoice.1'
class SpVoice(CoClassBaseClass): # A CoClass
	# SpVoice Class
	CLSID = IID('{96749377-3391-11D2-9EE3-00C04F797396}')
	coclass_sources = [
		_ISpeechVoiceEvents,
	]
	default_source = _ISpeechVoiceEvents
	coclass_interfaces = [
		ISpeechVoice,
	]
	default_interface = ISpeechVoice

win32com.client.CLSIDToClass.RegisterCLSID( "{96749377-3391-11D2-9EE3-00C04F797396}", SpVoice )
