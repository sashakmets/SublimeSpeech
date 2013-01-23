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
class ISpeechPhraseElement(DispatchBaseClass):
	'ISpeechPhraseElement Interface'
	CLSID = IID('{E6176F96-E373-4801-B223-3B62C068C0B4}')
	coclass_clsid = None

	_prop_map_get_ = {
		"ActualConfidence": (12, 2, (3, 0), (), "ActualConfidence", None),
		"AudioSizeBytes": (4, 2, (3, 0), (), "AudioSizeBytes", None),
		"AudioSizeTime": (2, 2, (3, 0), (), "AudioSizeTime", None),
		"AudioStreamOffset": (3, 2, (3, 0), (), "AudioStreamOffset", None),
		"AudioTimeOffset": (1, 2, (3, 0), (), "AudioTimeOffset", None),
		"DisplayAttributes": (10, 2, (3, 0), (), "DisplayAttributes", None),
		"DisplayText": (7, 2, (8, 0), (), "DisplayText", None),
		"EngineConfidence": (13, 2, (4, 0), (), "EngineConfidence", None),
		"LexicalForm": (8, 2, (8, 0), (), "LexicalForm", None),
		"Pronunciation": (9, 2, (12, 0), (), "Pronunciation", None),
		"RequiredConfidence": (11, 2, (3, 0), (), "RequiredConfidence", None),
		"RetainedSizeBytes": (6, 2, (3, 0), (), "RetainedSizeBytes", None),
		"RetainedStreamOffset": (5, 2, (3, 0), (), "RetainedStreamOffset", None),
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

win32com.client.CLSIDToClass.RegisterCLSID( "{E6176F96-E373-4801-B223-3B62C068C0B4}", ISpeechPhraseElement )
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

ISpeechPhraseElement_vtables_dispatch_ = 1
ISpeechPhraseElement_vtables_ = [
	(( u'AudioTimeOffset' , u'AudioTimeOffset' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'AudioSizeTime' , u'AudioSizeTime' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'AudioStreamOffset' , u'AudioStreamOffset' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'AudioSizeBytes' , u'AudioSizeBytes' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'RetainedStreamOffset' , u'RetainedStreamOffset' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'RetainedSizeBytes' , u'RetainedSizeBytes' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'DisplayText' , u'DisplayText' , ), 7, (7, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'LexicalForm' , u'LexicalForm' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'Pronunciation' , u'Pronunciation' , ), 9, (9, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'DisplayAttributes' , u'DisplayAttributes' , ), 10, (10, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'RequiredConfidence' , u'RequiredConfidence' , ), 11, (11, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'ActualConfidence' , u'ActualConfidence' , ), 12, (12, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'EngineConfidence' , u'EngineConfidence' , ), 13, (13, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
]

win32com.client.CLSIDToClass.RegisterCLSID( "{E6176F96-E373-4801-B223-3B62C068C0B4}", ISpeechPhraseElement )
