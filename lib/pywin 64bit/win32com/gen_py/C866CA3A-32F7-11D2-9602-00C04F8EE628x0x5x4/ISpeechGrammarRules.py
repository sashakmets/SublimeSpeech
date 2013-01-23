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
class ISpeechGrammarRules(DispatchBaseClass):
	'ISpeechGrammarRules Interface'
	CLSID = IID('{6FFA3B44-FC2D-40D1-8AFC-32911C7F1AD1}')
	coclass_clsid = None

	# Result is of type ISpeechGrammarRule
	def Add(self, RuleName=defaultNamedNotOptArg, Attributes=defaultNamedNotOptArg, RuleId=0):
		'Add'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), ((8, 1), (3, 1), (3, 49)),RuleName
			, Attributes, RuleId)
		if ret is not None:
			ret = Dispatch(ret, u'Add', '{AFE719CF-5DD1-44F2-999C-7A399F1CFCCC}')
		return ret

	def Commit(self):
		'Commit'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), (),)

	def CommitAndSave(self, ErrorText=pythoncom.Missing):
		'CommitAndSave'
		return self._ApplyTypes_(5, 1, (12, 0), ((16392, 2),), u'CommitAndSave', None,ErrorText
			)

	# Result is of type ISpeechGrammarRule
	def FindRule(self, RuleNameOrId=defaultNamedNotOptArg):
		'FindRule'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), ((12, 1),),RuleNameOrId
			)
		if ret is not None:
			ret = Dispatch(ret, u'FindRule', '{AFE719CF-5DD1-44F2-999C-7A399F1CFCCC}')
		return ret

	# Result is of type ISpeechGrammarRule
	def Item(self, Index=defaultNamedNotOptArg):
		'Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, u'Item', '{AFE719CF-5DD1-44F2-999C-7A399F1CFCCC}')
		return ret

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
		"Dynamic": (2, 2, (11, 0), (), "Dynamic", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{AFE719CF-5DD1-44F2-999C-7A399F1CFCCC}')
		return ret

	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{AFE719CF-5DD1-44F2-999C-7A399F1CFCCC}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

win32com.client.CLSIDToClass.RegisterCLSID( "{6FFA3B44-FC2D-40D1-8AFC-32911C7F1AD1}", ISpeechGrammarRules )
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

ISpeechGrammarRules_vtables_dispatch_ = 1
ISpeechGrammarRules_vtables_ = [
	(( u'Count' , u'Count' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'FindRule' , u'RuleNameOrId' , u'Rule' , ), 6, (6, (), [ (12, 1, None, None) , 
			(16393, 10, None, "IID('{AFE719CF-5DD1-44F2-999C-7A399F1CFCCC}')") , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'Item' , u'Index' , u'Rule' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{AFE719CF-5DD1-44F2-999C-7A399F1CFCCC}')") , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'_NewEnum' , u'EnumVARIANT' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 1 , )),
	(( u'Dynamic' , u'Dynamic' , ), 2, (2, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'Add' , u'RuleName' , u'Attributes' , u'RuleId' , u'Rule' , 
			), 3, (3, (), [ (8, 1, None, None) , (3, 1, None, None) , (3, 49, '0', None) , (16393, 10, None, "IID('{AFE719CF-5DD1-44F2-999C-7A399F1CFCCC}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'Commit' , ), 4, (4, (), [ ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'CommitAndSave' , u'ErrorText' , u'SaveStream' , ), 5, (5, (), [ (16392, 2, None, None) , 
			(16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

win32com.client.CLSIDToClass.RegisterCLSID( "{6FFA3B44-FC2D-40D1-8AFC-32911C7F1AD1}", ISpeechGrammarRules )
