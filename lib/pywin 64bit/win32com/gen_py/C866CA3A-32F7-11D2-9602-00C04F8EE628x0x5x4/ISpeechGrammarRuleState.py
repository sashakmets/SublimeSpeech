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
class ISpeechGrammarRuleState(DispatchBaseClass):
	'ISpeechGrammarRuleState Interface'
	CLSID = IID('{D4286F2C-EE67-45AE-B928-28D695362EDA}')
	coclass_clsid = None

	def AddRuleTransition(self, DestinationState=defaultNamedNotOptArg, Rule=defaultNamedNotOptArg, PropertyName=u'', PropertyId=0
			, PropertyValue=u'', Weight=1.0):
		'AddRuleTransition'
		return self._ApplyTypes_(4, 1, (24, 32), ((9, 1), (9, 1), (8, 49), (3, 49), (16396, 49), (4, 49)), u'AddRuleTransition', None,DestinationState
			, Rule, PropertyName, PropertyId, PropertyValue, Weight
			)

	def AddSpecialTransition(self, DestinationState=defaultNamedNotOptArg, Type=defaultNamedNotOptArg, PropertyName=u'', PropertyId=0
			, PropertyValue=u'', Weight=1.0):
		'AddSpecialTransition'
		return self._ApplyTypes_(5, 1, (24, 32), ((9, 1), (3, 1), (8, 49), (3, 49), (16396, 49), (4, 49)), u'AddSpecialTransition', None,DestinationState
			, Type, PropertyName, PropertyId, PropertyValue, Weight
			)

	def AddWordTransition(self, DestState=defaultNamedNotOptArg, Words=defaultNamedNotOptArg, Separators=u' ', Type=1
			, PropertyName=u'', PropertyId=0, PropertyValue=u'', Weight=1.0):
		'AddWordTransition'
		return self._ApplyTypes_(3, 1, (24, 32), ((9, 1), (8, 1), (8, 49), (3, 49), (8, 49), (3, 49), (16396, 49), (4, 49)), u'AddWordTransition', None,DestState
			, Words, Separators, Type, PropertyName, PropertyId
			, PropertyValue, Weight)

	_prop_map_get_ = {
		# Method 'Rule' returns object of type 'ISpeechGrammarRule'
		"Rule": (1, 2, (9, 0), (), "Rule", '{AFE719CF-5DD1-44F2-999C-7A399F1CFCCC}'),
		# Method 'Transitions' returns object of type 'ISpeechGrammarRuleStateTransitions'
		"Transitions": (2, 2, (9, 0), (), "Transitions", '{EABCE657-75BC-44A2-AA7F-C56476742963}'),
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

win32com.client.CLSIDToClass.RegisterCLSID( "{D4286F2C-EE67-45AE-B928-28D695362EDA}", ISpeechGrammarRuleState )
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

ISpeechGrammarRuleState_vtables_dispatch_ = 1
ISpeechGrammarRuleState_vtables_ = [
	(( u'Rule' , u'Rule' , ), 1, (1, (), [ (16393, 10, None, "IID('{AFE719CF-5DD1-44F2-999C-7A399F1CFCCC}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'Transitions' , u'Transitions' , ), 2, (2, (), [ (16393, 10, None, "IID('{EABCE657-75BC-44A2-AA7F-C56476742963}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'AddWordTransition' , u'DestState' , u'Words' , u'Separators' , u'Type' , 
			u'PropertyName' , u'PropertyId' , u'PropertyValue' , u'Weight' , ), 3, (3, (), [ 
			(9, 1, None, "IID('{D4286F2C-EE67-45AE-B928-28D695362EDA}')") , (8, 1, None, None) , (8, 49, "u' '", None) , (3, 49, '1', None) , (8, 49, "u''", None) , 
			(3, 49, '0', None) , (16396, 49, "u''", None) , (4, 49, '1.0', None) , ], 1 , 1 , 4 , 0 , 72 , (3, 32, None, None) , 0 , )),
	(( u'AddRuleTransition' , u'DestinationState' , u'Rule' , u'PropertyName' , u'PropertyId' , 
			u'PropertyValue' , u'Weight' , ), 4, (4, (), [ (9, 1, None, "IID('{D4286F2C-EE67-45AE-B928-28D695362EDA}')") , (9, 1, None, "IID('{AFE719CF-5DD1-44F2-999C-7A399F1CFCCC}')") , 
			(8, 49, "u''", None) , (3, 49, '0', None) , (16396, 49, "u''", None) , (4, 49, '1.0', None) , ], 1 , 1 , 4 , 0 , 80 , (3, 32, None, None) , 0 , )),
	(( u'AddSpecialTransition' , u'DestinationState' , u'Type' , u'PropertyName' , u'PropertyId' , 
			u'PropertyValue' , u'Weight' , ), 5, (5, (), [ (9, 1, None, "IID('{D4286F2C-EE67-45AE-B928-28D695362EDA}')") , (3, 1, None, None) , 
			(8, 49, "u''", None) , (3, 49, '0', None) , (16396, 49, "u''", None) , (4, 49, '1.0', None) , ], 1 , 1 , 4 , 0 , 88 , (3, 32, None, None) , 0 , )),
]

win32com.client.CLSIDToClass.RegisterCLSID( "{D4286F2C-EE67-45AE-B928-28D695362EDA}", ISpeechGrammarRuleState )
