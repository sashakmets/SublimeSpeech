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
class ISpeechRecognizer(DispatchBaseClass):
	'ISpeechRecognizer Interface'
	CLSID = IID('{2D5F1C0C-BD75-4B08-9478-3B11FEA2586C}')
	coclass_clsid = IID('{41B89B6B-9399-11D2-9623-00C04F8EE628}')

	# Result is of type ISpeechRecoContext
	def CreateRecoContext(self):
		'CreateRecoContext'
		ret = self._oleobj_.InvokeTypes(10, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, u'CreateRecoContext', '{580AA49D-7E1E-4809-B8E2-57DA806104B8}')
		return ret

	def DisplayUI(self, hWndParent=defaultNamedNotOptArg, Title=defaultNamedNotOptArg, TypeOfUI=defaultNamedNotOptArg, ExtraData=u''):
		'DisplayUI'
		return self._ApplyTypes_(17, 1, (24, 32), ((3, 1), (8, 1), (8, 1), (16396, 49)), u'DisplayUI', None,hWndParent
			, Title, TypeOfUI, ExtraData)

	def EmulateRecognition(self, TextElements=defaultNamedNotOptArg, ElementDisplayAttributes=u'', LanguageId=0):
		'EmulateRecognition'
		return self._ApplyTypes_(9, 1, (24, 32), ((12, 1), (16396, 49), (3, 49)), u'EmulateRecognition', None,TextElements
			, ElementDisplayAttributes, LanguageId)

	# Result is of type ISpeechObjectTokens
	def GetAudioInputs(self, RequiredAttributes=u'', OptionalAttributes=u''):
		'GetAudioInputs'
		return self._ApplyTypes_(19, 1, (9, 32), ((8, 49), (8, 49)), u'GetAudioInputs', '{9285B776-2E7B-4BC0-B53E-580EB6FA967F}',RequiredAttributes
			, OptionalAttributes)

	# Result is of type ISpeechAudioFormat
	def GetFormat(self, Type=defaultNamedNotOptArg):
		'GetFormat'
		ret = self._oleobj_.InvokeTypes(11, LCID, 1, (9, 0), ((3, 1),),Type
			)
		if ret is not None:
			ret = Dispatch(ret, u'GetFormat', '{E6E9C590-3E18-40E3-8299-061F98BDE7C7}')
		return ret

	# Result is of type ISpeechObjectTokens
	def GetProfiles(self, RequiredAttributes=u'', OptionalAttributes=u''):
		'GetProfiles'
		return self._ApplyTypes_(20, 1, (9, 32), ((8, 49), (8, 49)), u'GetProfiles', '{9285B776-2E7B-4BC0-B53E-580EB6FA967F}',RequiredAttributes
			, OptionalAttributes)

	def GetPropertyNumber(self, Name=defaultNamedNotOptArg, Value=defaultNamedNotOptArg):
		'GetPropertyNumber'
		return self._ApplyTypes_(13, 1, (11, 0), ((8, 1), (16387, 3)), u'GetPropertyNumber', None,Name
			, Value)

	def GetPropertyString(self, Name=defaultNamedNotOptArg, Value=defaultNamedNotOptArg):
		'GetPropertyString'
		return self._ApplyTypes_(15, 1, (11, 0), ((8, 1), (16392, 3)), u'GetPropertyString', None,Name
			, Value)

	# Result is of type ISpeechObjectTokens
	def GetRecognizers(self, RequiredAttributes=u'', OptionalAttributes=u''):
		'GetRecognizers'
		return self._ApplyTypes_(18, 1, (9, 32), ((8, 49), (8, 49)), u'GetRecognizers', '{9285B776-2E7B-4BC0-B53E-580EB6FA967F}',RequiredAttributes
			, OptionalAttributes)

	def IsUISupported(self, TypeOfUI=defaultNamedNotOptArg, ExtraData=u''):
		'IsUISupported'
		return self._ApplyTypes_(16, 1, (11, 32), ((8, 1), (16396, 49)), u'IsUISupported', None,TypeOfUI
			, ExtraData)

	def SetPropertyNumber(self, Name=defaultNamedNotOptArg, Value=defaultNamedNotOptArg):
		'SetPropertyNumber'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), ((8, 1), (3, 1)),Name
			, Value)

	def SetPropertyString(self, Name=defaultNamedNotOptArg, Value=defaultNamedNotOptArg):
		'SetPropertyString'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (11, 0), ((8, 1), (8, 1)),Name
			, Value)

	_prop_map_get_ = {
		"AllowAudioInputFormatChangesOnNextSet": (2, 2, (11, 0), (), "AllowAudioInputFormatChangesOnNextSet", None),
		# Method 'AudioInput' returns object of type 'ISpeechObjectToken'
		"AudioInput": (3, 2, (9, 0), (), "AudioInput", '{C74A3ADC-B727-4500-A84A-B526721C8B8C}'),
		# Method 'AudioInputStream' returns object of type 'ISpeechBaseStream'
		"AudioInputStream": (4, 2, (9, 0), (), "AudioInputStream", '{6450336F-7D49-4CED-8097-49D6DEE37294}'),
		"IsShared": (5, 2, (11, 0), (), "IsShared", None),
		# Method 'Profile' returns object of type 'ISpeechObjectToken'
		"Profile": (8, 2, (9, 0), (), "Profile", '{C74A3ADC-B727-4500-A84A-B526721C8B8C}'),
		# Method 'Recognizer' returns object of type 'ISpeechObjectToken'
		"Recognizer": (1, 2, (9, 0), (), "Recognizer", '{C74A3ADC-B727-4500-A84A-B526721C8B8C}'),
		"State": (6, 2, (3, 0), (), "State", None),
		# Method 'Status' returns object of type 'ISpeechRecognizerStatus'
		"Status": (7, 2, (9, 0), (), "Status", '{BFF9E781-53EC-484E-BB8A-0E1B5551E35C}'),
	}
	_prop_map_put_ = {
		"AllowAudioInputFormatChangesOnNextSet": ((2, LCID, 4, 0),()),
		"AudioInput": ((3, LCID, 8, 0),()),
		"AudioInputStream": ((4, LCID, 8, 0),()),
		"Profile": ((8, LCID, 8, 0),()),
		"Recognizer": ((1, LCID, 8, 0),()),
		"State": ((6, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

win32com.client.CLSIDToClass.RegisterCLSID( "{2D5F1C0C-BD75-4B08-9478-3B11FEA2586C}", ISpeechRecognizer )
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

ISpeechRecognizer_vtables_dispatch_ = 1
ISpeechRecognizer_vtables_ = [
	(( u'Recognizer' , u'Recognizer' , ), 1, (1, (), [ (9, 1, None, "IID('{C74A3ADC-B727-4500-A84A-B526721C8B8C}')") , ], 1 , 8 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'Recognizer' , u'Recognizer' , ), 1, (1, (), [ (16393, 10, None, "IID('{C74A3ADC-B727-4500-A84A-B526721C8B8C}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'AllowAudioInputFormatChangesOnNextSet' , u'Allow' , ), 2, (2, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 64 , )),
	(( u'AllowAudioInputFormatChangesOnNextSet' , u'Allow' , ), 2, (2, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 64 , )),
	(( u'AudioInput' , u'AudioInput' , ), 3, (3, (), [ (9, 49, '0', "IID('{C74A3ADC-B727-4500-A84A-B526721C8B8C}')") , ], 1 , 8 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'AudioInput' , u'AudioInput' , ), 3, (3, (), [ (16393, 10, None, "IID('{C74A3ADC-B727-4500-A84A-B526721C8B8C}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'AudioInputStream' , u'AudioInputStream' , ), 4, (4, (), [ (9, 49, '0', "IID('{6450336F-7D49-4CED-8097-49D6DEE37294}')") , ], 1 , 8 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'AudioInputStream' , u'AudioInputStream' , ), 4, (4, (), [ (16393, 10, None, "IID('{6450336F-7D49-4CED-8097-49D6DEE37294}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'IsShared' , u'Shared' , ), 5, (5, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'State' , u'State' , ), 6, (6, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'State' , u'State' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'Status' , u'Status' , ), 7, (7, (), [ (16393, 10, None, "IID('{BFF9E781-53EC-484E-BB8A-0E1B5551E35C}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'Profile' , u'Profile' , ), 8, (8, (), [ (9, 49, '0', "IID('{C74A3ADC-B727-4500-A84A-B526721C8B8C}')") , ], 1 , 8 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( u'Profile' , u'Profile' , ), 8, (8, (), [ (16393, 10, None, "IID('{C74A3ADC-B727-4500-A84A-B526721C8B8C}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( u'EmulateRecognition' , u'TextElements' , u'ElementDisplayAttributes' , u'LanguageId' , ), 9, (9, (), [ 
			(12, 1, None, None) , (16396, 49, "u''", None) , (3, 49, '0', None) , ], 1 , 1 , 4 , 0 , 168 , (3, 32, None, None) , 0 , )),
	(( u'CreateRecoContext' , u'NewContext' , ), 10, (10, (), [ (16393, 10, None, "IID('{580AA49D-7E1E-4809-B8E2-57DA806104B8}')") , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( u'GetFormat' , u'Type' , u'Format' , ), 11, (11, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{E6E9C590-3E18-40E3-8299-061F98BDE7C7}')") , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( u'SetPropertyNumber' , u'Name' , u'Value' , u'Supported' , ), 12, (12, (), [ 
			(8, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 64 , )),
	(( u'GetPropertyNumber' , u'Name' , u'Value' , u'Supported' , ), 13, (13, (), [ 
			(8, 1, None, None) , (16387, 3, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 64 , )),
	(( u'SetPropertyString' , u'Name' , u'Value' , u'Supported' , ), 14, (14, (), [ 
			(8, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 64 , )),
	(( u'GetPropertyString' , u'Name' , u'Value' , u'Supported' , ), 15, (15, (), [ 
			(8, 1, None, None) , (16392, 3, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 64 , )),
	(( u'IsUISupported' , u'TypeOfUI' , u'ExtraData' , u'Supported' , ), 16, (16, (), [ 
			(8, 1, None, None) , (16396, 49, "u''", None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 224 , (3, 32, None, None) , 0 , )),
	(( u'DisplayUI' , u'hWndParent' , u'Title' , u'TypeOfUI' , u'ExtraData' , 
			), 17, (17, (), [ (3, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (16396, 49, "u''", None) , ], 1 , 1 , 4 , 0 , 232 , (3, 32, None, None) , 0 , )),
	(( u'GetRecognizers' , u'RequiredAttributes' , u'OptionalAttributes' , u'ObjectTokens' , ), 18, (18, (), [ 
			(8, 49, "u''", None) , (8, 49, "u''", None) , (16393, 10, None, "IID('{9285B776-2E7B-4BC0-B53E-580EB6FA967F}')") , ], 1 , 1 , 4 , 0 , 240 , (3, 32, None, None) , 0 , )),
	(( u'GetAudioInputs' , u'RequiredAttributes' , u'OptionalAttributes' , u'ObjectTokens' , ), 19, (19, (), [ 
			(8, 49, "u''", None) , (8, 49, "u''", None) , (16393, 10, None, "IID('{9285B776-2E7B-4BC0-B53E-580EB6FA967F}')") , ], 1 , 1 , 4 , 0 , 248 , (3, 32, None, None) , 0 , )),
	(( u'GetProfiles' , u'RequiredAttributes' , u'OptionalAttributes' , u'ObjectTokens' , ), 20, (20, (), [ 
			(8, 49, "u''", None) , (8, 49, "u''", None) , (16393, 10, None, "IID('{9285B776-2E7B-4BC0-B53E-580EB6FA967F}')") , ], 1 , 1 , 4 , 0 , 256 , (3, 32, None, None) , 0 , )),
]

win32com.client.CLSIDToClass.RegisterCLSID( "{2D5F1C0C-BD75-4B08-9478-3B11FEA2586C}", ISpeechRecognizer )
