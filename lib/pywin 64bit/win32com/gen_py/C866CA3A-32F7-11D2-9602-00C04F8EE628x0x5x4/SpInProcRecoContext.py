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

from win32com.client import CoClassBaseClass
import sys
__import__('win32com.gen_py.C866CA3A-32F7-11D2-9602-00C04F8EE628x0x5x4._ISpeechRecoContextEvents')
_ISpeechRecoContextEvents = sys.modules['win32com.gen_py.C866CA3A-32F7-11D2-9602-00C04F8EE628x0x5x4._ISpeechRecoContextEvents']._ISpeechRecoContextEvents
__import__('win32com.gen_py.C866CA3A-32F7-11D2-9602-00C04F8EE628x0x5x4.ISpeechRecoContext')
ISpeechRecoContext = sys.modules['win32com.gen_py.C866CA3A-32F7-11D2-9602-00C04F8EE628x0x5x4.ISpeechRecoContext'].ISpeechRecoContext
# This CoClass is known by the name 'SAPI.SpInProcRecoContext.1'
class SpInProcRecoContext(CoClassBaseClass): # A CoClass
	# SpInProcRecoContext Class
	CLSID = IID('{73AD6842-ACE0-45E8-A4DD-8795881A2C2A}')
	coclass_sources = [
		_ISpeechRecoContextEvents,
	]
	default_source = _ISpeechRecoContextEvents
	coclass_interfaces = [
		ISpeechRecoContext,
	]
	default_interface = ISpeechRecoContext

win32com.client.CLSIDToClass.RegisterCLSID( "{73AD6842-ACE0-45E8-A4DD-8795881A2C2A}", SpInProcRecoContext )
