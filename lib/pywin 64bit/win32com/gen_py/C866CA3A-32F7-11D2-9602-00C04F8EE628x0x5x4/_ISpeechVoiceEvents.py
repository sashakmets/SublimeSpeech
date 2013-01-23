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

class _ISpeechVoiceEvents:
	CLSID = CLSID_Sink = IID('{A372ACD1-3BEF-4BBD-8FFB-CB3E2B416AF8}')
	coclass_clsid = IID('{96749377-3391-11D2-9EE3-00C04F797396}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        3 : "OnVoiceChange",
		        9 : "OnAudioLevel",
		        5 : "OnWord",
		       10 : "OnEnginePrivate",
		        7 : "OnSentence",
		        4 : "OnBookmark",
		        1 : "OnStartStream",
		        2 : "OnEndStream",
		        6 : "OnPhoneme",
		        8 : "OnViseme",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnVoiceChange(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg, VoiceObjectToken=defaultNamedNotOptArg):
#		'VoiceChange'
#	def OnAudioLevel(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg, AudioLevel=defaultNamedNotOptArg):
#		'AudioLevel'
#	def OnWord(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg, CharacterPosition=defaultNamedNotOptArg, Length=defaultNamedNotOptArg):
#		'Word'
#	def OnEnginePrivate(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg, EngineData=defaultNamedNotOptArg):
#		'EnginePrivate'
#	def OnSentence(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg, CharacterPosition=defaultNamedNotOptArg, Length=defaultNamedNotOptArg):
#		'Sentence'
#	def OnBookmark(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg, Bookmark=defaultNamedNotOptArg, BookmarkId=defaultNamedNotOptArg):
#		'Bookmark'
#	def OnStartStream(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg):
#		'StartStream'
#	def OnEndStream(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg):
#		'EndStream'
#	def OnPhoneme(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg, Duration=defaultNamedNotOptArg, NextPhoneId=defaultNamedNotOptArg
#			, Feature=defaultNamedNotOptArg, CurrentPhoneId=defaultNamedNotOptArg):
#		'Phoneme'
#	def OnViseme(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg, Duration=defaultNamedNotOptArg, NextVisemeId=defaultNamedNotOptArg
#			, Feature=defaultNamedNotOptArg, CurrentVisemeId=defaultNamedNotOptArg):
#		'Viseme'


win32com.client.CLSIDToClass.RegisterCLSID( "{A372ACD1-3BEF-4BBD-8FFB-CB3E2B416AF8}", _ISpeechVoiceEvents )
