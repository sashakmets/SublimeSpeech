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

class _ISpeechRecoContextEvents:
	CLSID = CLSID_Sink = IID('{7B8FCB42-0E9D-4F00-A048-7B04D6179D3D}')
	coclass_clsid = IID('{73AD6842-ACE0-45E8-A4DD-8795881A2C2A}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		       11 : "OnFalseRecognition",
		       16 : "OnRecognitionForOtherContext",
		       18 : "OnEnginePrivate",
		       17 : "OnAudioLevel",
		        1 : "OnStartStream",
		        3 : "OnBookmark",
		       13 : "OnRequestUI",
		       12 : "OnInterference",
		        4 : "OnSoundStart",
		        2 : "OnEndStream",
		       14 : "OnRecognizerStateChange",
		        9 : "OnPropertyNumberChange",
		        8 : "OnHypothesis",
		       15 : "OnAdaptation",
		        6 : "OnPhraseStart",
		        5 : "OnSoundEnd",
		       10 : "OnPropertyStringChange",
		        7 : "OnRecognition",
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
#	def OnFalseRecognition(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg, Result=defaultNamedNotOptArg):
#		'FalseRecognition'
#	def OnRecognitionForOtherContext(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg):
#		'RecognitionForOtherContext'
#	def OnEnginePrivate(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg, EngineData=defaultNamedNotOptArg):
#		'EnginePrivate'
#	def OnAudioLevel(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg, AudioLevel=defaultNamedNotOptArg):
#		'AudioLevel'
#	def OnStartStream(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg):
#		'StartStream'
#	def OnBookmark(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg, BookmarkId=defaultNamedNotOptArg, Options=defaultNamedNotOptArg):
#		'Bookmark'
#	def OnRequestUI(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg, UIType=defaultNamedNotOptArg):
#		'RequestUI'
#	def OnInterference(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg, Interference=defaultNamedNotOptArg):
#		'Interference'
#	def OnSoundStart(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg):
#		'SoundStart'
#	def OnEndStream(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg, StreamReleased=defaultNamedNotOptArg):
#		'EndStream'
#	def OnRecognizerStateChange(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg, NewState=defaultNamedNotOptArg):
#		'RecognizerStateChange'
#	def OnPropertyNumberChange(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg, PropertyName=defaultNamedNotOptArg, NewNumberValue=defaultNamedNotOptArg):
#		'PropertyNumberChange'
#	def OnHypothesis(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg, Result=defaultNamedNotOptArg):
#		'Hypothesis'
#	def OnAdaptation(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg):
#		'Adaptation'
#	def OnPhraseStart(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg):
#		'PhraseStart'
#	def OnSoundEnd(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg):
#		'SoundEnd'
#	def OnPropertyStringChange(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg, PropertyName=defaultNamedNotOptArg, NewStringValue=defaultNamedNotOptArg):
#		'PropertyStringChange'
#	def OnRecognition(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg, RecognitionType=defaultNamedNotOptArg, Result=defaultNamedNotOptArg):
#		'Recognition'


win32com.client.CLSIDToClass.RegisterCLSID( "{7B8FCB42-0E9D-4F00-A048-7B04D6179D3D}", _ISpeechRecoContextEvents )
