# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 2.6.5 (r265:79096, Mar 19 2010, 18:02:59) [MSC v.1500 64 bit (AMD64)]
# From type library '{C866CA3A-32F7-11D2-9602-00C04F8EE628}'
# On Wed Jan 23 16:28:38 2013
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
class ISpeechRecoContext(DispatchBaseClass):
	'ISpeechRecoContext Interface'
	CLSID = IID('{580AA49D-7E1E-4809-B8E2-57DA806104B8}')
	coclass_clsid = IID('{73AD6842-ACE0-45E8-A4DD-8795881A2C2A}')

	def Bookmark(self, Options=defaultNamedNotOptArg, StreamPos=defaultNamedNotOptArg, BookmarkId=defaultNamedNotOptArg):
		'Bookmark'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (24, 0), ((3, 1), (12, 1), (12, 1)),Options
			, StreamPos, BookmarkId)

	# Result is of type ISpeechRecoGrammar
	def CreateGrammar(self, GrammarId=0):
		'CreateGrammar'
		ret = self._oleobj_.InvokeTypes(14, LCID, 1, (9, 0), ((12, 49),),GrammarId
			)
		if ret is not None:
			ret = Dispatch(ret, u'CreateGrammar', '{B6D6F79F-2158-4E50-B5BC-9A9CCD852A09}')
		return ret

	# Result is of type ISpeechRecoResult
	def CreateResultFromMemory(self, ResultBlock=defaultNamedNotOptArg):
		'CreateResultFromMemory'
		ret = self._oleobj_.InvokeTypes(15, LCID, 1, (9, 0), ((16396, 1),),ResultBlock
			)
		if ret is not None:
			ret = Dispatch(ret, u'CreateResultFromMemory', '{ED2879CF-CED9-4EE6-A534-DE0191D5468D}')
		return ret

	def Pause(self):
		'Pause'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), (),)

	def Resume(self):
		'Resume'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), (),)

	def SetAdaptationData(self, AdaptationString=defaultNamedNotOptArg):
		'SetAdaptationData'
		return self._oleobj_.InvokeTypes(17, LCID, 1, (24, 0), ((8, 1),),AdaptationString
			)

	_prop_map_get_ = {
		"AllowVoiceFormatMatchingOnNextSet": (5, 2, (11, 0), (), "AllowVoiceFormatMatchingOnNextSet", None),
		"AudioInputInterferenceStatus": (2, 2, (3, 0), (), "AudioInputInterferenceStatus", None),
		"CmdMaxAlternates": (8, 2, (3, 0), (), "CmdMaxAlternates", None),
		"EventInterests": (7, 2, (3, 0), (), "EventInterests", None),
		# Method 'Recognizer' returns object of type 'ISpeechRecognizer'
		"Recognizer": (1, 2, (9, 0), (), "Recognizer", '{2D5F1C0C-BD75-4B08-9478-3B11FEA2586C}'),
		"RequestedUIType": (3, 2, (8, 0), (), "RequestedUIType", None),
		"RetainedAudio": (10, 2, (3, 0), (), "RetainedAudio", None),
		# Method 'RetainedAudioFormat' returns object of type 'ISpeechAudioFormat'
		"RetainedAudioFormat": (11, 2, (9, 0), (), "RetainedAudioFormat", '{E6E9C590-3E18-40E3-8299-061F98BDE7C7}'),
		"State": (9, 2, (3, 0), (), "State", None),
		# Method 'Voice' returns object of type 'ISpeechVoice'
		"Voice": (4, 2, (9, 0), (), "Voice", '{269316D8-57BD-11D2-9EEE-00C04F797396}'),
		"VoicePurgeEvent": (6, 2, (3, 0), (), "VoicePurgeEvent", None),
	}
	_prop_map_put_ = {
		"AllowVoiceFormatMatchingOnNextSet": ((5, LCID, 4, 0),()),
		"CmdMaxAlternates": ((8, LCID, 4, 0),()),
		"EventInterests": ((7, LCID, 4, 0),()),
		"RetainedAudio": ((10, LCID, 4, 0),()),
		"RetainedAudioFormat": ((11, LCID, 8, 0),()),
		"State": ((9, LCID, 4, 0),()),
		"Voice": ((4, LCID, 8, 0),()),
		"VoicePurgeEvent": ((6, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

win32com.client.CLSIDToClass.RegisterCLSID( "{580AA49D-7E1E-4809-B8E2-57DA806104B8}", ISpeechRecoContext )
# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 2.6.5 (r265:79096, Mar 19 2010, 18:02:59) [MSC v.1500 64 bit (AMD64)]
# From type library '{C866CA3A-32F7-11D2-9602-00C04F8EE628}'
# On Wed Jan 23 16:28:38 2013
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

ISpeechRecoContext_vtables_dispatch_ = 1
ISpeechRecoContext_vtables_ = [
	(( u'Recognizer' , u'Recognizer' , ), 1, (1, (), [ (16393, 10, None, "IID('{2D5F1C0C-BD75-4B08-9478-3B11FEA2586C}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'AudioInputInterferenceStatus' , u'Interference' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'RequestedUIType' , u'UIType' , ), 3, (3, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'Voice' , u'Voice' , ), 4, (4, (), [ (9, 1, None, "IID('{269316D8-57BD-11D2-9EEE-00C04F797396}')") , ], 1 , 8 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'Voice' , u'Voice' , ), 4, (4, (), [ (16393, 10, None, "IID('{269316D8-57BD-11D2-9EEE-00C04F797396}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'AllowVoiceFormatMatchingOnNextSet' , u'pAllow' , ), 5, (5, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 64 , )),
	(( u'AllowVoiceFormatMatchingOnNextSet' , u'pAllow' , ), 5, (5, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 64 , )),
	(( u'VoicePurgeEvent' , u'EventInterest' , ), 6, (6, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'VoicePurgeEvent' , u'EventInterest' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'EventInterests' , u'EventInterest' , ), 7, (7, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'EventInterests' , u'EventInterest' , ), 7, (7, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'CmdMaxAlternates' , u'MaxAlternates' , ), 8, (8, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'CmdMaxAlternates' , u'MaxAlternates' , ), 8, (8, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( u'State' , u'State' , ), 9, (9, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( u'State' , u'State' , ), 9, (9, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( u'RetainedAudio' , u'Option' , ), 10, (10, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( u'RetainedAudio' , u'Option' , ), 10, (10, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( u'RetainedAudioFormat' , u'Format' , ), 11, (11, (), [ (9, 1, None, "IID('{E6E9C590-3E18-40E3-8299-061F98BDE7C7}')") , ], 1 , 8 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( u'RetainedAudioFormat' , u'Format' , ), 11, (11, (), [ (16393, 10, None, "IID('{E6E9C590-3E18-40E3-8299-061F98BDE7C7}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( u'Pause' , ), 12, (12, (), [ ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( u'Resume' , ), 13, (13, (), [ ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( u'CreateGrammar' , u'GrammarId' , u'Grammar' , ), 14, (14, (), [ (12, 49, '0', None) , 
			(16393, 10, None, "IID('{B6D6F79F-2158-4E50-B5BC-9A9CCD852A09}')") , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( u'CreateResultFromMemory' , u'ResultBlock' , u'Result' , ), 15, (15, (), [ (16396, 1, None, None) , 
			(16393, 10, None, "IID('{ED2879CF-CED9-4EE6-A534-DE0191D5468D}')") , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( u'Bookmark' , u'Options' , u'StreamPos' , u'BookmarkId' , ), 16, (16, (), [ 
			(3, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( u'SetAdaptationData' , u'AdaptationString' , ), 17, (17, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
]

win32com.client.CLSIDToClass.RegisterCLSID( "{580AA49D-7E1E-4809-B8E2-57DA806104B8}", ISpeechRecoContext )
