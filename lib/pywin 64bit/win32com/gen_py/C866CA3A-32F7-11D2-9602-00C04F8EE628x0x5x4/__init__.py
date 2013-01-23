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

class constants:
	DISPID_SRGCmdLoadFromFile     =7          # from enum DISPIDSPRG
	DISPID_SRGCmdLoadFromMemory   =10         # from enum DISPIDSPRG
	DISPID_SRGCmdLoadFromObject   =8          # from enum DISPIDSPRG
	DISPID_SRGCmdLoadFromProprietaryGrammar=11         # from enum DISPIDSPRG
	DISPID_SRGCmdLoadFromResource =9          # from enum DISPIDSPRG
	DISPID_SRGCmdSetRuleIdState   =13         # from enum DISPIDSPRG
	DISPID_SRGCmdSetRuleState     =12         # from enum DISPIDSPRG
	DISPID_SRGCommit              =6          # from enum DISPIDSPRG
	DISPID_SRGDictationLoad       =14         # from enum DISPIDSPRG
	DISPID_SRGDictationSetState   =16         # from enum DISPIDSPRG
	DISPID_SRGDictationUnload     =15         # from enum DISPIDSPRG
	DISPID_SRGId                  =1          # from enum DISPIDSPRG
	DISPID_SRGIsPronounceable     =19         # from enum DISPIDSPRG
	DISPID_SRGRecoContext         =2          # from enum DISPIDSPRG
	DISPID_SRGReset               =5          # from enum DISPIDSPRG
	DISPID_SRGRules               =4          # from enum DISPIDSPRG
	DISPID_SRGSetTextSelection    =18         # from enum DISPIDSPRG
	DISPID_SRGSetWordSequenceData =17         # from enum DISPIDSPRG
	DISPID_SRGState               =3          # from enum DISPIDSPRG
	DISPIDSPTSI_ActiveLength      =2          # from enum DISPIDSPTSI
	DISPIDSPTSI_ActiveOffset      =1          # from enum DISPIDSPTSI
	DISPIDSPTSI_SelectionLength   =4          # from enum DISPIDSPTSI
	DISPIDSPTSI_SelectionOffset   =3          # from enum DISPIDSPTSI
	DISPID_SABufferInfo           =201        # from enum DISPID_SpeechAudio
	DISPID_SABufferNotifySize     =204        # from enum DISPID_SpeechAudio
	DISPID_SADefaultFormat        =202        # from enum DISPID_SpeechAudio
	DISPID_SAEventHandle          =205        # from enum DISPID_SpeechAudio
	DISPID_SASetState             =206        # from enum DISPID_SpeechAudio
	DISPID_SAStatus               =200        # from enum DISPID_SpeechAudio
	DISPID_SAVolume               =203        # from enum DISPID_SpeechAudio
	DISPID_SABIBufferSize         =2          # from enum DISPID_SpeechAudioBufferInfo
	DISPID_SABIEventBias          =3          # from enum DISPID_SpeechAudioBufferInfo
	DISPID_SABIMinNotification    =1          # from enum DISPID_SpeechAudioBufferInfo
	DISPID_SAFGetWaveFormatEx     =3          # from enum DISPID_SpeechAudioFormat
	DISPID_SAFGuid                =2          # from enum DISPID_SpeechAudioFormat
	DISPID_SAFSetWaveFormatEx     =4          # from enum DISPID_SpeechAudioFormat
	DISPID_SAFType                =1          # from enum DISPID_SpeechAudioFormat
	DISPID_SASCurrentDevicePosition=5          # from enum DISPID_SpeechAudioStatus
	DISPID_SASCurrentSeekPosition =4          # from enum DISPID_SpeechAudioStatus
	DISPID_SASFreeBufferSpace     =1          # from enum DISPID_SpeechAudioStatus
	DISPID_SASNonBlockingIO       =2          # from enum DISPID_SpeechAudioStatus
	DISPID_SASState               =3          # from enum DISPID_SpeechAudioStatus
	DISPID_SBSFormat              =1          # from enum DISPID_SpeechBaseStream
	DISPID_SBSRead                =2          # from enum DISPID_SpeechBaseStream
	DISPID_SBSSeek                =4          # from enum DISPID_SpeechBaseStream
	DISPID_SBSWrite               =3          # from enum DISPID_SpeechBaseStream
	DISPID_SCSBaseStream          =100        # from enum DISPID_SpeechCustomStream
	DISPID_SDKCreateKey           =8          # from enum DISPID_SpeechDataKey
	DISPID_SDKDeleteKey           =9          # from enum DISPID_SpeechDataKey
	DISPID_SDKDeleteValue         =10         # from enum DISPID_SpeechDataKey
	DISPID_SDKEnumKeys            =11         # from enum DISPID_SpeechDataKey
	DISPID_SDKEnumValues          =12         # from enum DISPID_SpeechDataKey
	DISPID_SDKGetBinaryValue      =2          # from enum DISPID_SpeechDataKey
	DISPID_SDKGetStringValue      =4          # from enum DISPID_SpeechDataKey
	DISPID_SDKGetlongValue        =6          # from enum DISPID_SpeechDataKey
	DISPID_SDKOpenKey             =7          # from enum DISPID_SpeechDataKey
	DISPID_SDKSetBinaryValue      =1          # from enum DISPID_SpeechDataKey
	DISPID_SDKSetLongValue        =5          # from enum DISPID_SpeechDataKey
	DISPID_SDKSetStringValue      =3          # from enum DISPID_SpeechDataKey
	DISPID_SFSClose               =101        # from enum DISPID_SpeechFileStream
	DISPID_SFSOpen                =100        # from enum DISPID_SpeechFileStream
	DISPID_SGRAddResource         =6          # from enum DISPID_SpeechGrammarRule
	DISPID_SGRAddState            =7          # from enum DISPID_SpeechGrammarRule
	DISPID_SGRAttributes          =1          # from enum DISPID_SpeechGrammarRule
	DISPID_SGRClear               =5          # from enum DISPID_SpeechGrammarRule
	DISPID_SGRId                  =4          # from enum DISPID_SpeechGrammarRule
	DISPID_SGRInitialState        =2          # from enum DISPID_SpeechGrammarRule
	DISPID_SGRName                =3          # from enum DISPID_SpeechGrammarRule
	DISPID_SGRSAddRuleTransition  =4          # from enum DISPID_SpeechGrammarRuleState
	DISPID_SGRSAddSpecialTransition=5          # from enum DISPID_SpeechGrammarRuleState
	DISPID_SGRSAddWordTransition  =3          # from enum DISPID_SpeechGrammarRuleState
	DISPID_SGRSRule               =1          # from enum DISPID_SpeechGrammarRuleState
	DISPID_SGRSTransitions        =2          # from enum DISPID_SpeechGrammarRuleState
	DISPID_SGRSTNextState         =8          # from enum DISPID_SpeechGrammarRuleStateTransition
	DISPID_SGRSTPropertyId        =6          # from enum DISPID_SpeechGrammarRuleStateTransition
	DISPID_SGRSTPropertyName      =5          # from enum DISPID_SpeechGrammarRuleStateTransition
	DISPID_SGRSTPropertyValue     =7          # from enum DISPID_SpeechGrammarRuleStateTransition
	DISPID_SGRSTRule              =3          # from enum DISPID_SpeechGrammarRuleStateTransition
	DISPID_SGRSTText              =2          # from enum DISPID_SpeechGrammarRuleStateTransition
	DISPID_SGRSTType              =1          # from enum DISPID_SpeechGrammarRuleStateTransition
	DISPID_SGRSTWeight            =4          # from enum DISPID_SpeechGrammarRuleStateTransition
	DISPID_SGRSTsCount            =1          # from enum DISPID_SpeechGrammarRuleStateTransitions
	DISPID_SGRSTsItem             =0          # from enum DISPID_SpeechGrammarRuleStateTransitions
	DISPID_SGRSTs_NewEnum         =-4         # from enum DISPID_SpeechGrammarRuleStateTransitions
	DISPID_SGRsAdd                =3          # from enum DISPID_SpeechGrammarRules
	DISPID_SGRsCommit             =4          # from enum DISPID_SpeechGrammarRules
	DISPID_SGRsCommitAndSave      =5          # from enum DISPID_SpeechGrammarRules
	DISPID_SGRsCount              =1          # from enum DISPID_SpeechGrammarRules
	DISPID_SGRsDynamic            =2          # from enum DISPID_SpeechGrammarRules
	DISPID_SGRsFindRule           =6          # from enum DISPID_SpeechGrammarRules
	DISPID_SGRsItem               =0          # from enum DISPID_SpeechGrammarRules
	DISPID_SGRs_NewEnum           =-4         # from enum DISPID_SpeechGrammarRules
	DISPID_SLAddPronunciation     =3          # from enum DISPID_SpeechLexicon
	DISPID_SLAddPronunciationByPhoneIds=4          # from enum DISPID_SpeechLexicon
	DISPID_SLGenerationId         =1          # from enum DISPID_SpeechLexicon
	DISPID_SLGetGenerationChange  =8          # from enum DISPID_SpeechLexicon
	DISPID_SLGetPronunciations    =7          # from enum DISPID_SpeechLexicon
	DISPID_SLGetWords             =2          # from enum DISPID_SpeechLexicon
	DISPID_SLRemovePronunciation  =5          # from enum DISPID_SpeechLexicon
	DISPID_SLRemovePronunciationByPhoneIds=6          # from enum DISPID_SpeechLexicon
	DISPID_SLPsCount              =1          # from enum DISPID_SpeechLexiconProns
	DISPID_SLPsItem               =0          # from enum DISPID_SpeechLexiconProns
	DISPID_SLPs_NewEnum           =-4         # from enum DISPID_SpeechLexiconProns
	DISPID_SLPLangId              =2          # from enum DISPID_SpeechLexiconPronunciation
	DISPID_SLPPartOfSpeech        =3          # from enum DISPID_SpeechLexiconPronunciation
	DISPID_SLPPhoneIds            =4          # from enum DISPID_SpeechLexiconPronunciation
	DISPID_SLPSymbolic            =5          # from enum DISPID_SpeechLexiconPronunciation
	DISPID_SLPType                =1          # from enum DISPID_SpeechLexiconPronunciation
	DISPID_SLWLangId              =1          # from enum DISPID_SpeechLexiconWord
	DISPID_SLWPronunciations      =4          # from enum DISPID_SpeechLexiconWord
	DISPID_SLWType                =2          # from enum DISPID_SpeechLexiconWord
	DISPID_SLWWord                =3          # from enum DISPID_SpeechLexiconWord
	DISPID_SLWsCount              =1          # from enum DISPID_SpeechLexiconWords
	DISPID_SLWsItem               =0          # from enum DISPID_SpeechLexiconWords
	DISPID_SLWs_NewEnum           =-4         # from enum DISPID_SpeechLexiconWords
	DISPID_SMSADeviceId           =300        # from enum DISPID_SpeechMMSysAudio
	DISPID_SMSALineId             =301        # from enum DISPID_SpeechMMSysAudio
	DISPID_SMSAMMHandle           =302        # from enum DISPID_SpeechMMSysAudio
	DISPID_SMSGetData             =101        # from enum DISPID_SpeechMemoryStream
	DISPID_SMSSetData             =100        # from enum DISPID_SpeechMemoryStream
	DISPID_SOTCategory            =3          # from enum DISPID_SpeechObjectToken
	DISPID_SOTCreateInstance      =7          # from enum DISPID_SpeechObjectToken
	DISPID_SOTDataKey             =2          # from enum DISPID_SpeechObjectToken
	DISPID_SOTDisplayUI           =12         # from enum DISPID_SpeechObjectToken
	DISPID_SOTGetAttribute        =6          # from enum DISPID_SpeechObjectToken
	DISPID_SOTGetDescription      =4          # from enum DISPID_SpeechObjectToken
	DISPID_SOTGetStorageFileName  =9          # from enum DISPID_SpeechObjectToken
	DISPID_SOTId                  =1          # from enum DISPID_SpeechObjectToken
	DISPID_SOTIsUISupported       =11         # from enum DISPID_SpeechObjectToken
	DISPID_SOTMatchesAttributes   =13         # from enum DISPID_SpeechObjectToken
	DISPID_SOTRemove              =8          # from enum DISPID_SpeechObjectToken
	DISPID_SOTRemoveStorageFileName=10         # from enum DISPID_SpeechObjectToken
	DISPID_SOTSetId               =5          # from enum DISPID_SpeechObjectToken
	DISPID_SOTCDefault            =2          # from enum DISPID_SpeechObjectTokenCategory
	DISPID_SOTCEnumerateTokens    =5          # from enum DISPID_SpeechObjectTokenCategory
	DISPID_SOTCGetDataKey         =4          # from enum DISPID_SpeechObjectTokenCategory
	DISPID_SOTCId                 =1          # from enum DISPID_SpeechObjectTokenCategory
	DISPID_SOTCSetId              =3          # from enum DISPID_SpeechObjectTokenCategory
	DISPID_SOTsCount              =1          # from enum DISPID_SpeechObjectTokens
	DISPID_SOTsItem               =0          # from enum DISPID_SpeechObjectTokens
	DISPID_SOTs_NewEnum           =-4         # from enum DISPID_SpeechObjectTokens
	DISPID_SPCIdToPhone           =3          # from enum DISPID_SpeechPhoneConverter
	DISPID_SPCLangId              =1          # from enum DISPID_SpeechPhoneConverter
	DISPID_SPCPhoneToId           =2          # from enum DISPID_SpeechPhoneConverter
	DISPID_SPACommit              =5          # from enum DISPID_SpeechPhraseAlternate
	DISPID_SPANumberOfElementsInResult=3          # from enum DISPID_SpeechPhraseAlternate
	DISPID_SPAPhraseInfo          =4          # from enum DISPID_SpeechPhraseAlternate
	DISPID_SPARecoResult          =1          # from enum DISPID_SpeechPhraseAlternate
	DISPID_SPAStartElementInResult=2          # from enum DISPID_SpeechPhraseAlternate
	DISPID_SPAsCount              =1          # from enum DISPID_SpeechPhraseAlternates
	DISPID_SPAsItem               =0          # from enum DISPID_SpeechPhraseAlternates
	DISPID_SPAs_NewEnum           =-4         # from enum DISPID_SpeechPhraseAlternates
	DISPID_SPPBRestorePhraseFromMemory=1          # from enum DISPID_SpeechPhraseBuilder
	DISPID_SPEActualConfidence    =12         # from enum DISPID_SpeechPhraseElement
	DISPID_SPEAudioSizeBytes      =4          # from enum DISPID_SpeechPhraseElement
	DISPID_SPEAudioSizeTime       =2          # from enum DISPID_SpeechPhraseElement
	DISPID_SPEAudioStreamOffset   =3          # from enum DISPID_SpeechPhraseElement
	DISPID_SPEAudioTimeOffset     =1          # from enum DISPID_SpeechPhraseElement
	DISPID_SPEDisplayAttributes   =10         # from enum DISPID_SpeechPhraseElement
	DISPID_SPEDisplayText         =7          # from enum DISPID_SpeechPhraseElement
	DISPID_SPEEngineConfidence    =13         # from enum DISPID_SpeechPhraseElement
	DISPID_SPELexicalForm         =8          # from enum DISPID_SpeechPhraseElement
	DISPID_SPEPronunciation       =9          # from enum DISPID_SpeechPhraseElement
	DISPID_SPERequiredConfidence  =11         # from enum DISPID_SpeechPhraseElement
	DISPID_SPERetainedSizeBytes   =6          # from enum DISPID_SpeechPhraseElement
	DISPID_SPERetainedStreamOffset=5          # from enum DISPID_SpeechPhraseElement
	DISPID_SPEsCount              =1          # from enum DISPID_SpeechPhraseElements
	DISPID_SPEsItem               =0          # from enum DISPID_SpeechPhraseElements
	DISPID_SPEs_NewEnum           =-4         # from enum DISPID_SpeechPhraseElements
	DISPID_SPIAudioSizeBytes      =5          # from enum DISPID_SpeechPhraseInfo
	DISPID_SPIAudioSizeTime       =7          # from enum DISPID_SpeechPhraseInfo
	DISPID_SPIAudioStreamPosition =4          # from enum DISPID_SpeechPhraseInfo
	DISPID_SPIElements            =10         # from enum DISPID_SpeechPhraseInfo
	DISPID_SPIEngineId            =12         # from enum DISPID_SpeechPhraseInfo
	DISPID_SPIEnginePrivateData   =13         # from enum DISPID_SpeechPhraseInfo
	DISPID_SPIGetDisplayAttributes=16         # from enum DISPID_SpeechPhraseInfo
	DISPID_SPIGetText             =15         # from enum DISPID_SpeechPhraseInfo
	DISPID_SPIGrammarId           =2          # from enum DISPID_SpeechPhraseInfo
	DISPID_SPILanguageId          =1          # from enum DISPID_SpeechPhraseInfo
	DISPID_SPIProperties          =9          # from enum DISPID_SpeechPhraseInfo
	DISPID_SPIReplacements        =11         # from enum DISPID_SpeechPhraseInfo
	DISPID_SPIRetainedSizeBytes   =6          # from enum DISPID_SpeechPhraseInfo
	DISPID_SPIRule                =8          # from enum DISPID_SpeechPhraseInfo
	DISPID_SPISaveToMemory        =14         # from enum DISPID_SpeechPhraseInfo
	DISPID_SPIStartTime           =3          # from enum DISPID_SpeechPhraseInfo
	DISPID_SPPsCount              =1          # from enum DISPID_SpeechPhraseProperties
	DISPID_SPPsItem               =0          # from enum DISPID_SpeechPhraseProperties
	DISPID_SPPs_NewEnum           =-4         # from enum DISPID_SpeechPhraseProperties
	DISPID_SPPChildren            =9          # from enum DISPID_SpeechPhraseProperty
	DISPID_SPPConfidence          =7          # from enum DISPID_SpeechPhraseProperty
	DISPID_SPPEngineConfidence    =6          # from enum DISPID_SpeechPhraseProperty
	DISPID_SPPFirstElement        =4          # from enum DISPID_SpeechPhraseProperty
	DISPID_SPPId                  =2          # from enum DISPID_SpeechPhraseProperty
	DISPID_SPPName                =1          # from enum DISPID_SpeechPhraseProperty
	DISPID_SPPNumberOfElements    =5          # from enum DISPID_SpeechPhraseProperty
	DISPID_SPPParent              =8          # from enum DISPID_SpeechPhraseProperty
	DISPID_SPPValue               =3          # from enum DISPID_SpeechPhraseProperty
	DISPID_SPRDisplayAttributes   =1          # from enum DISPID_SpeechPhraseReplacement
	DISPID_SPRFirstElement        =3          # from enum DISPID_SpeechPhraseReplacement
	DISPID_SPRNumberOfElements    =4          # from enum DISPID_SpeechPhraseReplacement
	DISPID_SPRText                =2          # from enum DISPID_SpeechPhraseReplacement
	DISPID_SPRsCount              =1          # from enum DISPID_SpeechPhraseReplacements
	DISPID_SPRsItem               =0          # from enum DISPID_SpeechPhraseReplacements
	DISPID_SPRs_NewEnum           =-4         # from enum DISPID_SpeechPhraseReplacements
	DISPID_SPRuleChildren         =6          # from enum DISPID_SpeechPhraseRule
	DISPID_SPRuleConfidence       =7          # from enum DISPID_SpeechPhraseRule
	DISPID_SPRuleEngineConfidence =8          # from enum DISPID_SpeechPhraseRule
	DISPID_SPRuleFirstElement     =3          # from enum DISPID_SpeechPhraseRule
	DISPID_SPRuleId               =2          # from enum DISPID_SpeechPhraseRule
	DISPID_SPRuleName             =1          # from enum DISPID_SpeechPhraseRule
	DISPID_SPRuleNumberOfElements =4          # from enum DISPID_SpeechPhraseRule
	DISPID_SPRuleParent           =5          # from enum DISPID_SpeechPhraseRule
	DISPID_SPRulesCount           =1          # from enum DISPID_SpeechPhraseRules
	DISPID_SPRulesItem            =0          # from enum DISPID_SpeechPhraseRules
	DISPID_SPRules_NewEnum        =-4         # from enum DISPID_SpeechPhraseRules
	DISPID_SRAllowVoiceFormatMatchingOnNextSet=5          # from enum DISPID_SpeechRecoContext
	DISPID_SRCAudioInInterferenceStatus=2          # from enum DISPID_SpeechRecoContext
	DISPID_SRCBookmark            =16         # from enum DISPID_SpeechRecoContext
	DISPID_SRCCmdMaxAlternates    =8          # from enum DISPID_SpeechRecoContext
	DISPID_SRCCreateGrammar       =14         # from enum DISPID_SpeechRecoContext
	DISPID_SRCCreateResultFromMemory=15         # from enum DISPID_SpeechRecoContext
	DISPID_SRCEventInterests      =7          # from enum DISPID_SpeechRecoContext
	DISPID_SRCPause               =12         # from enum DISPID_SpeechRecoContext
	DISPID_SRCRecognizer          =1          # from enum DISPID_SpeechRecoContext
	DISPID_SRCRequestedUIType     =3          # from enum DISPID_SpeechRecoContext
	DISPID_SRCResume              =13         # from enum DISPID_SpeechRecoContext
	DISPID_SRCRetainedAudio       =10         # from enum DISPID_SpeechRecoContext
	DISPID_SRCRetainedAudioFormat =11         # from enum DISPID_SpeechRecoContext
	DISPID_SRCSetAdaptationData   =17         # from enum DISPID_SpeechRecoContext
	DISPID_SRCState               =9          # from enum DISPID_SpeechRecoContext
	DISPID_SRCVoice               =4          # from enum DISPID_SpeechRecoContext
	DISPID_SRCVoicePurgeEvent     =6          # from enum DISPID_SpeechRecoContext
	DISPID_SRCEAdaptation         =15         # from enum DISPID_SpeechRecoContextEvents
	DISPID_SRCEAudioLevel         =17         # from enum DISPID_SpeechRecoContextEvents
	DISPID_SRCEBookmark           =3          # from enum DISPID_SpeechRecoContextEvents
	DISPID_SRCEEndStream          =2          # from enum DISPID_SpeechRecoContextEvents
	DISPID_SRCEEnginePrivate      =18         # from enum DISPID_SpeechRecoContextEvents
	DISPID_SRCEFalseRecognition   =11         # from enum DISPID_SpeechRecoContextEvents
	DISPID_SRCEHypothesis         =8          # from enum DISPID_SpeechRecoContextEvents
	DISPID_SRCEInterference       =12         # from enum DISPID_SpeechRecoContextEvents
	DISPID_SRCEPhraseStart        =6          # from enum DISPID_SpeechRecoContextEvents
	DISPID_SRCEPropertyNumberChange=9          # from enum DISPID_SpeechRecoContextEvents
	DISPID_SRCEPropertyStringChange=10         # from enum DISPID_SpeechRecoContextEvents
	DISPID_SRCERecognition        =7          # from enum DISPID_SpeechRecoContextEvents
	DISPID_SRCERecognitionForOtherContext=16         # from enum DISPID_SpeechRecoContextEvents
	DISPID_SRCERecognizerStateChange=14         # from enum DISPID_SpeechRecoContextEvents
	DISPID_SRCERequestUI          =13         # from enum DISPID_SpeechRecoContextEvents
	DISPID_SRCESoundEnd           =5          # from enum DISPID_SpeechRecoContextEvents
	DISPID_SRCESoundStart         =4          # from enum DISPID_SpeechRecoContextEvents
	DISPID_SRCEStartStream        =1          # from enum DISPID_SpeechRecoContextEvents
	DISPID_SRRAlternates          =5          # from enum DISPID_SpeechRecoResult
	DISPID_SRRAudio               =6          # from enum DISPID_SpeechRecoResult
	DISPID_SRRAudioFormat         =3          # from enum DISPID_SpeechRecoResult
	DISPID_SRRDiscardResultInfo   =9          # from enum DISPID_SpeechRecoResult
	DISPID_SRRPhraseInfo          =4          # from enum DISPID_SpeechRecoResult
	DISPID_SRRRecoContext         =1          # from enum DISPID_SpeechRecoResult
	DISPID_SRRSaveToMemory        =8          # from enum DISPID_SpeechRecoResult
	DISPID_SRRSpeakAudio          =7          # from enum DISPID_SpeechRecoResult
	DISPID_SRRTimes               =2          # from enum DISPID_SpeechRecoResult
	DISPID_SRRSetTextFeedback     =12         # from enum DISPID_SpeechRecoResult2
	DISPID_SRRTLength             =2          # from enum DISPID_SpeechRecoResultTimes
	DISPID_SRRTOffsetFromStart    =4          # from enum DISPID_SpeechRecoResultTimes
	DISPID_SRRTStreamTime         =1          # from enum DISPID_SpeechRecoResultTimes
	DISPID_SRRTTickCount          =3          # from enum DISPID_SpeechRecoResultTimes
	DISPID_SRAllowAudioInputFormatChangesOnNextSet=2          # from enum DISPID_SpeechRecognizer
	DISPID_SRAudioInput           =3          # from enum DISPID_SpeechRecognizer
	DISPID_SRAudioInputStream     =4          # from enum DISPID_SpeechRecognizer
	DISPID_SRCreateRecoContext    =10         # from enum DISPID_SpeechRecognizer
	DISPID_SRDisplayUI            =17         # from enum DISPID_SpeechRecognizer
	DISPID_SREmulateRecognition   =9          # from enum DISPID_SpeechRecognizer
	DISPID_SRGetFormat            =11         # from enum DISPID_SpeechRecognizer
	DISPID_SRGetPropertyNumber    =13         # from enum DISPID_SpeechRecognizer
	DISPID_SRGetPropertyString    =15         # from enum DISPID_SpeechRecognizer
	DISPID_SRGetRecognizers       =18         # from enum DISPID_SpeechRecognizer
	DISPID_SRIsShared             =5          # from enum DISPID_SpeechRecognizer
	DISPID_SRIsUISupported        =16         # from enum DISPID_SpeechRecognizer
	DISPID_SRProfile              =8          # from enum DISPID_SpeechRecognizer
	DISPID_SRRecognizer           =1          # from enum DISPID_SpeechRecognizer
	DISPID_SRSetPropertyNumber    =12         # from enum DISPID_SpeechRecognizer
	DISPID_SRSetPropertyString    =14         # from enum DISPID_SpeechRecognizer
	DISPID_SRState                =6          # from enum DISPID_SpeechRecognizer
	DISPID_SRStatus               =7          # from enum DISPID_SpeechRecognizer
	DISPID_SVGetAudioInputs       =19         # from enum DISPID_SpeechRecognizer
	DISPID_SVGetProfiles          =20         # from enum DISPID_SpeechRecognizer
	DISPID_SRSAudioStatus         =1          # from enum DISPID_SpeechRecognizerStatus
	DISPID_SRSClsidEngine         =5          # from enum DISPID_SpeechRecognizerStatus
	DISPID_SRSCurrentStreamNumber =3          # from enum DISPID_SpeechRecognizerStatus
	DISPID_SRSCurrentStreamPosition=2          # from enum DISPID_SpeechRecognizerStatus
	DISPID_SRSNumberOfActiveRules =4          # from enum DISPID_SpeechRecognizerStatus
	DISPID_SRSSupportedLanguages  =6          # from enum DISPID_SpeechRecognizerStatus
	DISPID_SVAlertBoundary        =10         # from enum DISPID_SpeechVoice
	DISPID_SVAllowAudioOuputFormatChangesOnNextSet=7          # from enum DISPID_SpeechVoice
	DISPID_SVAudioOutput          =3          # from enum DISPID_SpeechVoice
	DISPID_SVAudioOutputStream    =4          # from enum DISPID_SpeechVoice
	DISPID_SVDisplayUI            =22         # from enum DISPID_SpeechVoice
	DISPID_SVEventInterests       =8          # from enum DISPID_SpeechVoice
	DISPID_SVGetAudioOutputs      =18         # from enum DISPID_SpeechVoice
	DISPID_SVGetVoices            =17         # from enum DISPID_SpeechVoice
	DISPID_SVIsUISupported        =21         # from enum DISPID_SpeechVoice
	DISPID_SVPause                =14         # from enum DISPID_SpeechVoice
	DISPID_SVPriority             =9          # from enum DISPID_SpeechVoice
	DISPID_SVRate                 =5          # from enum DISPID_SpeechVoice
	DISPID_SVResume               =15         # from enum DISPID_SpeechVoice
	DISPID_SVSkip                 =16         # from enum DISPID_SpeechVoice
	DISPID_SVSpeak                =12         # from enum DISPID_SpeechVoice
	DISPID_SVSpeakCompleteEvent   =20         # from enum DISPID_SpeechVoice
	DISPID_SVSpeakStream          =13         # from enum DISPID_SpeechVoice
	DISPID_SVStatus               =1          # from enum DISPID_SpeechVoice
	DISPID_SVSyncronousSpeakTimeout=11         # from enum DISPID_SpeechVoice
	DISPID_SVVoice                =2          # from enum DISPID_SpeechVoice
	DISPID_SVVolume               =6          # from enum DISPID_SpeechVoice
	DISPID_SVWaitUntilDone        =19         # from enum DISPID_SpeechVoice
	DISPID_SVEAudioLevel          =9          # from enum DISPID_SpeechVoiceEvent
	DISPID_SVEBookmark            =4          # from enum DISPID_SpeechVoiceEvent
	DISPID_SVEEnginePrivate       =10         # from enum DISPID_SpeechVoiceEvent
	DISPID_SVEPhoneme             =6          # from enum DISPID_SpeechVoiceEvent
	DISPID_SVESentenceBoundary    =7          # from enum DISPID_SpeechVoiceEvent
	DISPID_SVEStreamEnd           =2          # from enum DISPID_SpeechVoiceEvent
	DISPID_SVEStreamStart         =1          # from enum DISPID_SpeechVoiceEvent
	DISPID_SVEViseme              =8          # from enum DISPID_SpeechVoiceEvent
	DISPID_SVEVoiceChange         =3          # from enum DISPID_SpeechVoiceEvent
	DISPID_SVEWord                =5          # from enum DISPID_SpeechVoiceEvent
	DISPID_SVSCurrentStreamNumber =1          # from enum DISPID_SpeechVoiceStatus
	DISPID_SVSInputSentenceLength =8          # from enum DISPID_SpeechVoiceStatus
	DISPID_SVSInputSentencePosition=7          # from enum DISPID_SpeechVoiceStatus
	DISPID_SVSInputWordLength     =6          # from enum DISPID_SpeechVoiceStatus
	DISPID_SVSInputWordPosition   =5          # from enum DISPID_SpeechVoiceStatus
	DISPID_SVSLastBookmark        =9          # from enum DISPID_SpeechVoiceStatus
	DISPID_SVSLastBookmarkId      =10         # from enum DISPID_SpeechVoiceStatus
	DISPID_SVSLastResult          =3          # from enum DISPID_SpeechVoiceStatus
	DISPID_SVSLastStreamNumberQueued=2          # from enum DISPID_SpeechVoiceStatus
	DISPID_SVSPhonemeId           =11         # from enum DISPID_SpeechVoiceStatus
	DISPID_SVSRunningState        =4          # from enum DISPID_SpeechVoiceStatus
	DISPID_SVSVisemeId            =12         # from enum DISPID_SpeechVoiceStatus
	DISPID_SWFEAvgBytesPerSec     =4          # from enum DISPID_SpeechWaveFormatEx
	DISPID_SWFEBitsPerSample      =6          # from enum DISPID_SpeechWaveFormatEx
	DISPID_SWFEBlockAlign         =5          # from enum DISPID_SpeechWaveFormatEx
	DISPID_SWFEChannels           =2          # from enum DISPID_SpeechWaveFormatEx
	DISPID_SWFEExtraData          =7          # from enum DISPID_SpeechWaveFormatEx
	DISPID_SWFEFormatTag          =1          # from enum DISPID_SpeechWaveFormatEx
	DISPID_SWFESamplesPerSec      =3          # from enum DISPID_SpeechWaveFormatEx
	DISPID_SRRGetXMLErrorInfo     =11         # from enum DISPID_SpeechXMLRecoResult
	DISPID_SRRGetXMLResult        =10         # from enum DISPID_SpeechXMLRecoResult
	SPAR_High                     =3          # from enum SPADAPTATIONRELEVANCE
	SPAR_Low                      =1          # from enum SPADAPTATIONRELEVANCE
	SPAR_Medium                   =2          # from enum SPADAPTATIONRELEVANCE
	SPAR_Unknown                  =0          # from enum SPADAPTATIONRELEVANCE
	SPAO_NONE                     =0          # from enum SPAUDIOOPTIONS
	SPAO_RETAIN_AUDIO             =1          # from enum SPAUDIOOPTIONS
	SPBO_AHEAD                    =2          # from enum SPBOOKMARKOPTIONS
	SPBO_NONE                     =0          # from enum SPBOOKMARKOPTIONS
	SPBO_PAUSE                    =1          # from enum SPBOOKMARKOPTIONS
	SPBO_TIME_UNITS               =4          # from enum SPBOOKMARKOPTIONS
	SPCT_COMMAND                  =0          # from enum SPCATEGORYTYPE
	SPCT_DICTATION                =1          # from enum SPCATEGORYTYPE
	SPCT_SLEEP                    =2          # from enum SPCATEGORYTYPE
	SPCT_SUB_COMMAND              =3          # from enum SPCATEGORYTYPE
	SPCT_SUB_DICTATION            =4          # from enum SPCATEGORYTYPE
	SPCS_DISABLED                 =0          # from enum SPCONTEXTSTATE
	SPCS_ENABLED                  =1          # from enum SPCONTEXTSTATE
	SPDKL_CurrentConfig           =5          # from enum SPDATAKEYLOCATION
	SPDKL_CurrentUser             =1          # from enum SPDATAKEYLOCATION
	SPDKL_DefaultLocation         =0          # from enum SPDATAKEYLOCATION
	SPDKL_LocalMachine            =2          # from enum SPDATAKEYLOCATION
	SPEI_ACTIVE_CATEGORY_CHANGED  =53         # from enum SPEVENTENUM
	SPEI_ADAPTATION               =47         # from enum SPEVENTENUM
	SPEI_END_INPUT_STREAM         =2          # from enum SPEVENTENUM
	SPEI_END_SR_STREAM            =34         # from enum SPEVENTENUM
	SPEI_FALSE_RECOGNITION        =43         # from enum SPEVENTENUM
	SPEI_HYPOTHESIS               =39         # from enum SPEVENTENUM
	SPEI_INTERFERENCE             =44         # from enum SPEVENTENUM
	SPEI_MAX_SR                   =55         # from enum SPEVENTENUM
	SPEI_MAX_TTS                  =15         # from enum SPEVENTENUM
	SPEI_MIN_SR                   =34         # from enum SPEVENTENUM
	SPEI_MIN_TTS                  =1          # from enum SPEVENTENUM
	SPEI_PHONEME                  =6          # from enum SPEVENTENUM
	SPEI_PHRASE_START             =37         # from enum SPEVENTENUM
	SPEI_PROPERTY_NUM_CHANGE      =41         # from enum SPEVENTENUM
	SPEI_PROPERTY_STRING_CHANGE   =42         # from enum SPEVENTENUM
	SPEI_RECOGNITION              =38         # from enum SPEVENTENUM
	SPEI_RECO_OTHER_CONTEXT       =49         # from enum SPEVENTENUM
	SPEI_RECO_STATE_CHANGE        =46         # from enum SPEVENTENUM
	SPEI_REQUEST_UI               =45         # from enum SPEVENTENUM
	SPEI_RESERVED1                =30         # from enum SPEVENTENUM
	SPEI_RESERVED2                =33         # from enum SPEVENTENUM
	SPEI_RESERVED3                =63         # from enum SPEVENTENUM
	SPEI_RESERVED5                =54         # from enum SPEVENTENUM
	SPEI_RESERVED6                =55         # from enum SPEVENTENUM
	SPEI_SENTENCE_BOUNDARY        =7          # from enum SPEVENTENUM
	SPEI_SOUND_END                =36         # from enum SPEVENTENUM
	SPEI_SOUND_START              =35         # from enum SPEVENTENUM
	SPEI_SR_AUDIO_LEVEL           =50         # from enum SPEVENTENUM
	SPEI_SR_BOOKMARK              =40         # from enum SPEVENTENUM
	SPEI_SR_PRIVATE               =52         # from enum SPEVENTENUM
	SPEI_SR_RETAINEDAUDIO         =51         # from enum SPEVENTENUM
	SPEI_START_INPUT_STREAM       =1          # from enum SPEVENTENUM
	SPEI_START_SR_STREAM          =48         # from enum SPEVENTENUM
	SPEI_TTS_AUDIO_LEVEL          =9          # from enum SPEVENTENUM
	SPEI_TTS_BOOKMARK             =4          # from enum SPEVENTENUM
	SPEI_TTS_PRIVATE              =15         # from enum SPEVENTENUM
	SPEI_UNDEFINED                =0          # from enum SPEVENTENUM
	SPEI_VISEME                   =8          # from enum SPEVENTENUM
	SPEI_VOICE_CHANGE             =3          # from enum SPEVENTENUM
	SPEI_WORD_BOUNDARY            =5          # from enum SPEVENTENUM
	SPFM_CREATE                   =2          # from enum SPFILEMODE
	SPFM_CREATE_ALWAYS            =3          # from enum SPFILEMODE
	SPFM_NUM_MODES                =4          # from enum SPFILEMODE
	SPFM_OPEN_READONLY            =0          # from enum SPFILEMODE
	SPFM_OPEN_READWRITE           =1          # from enum SPFILEMODE
	SPGS_DISABLED                 =0          # from enum SPGRAMMARSTATE
	SPGS_ENABLED                  =1          # from enum SPGRAMMARSTATE
	SPGS_EXCLUSIVE                =3          # from enum SPGRAMMARSTATE
	SPWT_DISPLAY                  =0          # from enum SPGRAMMARWORDTYPE
	SPWT_LEXICAL                  =1          # from enum SPGRAMMARWORDTYPE
	SPWT_LEXICAL_NO_SPECIAL_CHARS =3          # from enum SPGRAMMARWORDTYPE
	SPWT_PRONUNCIATION            =2          # from enum SPGRAMMARWORDTYPE
	SPINTERFERENCE_NOISE          =1          # from enum SPINTERFERENCE
	SPINTERFERENCE_NONE           =0          # from enum SPINTERFERENCE
	SPINTERFERENCE_NOSIGNAL       =2          # from enum SPINTERFERENCE
	SPINTERFERENCE_TOOFAST        =5          # from enum SPINTERFERENCE
	SPINTERFERENCE_TOOLOUD        =3          # from enum SPINTERFERENCE
	SPINTERFERENCE_TOOQUIET       =4          # from enum SPINTERFERENCE
	SPINTERFERENCE_TOOSLOW        =6          # from enum SPINTERFERENCE
	eLEXTYPE_APP                  =2          # from enum SPLEXICONTYPE
	eLEXTYPE_LETTERTOSOUND        =8          # from enum SPLEXICONTYPE
	eLEXTYPE_MORPHOLOGY           =16         # from enum SPLEXICONTYPE
	eLEXTYPE_PRIVATE1             =4096       # from enum SPLEXICONTYPE
	eLEXTYPE_PRIVATE10            =2097152    # from enum SPLEXICONTYPE
	eLEXTYPE_PRIVATE11            =4194304    # from enum SPLEXICONTYPE
	eLEXTYPE_PRIVATE12            =8388608    # from enum SPLEXICONTYPE
	eLEXTYPE_PRIVATE13            =16777216   # from enum SPLEXICONTYPE
	eLEXTYPE_PRIVATE14            =33554432   # from enum SPLEXICONTYPE
	eLEXTYPE_PRIVATE15            =67108864   # from enum SPLEXICONTYPE
	eLEXTYPE_PRIVATE16            =134217728  # from enum SPLEXICONTYPE
	eLEXTYPE_PRIVATE17            =268435456  # from enum SPLEXICONTYPE
	eLEXTYPE_PRIVATE18            =536870912  # from enum SPLEXICONTYPE
	eLEXTYPE_PRIVATE19            =1073741824 # from enum SPLEXICONTYPE
	eLEXTYPE_PRIVATE2             =8192       # from enum SPLEXICONTYPE
	eLEXTYPE_PRIVATE20            =-2147483648 # from enum SPLEXICONTYPE
	eLEXTYPE_PRIVATE3             =16384      # from enum SPLEXICONTYPE
	eLEXTYPE_PRIVATE4             =32768      # from enum SPLEXICONTYPE
	eLEXTYPE_PRIVATE5             =65536      # from enum SPLEXICONTYPE
	eLEXTYPE_PRIVATE6             =131072     # from enum SPLEXICONTYPE
	eLEXTYPE_PRIVATE7             =262144     # from enum SPLEXICONTYPE
	eLEXTYPE_PRIVATE8             =524288     # from enum SPLEXICONTYPE
	eLEXTYPE_PRIVATE9             =1048576    # from enum SPLEXICONTYPE
	eLEXTYPE_RESERVED10           =2048       # from enum SPLEXICONTYPE
	eLEXTYPE_RESERVED4            =32         # from enum SPLEXICONTYPE
	eLEXTYPE_RESERVED6            =128        # from enum SPLEXICONTYPE
	eLEXTYPE_RESERVED7            =256        # from enum SPLEXICONTYPE
	eLEXTYPE_RESERVED8            =512        # from enum SPLEXICONTYPE
	eLEXTYPE_RESERVED9            =1024       # from enum SPLEXICONTYPE
	eLEXTYPE_USER                 =1          # from enum SPLEXICONTYPE
	eLEXTYPE_USER_SHORTCUT        =64         # from enum SPLEXICONTYPE
	eLEXTYPE_VENDORLEXICON        =4          # from enum SPLEXICONTYPE
	SPLO_DYNAMIC                  =1          # from enum SPLOADOPTIONS
	SPLO_STATIC                   =0          # from enum SPLOADOPTIONS
	SPPS_Function                 =16384      # from enum SPPARTOFSPEECH
	SPPS_Interjection             =20480      # from enum SPPARTOFSPEECH
	SPPS_LMA                      =28672      # from enum SPPARTOFSPEECH
	SPPS_Modifier                 =12288      # from enum SPPARTOFSPEECH
	SPPS_Noncontent               =24576      # from enum SPPARTOFSPEECH
	SPPS_NotOverriden             =-1         # from enum SPPARTOFSPEECH
	SPPS_Noun                     =4096       # from enum SPPARTOFSPEECH
	SPPS_SuppressWord             =61440      # from enum SPPARTOFSPEECH
	SPPS_Unknown                  =0          # from enum SPPARTOFSPEECH
	SPPS_Verb                     =8192       # from enum SPPARTOFSPEECH
	SPRST_ACTIVE                  =1          # from enum SPRECOSTATE
	SPRST_ACTIVE_ALWAYS           =2          # from enum SPRECOSTATE
	SPRST_INACTIVE                =0          # from enum SPRECOSTATE
	SPRST_INACTIVE_WITH_PURGE     =3          # from enum SPRECOSTATE
	SPRST_NUM_STATES              =4          # from enum SPRECOSTATE
	SPRS_ACTIVE                   =1          # from enum SPRULESTATE
	SPRS_ACTIVE_USER_DELIMITED    =4          # from enum SPRULESTATE
	SPRS_ACTIVE_WITH_AUTO_PAUSE   =3          # from enum SPRULESTATE
	SPRS_INACTIVE                 =0          # from enum SPRULESTATE
	SPSMF_SAPI_PROPERTIES         =0          # from enum SPSEMANTICFORMAT
	SPSMF_SRGS_SAPIPROPERTIES     =2          # from enum SPSEMANTICFORMAT
	SPSMF_SRGS_SEMANTICINTERPRETATION_MS=1          # from enum SPSEMANTICFORMAT
	SPSMF_SRGS_SEMANTICINTERPRETATION_W3C=8          # from enum SPSEMANTICFORMAT
	SPSMF_UPS                     =4          # from enum SPSEMANTICFORMAT
	SPPS_RESERVED1                =12288      # from enum SPSHORTCUTTYPE
	SPPS_RESERVED2                =16384      # from enum SPSHORTCUTTYPE
	SPPS_RESERVED3                =20480      # from enum SPSHORTCUTTYPE
	SPPS_RESERVED4                =61440      # from enum SPSHORTCUTTYPE
	SPSHT_EMAIL                   =4096       # from enum SPSHORTCUTTYPE
	SPSHT_NotOverriden            =-1         # from enum SPSHORTCUTTYPE
	SPSHT_OTHER                   =8192       # from enum SPSHORTCUTTYPE
	SPSHT_Unknown                 =0          # from enum SPSHORTCUTTYPE
	SP_VISEME_0                   =0          # from enum SPVISEMES
	SP_VISEME_1                   =1          # from enum SPVISEMES
	SP_VISEME_10                  =10         # from enum SPVISEMES
	SP_VISEME_11                  =11         # from enum SPVISEMES
	SP_VISEME_12                  =12         # from enum SPVISEMES
	SP_VISEME_13                  =13         # from enum SPVISEMES
	SP_VISEME_14                  =14         # from enum SPVISEMES
	SP_VISEME_15                  =15         # from enum SPVISEMES
	SP_VISEME_16                  =16         # from enum SPVISEMES
	SP_VISEME_17                  =17         # from enum SPVISEMES
	SP_VISEME_18                  =18         # from enum SPVISEMES
	SP_VISEME_19                  =19         # from enum SPVISEMES
	SP_VISEME_2                   =2          # from enum SPVISEMES
	SP_VISEME_20                  =20         # from enum SPVISEMES
	SP_VISEME_21                  =21         # from enum SPVISEMES
	SP_VISEME_3                   =3          # from enum SPVISEMES
	SP_VISEME_4                   =4          # from enum SPVISEMES
	SP_VISEME_5                   =5          # from enum SPVISEMES
	SP_VISEME_6                   =6          # from enum SPVISEMES
	SP_VISEME_7                   =7          # from enum SPVISEMES
	SP_VISEME_8                   =8          # from enum SPVISEMES
	SP_VISEME_9                   =9          # from enum SPVISEMES
	SPVPRI_ALERT                  =1          # from enum SPVPRIORITY
	SPVPRI_NORMAL                 =0          # from enum SPVPRIORITY
	SPVPRI_OVER                   =2          # from enum SPVPRIORITY
	SPWF_INPUT                    =0          # from enum SPWAVEFORMATTYPE
	SPWF_SRENGINE                 =1          # from enum SPWAVEFORMATTYPE
	SPWP_KNOWN_WORD_PRONOUNCEABLE =2          # from enum SPWORDPRONOUNCEABLE
	SPWP_UNKNOWN_WORD_PRONOUNCEABLE=1          # from enum SPWORDPRONOUNCEABLE
	SPWP_UNKNOWN_WORD_UNPRONOUNCEABLE=0          # from enum SPWORDPRONOUNCEABLE
	eWORDTYPE_ADDED               =1          # from enum SPWORDTYPE
	eWORDTYPE_DELETED             =2          # from enum SPWORDTYPE
	SPXRO_Alternates_SML          =1          # from enum SPXMLRESULTOPTIONS
	SPXRO_SML                     =0          # from enum SPXMLRESULTOPTIONS
	SAFT11kHz16BitMono            =10         # from enum SpeechAudioFormatType
	SAFT11kHz16BitStereo          =11         # from enum SpeechAudioFormatType
	SAFT11kHz8BitMono             =8          # from enum SpeechAudioFormatType
	SAFT11kHz8BitStereo           =9          # from enum SpeechAudioFormatType
	SAFT12kHz16BitMono            =14         # from enum SpeechAudioFormatType
	SAFT12kHz16BitStereo          =15         # from enum SpeechAudioFormatType
	SAFT12kHz8BitMono             =12         # from enum SpeechAudioFormatType
	SAFT12kHz8BitStereo           =13         # from enum SpeechAudioFormatType
	SAFT16kHz16BitMono            =18         # from enum SpeechAudioFormatType
	SAFT16kHz16BitStereo          =19         # from enum SpeechAudioFormatType
	SAFT16kHz8BitMono             =16         # from enum SpeechAudioFormatType
	SAFT16kHz8BitStereo           =17         # from enum SpeechAudioFormatType
	SAFT22kHz16BitMono            =22         # from enum SpeechAudioFormatType
	SAFT22kHz16BitStereo          =23         # from enum SpeechAudioFormatType
	SAFT22kHz8BitMono             =20         # from enum SpeechAudioFormatType
	SAFT22kHz8BitStereo           =21         # from enum SpeechAudioFormatType
	SAFT24kHz16BitMono            =26         # from enum SpeechAudioFormatType
	SAFT24kHz16BitStereo          =27         # from enum SpeechAudioFormatType
	SAFT24kHz8BitMono             =24         # from enum SpeechAudioFormatType
	SAFT24kHz8BitStereo           =25         # from enum SpeechAudioFormatType
	SAFT32kHz16BitMono            =30         # from enum SpeechAudioFormatType
	SAFT32kHz16BitStereo          =31         # from enum SpeechAudioFormatType
	SAFT32kHz8BitMono             =28         # from enum SpeechAudioFormatType
	SAFT32kHz8BitStereo           =29         # from enum SpeechAudioFormatType
	SAFT44kHz16BitMono            =34         # from enum SpeechAudioFormatType
	SAFT44kHz16BitStereo          =35         # from enum SpeechAudioFormatType
	SAFT44kHz8BitMono             =32         # from enum SpeechAudioFormatType
	SAFT44kHz8BitStereo           =33         # from enum SpeechAudioFormatType
	SAFT48kHz16BitMono            =38         # from enum SpeechAudioFormatType
	SAFT48kHz16BitStereo          =39         # from enum SpeechAudioFormatType
	SAFT48kHz8BitMono             =36         # from enum SpeechAudioFormatType
	SAFT48kHz8BitStereo           =37         # from enum SpeechAudioFormatType
	SAFT8kHz16BitMono             =6          # from enum SpeechAudioFormatType
	SAFT8kHz16BitStereo           =7          # from enum SpeechAudioFormatType
	SAFT8kHz8BitMono              =4          # from enum SpeechAudioFormatType
	SAFT8kHz8BitStereo            =5          # from enum SpeechAudioFormatType
	SAFTADPCM_11kHzMono           =59         # from enum SpeechAudioFormatType
	SAFTADPCM_11kHzStereo         =60         # from enum SpeechAudioFormatType
	SAFTADPCM_22kHzMono           =61         # from enum SpeechAudioFormatType
	SAFTADPCM_22kHzStereo         =62         # from enum SpeechAudioFormatType
	SAFTADPCM_44kHzMono           =63         # from enum SpeechAudioFormatType
	SAFTADPCM_44kHzStereo         =64         # from enum SpeechAudioFormatType
	SAFTADPCM_8kHzMono            =57         # from enum SpeechAudioFormatType
	SAFTADPCM_8kHzStereo          =58         # from enum SpeechAudioFormatType
	SAFTCCITT_ALaw_11kHzMono      =43         # from enum SpeechAudioFormatType
	SAFTCCITT_ALaw_11kHzStereo    =44         # from enum SpeechAudioFormatType
	SAFTCCITT_ALaw_22kHzMono      =45         # from enum SpeechAudioFormatType
	SAFTCCITT_ALaw_22kHzStereo    =46         # from enum SpeechAudioFormatType
	SAFTCCITT_ALaw_44kHzMono      =47         # from enum SpeechAudioFormatType
	SAFTCCITT_ALaw_44kHzStereo    =48         # from enum SpeechAudioFormatType
	SAFTCCITT_ALaw_8kHzMono       =41         # from enum SpeechAudioFormatType
	SAFTCCITT_ALaw_8kHzStereo     =42         # from enum SpeechAudioFormatType
	SAFTCCITT_uLaw_11kHzMono      =51         # from enum SpeechAudioFormatType
	SAFTCCITT_uLaw_11kHzStereo    =52         # from enum SpeechAudioFormatType
	SAFTCCITT_uLaw_22kHzMono      =53         # from enum SpeechAudioFormatType
	SAFTCCITT_uLaw_22kHzStereo    =54         # from enum SpeechAudioFormatType
	SAFTCCITT_uLaw_44kHzMono      =55         # from enum SpeechAudioFormatType
	SAFTCCITT_uLaw_44kHzStereo    =56         # from enum SpeechAudioFormatType
	SAFTCCITT_uLaw_8kHzMono       =49         # from enum SpeechAudioFormatType
	SAFTCCITT_uLaw_8kHzStereo     =50         # from enum SpeechAudioFormatType
	SAFTDefault                   =-1         # from enum SpeechAudioFormatType
	SAFTExtendedAudioFormat       =3          # from enum SpeechAudioFormatType
	SAFTGSM610_11kHzMono          =66         # from enum SpeechAudioFormatType
	SAFTGSM610_22kHzMono          =67         # from enum SpeechAudioFormatType
	SAFTGSM610_44kHzMono          =68         # from enum SpeechAudioFormatType
	SAFTGSM610_8kHzMono           =65         # from enum SpeechAudioFormatType
	SAFTNoAssignedFormat          =0          # from enum SpeechAudioFormatType
	SAFTNonStandardFormat         =2          # from enum SpeechAudioFormatType
	SAFTText                      =1          # from enum SpeechAudioFormatType
	SAFTTrueSpeech_8kHz1BitMono   =40         # from enum SpeechAudioFormatType
	SASClosed                     =0          # from enum SpeechAudioState
	SASPause                      =2          # from enum SpeechAudioState
	SASRun                        =3          # from enum SpeechAudioState
	SASStop                       =1          # from enum SpeechAudioState
	SBONone                       =0          # from enum SpeechBookmarkOptions
	SBOPause                      =1          # from enum SpeechBookmarkOptions
	SpeechAllElements             =-1         # from enum SpeechConstants
	Speech_Default_Weight         =1.0        # from enum SpeechConstants
	Speech_Max_Pron_Length        =384        # from enum SpeechConstants
	Speech_Max_Word_Length        =128        # from enum SpeechConstants
	Speech_StreamPos_Asap         =0          # from enum SpeechConstants
	Speech_StreamPos_RealTime     =-1         # from enum SpeechConstants
	SDKLCurrentConfig             =5          # from enum SpeechDataKeyLocation
	SDKLCurrentUser               =1          # from enum SpeechDataKeyLocation
	SDKLDefaultLocation           =0          # from enum SpeechDataKeyLocation
	SDKLLocalMachine              =2          # from enum SpeechDataKeyLocation
	SDTAll                        =255        # from enum SpeechDiscardType
	SDTAlternates                 =128        # from enum SpeechDiscardType
	SDTAudio                      =64         # from enum SpeechDiscardType
	SDTDisplayText                =8          # from enum SpeechDiscardType
	SDTLexicalForm                =16         # from enum SpeechDiscardType
	SDTPronunciation              =32         # from enum SpeechDiscardType
	SDTProperty                   =1          # from enum SpeechDiscardType
	SDTReplacement                =2          # from enum SpeechDiscardType
	SDTRule                       =4          # from enum SpeechDiscardType
	SDA_Consume_Leading_Spaces    =8          # from enum SpeechDisplayAttributes
	SDA_No_Trailing_Space         =0          # from enum SpeechDisplayAttributes
	SDA_One_Trailing_Space        =2          # from enum SpeechDisplayAttributes
	SDA_Two_Trailing_Spaces       =4          # from enum SpeechDisplayAttributes
	SECFDefault                   =196609     # from enum SpeechEmulationCompareFlags
	SECFEmulateResult             =1073741824 # from enum SpeechEmulationCompareFlags
	SECFIgnoreCase                =1          # from enum SpeechEmulationCompareFlags
	SECFIgnoreKanaType            =65536      # from enum SpeechEmulationCompareFlags
	SECFIgnoreWidth               =131072     # from enum SpeechEmulationCompareFlags
	SECFNoSpecialChars            =536870912  # from enum SpeechEmulationCompareFlags
	SECHighConfidence             =1          # from enum SpeechEngineConfidence
	SECLowConfidence              =-1         # from enum SpeechEngineConfidence
	SECNormalConfidence           =0          # from enum SpeechEngineConfidence
	SFTInput                      =0          # from enum SpeechFormatType
	SFTSREngine                   =1          # from enum SpeechFormatType
	SGRSTTDictation               =3          # from enum SpeechGrammarRuleStateTransitionType
	SGRSTTEpsilon                 =0          # from enum SpeechGrammarRuleStateTransitionType
	SGRSTTRule                    =2          # from enum SpeechGrammarRuleStateTransitionType
	SGRSTTTextBuffer              =5          # from enum SpeechGrammarRuleStateTransitionType
	SGRSTTWildcard                =4          # from enum SpeechGrammarRuleStateTransitionType
	SGRSTTWord                    =1          # from enum SpeechGrammarRuleStateTransitionType
	SGSDisabled                   =0          # from enum SpeechGrammarState
	SGSEnabled                    =1          # from enum SpeechGrammarState
	SGSExclusive                  =3          # from enum SpeechGrammarState
	SGDisplay                     =0          # from enum SpeechGrammarWordType
	SGLexical                     =1          # from enum SpeechGrammarWordType
	SGLexicalNoSpecialChars       =3          # from enum SpeechGrammarWordType
	SGPronounciation              =2          # from enum SpeechGrammarWordType
	SINoSignal                    =2          # from enum SpeechInterference
	SINoise                       =1          # from enum SpeechInterference
	SINone                        =0          # from enum SpeechInterference
	SITooFast                     =5          # from enum SpeechInterference
	SITooLoud                     =3          # from enum SpeechInterference
	SITooQuiet                    =4          # from enum SpeechInterference
	SITooSlow                     =6          # from enum SpeechInterference
	SLTApp                        =2          # from enum SpeechLexiconType
	SLTUser                       =1          # from enum SpeechLexiconType
	SLODynamic                    =1          # from enum SpeechLoadOption
	SLOStatic                     =0          # from enum SpeechLoadOption
	SPSFunction                   =16384      # from enum SpeechPartOfSpeech
	SPSInterjection               =20480      # from enum SpeechPartOfSpeech
	SPSLMA                        =28672      # from enum SpeechPartOfSpeech
	SPSModifier                   =12288      # from enum SpeechPartOfSpeech
	SPSNotOverriden               =-1         # from enum SpeechPartOfSpeech
	SPSNoun                       =4096       # from enum SpeechPartOfSpeech
	SPSSuppressWord               =61440      # from enum SpeechPartOfSpeech
	SPSUnknown                    =0          # from enum SpeechPartOfSpeech
	SPSVerb                       =8192       # from enum SpeechPartOfSpeech
	SRCS_Disabled                 =0          # from enum SpeechRecoContextState
	SRCS_Enabled                  =1          # from enum SpeechRecoContextState
	SREAdaptation                 =8192       # from enum SpeechRecoEvents
	SREAllEvents                  =393215     # from enum SpeechRecoEvents
	SREAudioLevel                 =65536      # from enum SpeechRecoEvents
	SREBookmark                   =64         # from enum SpeechRecoEvents
	SREFalseRecognition           =512        # from enum SpeechRecoEvents
	SREHypothesis                 =32         # from enum SpeechRecoEvents
	SREInterference               =1024       # from enum SpeechRecoEvents
	SREPhraseStart                =8          # from enum SpeechRecoEvents
	SREPrivate                    =262144     # from enum SpeechRecoEvents
	SREPropertyNumChange          =128        # from enum SpeechRecoEvents
	SREPropertyStringChange       =256        # from enum SpeechRecoEvents
	SRERecoOtherContext           =32768      # from enum SpeechRecoEvents
	SRERecognition                =16         # from enum SpeechRecoEvents
	SRERequestUI                  =2048       # from enum SpeechRecoEvents
	SRESoundEnd                   =4          # from enum SpeechRecoEvents
	SRESoundStart                 =2          # from enum SpeechRecoEvents
	SREStateChange                =4096       # from enum SpeechRecoEvents
	SREStreamEnd                  =1          # from enum SpeechRecoEvents
	SREStreamStart                =16384      # from enum SpeechRecoEvents
	SRTAutopause                  =1          # from enum SpeechRecognitionType
	SRTEmulated                   =2          # from enum SpeechRecognitionType
	SRTExtendableParse            =8          # from enum SpeechRecognitionType
	SRTReSent                     =16         # from enum SpeechRecognitionType
	SRTSMLTimeout                 =4          # from enum SpeechRecognitionType
	SRTStandard                   =0          # from enum SpeechRecognitionType
	SRSActive                     =1          # from enum SpeechRecognizerState
	SRSActiveAlways               =2          # from enum SpeechRecognizerState
	SRSInactive                   =0          # from enum SpeechRecognizerState
	SRSInactiveWithPurge          =3          # from enum SpeechRecognizerState
	SRAONone                      =0          # from enum SpeechRetainedAudioOptions
	SRAORetainAudio               =1          # from enum SpeechRetainedAudioOptions
	SRADefaultToActive            =2          # from enum SpeechRuleAttributes
	SRADynamic                    =32         # from enum SpeechRuleAttributes
	SRAExport                     =4          # from enum SpeechRuleAttributes
	SRAImport                     =8          # from enum SpeechRuleAttributes
	SRAInterpreter                =16         # from enum SpeechRuleAttributes
	SRARoot                       =64         # from enum SpeechRuleAttributes
	SRATopLevel                   =1          # from enum SpeechRuleAttributes
	SGDSActive                    =1          # from enum SpeechRuleState
	SGDSActiveUserDelimited       =4          # from enum SpeechRuleState
	SGDSActiveWithAutoPause       =3          # from enum SpeechRuleState
	SGDSInactive                  =0          # from enum SpeechRuleState
	SRSEDone                      =1          # from enum SpeechRunState
	SRSEIsSpeaking                =2          # from enum SpeechRunState
	SSTTDictation                 =2          # from enum SpeechSpecialTransitionType
	SSTTTextBuffer                =3          # from enum SpeechSpecialTransitionType
	SSTTWildcard                  =1          # from enum SpeechSpecialTransitionType
	SSFMCreate                    =2          # from enum SpeechStreamFileMode
	SSFMCreateForWrite            =3          # from enum SpeechStreamFileMode
	SSFMOpenForRead               =0          # from enum SpeechStreamFileMode
	SSFMOpenReadWrite             =1          # from enum SpeechStreamFileMode
	SSSPTRelativeToCurrentPosition=1          # from enum SpeechStreamSeekPositionType
	SSSPTRelativeToEnd            =2          # from enum SpeechStreamSeekPositionType
	SSSPTRelativeToStart          =0          # from enum SpeechStreamSeekPositionType
	SpeechAddRemoveWord           =u'AddRemoveWord' # from enum SpeechStringConstants
	SpeechAudioFormatGUIDText     =u'{7CEEF9F9-3D13-11d2-9EE7-00C04F797396}' # from enum SpeechStringConstants
	SpeechAudioFormatGUIDWave     =u'{C31ADBAE-527F-4ff5-A230-F62BB61FF70C}' # from enum SpeechStringConstants
	SpeechAudioProperties         =u'AudioProperties' # from enum SpeechStringConstants
	SpeechAudioVolume             =u'AudioVolume' # from enum SpeechStringConstants
	SpeechCategoryAppLexicons     =u'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\AppLexicons' # from enum SpeechStringConstants
	SpeechCategoryAudioIn         =u'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\AudioInput' # from enum SpeechStringConstants
	SpeechCategoryAudioOut        =u'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\AudioOutput' # from enum SpeechStringConstants
	SpeechCategoryPhoneConverters =u'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\PhoneConverters' # from enum SpeechStringConstants
	SpeechCategoryRecoProfiles    =u'HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Speech\\RecoProfiles' # from enum SpeechStringConstants
	SpeechCategoryRecognizers     =u'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Recognizers' # from enum SpeechStringConstants
	SpeechCategoryVoices          =u'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices' # from enum SpeechStringConstants
	SpeechDictationTopicSpelling  =u'Spelling' # from enum SpeechStringConstants
	SpeechEngineProperties        =u'EngineProperties' # from enum SpeechStringConstants
	SpeechGrammarTagDictation     =u'*'       # from enum SpeechStringConstants
	SpeechGrammarTagUnlimitedDictation=u'*+'      # from enum SpeechStringConstants
	SpeechGrammarTagWildcard      =u'...'     # from enum SpeechStringConstants
	SpeechMicTraining             =u'MicTraining' # from enum SpeechStringConstants
	SpeechPropertyAdaptationOn    =u'AdaptationOn' # from enum SpeechStringConstants
	SpeechPropertyComplexResponseSpeed=u'ComplexResponseSpeed' # from enum SpeechStringConstants
	SpeechPropertyHighConfidenceThreshold=u'HighConfidenceThreshold' # from enum SpeechStringConstants
	SpeechPropertyLowConfidenceThreshold=u'LowConfidenceThreshold' # from enum SpeechStringConstants
	SpeechPropertyNormalConfidenceThreshold=u'NormalConfidenceThreshold' # from enum SpeechStringConstants
	SpeechPropertyResourceUsage   =u'ResourceUsage' # from enum SpeechStringConstants
	SpeechPropertyResponseSpeed   =u'ResponseSpeed' # from enum SpeechStringConstants
	SpeechRecoProfileProperties   =u'RecoProfileProperties' # from enum SpeechStringConstants
	SpeechRegistryLocalMachineRoot=u'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech' # from enum SpeechStringConstants
	SpeechRegistryUserRoot        =u'HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Speech' # from enum SpeechStringConstants
	SpeechTokenIdUserLexicon      =u'HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Speech\\CurrentUserLexicon' # from enum SpeechStringConstants
	SpeechTokenKeyAttributes      =u'Attributes' # from enum SpeechStringConstants
	SpeechTokenKeyFiles           =u'Files'   # from enum SpeechStringConstants
	SpeechTokenKeyUI              =u'UI'      # from enum SpeechStringConstants
	SpeechTokenValueCLSID         =u'CLSID'   # from enum SpeechStringConstants
	SpeechUserTraining            =u'UserTraining' # from enum SpeechStringConstants
	SpeechVoiceCategoryTTSRate    =u'DefaultTTSRate' # from enum SpeechStringConstants
	SpeechVoiceSkipTypeSentence   =u'Sentence' # from enum SpeechStringConstants
	STCAll                        =23         # from enum SpeechTokenContext
	STCInprocHandler              =2          # from enum SpeechTokenContext
	STCInprocServer               =1          # from enum SpeechTokenContext
	STCLocalServer                =4          # from enum SpeechTokenContext
	STCRemoteServer               =16         # from enum SpeechTokenContext
	STSF_AppData                  =26         # from enum SpeechTokenShellFolder
	STSF_CommonAppData            =35         # from enum SpeechTokenShellFolder
	STSF_FlagCreate               =32768      # from enum SpeechTokenShellFolder
	STSF_LocalAppData             =28         # from enum SpeechTokenShellFolder
	SVF_Emphasis                  =2          # from enum SpeechVisemeFeature
	SVF_None                      =0          # from enum SpeechVisemeFeature
	SVF_Stressed                  =1          # from enum SpeechVisemeFeature
	SVP_0                         =0          # from enum SpeechVisemeType
	SVP_1                         =1          # from enum SpeechVisemeType
	SVP_10                        =10         # from enum SpeechVisemeType
	SVP_11                        =11         # from enum SpeechVisemeType
	SVP_12                        =12         # from enum SpeechVisemeType
	SVP_13                        =13         # from enum SpeechVisemeType
	SVP_14                        =14         # from enum SpeechVisemeType
	SVP_15                        =15         # from enum SpeechVisemeType
	SVP_16                        =16         # from enum SpeechVisemeType
	SVP_17                        =17         # from enum SpeechVisemeType
	SVP_18                        =18         # from enum SpeechVisemeType
	SVP_19                        =19         # from enum SpeechVisemeType
	SVP_2                         =2          # from enum SpeechVisemeType
	SVP_20                        =20         # from enum SpeechVisemeType
	SVP_21                        =21         # from enum SpeechVisemeType
	SVP_3                         =3          # from enum SpeechVisemeType
	SVP_4                         =4          # from enum SpeechVisemeType
	SVP_5                         =5          # from enum SpeechVisemeType
	SVP_6                         =6          # from enum SpeechVisemeType
	SVP_7                         =7          # from enum SpeechVisemeType
	SVP_8                         =8          # from enum SpeechVisemeType
	SVP_9                         =9          # from enum SpeechVisemeType
	SVEAllEvents                  =33790      # from enum SpeechVoiceEvents
	SVEAudioLevel                 =512        # from enum SpeechVoiceEvents
	SVEBookmark                   =16         # from enum SpeechVoiceEvents
	SVEEndInputStream             =4          # from enum SpeechVoiceEvents
	SVEPhoneme                    =64         # from enum SpeechVoiceEvents
	SVEPrivate                    =32768      # from enum SpeechVoiceEvents
	SVESentenceBoundary           =128        # from enum SpeechVoiceEvents
	SVEStartInputStream           =2          # from enum SpeechVoiceEvents
	SVEViseme                     =256        # from enum SpeechVoiceEvents
	SVEVoiceChange                =8          # from enum SpeechVoiceEvents
	SVEWordBoundary               =32         # from enum SpeechVoiceEvents
	SVPAlert                      =1          # from enum SpeechVoicePriority
	SVPNormal                     =0          # from enum SpeechVoicePriority
	SVPOver                       =2          # from enum SpeechVoicePriority
	SVSFDefault                   =0          # from enum SpeechVoiceSpeakFlags
	SVSFIsFilename                =4          # from enum SpeechVoiceSpeakFlags
	SVSFIsNotXML                  =16         # from enum SpeechVoiceSpeakFlags
	SVSFIsXML                     =8          # from enum SpeechVoiceSpeakFlags
	SVSFNLPMask                   =64         # from enum SpeechVoiceSpeakFlags
	SVSFNLPSpeakPunc              =64         # from enum SpeechVoiceSpeakFlags
	SVSFParseAutodetect           =0          # from enum SpeechVoiceSpeakFlags
	SVSFParseMask                 =384        # from enum SpeechVoiceSpeakFlags
	SVSFParseSapi                 =128        # from enum SpeechVoiceSpeakFlags
	SVSFParseSsml                 =256        # from enum SpeechVoiceSpeakFlags
	SVSFPersistXML                =32         # from enum SpeechVoiceSpeakFlags
	SVSFPurgeBeforeSpeak          =2          # from enum SpeechVoiceSpeakFlags
	SVSFUnusedFlags               =-512       # from enum SpeechVoiceSpeakFlags
	SVSFVoiceMask                 =511        # from enum SpeechVoiceSpeakFlags
	SVSFlagsAsync                 =1          # from enum SpeechVoiceSpeakFlags
	SWPKnownWordPronounceable     =2          # from enum SpeechWordPronounceable
	SWPUnknownWordPronounceable   =1          # from enum SpeechWordPronounceable
	SWPUnknownWordUnpronounceable =0          # from enum SpeechWordPronounceable
	SWTAdded                      =1          # from enum SpeechWordType
	SWTDeleted                    =2          # from enum SpeechWordType
	SPAS_CLOSED                   =0          # from enum _SPAUDIOSTATE
	SPAS_PAUSE                    =2          # from enum _SPAUDIOSTATE
	SPAS_RUN                      =3          # from enum _SPAUDIOSTATE
	SPAS_STOP                     =1          # from enum _SPAUDIOSTATE

RecordMap = {
	###u'SPRULE': '{00000000-0000-0000-0000-000000000000}', # Record disabled because it doesn't have a non-null GUID
}

CLSIDToClassMap = {}
CLSIDToPackageMap = {
	'{CFF8E175-019E-11D3-A08E-00C04F8EF9B5}' : u'ISpeechAudio',
	'{7013943A-E2EC-11D2-A086-00C04F8EF9B5}' : u'SpStreamFormatConverter',
	'{3BEE4890-4FE9-4A37-8C1E-5E7E12791C1F}' : u'SpSharedRecognizer',
	'{9185F743-1143-4C28-86B5-BFF14F20E5C8}' : u'SpPhoneConverter',
	'{7A1EF0D5-1581-4741-88E4-209A49F11A10}' : u'ISpeechWaveFormatEx',
	'{947812B3-2AE1-4644-BA86-9E90DED7EC91}' : u'SpFileStream',
	'{0F92030A-CBFD-4AB8-A164-FF5985547FF6}' : u'SpTextSelectionInformation',
	'{EABCE657-75BC-44A2-AA7F-C56476742963}' : u'ISpeechGrammarRuleStateTransitions',
	'{CAFD1DB1-41D1-4A06-9863-E2E81DA17A9A}' : u'ISpeechGrammarRuleStateTransition',
	'{1A9E9F4F-104F-4DB8-A115-EFD7FD0C97AE}' : u'ISpeechCustomStream',
	'{41B89B6B-9399-11D2-9623-00C04F8EE628}' : u'SpInprocRecognizer',
	'{4F414126-DFE3-4629-99EE-797978317EAD}' : u'SpPhoneticAlphabetConverter',
	'{7B8FCB42-0E9D-4F00-A048-7B04D6179D3D}' : u'_ISpeechRecoContextEvents',
	'{9EF96870-E160-4792-820D-48CF0649E4EC}' : u'SpAudioFormat',
	'{9047D593-01DD-4B72-81A3-E4A0CA69F407}' : u'ISpeechPhraseRules',
	'{0D722F1A-9FCF-4E62-96D8-6DF8F01A26AA}' : u'SpShortcut',
	'{AF67F125-AB39-4E93-B4A2-CC2E66E182A7}' : u'ISpeechFileStream',
	'{0626B328-3478-467D-A0B3-D0853B93DDA3}' : u'ISpeechPhraseElements',
	'{27864A2A-2B9F-4CB8-92D3-0D2722FD1E73}' : u'ISpeechPhraseAlternate',
	'{715D9C59-4442-11D2-9605-00C04F8EE628}' : u'SpStream',
	'{269316D8-57BD-11D2-9EEE-00C04F797396}' : u'ISpeechVoice',
	'{6450336F-7D49-4CED-8097-49D6DEE37294}' : u'ISpeechBaseStream',
	'{3C76AF6D-1FD7-4831-81D1-3B71D5A13C44}' : u'ISpeechMMSysAudio',
	'{4E5B933C-C9BE-48ED-8842-1EE51BB1D4FF}' : u'ISpeechLexiconWord',
	'{08166B47-102E-4B23-A599-BDB98DBFD1F4}' : u'ISpeechPhraseProperties',
	'{47206204-5ECA-11D2-960F-00C04F8EE628}' : u'SpSharedRecoContext',
	'{62B3B8FB-F6E7-41BE-BDCB-056B1C29EFC0}' : u'ISpeechRecoResultTimes',
	'{E6E9C590-3E18-40E3-8299-061F98BDE7C7}' : u'ISpeechAudioFormat',
	'{8E0A246D-D3C8-45DE-8657-04290C458C3C}' : u'ISpeechRecoResult2',
	'{AFE719CF-5DD1-44F2-999C-7A399F1CFCCC}' : u'ISpeechGrammarRule',
	'{D4286F2C-EE67-45AE-B928-28D695362EDA}' : u'ISpeechGrammarRuleState',
	'{E6176F96-E373-4801-B223-3B62C068C0B4}' : u'ISpeechPhraseElement',
	'{2890A410-53A7-4FB5-94EC-06D4998E3D02}' : u'ISpeechPhraseReplacement',
	'{8BE47B07-57F6-11D2-9EEE-00C04F797396}' : u'ISpeechVoiceStatus',
	'{38BC662F-2257-4525-959E-2069D2596C05}' : u'ISpeechPhraseReplacements',
	'{EF411752-3736-4CB4-9C8C-8EF4CCB58EFE}' : u'SpObjectToken',
	'{580AA49D-7E1E-4809-B8E2-57DA806104B8}' : u'ISpeechRecoContext',
	'{8DBEF13F-1948-4AA8-8CF0-048EEBED95D8}' : u'SpCustomStream',
	'{3DA7627A-C7AE-4B23-8708-638C50362C25}' : u'ISpeechLexicon',
	'{72829128-5682-4704-A0D4-3E2BB6F2EAD3}' : u'ISpeechLexiconPronunciations',
	'{AAEC54AF-8F85-4924-944D-B79D39D72E19}' : u'ISpeechXMLRecoResult',
	'{A8C680EB-3D32-11D2-9EE7-00C04F797396}' : u'SpMMAudioOut',
	'{C79A574C-63BE-44B9-801F-283F87F898BE}' : u'SpWaveFormatEx',
	'{2D5F1C0C-BD75-4B08-9478-3B11FEA2586C}' : u'ISpeechRecognizer',
	'{6FFA3B44-FC2D-40D1-8AFC-32911C7F1AD1}' : u'ISpeechGrammarRules',
	'{B9AC5783-FCD0-4B21-B119-B4F8DA8FD2C3}' : u'ISpeechResourceLoader',
	'{C9E37C15-DF92-4727-85D6-72E5EEB6995A}' : u'SpUnCompressedLexicon',
	'{C74A3ADC-B727-4500-A84A-B526721C8B8C}' : u'ISpeechObjectToken',
	'{CF3D2E50-53F2-11D2-960C-00C04F8EE628}' : u'SpMMAudioIn',
	'{ED2879CF-CED9-4EE6-A534-DE0191D5468D}' : u'ISpeechRecoResult',
	'{A910187F-0C7A-45AC-92CC-59EDAFB77B53}' : u'SpObjectTokenCategory',
	'{EEB14B68-808B-4ABE-A5EA-B51DA7588008}' : u'ISpeechMemoryStream',
	'{90903716-2F42-11D3-9C26-00C04F8EF87C}' : u'SpCompressedLexicon',
	'{CE563D48-961E-4732-A2E1-378A42B430BE}' : u'ISpeechPhraseProperty',
	'{73AD6842-ACE0-45E8-A4DD-8795881A2C2A}' : u'SpInProcRecoContext',
	'{9285B776-2E7B-4BC0-B53E-580EB6FA967F}' : u'ISpeechObjectTokens',
	'{3B9C7E7A-6EEE-4DED-9092-11657279ADBE}' : u'ISpeechTextSelectionInformation',
	'{B238B6D5-F276-4C3D-A6C1-2974801C3CC2}' : u'ISpeechPhraseAlternates',
	'{8D199862-415E-47D5-AC4F-FAA608B424E6}' : u'ISpeechLexiconWords',
	'{B6D6F79F-2158-4E50-B5BC-9A9CCD852A09}' : u'ISpeechRecoGrammar',
	'{A372ACD1-3BEF-4BBD-8FFB-CB3E2B416AF8}' : u'_ISpeechVoiceEvents',
	'{BFF9E781-53EC-484E-BB8A-0E1B5551E35C}' : u'ISpeechRecognizerStatus',
	'{C62D9C91-7458-47F6-862D-1EF86FB0B278}' : u'ISpeechAudioStatus',
	'{6D60EB64-ACED-40A6-BBF3-4E557F71DEE2}' : u'ISpeechRecoResultDispatch',
	'{CE17C09B-4EFA-44D5-A4C9-59D9585AB0CD}' : u'ISpeechDataKey',
	'{E2AE5372-5D40-11D2-960E-00C04F8EE628}' : u'SpNotifyTranslator',
	'{455F24E9-7396-4A16-9715-7C0FDBE3EFE3}' : u'SpNullPhoneConverter',
	'{95252C5D-9E43-4F4A-9899-48EE73352F9F}' : u'ISpeechLexiconPronunciation',
	'{CA7EAC50-2D01-4145-86D4-5AE7D70F4469}' : u'ISpeechObjectTokenCategory',
	'{C23FC28D-C55F-4720-8B32-91F73C2BD5D1}' : u'SpPhraseInfoBuilder',
	'{3B151836-DF3A-4E0A-846C-D2ADC9334333}' : u'ISpeechPhraseInfoBuilder',
	'{C3E4F353-433F-43D6-89A1-6A62A7054C3D}' : u'ISpeechPhoneConverter',
	'{AB1890A0-E91F-11D2-BB91-00C04F8EE6C0}' : u'SpMMAudioEnum',
	'{961559CF-4E67-4662-8BF0-D93F1FCD61B3}' : u'ISpeechPhraseInfo',
	'{0655E396-25D0-11D3-9C26-00C04F8EF87C}' : u'SpLexicon',
	'{A7BFE112-A4A0-48D9-B602-C313843F6964}' : u'ISpeechPhraseRule',
	'{96749373-3391-11D2-9EE3-00C04F797396}' : u'SpResourceManager',
	'{11B103D8-1142-4EDF-A093-82FB3915F8CC}' : u'ISpeechAudioBufferInfo',
	'{96749377-3391-11D2-9EE3-00C04F797396}' : u'SpVoice',
	'{5FB7EF7D-DFF4-468A-B6B7-2FCBD188F994}' : u'SpMemoryStream',
}
VTablesToClassMap = {}
VTablesToPackageMap = {
	'{CFF8E175-019E-11D3-A08E-00C04F8EF9B5}' : 'ISpeechAudio',
	'{5B4FB971-B115-4DE1-AD97-E482E3BF6EE4}' : 'ISpProperties',
	'{8FC6D974-C81E-4098-93C5-0147F61ED4D3}' : 'ISpRecognizer2',
	'{C05C768F-FAE8-4EC2-8E07-338321C12452}' : 'ISpAudio',
	'{7A1EF0D5-1581-4741-88E4-209A49F11A10}' : 'ISpeechWaveFormatEx',
	'{4B37BC9E-9ED6-44A3-93D3-18F022B79EC3}' : 'ISpRecoGrammar2',
	'{20B053BE-E235-43CD-9A2A-8D17A48B7842}' : 'ISpRecoResult',
	'{EABCE657-75BC-44A2-AA7F-C56476742963}' : 'ISpeechGrammarRuleStateTransitions',
	'{ACA16614-5D3D-11D2-960E-00C04F8EE628}' : 'ISpNotifyTranslator',
	'{CAFD1DB1-41D1-4A06-9863-E2E81DA17A9A}' : 'ISpeechGrammarRuleStateTransition',
	'{1A9E9F4F-104F-4DB8-A115-EFD7FD0C97AE}' : 'ISpeechCustomStream',
	'{2D3D3845-39AF-4850-BBF9-40B49780011D}' : 'ISpObjectTokenCategory',
	'{BE7A9CC9-5F9E-11D2-960F-00C04F8EE628}' : 'ISpEventSink',
	'{B2745EFD-42CE-48CA-81F1-A96E02538A90}' : 'ISpPhoneticAlphabetSelection',
	'{BE7A9CCE-5F9E-11D2-960F-00C04F8EE628}' : 'ISpEventSource',
	'{DF1B943C-5838-4AA2-8706-D7CD5B333499}' : 'ISpRecognizer3',
	'{5EFF4AEF-8487-11D2-961C-00C04F8EE628}' : 'ISpNotifySource',
	'{9047D593-01DD-4B72-81A3-E4A0CA69F407}' : 'ISpeechPhraseRules',
	'{21B501A0-0EC7-46C9-92C3-A2BC784C54B9}' : 'ISpSerializeState',
	'{79EAC9ED-BAF9-11CE-8C82-00AA004BA90B}' : 'IInternetSecurityMgrSite',
	'{79EAC9EE-BAF9-11CE-8C82-00AA004BA90B}' : 'IInternetSecurityManager',
	'{15806F6E-1D70-4B48-98E6-3B1A007509AB}' : 'ISpMMSysAudio',
	'{AF67F125-AB39-4E93-B4A2-CC2E66E182A7}' : 'ISpeechFileStream',
	'{0626B328-3478-467D-A0B3-D0853B93DDA3}' : 'ISpeechPhraseElements',
	'{27864A2A-2B9F-4CB8-92D3-0D2722FD1E73}' : 'ISpeechPhraseAlternate',
	'{269316D8-57BD-11D2-9EEE-00C04F797396}' : 'ISpeechVoice',
	'{259684DC-37C3-11D2-9603-00C04F8EE628}' : 'ISpNotifySink',
	'{6450336F-7D49-4CED-8097-49D6DEE37294}' : 'ISpeechBaseStream',
	'{8FCEBC98-4E49-4067-9C6C-D86A0E092E3D}' : 'ISpPhraseAlt',
	'{3C76AF6D-1FD7-4831-81D1-3B71D5A13C44}' : 'ISpeechMMSysAudio',
	'{5B559F40-E952-11D2-BB91-00C04F8EE6C0}' : 'ISpObjectWithToken',
	'{4E5B933C-C9BE-48ED-8842-1EE51BB1D4FF}' : 'ISpeechLexiconWord',
	'{133ADCD4-19B4-4020-9FDC-842E78253B17}' : 'ISpPhoneticAlphabetConverter',
	'{08166B47-102E-4B23-A599-BDB98DBFD1F4}' : 'ISpeechPhraseProperties',
	'{BEAD311C-52FF-437F-9464-6B21054CA73D}' : 'ISpRecoContext2',
	'{62B3B8FB-F6E7-41BE-BDCB-056B1C29EFC0}' : 'ISpeechRecoResultTimes',
	'{E6E9C590-3E18-40E3-8299-061F98BDE7C7}' : 'ISpeechAudioFormat',
	'{8E0A246D-D3C8-45DE-8657-04290C458C3C}' : 'ISpeechRecoResult2',
	'{0000000C-0000-0000-C000-000000000046}' : 'IStream',
	'{AFE719CF-5DD1-44F2-999C-7A399F1CFCCC}' : 'ISpeechGrammarRule',
	'{93384E18-5014-43D5-ADBB-A78E055926BD}' : 'ISpResourceManager',
	'{12E3CCA9-7518-44C5-A5E7-BA5A79CB929E}' : 'ISpStream',
	'{D4286F2C-EE67-45AE-B928-28D695362EDA}' : 'ISpeechGrammarRuleState',
	'{E6176F96-E373-4801-B223-3B62C068C0B4}' : 'ISpeechPhraseElement',
	'{2890A410-53A7-4FB5-94EC-06D4998E3D02}' : 'ISpeechPhraseReplacement',
	'{8137828F-591A-4A42-BE58-49EA7EBAAC68}' : 'ISpGrammarBuilder',
	'{1A5C0354-B621-4B5A-8791-D306ED379E53}' : 'ISpPhrase',
	'{8BE47B07-57F6-11D2-9EEE-00C04F797396}' : 'ISpeechVoiceStatus',
	'{38BC662F-2257-4525-959E-2069D2596C05}' : 'ISpeechPhraseReplacements',
	'{580AA49D-7E1E-4809-B8E2-57DA806104B8}' : 'ISpeechRecoContext',
	'{3DA7627A-C7AE-4B23-8708-638C50362C25}' : 'ISpeechLexicon',
	'{72829128-5682-4704-A0D4-3E2BB6F2EAD3}' : 'ISpeechLexiconPronunciations',
	'{AAEC54AF-8F85-4924-944D-B79D39D72E19}' : 'ISpeechXMLRecoResult',
	'{AE39362B-45A8-4074-9B9E-CCF49AA2D0B6}' : 'ISpXMLRecoResult',
	'{2D5F1C0C-BD75-4B08-9478-3B11FEA2586C}' : 'ISpeechRecognizer',
	'{6FFA3B44-FC2D-40D1-8AFC-32911C7F1AD1}' : 'ISpeechGrammarRules',
	'{C74A3ADC-B727-4500-A84A-B526721C8B8C}' : 'ISpeechObjectToken',
	'{C2B5F241-DAA0-4507-9E16-5A1EAA2B7A5C}' : 'ISpRecognizer',
	'{BED530BE-2606-4F4D-A1C0-54C5CDA5566F}' : 'ISpStreamFormat',
	'{ED2879CF-CED9-4EE6-A534-DE0191D5468D}' : 'ISpeechRecoResult',
	'{6C44DF74-72B9-4992-A1EC-EF996E0422D4}' : 'ISpVoice',
	'{EEB14B68-808B-4ABE-A5EA-B51DA7588008}' : 'ISpeechMemoryStream',
	'{CE563D48-961E-4732-A2E1-378A42B430BE}' : 'ISpeechPhraseProperty',
	'{9285B776-2E7B-4BC0-B53E-580EB6FA967F}' : 'ISpeechObjectTokens',
	'{3B9C7E7A-6EEE-4DED-9092-11657279ADBE}' : 'ISpeechTextSelectionInformation',
	'{DA0CD0F9-14A2-4F09-8C2A-85CC48979345}' : 'ISpRecoCategory',
	'{3DF681E2-EA56-11D9-8BDE-F66BAD1E3F3A}' : 'ISpShortcut',
	'{B238B6D5-F276-4C3D-A6C1-2974801C3CC2}' : 'ISpeechPhraseAlternates',
	'{8D199862-415E-47D5-AC4F-FAA608B424E6}' : 'ISpeechLexiconWords',
	'{6D5140C1-7436-11CE-8034-00AA006009FA}' : 'IServiceProvider',
	'{B6D6F79F-2158-4E50-B5BC-9A9CCD852A09}' : 'ISpeechRecoGrammar',
	'{06B64F9E-7FDA-11D2-B4F2-00C04F797396}' : 'IEnumSpObjectTokens',
	'{BFF9E781-53EC-484E-BB8A-0E1B5551E35C}' : 'ISpeechRecognizerStatus',
	'{C62D9C91-7458-47F6-862D-1EF86FB0B278}' : 'ISpeechAudioStatus',
	'{2177DB29-7F45-47D0-8554-067E91C80502}' : 'ISpRecoGrammar',
	'{6D60EB64-ACED-40A6-BBF3-4E557F71DEE2}' : 'ISpeechRecoResultDispatch',
	'{CE17C09B-4EFA-44D5-A4C9-59D9585AB0CD}' : 'ISpeechDataKey',
	'{95252C5D-9E43-4F4A-9899-48EE73352F9F}' : 'ISpeechLexiconPronunciation',
	'{CA7EAC50-2D01-4145-86D4-5AE7D70F4469}' : 'ISpeechObjectTokenCategory',
	'{8445C581-0CAC-4A38-ABFE-9B2CE2826455}' : 'ISpPhoneConverter',
	'{3B151836-DF3A-4E0A-846C-D2ADC9334333}' : 'ISpeechPhraseInfoBuilder',
	'{00000101-0000-0000-C000-000000000046}' : 'IEnumString',
	'{C3E4F353-433F-43D6-89A1-6A62A7054C3D}' : 'ISpeechPhoneConverter',
	'{0C733A30-2A1C-11CE-ADE5-00AA0044773D}' : 'ISequentialStream',
	'{678A932C-EA71-4446-9B41-78FDA6280A29}' : 'ISpStreamFormatConverter',
	'{961559CF-4E67-4662-8BF0-D93F1FCD61B3}' : 'ISpeechPhraseInfo',
	'{A7BFE112-A4A0-48D9-B602-C313843F6964}' : 'ISpeechPhraseRule',
	'{DA41A7C2-5383-4DB2-916B-6C1719E3DB58}' : 'ISpLexicon',
	'{11B103D8-1142-4EDF-A093-82FB3915F8CC}' : 'ISpeechAudioBufferInfo',
	'{14056581-E16C-11D2-BB90-00C04F8EE6C0}' : 'ISpDataKey',
	'{B9AC5783-FCD0-4B21-B119-B4F8DA8FD2C3}' : 'ISpeechResourceLoader',
	'{F740A62F-7C15-489E-8234-940A33D9272D}' : 'ISpRecoContext',
	'{14056589-E16C-11D2-BB90-00C04F8EE6C0}' : 'ISpObjectToken',
}


NamesToIIDMap = {
	'ISpeechRecoResult' : '{ED2879CF-CED9-4EE6-A534-DE0191D5468D}',
	'ISpRecoCategory' : '{DA0CD0F9-14A2-4F09-8C2A-85CC48979345}',
	'ISpeechPhraseProperties' : '{08166B47-102E-4B23-A599-BDB98DBFD1F4}',
	'ISpeechPhraseRules' : '{9047D593-01DD-4B72-81A3-E4A0CA69F407}',
	'ISpeechMemoryStream' : '{EEB14B68-808B-4ABE-A5EA-B51DA7588008}',
	'ISpeechAudioStatus' : '{C62D9C91-7458-47F6-862D-1EF86FB0B278}',
	'ISpEventSink' : '{BE7A9CC9-5F9E-11D2-960F-00C04F8EE628}',
	'ISpMMSysAudio' : '{15806F6E-1D70-4B48-98E6-3B1A007509AB}',
	'ISpeechGrammarRule' : '{AFE719CF-5DD1-44F2-999C-7A399F1CFCCC}',
	'ISpeechVoice' : '{269316D8-57BD-11D2-9EEE-00C04F797396}',
	'ISpNotifySink' : '{259684DC-37C3-11D2-9603-00C04F8EE628}',
	'ISpeechPhraseInfo' : '{961559CF-4E67-4662-8BF0-D93F1FCD61B3}',
	'ISpPhrase' : '{1A5C0354-B621-4B5A-8791-D306ED379E53}',
	'IEnumString' : '{00000101-0000-0000-C000-000000000046}',
	'ISpProperties' : '{5B4FB971-B115-4DE1-AD97-E482E3BF6EE4}',
	'ISpeechGrammarRuleState' : '{D4286F2C-EE67-45AE-B928-28D695362EDA}',
	'ISpeechPhraseReplacements' : '{38BC662F-2257-4525-959E-2069D2596C05}',
	'ISpeechAudio' : '{CFF8E175-019E-11D3-A08E-00C04F8EF9B5}',
	'ISpeechLexiconPronunciations' : '{72829128-5682-4704-A0D4-3E2BB6F2EAD3}',
	'ISpNotifyTranslator' : '{ACA16614-5D3D-11D2-960E-00C04F8EE628}',
	'ISpeechWaveFormatEx' : '{7A1EF0D5-1581-4741-88E4-209A49F11A10}',
	'ISpeechAudioBufferInfo' : '{11B103D8-1142-4EDF-A093-82FB3915F8CC}',
	'ISpRecognizer2' : '{8FC6D974-C81E-4098-93C5-0147F61ED4D3}',
	'ISpRecognizer3' : '{DF1B943C-5838-4AA2-8706-D7CD5B333499}',
	'ISpeechPhraseElement' : '{E6176F96-E373-4801-B223-3B62C068C0B4}',
	'IStream' : '{0000000C-0000-0000-C000-000000000046}',
	'ISpEventSource' : '{BE7A9CCE-5F9E-11D2-960F-00C04F8EE628}',
	'ISpRecoResult' : '{20B053BE-E235-43CD-9A2A-8D17A48B7842}',
	'ISpRecoGrammar2' : '{4B37BC9E-9ED6-44A3-93D3-18F022B79EC3}',
	'ISpeechRecoResultTimes' : '{62B3B8FB-F6E7-41BE-BDCB-056B1C29EFC0}',
	'ISpNotifySource' : '{5EFF4AEF-8487-11D2-961C-00C04F8EE628}',
	'ISpeechObjectTokens' : '{9285B776-2E7B-4BC0-B53E-580EB6FA967F}',
	'ISpRecognizer' : '{C2B5F241-DAA0-4507-9E16-5A1EAA2B7A5C}',
	'ISpRecoGrammar' : '{2177DB29-7F45-47D0-8554-067E91C80502}',
	'ISpeechRecoResult2' : '{8E0A246D-D3C8-45DE-8657-04290C458C3C}',
	'ISpObjectTokenCategory' : '{2D3D3845-39AF-4850-BBF9-40B49780011D}',
	'ISpStreamFormatConverter' : '{678A932C-EA71-4446-9B41-78FDA6280A29}',
	'ISpeechGrammarRules' : '{6FFA3B44-FC2D-40D1-8AFC-32911C7F1AD1}',
	'ISpeechLexiconWords' : '{8D199862-415E-47D5-AC4F-FAA608B424E6}',
	'IEnumSpObjectTokens' : '{06B64F9E-7FDA-11D2-B4F2-00C04F797396}',
	'ISpeechTextSelectionInformation' : '{3B9C7E7A-6EEE-4DED-9092-11657279ADBE}',
	'ISpPhoneticAlphabetSelection' : '{B2745EFD-42CE-48CA-81F1-A96E02538A90}',
	'ISpeechRecoGrammar' : '{B6D6F79F-2158-4E50-B5BC-9A9CCD852A09}',
	'ISpeechPhraseAlternate' : '{27864A2A-2B9F-4CB8-92D3-0D2722FD1E73}',
	'ISpeechMMSysAudio' : '{3C76AF6D-1FD7-4831-81D1-3B71D5A13C44}',
	'ISpeechRecoContext' : '{580AA49D-7E1E-4809-B8E2-57DA806104B8}',
	'ISpeechLexiconPronunciation' : '{95252C5D-9E43-4F4A-9899-48EE73352F9F}',
	'ISpeechPhraseReplacement' : '{2890A410-53A7-4FB5-94EC-06D4998E3D02}',
	'ISpeechGrammarRuleStateTransitions' : '{EABCE657-75BC-44A2-AA7F-C56476742963}',
	'ISpRecoContext2' : '{BEAD311C-52FF-437F-9464-6B21054CA73D}',
	'ISpPhoneConverter' : '{8445C581-0CAC-4A38-ABFE-9B2CE2826455}',
	'IInternetSecurityManager' : '{79EAC9EE-BAF9-11CE-8C82-00AA004BA90B}',
	'ISpLexicon' : '{DA41A7C2-5383-4DB2-916B-6C1719E3DB58}',
	'ISpeechRecognizer' : '{2D5F1C0C-BD75-4B08-9478-3B11FEA2586C}',
	'ISpeechPhoneConverter' : '{C3E4F353-433F-43D6-89A1-6A62A7054C3D}',
	'ISequentialStream' : '{0C733A30-2A1C-11CE-ADE5-00AA0044773D}',
	'ISpStream' : '{12E3CCA9-7518-44C5-A5E7-BA5A79CB929E}',
	'ISpeechLexiconWord' : '{4E5B933C-C9BE-48ED-8842-1EE51BB1D4FF}',
	'ISpRecoContext' : '{F740A62F-7C15-489E-8234-940A33D9272D}',
	'ISpeechVoiceStatus' : '{8BE47B07-57F6-11D2-9EEE-00C04F797396}',
	'ISpeechPhraseProperty' : '{CE563D48-961E-4732-A2E1-378A42B430BE}',
	'ISpeechPhraseRule' : '{A7BFE112-A4A0-48D9-B602-C313843F6964}',
	'ISpeechPhraseElements' : '{0626B328-3478-467D-A0B3-D0853B93DDA3}',
	'ISpPhoneticAlphabetConverter' : '{133ADCD4-19B4-4020-9FDC-842E78253B17}',
	'ISpeechCustomStream' : '{1A9E9F4F-104F-4DB8-A115-EFD7FD0C97AE}',
	'ISpStreamFormat' : '{BED530BE-2606-4F4D-A1C0-54C5CDA5566F}',
	'ISpeechXMLRecoResult' : '{AAEC54AF-8F85-4924-944D-B79D39D72E19}',
	'ISpeechPhraseAlternates' : '{B238B6D5-F276-4C3D-A6C1-2974801C3CC2}',
	'ISpShortcut' : '{3DF681E2-EA56-11D9-8BDE-F66BAD1E3F3A}',
	'ISpeechPhraseInfoBuilder' : '{3B151836-DF3A-4E0A-846C-D2ADC9334333}',
	'ISpPhraseAlt' : '{8FCEBC98-4E49-4067-9C6C-D86A0E092E3D}',
	'ISpGrammarBuilder' : '{8137828F-591A-4A42-BE58-49EA7EBAAC68}',
	'ISpVoice' : '{6C44DF74-72B9-4992-A1EC-EF996E0422D4}',
	'ISpDataKey' : '{14056581-E16C-11D2-BB90-00C04F8EE6C0}',
	'ISpXMLRecoResult' : '{AE39362B-45A8-4074-9B9E-CCF49AA2D0B6}',
	'ISpeechResourceLoader' : '{B9AC5783-FCD0-4B21-B119-B4F8DA8FD2C3}',
	'ISpeechObjectTokenCategory' : '{CA7EAC50-2D01-4145-86D4-5AE7D70F4469}',
	'ISpResourceManager' : '{93384E18-5014-43D5-ADBB-A78E055926BD}',
	'IInternetSecurityMgrSite' : '{79EAC9ED-BAF9-11CE-8C82-00AA004BA90B}',
	'ISpeechLexicon' : '{3DA7627A-C7AE-4B23-8708-638C50362C25}',
	'ISpeechAudioFormat' : '{E6E9C590-3E18-40E3-8299-061F98BDE7C7}',
	'ISpeechBaseStream' : '{6450336F-7D49-4CED-8097-49D6DEE37294}',
	'ISpeechRecognizerStatus' : '{BFF9E781-53EC-484E-BB8A-0E1B5551E35C}',
	'ISpeechDataKey' : '{CE17C09B-4EFA-44D5-A4C9-59D9585AB0CD}',
	'_ISpeechVoiceEvents' : '{A372ACD1-3BEF-4BBD-8FFB-CB3E2B416AF8}',
	'ISpeechRecoResultDispatch' : '{6D60EB64-ACED-40A6-BBF3-4E557F71DEE2}',
	'_ISpeechRecoContextEvents' : '{7B8FCB42-0E9D-4F00-A048-7B04D6179D3D}',
	'ISpeechGrammarRuleStateTransition' : '{CAFD1DB1-41D1-4A06-9863-E2E81DA17A9A}',
	'ISpObjectToken' : '{14056589-E16C-11D2-BB90-00C04F8EE6C0}',
	'IServiceProvider' : '{6D5140C1-7436-11CE-8034-00AA006009FA}',
	'ISpAudio' : '{C05C768F-FAE8-4EC2-8E07-338321C12452}',
	'ISpeechFileStream' : '{AF67F125-AB39-4E93-B4A2-CC2E66E182A7}',
	'ISpSerializeState' : '{21B501A0-0EC7-46C9-92C3-A2BC784C54B9}',
	'ISpObjectWithToken' : '{5B559F40-E952-11D2-BB91-00C04F8EE6C0}',
	'ISpeechObjectToken' : '{C74A3ADC-B727-4500-A84A-B526721C8B8C}',
}

win32com.client.constants.__dicts__.append(constants.__dict__)

