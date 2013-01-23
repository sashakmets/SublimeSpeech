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
class ISpeechRecoGrammar(DispatchBaseClass):
	'ISpeechRecoGrammar Interface'
	CLSID = IID('{B6D6F79F-2158-4E50-B5BC-9A9CCD852A09}')
	coclass_clsid = None

	def CmdLoadFromFile(self, FileName=defaultNamedNotOptArg, LoadOption=0):
		'CmdLoadFromFile'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (24, 0), ((8, 1), (3, 49)),FileName
			, LoadOption)

	def CmdLoadFromMemory(self, GrammarData=defaultNamedNotOptArg, LoadOption=0):
		'CmdLoadFromMemory'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), ((12, 1), (3, 49)),GrammarData
			, LoadOption)

	def CmdLoadFromObject(self, ClassId=defaultNamedNotOptArg, GrammarName=defaultNamedNotOptArg, LoadOption=0):
		'CmdLoadFromObject'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), ((8, 1), (8, 1), (3, 49)),ClassId
			, GrammarName, LoadOption)

	def CmdLoadFromProprietaryGrammar(self, ProprietaryGuid=defaultNamedNotOptArg, ProprietaryString=defaultNamedNotOptArg, ProprietaryData=defaultNamedNotOptArg, LoadOption=0):
		'CmdLoadFromProprietaryGrammar'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), ((8, 1), (8, 1), (12, 1), (3, 49)),ProprietaryGuid
			, ProprietaryString, ProprietaryData, LoadOption)

	def CmdLoadFromResource(self, hModule=defaultNamedNotOptArg, ResourceName=defaultNamedNotOptArg, ResourceType=defaultNamedNotOptArg, LanguageId=defaultNamedNotOptArg
			, LoadOption=0):
		'CmdLoadFromResource'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), ((3, 1), (12, 1), (12, 1), (3, 1), (3, 49)),hModule
			, ResourceName, ResourceType, LanguageId, LoadOption)

	def CmdSetRuleIdState(self, RuleId=defaultNamedNotOptArg, State=defaultNamedNotOptArg):
		'CmdSetRuleIdState'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), ((3, 1), (3, 1)),RuleId
			, State)

	def CmdSetRuleState(self, Name=defaultNamedNotOptArg, State=defaultNamedNotOptArg):
		'CmdSetRuleState'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), ((8, 1), (3, 1)),Name
			, State)

	def DictationLoad(self, TopicName=u'', LoadOption=0):
		'DictationLoad'
		return self._ApplyTypes_(14, 1, (24, 32), ((8, 49), (3, 49)), u'DictationLoad', None,TopicName
			, LoadOption)

	def DictationSetState(self, State=defaultNamedNotOptArg):
		'DictationSetState'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (24, 0), ((3, 1),),State
			)

	def DictationUnload(self):
		'DictationUnload'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (24, 0), (),)

	def IsPronounceable(self, Word=defaultNamedNotOptArg):
		'IsPronounceable'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (3, 0), ((8, 1),),Word
			)

	def Reset(self, NewLanguage=0):
		'Reset'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), ((3, 49),),NewLanguage
			)

	def SetTextSelection(self, Info=defaultNamedNotOptArg):
		'SetTextSelection'
		return self._oleobj_.InvokeTypes(18, LCID, 1, (24, 0), ((9, 1),),Info
			)

	def SetWordSequenceData(self, Text=defaultNamedNotOptArg, TextLength=defaultNamedNotOptArg, Info=defaultNamedNotOptArg):
		'SetWordSequenceData'
		return self._oleobj_.InvokeTypes(17, LCID, 1, (24, 0), ((8, 1), (3, 1), (9, 1)),Text
			, TextLength, Info)

	_prop_map_get_ = {
		"Id": (1, 2, (12, 0), (), "Id", None),
		# Method 'RecoContext' returns object of type 'ISpeechRecoContext'
		"RecoContext": (2, 2, (9, 0), (), "RecoContext", '{580AA49D-7E1E-4809-B8E2-57DA806104B8}'),
		# Method 'Rules' returns object of type 'ISpeechGrammarRules'
		"Rules": (4, 2, (9, 0), (), "Rules", '{6FFA3B44-FC2D-40D1-8AFC-32911C7F1AD1}'),
		"State": (3, 2, (3, 0), (), "State", None),
	}
	_prop_map_put_ = {
		"State": ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

win32com.client.CLSIDToClass.RegisterCLSID( "{B6D6F79F-2158-4E50-B5BC-9A9CCD852A09}", ISpeechRecoGrammar )
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

ISpeechRecoGrammar_vtables_dispatch_ = 1
ISpeechRecoGrammar_vtables_ = [
	(( u'Id' , u'Id' , ), 1, (1, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'RecoContext' , u'RecoContext' , ), 2, (2, (), [ (16393, 10, None, "IID('{580AA49D-7E1E-4809-B8E2-57DA806104B8}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'State' , u'State' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'State' , u'State' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'Rules' , u'Rules' , ), 4, (4, (), [ (16393, 10, None, "IID('{6FFA3B44-FC2D-40D1-8AFC-32911C7F1AD1}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'Reset' , u'NewLanguage' , ), 5, (5, (), [ (3, 49, '0', None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'CmdLoadFromFile' , u'FileName' , u'LoadOption' , ), 7, (7, (), [ (8, 1, None, None) , 
			(3, 49, '0', None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'CmdLoadFromObject' , u'ClassId' , u'GrammarName' , u'LoadOption' , ), 8, (8, (), [ 
			(8, 1, None, None) , (8, 1, None, None) , (3, 49, '0', None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'CmdLoadFromResource' , u'hModule' , u'ResourceName' , u'ResourceType' , u'LanguageId' , 
			u'LoadOption' , ), 9, (9, (), [ (3, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , 
			(3, 1, None, None) , (3, 49, '0', None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'CmdLoadFromMemory' , u'GrammarData' , u'LoadOption' , ), 10, (10, (), [ (12, 1, None, None) , 
			(3, 49, '0', None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'CmdLoadFromProprietaryGrammar' , u'ProprietaryGuid' , u'ProprietaryString' , u'ProprietaryData' , u'LoadOption' , 
			), 11, (11, (), [ (8, 1, None, None) , (8, 1, None, None) , (12, 1, None, None) , (3, 49, '0', None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'CmdSetRuleState' , u'Name' , u'State' , ), 12, (12, (), [ (8, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'CmdSetRuleIdState' , u'RuleId' , u'State' , ), 13, (13, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( u'DictationLoad' , u'TopicName' , u'LoadOption' , ), 14, (14, (), [ (8, 49, "u''", None) , 
			(3, 49, '0', None) , ], 1 , 1 , 4 , 0 , 160 , (3, 32, None, None) , 0 , )),
	(( u'DictationUnload' , ), 15, (15, (), [ ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( u'DictationSetState' , u'State' , ), 16, (16, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( u'SetWordSequenceData' , u'Text' , u'TextLength' , u'Info' , ), 17, (17, (), [ 
			(8, 1, None, None) , (3, 1, None, None) , (9, 1, None, "IID('{3B9C7E7A-6EEE-4DED-9092-11657279ADBE}')") , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( u'SetTextSelection' , u'Info' , ), 18, (18, (), [ (9, 1, None, "IID('{3B9C7E7A-6EEE-4DED-9092-11657279ADBE}')") , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( u'IsPronounceable' , u'Word' , u'WordPronounceable' , ), 19, (19, (), [ (8, 1, None, None) , 
			(16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
]

win32com.client.CLSIDToClass.RegisterCLSID( "{B6D6F79F-2158-4E50-B5BC-9A9CCD852A09}", ISpeechRecoGrammar )
