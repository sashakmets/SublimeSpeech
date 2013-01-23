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
class ISpeechPhraseRule(DispatchBaseClass):
	'ISpeechPhraseRule Interface'
	CLSID = IID('{A7BFE112-A4A0-48D9-B602-C313843F6964}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Children' returns object of type 'ISpeechPhraseRules'
		"Children": (6, 2, (9, 0), (), "Children", '{9047D593-01DD-4B72-81A3-E4A0CA69F407}'),
		"Confidence": (7, 2, (3, 0), (), "Confidence", None),
		"EngineConfidence": (8, 2, (4, 0), (), "EngineConfidence", None),
		"FirstElement": (3, 2, (3, 0), (), "FirstElement", None),
		"Id": (2, 2, (3, 0), (), "Id", None),
		"Name": (1, 2, (8, 0), (), "Name", None),
		"NumberOfElements": (4, 2, (3, 0), (), "NumberOfElements", None),
		# Method 'Parent' returns object of type 'ISpeechPhraseRule'
		"Parent": (5, 2, (9, 0), (), "Parent", '{A7BFE112-A4A0-48D9-B602-C313843F6964}'),
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

win32com.client.CLSIDToClass.RegisterCLSID( "{A7BFE112-A4A0-48D9-B602-C313843F6964}", ISpeechPhraseRule )
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

ISpeechPhraseRule_vtables_dispatch_ = 1
ISpeechPhraseRule_vtables_ = [
	(( u'Name' , u'Name' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'Id' , u'Id' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'FirstElement' , u'FirstElement' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'NumberOfElements' , u'NumberOfElements' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'Parent' , u'Parent' , ), 5, (5, (), [ (16393, 10, None, "IID('{A7BFE112-A4A0-48D9-B602-C313843F6964}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'Children' , u'Children' , ), 6, (6, (), [ (16393, 10, None, "IID('{9047D593-01DD-4B72-81A3-E4A0CA69F407}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'Confidence' , u'ActualConfidence' , ), 7, (7, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'EngineConfidence' , u'EngineConfidence' , ), 8, (8, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

win32com.client.CLSIDToClass.RegisterCLSID( "{A7BFE112-A4A0-48D9-B602-C313843F6964}", ISpeechPhraseRule )
