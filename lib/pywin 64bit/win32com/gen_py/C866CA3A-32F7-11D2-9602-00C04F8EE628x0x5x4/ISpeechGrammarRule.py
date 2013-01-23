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
class ISpeechGrammarRule(DispatchBaseClass):
	'ISpeechGrammarRule Interface'
	CLSID = IID('{AFE719CF-5DD1-44F2-999C-7A399F1CFCCC}')
	coclass_clsid = None

	def AddResource(self, ResourceName=defaultNamedNotOptArg, ResourceValue=defaultNamedNotOptArg):
		'AddResource'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), ((8, 1), (8, 1)),ResourceName
			, ResourceValue)

	# Result is of type ISpeechGrammarRuleState
	def AddState(self):
		'AddState'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, u'AddState', '{D4286F2C-EE67-45AE-B928-28D695362EDA}')
		return ret

	def Clear(self):
		'Clear'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Attributes": (1, 2, (3, 0), (), "Attributes", None),
		"Id": (4, 2, (3, 0), (), "Id", None),
		# Method 'InitialState' returns object of type 'ISpeechGrammarRuleState'
		"InitialState": (2, 2, (9, 0), (), "InitialState", '{D4286F2C-EE67-45AE-B928-28D695362EDA}'),
		"Name": (3, 2, (8, 0), (), "Name", None),
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

win32com.client.CLSIDToClass.RegisterCLSID( "{AFE719CF-5DD1-44F2-999C-7A399F1CFCCC}", ISpeechGrammarRule )
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

ISpeechGrammarRule_vtables_dispatch_ = 1
ISpeechGrammarRule_vtables_ = [
	(( u'Attributes' , u'Attributes' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'InitialState' , u'State' , ), 2, (2, (), [ (16393, 10, None, "IID('{D4286F2C-EE67-45AE-B928-28D695362EDA}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'Name' , u'Name' , ), 3, (3, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'Id' , u'Id' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'Clear' , ), 5, (5, (), [ ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'AddResource' , u'ResourceName' , u'ResourceValue' , ), 6, (6, (), [ (8, 1, None, None) , 
			(8, 1, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'AddState' , u'State' , ), 7, (7, (), [ (16393, 10, None, "IID('{D4286F2C-EE67-45AE-B928-28D695362EDA}')") , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

win32com.client.CLSIDToClass.RegisterCLSID( "{AFE719CF-5DD1-44F2-999C-7A399F1CFCCC}", ISpeechGrammarRule )
