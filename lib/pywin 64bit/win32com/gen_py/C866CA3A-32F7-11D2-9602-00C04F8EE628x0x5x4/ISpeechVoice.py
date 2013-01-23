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

from win32com.client import DispatchBaseClass
class ISpeechVoice(DispatchBaseClass):
	'ISpeechVoice Interface'
	CLSID = IID('{269316D8-57BD-11D2-9EEE-00C04F797396}')
	coclass_clsid = IID('{96749377-3391-11D2-9EE3-00C04F797396}')

	def DisplayUI(self, hWndParent=defaultNamedNotOptArg, Title=defaultNamedNotOptArg, TypeOfUI=defaultNamedNotOptArg, ExtraData=u''):
		'DisplayUI'
		return self._ApplyTypes_(22, 1, (24, 32), ((3, 1), (8, 1), (8, 1), (16396, 49)), u'DisplayUI', None,hWndParent
			, Title, TypeOfUI, ExtraData)

	# Result is of type ISpeechObjectTokens
	def GetAudioOutputs(self, RequiredAttributes=u'', OptionalAttributes=u''):
		'GetAudioOutputs'
		return self._ApplyTypes_(18, 1, (9, 32), ((8, 49), (8, 49)), u'GetAudioOutputs', '{9285B776-2E7B-4BC0-B53E-580EB6FA967F}',RequiredAttributes
			, OptionalAttributes)

	# Result is of type ISpeechObjectTokens
	def GetVoices(self, RequiredAttributes=u'', OptionalAttributes=u''):
		'GetVoices'
		return self._ApplyTypes_(17, 1, (9, 32), ((8, 49), (8, 49)), u'GetVoices', '{9285B776-2E7B-4BC0-B53E-580EB6FA967F}',RequiredAttributes
			, OptionalAttributes)

	def IsUISupported(self, TypeOfUI=defaultNamedNotOptArg, ExtraData=u''):
		'IsUISupported'
		return self._ApplyTypes_(21, 1, (11, 32), ((8, 1), (16396, 49)), u'IsUISupported', None,TypeOfUI
			, ExtraData)

	def Pause(self):
		'Pauses the voices rendering.'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), (),)

	def Resume(self):
		'Resumes the voices rendering.'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (24, 0), (),)

	def Skip(self, Type=defaultNamedNotOptArg, NumItems=defaultNamedNotOptArg):
		'Skips rendering the specified number of items.'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (3, 0), ((8, 1), (3, 1)),Type
			, NumItems)

	def Speak(self, Text=defaultNamedNotOptArg, Flags=0):
		'Speak'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (3, 0), ((8, 1), (3, 49)),Text
			, Flags)

	def SpeakCompleteEvent(self):
		'SpeakCompleteEvent'
		return self._oleobj_.InvokeTypes(20, LCID, 1, (3, 0), (),)

	def SpeakStream(self, Stream=defaultNamedNotOptArg, Flags=0):
		'SpeakStream'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (3, 0), ((9, 1), (3, 49)),Stream
			, Flags)

	def WaitUntilDone(self, msTimeout=defaultNamedNotOptArg):
		'WaitUntilDone'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (11, 0), ((3, 1),),msTimeout
			)

	_prop_map_get_ = {
		"AlertBoundary": (10, 2, (3, 0), (), "AlertBoundary", None),
		"AllowAudioOutputFormatChangesOnNextSet": (7, 2, (11, 0), (), "AllowAudioOutputFormatChangesOnNextSet", None),
		# Method 'AudioOutput' returns object of type 'ISpeechObjectToken'
		"AudioOutput": (3, 2, (9, 0), (), "AudioOutput", '{C74A3ADC-B727-4500-A84A-B526721C8B8C}'),
		# Method 'AudioOutputStream' returns object of type 'ISpeechBaseStream'
		"AudioOutputStream": (4, 2, (9, 0), (), "AudioOutputStream", '{6450336F-7D49-4CED-8097-49D6DEE37294}'),
		"EventInterests": (8, 2, (3, 0), (), "EventInterests", None),
		"Priority": (9, 2, (3, 0), (), "Priority", None),
		"Rate": (5, 2, (3, 0), (), "Rate", None),
		# Method 'Status' returns object of type 'ISpeechVoiceStatus'
		"Status": (1, 2, (9, 0), (), "Status", '{8BE47B07-57F6-11D2-9EEE-00C04F797396}'),
		"SynchronousSpeakTimeout": (11, 2, (3, 0), (), "SynchronousSpeakTimeout", None),
		# Method 'Voice' returns object of type 'ISpeechObjectToken'
		"Voice": (2, 2, (9, 0), (), "Voice", '{C74A3ADC-B727-4500-A84A-B526721C8B8C}'),
		"Volume": (6, 2, (3, 0), (), "Volume", None),
	}
	_prop_map_put_ = {
		"AlertBoundary": ((10, LCID, 4, 0),()),
		"AllowAudioOutputFormatChangesOnNextSet": ((7, LCID, 4, 0),()),
		"AudioOutput": ((3, LCID, 8, 0),()),
		"AudioOutputStream": ((4, LCID, 8, 0),()),
		"EventInterests": ((8, LCID, 4, 0),()),
		"Priority": ((9, LCID, 4, 0),()),
		"Rate": ((5, LCID, 4, 0),()),
		"SynchronousSpeakTimeout": ((11, LCID, 4, 0),()),
		"Voice": ((2, LCID, 8, 0),()),
		"Volume": ((6, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

win32com.client.CLSIDToClass.RegisterCLSID( "{269316D8-57BD-11D2-9EEE-00C04F797396}", ISpeechVoice )
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

ISpeechVoice_vtables_dispatch_ = 1
ISpeechVoice_vtables_ = [
	(( u'Status' , u'Status' , ), 1, (1, (), [ (16393, 10, None, "IID('{8BE47B07-57F6-11D2-9EEE-00C04F797396}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'Voice' , u'Voice' , ), 2, (2, (), [ (16393, 10, None, "IID('{C74A3ADC-B727-4500-A84A-B526721C8B8C}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'Voice' , u'Voice' , ), 2, (2, (), [ (9, 1, None, "IID('{C74A3ADC-B727-4500-A84A-B526721C8B8C}')") , ], 1 , 8 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'AudioOutput' , u'AudioOutput' , ), 3, (3, (), [ (16393, 10, None, "IID('{C74A3ADC-B727-4500-A84A-B526721C8B8C}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'AudioOutput' , u'AudioOutput' , ), 3, (3, (), [ (9, 1, None, "IID('{C74A3ADC-B727-4500-A84A-B526721C8B8C}')") , ], 1 , 8 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'AudioOutputStream' , u'AudioOutputStream' , ), 4, (4, (), [ (16393, 10, None, "IID('{6450336F-7D49-4CED-8097-49D6DEE37294}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'AudioOutputStream' , u'AudioOutputStream' , ), 4, (4, (), [ (9, 1, None, "IID('{6450336F-7D49-4CED-8097-49D6DEE37294}')") , ], 1 , 8 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'Rate' , u'Rate' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'Rate' , u'Rate' , ), 5, (5, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'Volume' , u'Volume' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'Volume' , u'Volume' , ), 6, (6, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'AllowAudioOutputFormatChangesOnNextSet' , u'Allow' , ), 7, (7, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 64 , )),
	(( u'AllowAudioOutputFormatChangesOnNextSet' , u'Allow' , ), 7, (7, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 64 , )),
	(( u'EventInterests' , u'EventInterestFlags' , ), 8, (8, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( u'EventInterests' , u'EventInterestFlags' , ), 8, (8, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( u'Priority' , u'Priority' , ), 9, (9, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( u'Priority' , u'Priority' , ), 9, (9, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( u'AlertBoundary' , u'Boundary' , ), 10, (10, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( u'AlertBoundary' , u'Boundary' , ), 10, (10, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( u'SynchronousSpeakTimeout' , u'msTimeout' , ), 11, (11, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( u'SynchronousSpeakTimeout' , u'msTimeout' , ), 11, (11, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( u'Speak' , u'Text' , u'Flags' , u'StreamNumber' , ), 12, (12, (), [ 
			(8, 1, None, None) , (3, 49, '0', None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( u'SpeakStream' , u'Stream' , u'Flags' , u'StreamNumber' , ), 13, (13, (), [ 
			(9, 1, None, "IID('{6450336F-7D49-4CED-8097-49D6DEE37294}')") , (3, 49, '0', None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( u'Pause' , ), 14, (14, (), [ ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( u'Resume' , ), 15, (15, (), [ ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( u'Skip' , u'Type' , u'NumItems' , u'NumSkipped' , ), 16, (16, (), [ 
			(8, 1, None, None) , (3, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( u'GetVoices' , u'RequiredAttributes' , u'OptionalAttributes' , u'ObjectTokens' , ), 17, (17, (), [ 
			(8, 49, "u''", None) , (8, 49, "u''", None) , (16393, 10, None, "IID('{9285B776-2E7B-4BC0-B53E-580EB6FA967F}')") , ], 1 , 1 , 4 , 0 , 264 , (3, 32, None, None) , 0 , )),
	(( u'GetAudioOutputs' , u'RequiredAttributes' , u'OptionalAttributes' , u'ObjectTokens' , ), 18, (18, (), [ 
			(8, 49, "u''", None) , (8, 49, "u''", None) , (16393, 10, None, "IID('{9285B776-2E7B-4BC0-B53E-580EB6FA967F}')") , ], 1 , 1 , 4 , 0 , 272 , (3, 32, None, None) , 0 , )),
	(( u'WaitUntilDone' , u'msTimeout' , u'Done' , ), 19, (19, (), [ (3, 1, None, None) , 
			(16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( u'SpeakCompleteEvent' , u'Handle' , ), 20, (20, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 64 , )),
	(( u'IsUISupported' , u'TypeOfUI' , u'ExtraData' , u'Supported' , ), 21, (21, (), [ 
			(8, 1, None, None) , (16396, 49, "u''", None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 296 , (3, 32, None, None) , 0 , )),
	(( u'DisplayUI' , u'hWndParent' , u'Title' , u'TypeOfUI' , u'ExtraData' , 
			), 22, (22, (), [ (3, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (16396, 49, "u''", None) , ], 1 , 1 , 4 , 0 , 304 , (3, 32, None, None) , 0 , )),
]

win32com.client.CLSIDToClass.RegisterCLSID( "{269316D8-57BD-11D2-9EEE-00C04F797396}", ISpeechVoice )
