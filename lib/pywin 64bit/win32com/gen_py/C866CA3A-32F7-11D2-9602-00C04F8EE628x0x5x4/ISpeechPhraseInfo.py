# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 2.6.5 (r265:79096, Mar 19 2010, 18:02:59) [MSC v.1500 64 bit (AMD64)]
# From type library '{C866CA3A-32F7-11D2-9602-00C04F8EE628}'
# On Wed Jan 23 16:37:09 2013
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
class ISpeechPhraseInfo(DispatchBaseClass):
	'ISpeechPhraseInfo Interface'
	CLSID = IID('{961559CF-4E67-4662-8BF0-D93F1FCD61B3}')
	coclass_clsid = None

	def GetDisplayAttributes(self, StartElement=0, Elements=-1, UseReplacements=True):
		'DisplayAttributes'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (3, 0), ((3, 49), (3, 49), (11, 49)),StartElement
			, Elements, UseReplacements)

	def GetText(self, StartElement=0, Elements=-1, UseReplacements=True):
		'GetText'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(15, LCID, 1, (8, 0), ((3, 49), (3, 49), (11, 49)),StartElement
			, Elements, UseReplacements)

	def SaveToMemory(self):
		'SaveToMemory'
		return self._ApplyTypes_(14, 1, (12, 0), (), u'SaveToMemory', None,)

	_prop_map_get_ = {
		"AudioSizeBytes": (5, 2, (3, 0), (), "AudioSizeBytes", None),
		"AudioSizeTime": (7, 2, (3, 0), (), "AudioSizeTime", None),
		"AudioStreamPosition": (4, 2, (12, 0), (), "AudioStreamPosition", None),
		# Method 'Elements' returns object of type 'ISpeechPhraseElements'
		"Elements": (10, 2, (9, 0), (), "Elements", '{0626B328-3478-467D-A0B3-D0853B93DDA3}'),
		"EngineId": (12, 2, (8, 0), (), "EngineId", None),
		"EnginePrivateData": (13, 2, (12, 0), (), "EnginePrivateData", None),
		"GrammarId": (2, 2, (12, 0), (), "GrammarId", None),
		"LanguageId": (1, 2, (3, 0), (), "LanguageId", None),
		# Method 'Properties' returns object of type 'ISpeechPhraseProperties'
		"Properties": (9, 2, (9, 0), (), "Properties", '{08166B47-102E-4B23-A599-BDB98DBFD1F4}'),
		# Method 'Replacements' returns object of type 'ISpeechPhraseReplacements'
		"Replacements": (11, 2, (9, 0), (), "Replacements", '{38BC662F-2257-4525-959E-2069D2596C05}'),
		"RetainedSizeBytes": (6, 2, (3, 0), (), "RetainedSizeBytes", None),
		# Method 'Rule' returns object of type 'ISpeechPhraseRule'
		"Rule": (8, 2, (9, 0), (), "Rule", '{A7BFE112-A4A0-48D9-B602-C313843F6964}'),
		"StartTime": (3, 2, (12, 0), (), "StartTime", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

win32com.client.CLSIDToClass.RegisterCLSID( "{961559CF-4E67-4662-8BF0-D93F1FCD61B3}", ISpeechPhraseInfo )
# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 2.6.5 (r265:79096, Mar 19 2010, 18:02:59) [MSC v.1500 64 bit (AMD64)]
# From type library '{C866CA3A-32F7-11D2-9602-00C04F8EE628}'
# On Wed Jan 23 16:37:09 2013
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

ISpeechPhraseInfo_vtables_dispatch_ = 1
ISpeechPhraseInfo_vtables_ = [
	(( u'LanguageId' , u'LanguageId' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'GrammarId' , u'GrammarId' , ), 2, (2, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'StartTime' , u'StartTime' , ), 3, (3, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'AudioStreamPosition' , u'AudioStreamPosition' , ), 4, (4, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'AudioSizeBytes' , u'pAudioSizeBytes' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'RetainedSizeBytes' , u'RetainedSizeBytes' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'AudioSizeTime' , u'AudioSizeTime' , ), 7, (7, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'Rule' , u'Rule' , ), 8, (8, (), [ (16393, 10, None, "IID('{A7BFE112-A4A0-48D9-B602-C313843F6964}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'Properties' , u'Properties' , ), 9, (9, (), [ (16393, 10, None, "IID('{08166B47-102E-4B23-A599-BDB98DBFD1F4}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'Elements' , u'Elements' , ), 10, (10, (), [ (16393, 10, None, "IID('{0626B328-3478-467D-A0B3-D0853B93DDA3}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'Replacements' , u'Replacements' , ), 11, (11, (), [ (16393, 10, None, "IID('{38BC662F-2257-4525-959E-2069D2596C05}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'EngineId' , u'EngineIdGuid' , ), 12, (12, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'EnginePrivateData' , u'PrivateData' , ), 13, (13, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( u'SaveToMemory' , u'PhraseBlock' , ), 14, (14, (), [ (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( u'GetText' , u'StartElement' , u'Elements' , u'UseReplacements' , u'Text' , 
			), 15, (15, (), [ (3, 49, '0', None) , (3, 49, '-1', None) , (11, 49, 'True', None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( u'GetDisplayAttributes' , u'StartElement' , u'Elements' , u'UseReplacements' , u'DisplayAttributes' , 
			), 16, (16, (), [ (3, 49, '0', None) , (3, 49, '-1', None) , (11, 49, 'True', None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
]

win32com.client.CLSIDToClass.RegisterCLSID( "{961559CF-4E67-4662-8BF0-D93F1FCD61B3}", ISpeechPhraseInfo )
