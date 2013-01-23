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
class ISpeechRecoResultDispatch(DispatchBaseClass):
	'ISpeechRecoResultDispatch Interface'
	CLSID = IID('{6D60EB64-ACED-40A6-BBF3-4E557F71DEE2}')
	coclass_clsid = None

	# Result is of type ISpeechPhraseAlternates
	def Alternates(self, RequestCount=defaultNamedNotOptArg, StartElement=0, Elements=-1):
		'Alternates'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), ((3, 1), (3, 49), (3, 49)),RequestCount
			, StartElement, Elements)
		if ret is not None:
			ret = Dispatch(ret, u'Alternates', '{B238B6D5-F276-4C3D-A6C1-2974801C3CC2}')
		return ret

	# Result is of type ISpeechMemoryStream
	def Audio(self, StartElement=0, Elements=-1):
		'Audio'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), ((3, 49), (3, 49)),StartElement
			, Elements)
		if ret is not None:
			ret = Dispatch(ret, u'Audio', '{EEB14B68-808B-4ABE-A5EA-B51DA7588008}')
		return ret

	def DiscardResultInfo(self, ValueTypes=defaultNamedNotOptArg):
		'DiscardResultInfo'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), ((3, 1),),ValueTypes
			)

	def GetXMLErrorInfo(self, LineNumber=pythoncom.Missing, ScriptLine=pythoncom.Missing, Source=pythoncom.Missing, Description=pythoncom.Missing
			, ResultCode=pythoncom.Missing):
		'GetXMLErrorInfo'
		return self._ApplyTypes_(11, 1, (11, 0), ((16387, 2), (16392, 2), (16392, 2), (16392, 2), (16387, 2)), u'GetXMLErrorInfo', None,LineNumber
			, ScriptLine, Source, Description, ResultCode)

	def GetXMLResult(self, Options=defaultNamedNotOptArg):
		'GetXMLResult'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(10, LCID, 1, (8, 0), ((3, 1),),Options
			)

	def SaveToMemory(self):
		'SaveToMemory'
		return self._ApplyTypes_(8, 1, (12, 0), (), u'SaveToMemory', None,)

	def SetTextFeedback(self, Feedback=defaultNamedNotOptArg, WasSuccessful=defaultNamedNotOptArg):
		'SetTextFeedback'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), ((8, 1), (11, 1)),Feedback
			, WasSuccessful)

	def SpeakAudio(self, StartElement=0, Elements=-1, Flags=0):
		'SpeakAudio'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (3, 0), ((3, 49), (3, 49), (3, 49)),StartElement
			, Elements, Flags)

	_prop_map_get_ = {
		# Method 'AudioFormat' returns object of type 'ISpeechAudioFormat'
		"AudioFormat": (3, 2, (9, 0), (), "AudioFormat", '{E6E9C590-3E18-40E3-8299-061F98BDE7C7}'),
		# Method 'PhraseInfo' returns object of type 'ISpeechPhraseInfo'
		"PhraseInfo": (4, 2, (9, 0), (), "PhraseInfo", '{961559CF-4E67-4662-8BF0-D93F1FCD61B3}'),
		# Method 'RecoContext' returns object of type 'ISpeechRecoContext'
		"RecoContext": (1, 2, (9, 0), (), "RecoContext", '{580AA49D-7E1E-4809-B8E2-57DA806104B8}'),
		# Method 'Times' returns object of type 'ISpeechRecoResultTimes'
		"Times": (2, 2, (9, 0), (), "Times", '{62B3B8FB-F6E7-41BE-BDCB-056B1C29EFC0}'),
	}
	_prop_map_put_ = {
		"AudioFormat": ((3, LCID, 8, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

win32com.client.CLSIDToClass.RegisterCLSID( "{6D60EB64-ACED-40A6-BBF3-4E557F71DEE2}", ISpeechRecoResultDispatch )
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

ISpeechRecoResultDispatch_vtables_dispatch_ = 1
ISpeechRecoResultDispatch_vtables_ = [
	(( u'RecoContext' , u'RecoContext' , ), 1, (1, (), [ (16393, 10, None, "IID('{580AA49D-7E1E-4809-B8E2-57DA806104B8}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'Times' , u'Times' , ), 2, (2, (), [ (16393, 10, None, "IID('{62B3B8FB-F6E7-41BE-BDCB-056B1C29EFC0}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'AudioFormat' , u'Format' , ), 3, (3, (), [ (9, 1, None, "IID('{E6E9C590-3E18-40E3-8299-061F98BDE7C7}')") , ], 1 , 8 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'AudioFormat' , u'Format' , ), 3, (3, (), [ (16393, 10, None, "IID('{E6E9C590-3E18-40E3-8299-061F98BDE7C7}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'PhraseInfo' , u'PhraseInfo' , ), 4, (4, (), [ (16393, 10, None, "IID('{961559CF-4E67-4662-8BF0-D93F1FCD61B3}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'Alternates' , u'RequestCount' , u'StartElement' , u'Elements' , u'Alternates' , 
			), 5, (5, (), [ (3, 1, None, None) , (3, 49, '0', None) , (3, 49, '-1', None) , (16393, 10, None, "IID('{B238B6D5-F276-4C3D-A6C1-2974801C3CC2}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'Audio' , u'StartElement' , u'Elements' , u'Stream' , ), 6, (6, (), [ 
			(3, 49, '0', None) , (3, 49, '-1', None) , (16393, 10, None, "IID('{EEB14B68-808B-4ABE-A5EA-B51DA7588008}')") , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'SpeakAudio' , u'StartElement' , u'Elements' , u'Flags' , u'StreamNumber' , 
			), 7, (7, (), [ (3, 49, '0', None) , (3, 49, '-1', None) , (3, 49, '0', None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'SaveToMemory' , u'ResultBlock' , ), 8, (8, (), [ (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'DiscardResultInfo' , u'ValueTypes' , ), 9, (9, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'GetXMLResult' , u'Options' , u'pResult' , ), 10, (10, (), [ (3, 1, None, None) , 
			(16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'GetXMLErrorInfo' , u'LineNumber' , u'ScriptLine' , u'Source' , u'Description' , 
			u'ResultCode' , u'IsError' , ), 11, (11, (), [ (16387, 2, None, None) , (16392, 2, None, None) , 
			(16392, 2, None, None) , (16392, 2, None, None) , (16387, 2, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'SetTextFeedback' , u'Feedback' , u'WasSuccessful' , ), 12, (12, (), [ (8, 1, None, None) , 
			(11, 1, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
]

win32com.client.CLSIDToClass.RegisterCLSID( "{6D60EB64-ACED-40A6-BBF3-4E557F71DEE2}", ISpeechRecoResultDispatch )
