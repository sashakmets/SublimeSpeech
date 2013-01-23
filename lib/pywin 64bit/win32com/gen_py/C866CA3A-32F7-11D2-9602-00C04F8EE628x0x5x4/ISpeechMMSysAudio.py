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
class ISpeechMMSysAudio(DispatchBaseClass):
	'ISpeechMMSysAudio Interface'
	CLSID = IID('{3C76AF6D-1FD7-4831-81D1-3B71D5A13C44}')
	coclass_clsid = IID('{CF3D2E50-53F2-11D2-960C-00C04F8EE628}')

	def Read(self, Buffer=pythoncom.Missing, NumberOfBytes=defaultNamedNotOptArg):
		'Read'
		return self._ApplyTypes_(2, 1, (3, 0), ((16396, 2), (3, 1)), u'Read', None,Buffer
			, NumberOfBytes)

	def Seek(self, Position=defaultNamedNotOptArg, Origin=0):
		'Seek'
		return self._ApplyTypes_(4, 1, (12, 0), ((12, 1), (3, 49)), u'Seek', None,Position
			, Origin)

	def SetState(self, State=defaultNamedNotOptArg):
		'SetState'
		return self._oleobj_.InvokeTypes(206, LCID, 1, (24, 0), ((3, 1),),State
			)

	def Write(self, Buffer=defaultNamedNotOptArg):
		'Write'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (3, 0), ((12, 1),),Buffer
			)

	_prop_map_get_ = {
		# Method 'BufferInfo' returns object of type 'ISpeechAudioBufferInfo'
		"BufferInfo": (201, 2, (9, 0), (), "BufferInfo", '{11B103D8-1142-4EDF-A093-82FB3915F8CC}'),
		"BufferNotifySize": (204, 2, (3, 0), (), "BufferNotifySize", None),
		# Method 'DefaultFormat' returns object of type 'ISpeechAudioFormat'
		"DefaultFormat": (202, 2, (9, 0), (), "DefaultFormat", '{E6E9C590-3E18-40E3-8299-061F98BDE7C7}'),
		"DeviceId": (300, 2, (3, 0), (), "DeviceId", None),
		"EventHandle": (205, 2, (3, 0), (), "EventHandle", None),
		# Method 'Format' returns object of type 'ISpeechAudioFormat'
		"Format": (1, 2, (9, 0), (), "Format", '{E6E9C590-3E18-40E3-8299-061F98BDE7C7}'),
		"LineId": (301, 2, (3, 0), (), "LineId", None),
		"MMHandle": (302, 2, (3, 0), (), "MMHandle", None),
		# Method 'Status' returns object of type 'ISpeechAudioStatus'
		"Status": (200, 2, (9, 0), (), "Status", '{C62D9C91-7458-47F6-862D-1EF86FB0B278}'),
		"Volume": (203, 2, (3, 0), (), "Volume", None),
	}
	_prop_map_put_ = {
		"BufferNotifySize": ((204, LCID, 4, 0),()),
		"DeviceId": ((300, LCID, 4, 0),()),
		"Format": ((1, LCID, 8, 0),()),
		"LineId": ((301, LCID, 4, 0),()),
		"Volume": ((203, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

win32com.client.CLSIDToClass.RegisterCLSID( "{3C76AF6D-1FD7-4831-81D1-3B71D5A13C44}", ISpeechMMSysAudio )
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

ISpeechMMSysAudio_vtables_dispatch_ = 1
ISpeechMMSysAudio_vtables_ = [
	(( u'DeviceId' , u'DeviceId' , ), 300, (300, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( u'DeviceId' , u'DeviceId' , ), 300, (300, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( u'LineId' , u'LineId' , ), 301, (301, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( u'LineId' , u'LineId' , ), 301, (301, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( u'MMHandle' , u'Handle' , ), 302, (302, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 64 , )),
]

win32com.client.CLSIDToClass.RegisterCLSID( "{3C76AF6D-1FD7-4831-81D1-3B71D5A13C44}", ISpeechMMSysAudio )
