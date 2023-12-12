import crypto
from winerror import ERROR_ALREADY_EXISTS
from win32event import CreateMutex
from win32gui import GetWindowRect, SetWindowPos, SetForegroundWindow
from win32con import PROCESS_ALL_ACCESS, HWND_TOP, SWP_NOSIZE, WM_CLOSE
from win32process import GetProcessTimes, WriteProcessMemory, GetWindowThreadProcessId, TerminateProcess
from win32api import OpenProcess, GetModuleHandle, GetLastError, CloseHandle
from win32com.client import Dispatch
from comtypes.client import CreateObject
from PySide2.QtCore import QMutex, QMutexLocker, QTimer, QThread
from PySide2.QtWidgets import QMessageBox, QApplication, QWidget, QPushButton
from PySide2.QtGui import QScreen
import win32timezone
import subprocess
import copy
from logging.handlers import TimedRotatingFileHandler
import logging
import ctypes
import socket
import pythoncom
import os
import random
import json
import platform
import wmi
import time
import base64
client_ver = "5.4.40"
# 标准库

# 第三方库

# 本地库


# ------------------------- 插件命令类 ---------------------------
class BaseObj():  # 此类用来改方法名
    def __init__(self, obj):
        # 定制版本修改函数名
        if is_custom:
            self.CreateFoobarCustom = obj.EhUpARlLbu
            self.CreateFoobarEllipse = obj.lgCWKtKp
            self.CreateFoobarRect = obj.ntFmGJtEQZ
            self.CreateFoobarRoundRect = obj.XcQGdJtguFnpYBg
            self.FoobarClearText = obj.kxwQQPRPhhCW
            self.FoobarClose = obj.eLFWSdi
            self.FoobarDrawLine = obj.GyjUsURuHPaLswc
            self.FoobarDrawPic = obj.UhnzAqYQnmb
            self.FoobarDrawText = obj.lwNfAGUXeLKg
            self.FoobarFillRect = obj.WVdygTXbZArtRH
            self.FoobarLock = obj.EPRaps
            self.FoobarPrintText = obj.jUtVN
            self.FoobarSetFont = obj.jUbXPaoBaY
            self.FoobarSetSave = obj.TcCoZrLkySlfRD
            self.FoobarStartGif = obj.BhnDMTiYLovm
            self.FoobarStopGif = obj.GjSkiPfhWuoWKI
            self.FoobarTextLineGap = obj.uECYqXBU
            self.FoobarTextPrintDir = obj.cwYLvs
            self.FoobarTextRect = obj.RXeoKWRjVugcmMj
            self.FoobarUnlock = obj.ZJqkXd
            self.FoobarUpdate = obj.fCgGqibEcEVniu
            self.FoobarSetTrans = obj.TXyFl
            self.ClientToScreen = obj.TmQwwjXLmljWJl
            self.EnumProcess = obj.mwAAfhmG
            self.EnumWindow = obj.UieFqMCYQPaen
            self.EnumWindowByProcess = obj.mfkNSHS
            self.EnumWindowByProcessId = obj.pPGqUHwUiGpBK
            self.EnumWindowSuper = obj.InSejfNtveK
            self.FindWindow = obj.BhCfg
            self.FindWindowByProcess = obj.rbzY
            self.FindWindowByProcessId = obj.genLsT
            self.FindWindowEx = obj.TkDrkZ
            self.FindWindowSuper = obj.UDtpQsFmk
            self.GetClientRect = obj.PxCDnBak
            self.GetClientSize = obj.nUhD
            self.GetForegroundFocus = obj.zcNz
            self.GetForegroundWindow = obj.vtRkyNoqrnhZX
            self.GetMousePointWindow = obj.vpFzlZALYaVgT
            self.GetPointWindow = obj.fKWFWazzcqXaNGu
            self.GetProcessInfo = obj.lFYw
            self.GetSpecialWindow = obj.HXsoZtnSEFeyHnv
            self.GetWindow = obj.vlTXcRmeuEQH
            self.GetWindowClass = obj.ZKnUzTJZyZR
            self.GetWindowProcessId = obj.rrJCQKxhSlUGQbj
            self.GetWindowProcessPath = obj.uyjryvMCTdMY
            self.GetWindowRect = obj.yRWu
            self.GetWindowState = obj.rSQuIfpoh
            self.GetWindowTitle = obj.UxiWrHXUxB
            self.MoveWindow = obj.IUfLPfw
            self.ScreenToClient = obj.GciSBjGDc
            self.SendPaste = obj.KUxNcySmLATs
            self.SendString = obj.DboIrdgPVhfbG
            self.SendString2 = obj.fYPdcJko
            self.SendStringIme = obj.audS
            self.SendStringIme2 = obj.uyRqNKMqpmcVDZ
            self.SetClientSize = obj.XlhXljfZP
            self.SetWindowSize = obj.DLKZEWRdXZSce
            self.SetWindowState = obj.YKLjYBQsGJE
            self.SetWindowText = obj.NuCTqzvojKfTEy
            self.SetWindowTransparent = obj.YlIH
            self.FaqCancel = obj.wJCzVjNXGpXLSl
            self.FaqCapture = obj.wBBnGFPtwNhK
            self.FaqCaptureFromFile = obj.lkbFvYMEzujuqHs
            self.FaqCaptureString = obj.WPksLcH
            self.FaqFetch = obj.eWbLpMeliu
            self.FaqGetSize = obj.tewWIWkDzuWLqP
            self.FaqPost = obj.ZNPlfhclgHVWv
            self.FaqSend = obj.LZilacmbQacEurx
            self.FaqIsPosted = obj.CozFmrQnyfZwSai
            self.DmGuard = obj.tZlT
            self.UnLoadDriver = obj.kBKGKLZtACiv
            self.DmGuardParams = obj.SNadiPYBF
            self.BindWindow = obj.KLprUwUyYe
            self.BindWindowEx = obj.IZcHi
            self.DownCpu = obj.XGgB
            self.EnableBind = obj.veoeNtjJcyjlw
            self.EnableFakeActive = obj.sMIRYsJWaxtIH
            self.EnableIme = obj.vpbrVbiRUGXdx
            self.EnableKeypadMsg = obj.KfDinEJ
            self.EnableKeypadPatch = obj.VMMvSfbfjU
            self.EnableKeypadSync = obj.FTfWkatMwuogm
            self.EnableMouseMsg = obj.WoFYndhrdwVIlC
            self.EnableMouseSync = obj.PYxmyt
            self.EnableRealKeypad = obj.cAaPLAY
            self.EnableRealMouse = obj.EaTcmnFGv
            self.EnableSpeedDx = obj.hvlfVB
            self.ForceUnBindWindow = obj.kmZSBhGrZbNpb
            self.GetBindWindow = obj.EYGoDwv
            self.IsBind = obj.qCiQQPz
            self.LockDisplay = obj.LeeUGc
            self.LockInput = obj.nJaMepmk
            self.LockMouseRect = obj.UYQZKJPhDWjG
            self.SetDisplayDelay = obj.GWuepJmxTT
            self.SwitchBindWindow = obj.UlfStVlLsYz
            self.UnBindWindow = obj.VWqvFMl
            self.SetAero = obj.qgkdIZRHka
            self.SetDisplayRefreshDelay = obj.gbpimGKd
            self.GetFps = obj.qfztxKcqAoS
            self.HackSpeed = obj.DbBEqDNPFABAQbh
            self.AsmAdd = obj.LgUHodDuYRoPXM
            self.AsmCall = obj.bYhZXzBG
            self.AsmClear = obj.SjBJvFgkkv
            self.DisAssemble = obj.rVvyZkRPRJqG
            self.Assemble = obj.XXvQHYlVLqMWo
            self.AsmCallEx = obj.mwTKHjqZPG
            self.AsmSetTimeout = obj.QeQPiDRFgLptVAS
            self.GetBasePath = obj.LJVcaVW
            self.GetDmCount = obj.YkepfNfW
            self.GetID = obj.foqUDNywRtqjt
            self.GetLastError = obj.FhDi
            self.GetPath = obj.EKTpCzlEgY
            self.Reg = obj.ioXTKlZ
            self.RegEx = obj.CDfXHzAgTc
            self.RegExNoMac = obj.FToaWdGEGQAqa
            self.RegNoMac = obj.pCFQuUZYHXo
            self.SetDisplayInput = obj.oPRGPq
            self.SetEnumWindowDelay = obj.bbcrh
            self.SetPath = obj.awkZJpPYUZrH
            self.SetShowErrorMsg = obj.bVAmUhmpmSaDt
            self.Ver = obj.sykFwA
            self.EnablePicCache = obj.MDgRXEUtSjJE
            self.SpeedNormalGraphic = obj.fDcTvsdiWy
            self.GetCursorPos = obj.juXWERLqVv
            self.GetCursorShape = obj.XBMIcT
            self.GetCursorShapeEx = obj.UwsWGYaQoo
            self.GetCursorSpot = obj.DmGNsPtnEZsS
            self.GetKeyState = obj.ozjTMcBhwfNQJnU
            self.KeyDown = obj.qvDU
            self.KeyDownChar = obj.MSNhDBJCWU
            self.KeyPress = obj.aGKRFugcoftZ
            self.KeyPressChar = obj.qWNaFdokRSsc
            self.KeyPressStr = obj.SbUaJnVBehL
            self.KeyUp = obj.vGxYUbRNAoew
            self.KeyUpChar = obj.zJEDsJBxqQ
            self.LeftClick = obj.kyDaLAjukVycraY
            self.LeftDoubleClick = obj.UVRioGoDkLxQRc
            self.LeftDown = obj.UmgZZlu
            self.LeftUp = obj.DKTPcrGHEfB
            self.MiddleClick = obj.cNWbWnGnzVoM
            self.MiddleDown = obj.HvNcrIYU
            self.MiddleUp = obj.zJiktWpnyI
            self.MoveR = obj.MjBZgaJKIo
            self.MoveTo = obj.tUtInvAB
            self.MoveToEx = obj.yKhPoqhiKxqxvQ
            self.RightClick = obj.dKRkHlS
            self.RightDown = obj.ImBrmWx
            self.RightUp = obj.iyQww
            self.SetKeypadDelay = obj.HomtUeYPy
            self.SetMouseDelay = obj.DyVTRgehaVBm
            self.SetSimMode = obj.VDFgIofmisHSTvf
            self.WaitKey = obj.BfRmdxDdN
            self.WheelDown = obj.eRywFINUvcbtkl
            self.WheelUp = obj.ExrwBAzyQsS
            self.GetMouseSpeed = obj.wYhSWQbNi
            self.SetMouseSpeed = obj.TAyZ
            self.EnableMouseAccuracy = obj.zGor
            self.DoubleToData = obj.wMZpYHHKEvvVkBR
            self.FindData = obj.zgAPc
            self.FindDataEx = obj.bauYhwei
            self.FindDouble = obj.BhaITY
            self.FindDoubleEx = obj.lxRp
            self.FindFloat = obj.htBZ
            self.FindFloatEx = obj.qwYRxLPxtVstqL
            self.FindInt = obj.vnBJWGERHCWXh
            self.FindIntEx = obj.kfeEwlDcNLlW
            self.FindString = obj.noMu
            self.FindStringEx = obj.diFIguSzZN
            self.FloatToData = obj.kSXVnC
            self.FreeProcessMemory = obj.bZJzFkjbVfyW
            self.GetCommandLine = obj.nsgFvWsGbPXf
            self.GetModuleBaseAddr = obj.TrdVeV
            self.IntToData = obj.GpiwxXzGz
            self.OpenProcess = obj.pyZnSzio
            self.ReadData = obj.HMHWzbBWVBF
            self.ReadDataAddr = obj.CybwUV
            self.ReadDouble = obj.LLQhnNYc
            self.ReadDoubleAddr = obj.dyuhInuivnv
            self.ReadFloat = obj.jAbYkBSKQb
            self.ReadFloatAddr = obj.sbMI
            self.ReadInt = obj.cvELYkBcWuzTEiA
            self.ReadIntAddr = obj.aKlCA
            self.ReadString = obj.aGRGSapQTQZtyL
            self.ReadStringAddr = obj.DEIza
            self.SetMemoryFindResultToFile = obj.ypzMeuKocnXwq
            self.SetMemoryHwndAsProcessId = obj.WkkrycCq
            self.StringToData = obj.FUMNfugw
            self.TerminateProcess = obj.YwglR
            self.VirtualAllocEx = obj.SZMJvf
            self.VirtualFreeEx = obj.vVumSoV
            self.WriteData = obj.JjHyzfsWKocbxw
            self.WriteDataAddr = obj.ZASzmYDGW
            self.WriteDouble = obj.xZJt
            self.WriteDoubleAddr = obj.bhKne
            self.WriteFloat = obj.BNGHkS
            self.WriteFloatAddr = obj.Eaqhdp
            self.WriteInt = obj.cTFNGpLBGrEkHYh
            self.WriteIntAddr = obj.MClrZjcQgwSUJhl
            self.WriteString = obj.iqJDKocUGgRtn
            self.WriteStringAddr = obj.RTvzj
            self.VirtualProtectEx = obj.ZDBfPVDux
            self.ReadDataToBin = obj.vWkVntbaxUhuj
            self.WriteDataFromBin = obj.zAQHB
            self.ReadDataAddrToBin = obj.KYkakaeddmLqQxT
            self.WriteDataAddrFromBin = obj.pcomjHDKrKKsGu
            self.SetParam64ToPointer = obj.EENRcWnwVxAo
            self.VirtualQueryEx = obj.geeHfrs
            self.GetRemoteApiAddress = obj.cihZrLUgBdC
            self.GetModuleSize = obj.clzCzfDkB
            self.ExcludePos = obj.SQYJ
            self.FindNearestPos = obj.SRYXeTqYfUpLq
            self.SortPosDistance = obj.piGbZseh
            self.AppendPicAddr = obj.GAZtftMFmtbh
            self.BGR2RGB = obj.VxUhDNlce
            self.Capture = obj.kYQzxxyjXPdKg
            self.CaptureGif = obj.rkFFlV
            self.CaptureJpg = obj.lTZeb
            self.CapturePng = obj.HRQQNH
            self.CapturePre = obj.nVEEPLbBM
            self.CmpColor = obj.mYjueWhY
            self.EnableDisplayDebug = obj.ILcRpCs
            self.EnableGetColorByCapture = obj.vNkRdjsapDK
            self.FindColor = obj.GsjYuLuqw
            self.FindColorBlock = obj.CTFpfS
            self.FindColorBlockEx = obj.IhDnxToNkaX
            self.FindColorE = obj.LZmYpG
            self.FindColorEx = obj.XGCtDEs
            self.FindMulColor = obj.qWdv
            self.FindMultiColor = obj.ayJmRGR
            self.FindMultiColorE = obj.zSjrzdbahcU
            self.FindMultiColorEx = obj.hUlX
            self.FindPic = obj.VXILbSmrtawg
            self.FindPicE = obj.nWhuSkjDQKkdCAn
            self.FindPicEx = obj.QNuAVaVedzePF
            self.FindPicExS = obj.nDvRmwtb
            self.FindPicMem = obj.AJouYeqtcrlgEv
            self.FindPicMemE = obj.sYZrEhIbNqDao
            self.FindPicMemEx = obj.XvQgfYK
            self.FindPicS = obj.Cdtn
            self.FindShape = obj.CjVZaZuKr
            self.FindShapeE = obj.FeUAguWNyklAoW
            self.FindShapeEx = obj.FgZH
            self.FreePic = obj.gxWWqdrMQHAbTzu
            self.GetAveHSV = obj.PtlvPItIr
            self.GetAveRGB = obj.euvaaQsvM
            self.GetColor = obj.XeXuRiCJlNbgw
            self.GetColorBGR = obj.ufVkmrQ
            self.GetColorHSV = obj.fnGouIjsfNXP
            self.GetColorNum = obj.kKluPeE
            self.GetPicSize = obj.GtbWDwrjJA
            self.GetScreenData = obj.njYitXhQM
            self.GetScreenDataBmp = obj.dgvvWzSYGK
            self.ImageToBmp = obj.nKvkuU
            self.IsDisplayDead = obj.iDzaZaRuIsZU
            self.LoadPic = obj.uiiqvBP
            self.MatchPicName = obj.VXoLeWKxgMhMuc
            self.RGB2BGR = obj.aaRFcTgYxxnf
            self.SetPicPwd = obj.hGeMyeSRVfKQ
            self.LoadPicByte = obj.LXLeD
            self.SetExcludeRegion = obj.mAIgdj
            self.EnableFindPicMultithread = obj.FSKsIlPk
            self.CopyFile = obj.PabUvUoKPPQ
            self.CreateFolder = obj.qDZbFRXDjmY
            self.DecodeFile = obj.bYBXIfnAyYqy
            self.DeleteFile = obj.sVqZeEwLHsKeN
            self.DeleteFolder = obj.ZudUoIZqmAbzEN
            self.DeleteIni = obj.dCzELknbdXiU
            self.DeleteIniPwd = obj.ihbRWLVAU
            self.DownloadFile = obj.HVDbZ
            self.EncodeFile = obj.YissQwTJnkrXTKJ
            self.EnumIniKey = obj.ZBCVhmC
            self.EnumIniKeyPwd = obj.DKfJwzXXHFV
            self.EnumIniSection = obj.aVyocvjHMk
            self.EnumIniSectionPwd = obj.tiayVZVwX
            self.GetFileLength = obj.Mbue
            self.IsFileExist = obj.cFNYJLxaYnbb
            self.MoveFile = obj.RfXCXaqQwVwJJr
            self.ReadFile = obj.wKRYWgHD
            self.ReadIni = obj.qLkyCUabEJmZX
            self.ReadIniPwd = obj.fAYufhdjxDte
            self.SelectDirectory = obj.RRXMSztNTLZCjk
            self.SelectFile = obj.fyYhtAWoyeTA
            self.WriteFile = obj.qQaQCefrnkH
            self.WriteIni = obj.UyDEwDzz
            self.WriteIniPwd = obj.MzDuizuo
            self.IsFolderExist = obj.IXAkYYRfcun
            self.GetRealPath = obj.yPFWSyyAw
            self.AddDict = obj.lUCMECSACUvB
            self.ClearDict = obj.FBHYFqXuvCFWejZ
            self.FetchWord = obj.tbffgmSYRgQ
            self.FindStr = obj.AnHcQTuvPbUztE
            self.FindStrE = obj.JTiF
            self.FindStrEx = obj.AEvrE
            self.FindStrExS = obj.lEYctC
            self.FindStrFast = obj.DvRCqMvzPTe
            self.FindStrFastE = obj.dkZbsBman
            self.FindStrFastEx = obj.TCvwZinmcS
            self.FindStrFastExS = obj.iHGRuRbflSDhBbu
            self.FindStrFastS = obj.tsqMdRuW
            self.FindStrS = obj.hUutZ
            self.FindStrWithFont = obj.fQLPSxhFV
            self.FindStrWithFontE = obj.tbyi
            self.FindStrWithFontEx = obj.vKveqzo
            self.GetDict = obj.SVaiWRHLHmIv
            self.GetDictCount = obj.UaDsbbwoSb
            self.GetDictInfo = obj.KAVcL
            self.GetNowDict = obj.StFHoWzu
            self.GetResultCount = obj.crAnPeP
            self.GetResultPos = obj.ZPdVqQEkulT
            self.GetWordResultCount = obj.QuTRJ
            self.GetWordResultPos = obj.zQRxNdP
            self.GetWordResultStr = obj.ClruncBpDM
            self.GetWords = obj.NJxgZpvgvQmfg
            self.GetWordsNoDict = obj.GklQWDFJM
            self.Ocr = obj.keEymEzH
            self.OcrEx = obj.meFECTiSk
            self.OcrExOne = obj.RPeMbjNT
            self.OcrInFile = obj.cvaKQ
            self.SaveDict = obj.rNHfTNckn
            self.SetColGapNoDict = obj.FlnGLERsytYkrc
            self.SetDict = obj.nuxHjoHKgHqo
            self.SetDictMem = obj.FXcTJLp
            self.SetDictPwd = obj.qExUB
            self.SetExactOcr = obj.DotoYUWJRmSJrZr
            self.SetMinColGap = obj.kJCPVXwcEsx
            self.SetMinRowGap = obj.BBoxuqyYUzA
            self.SetRowGapNoDict = obj.HGccyljoXfy
            self.SetWordGap = obj.ckfCzD
            self.SetWordGapNoDict = obj.fcaeW
            self.SetWordLineHeight = obj.WheILcf
            self.SetWordLineHeightNoDict = obj.VayXx
            self.UseDict = obj.CeuVduBgkLV
            self.EnableShareDict = obj.KNPbYpDQLooWryu
            self.Beep = obj.YfirrVCZcUzByx
            self.CheckFontSmooth = obj.sXvWAjveLXGqE
            self.CheckUAC = obj.vJbbkNNIyEQdwp
            self.Delay = obj.DdAQyBWjLt
            self.Delays = obj.BrvDDDhxWPRkH
            self.DisableFontSmooth = obj.fvFJsk
            self.DisablePowerSave = obj.cQiHAuCD
            self.DisableScreenSave = obj.QxZgrIJoP
            self.ExitOs = obj.ZjFFcEqSiH
            self.GetClipboard = obj.KJrDomcTUDYR
            self.GetDir = obj.tUEg
            self.GetDiskSerial = obj.RXGb
            self.GetDisplayInfo = obj.WkQsXUVqTARggTc
            self.GetMachineCode = obj.irMCkETVVoL
            self.GetMachineCodeNoMac = obj.vbGgGl
            self.GetNetTime = obj.nFcezFHZuzFw
            self.GetNetTimeByIp = obj.ZWsLNpnJFcIIV
            self.GetNetTimeSafe = obj.lmTt
            self.GetOsType = obj.ylUzeknuVSY
            self.GetScreenDepth = obj.aFamlRQjZ
            self.GetScreenHeight = obj.sREomrGQisRe
            self.GetScreenWidth = obj.KDjywf
            self.GetTime = obj.EpYrRxHWcj
            self.Is64Bit = obj.vtzDPu
            self.Play = obj.ZYdIoYPUCHDk
            self.RunApp = obj.iQSkun
            self.SetClipboard = obj.SKME
            self.SetDisplayAcceler = obj.lzDmDSZgICI
            self.SetScreen = obj.VNonF
            self.SetUAC = obj.lrib
            self.Stop = obj.hcXf
            self.EnableFontSmooth = obj.oyIbRHnpHVE
            self.DisableCloseDisplayAndSleep = obj.wRnWNKwiX
            self.SetLocale = obj.HSShfMQmDFuVUvU
            self.GetLocale = obj.JwGwNWkVg
            self.Int64ToInt32 = obj.hRxaoipClYjFqkM
            self.GetDPI = obj.eIkdntG
            self.GetCpuType = obj.TzzoedEHPxLqpWZ
            self.GetOsBuildNumber = obj.mRaUUDdC
            self.ShowTaskBarIcon = obj.XxHQVdXz
            self.IsSurrpotVt = obj.VYgCBR
            self.GetDiskModel = obj.BDWb
            self.GetDiskReversion = obj.SqpMH
            self.GetCpuUsage = obj.ZIyHVQs
            self.GetMemoryUsage = obj.tnlUnBbAKVHSW
            self.ActiveInputMethod = obj.pBfpDJy
            self.CheckInputMethod = obj.nBNxVB
            self.EnterCri = obj.SJQMPByPwLPNGpr
            self.FindInputMethod = obj.vNloQFZCdmoqpsr
            self.InitCri = obj.WuWzCrRbhF
            self.LeaveCri = obj.JENCwZX
            self.ShowScrMsg = obj.UfXzRVi
            self.Md5 = obj.QnFBpC
            self.GetMac = obj.zwfrBiETeeHLYCZ
            self.SetExportDict = obj.JxMg
            self.ReadFileData = obj.bShCXtHgYrFCJ
            self.ReleaseRef = obj.sjrjrqrwkx
            self.SetExitThread = obj.Hdupsz
            self.ExecuteCmd = obj.SHjIRxvp
            self.Hex32 = obj.HPypgHhxbNWwyq
            self.Hex64 = obj.bxzGRstwLRoeVmz


class Lw():
    def __init__(self, obj):
        # Com组件对象
        self.obj = obj
        # 线程锁
        self.mutex = QMutex(QMutex.Recursive)

    def set_path(self, path_res: str):
        # 设置资源路径
        self.obj.SetPath(path_res)

    def set_dict(self, idx: int, file_zk: str):
        # 设置字库序号, lw设置字库时可设置解密的pwd
        self.obj.SetDict(idx, file_zk, self.zk_pwd)

    def set_pic_pwd(self, pic_pwd=""):
        self.obj.SetPicPwd(pic_pwd.center(10, "*"))

    def set_dict_pwd(self, zk_pwd=""):
        self.zk_pwd = zk_pwd.center(10, "*")

    def bind_window(self, hwnd: str) -> bool:
        locker = QMutexLocker(self.mutex)
        ret = self.obj.BindWindow(
            hwnd, mode_display, mode_mouse, mode_keypad, mode_public, mode_back)
        if ret:  # 绑定窗口成功后激活窗口才能运行
            activate_wnd(hwnd)
        return ret

    # 获取子窗口句柄, 没找到返回0
    def get_son_hwnd(self, hwnd: int) -> int:
        locker = QMutexLocker(self.mutex)
        son = self.obj.GetSonWindow(hwnd)
        if son == 0:
            return 0
        son_son = self.obj.GetSonWindow(son)
        son_son_son = self.obj.GetSonWindow(son_son)
        return son_son_son

    def unbind_window(self):
        locker = QMutexLocker(self.mutex)
        self.obj.UnBindWindow()

    # 切换绑定检测窗口
    def switch_bind_detect_window(self, hwnd: int):
        locker = QMutexLocker(self.mutex)
        self.obj.UnBindWindow()
        gdi, windows3, windows = 1, 2, 1
        self.obj.BindWindow(hwnd, gdi, windows3, windows, 0, 0)

    # 切换绑定游戏窗口
    def switch_bind_game_window(self, hwnd: int):
        locker = QMutexLocker(self.mutex)
        self.obj.UnBindWindow()
        self.obj.BindWindow(hwnd, mode_display, mode_mouse,
                            mode_keypad, mode_public, mode_back)
        activate_wnd(hwnd)  # 过完验证要激活窗口

    def lock_input(self, state: str):
        locker = QMutexLocker(self.mutex)
        map_dict = {"关闭锁定": 0, "锁定键鼠": 1, "锁定鼠标": 2, "锁定键盘": 3}
        flag = map_dict[state]
        self.obj.LockInput(flag)

    def capture(self, x1, y1, x2, y2, save_path):
        # type: (int, int, int, int, str) -> None
        locker = QMutexLocker(self.mutex)
        self.obj.Capture(x1, y1, x2, y2, save_path)

    # 获取通配符对应的文件集合，每个图片以|分割
    def match_pic(self, pic: str, dir="") -> str:
        locker = QMutexLocker(self.mutex)
        if dir != "":  # 设置指定路径
            self.obj.SetPath(dir)
        ret = self.obj.MatchPicName(pic)
        if dir != "":  # 设置回原路径
            self.obj.SetPath(DIR_RES)
        return ret

    # 枚举窗口, 枚举到返回一个整数列表, 没枚举出返回空列表
    def enum_window(self) -> [int]:
        locker = QMutexLocker(self.mutex)
        hwnds = self.obj.EnumWindow(WND_TITLE, WND_CLASS, PROC_NAME)
        if hwnds is None or hwnds == "":
            return []
        hwnd_list = hwnds.split(",")
        ret_list = [int(hwnd) for hwnd in hwnd_list]

        # lw还需要判断窗口进程创建时间来对窗口排序
        time_hwnd_dict = {}
        for hwnd in ret_list:
            pid = self.obj.GetWindowProcessId(hwnd)
            hProcess = OpenProcess(PROCESS_ALL_ACCESS, False, pid)
            time_dict = GetProcessTimes(hProcess)
            # pywintypes.datetime(2020, 12, 26, 0, 59, 33, 948000, tzinfo=TimeZoneInfo('GMT Standard Time', True))
            create_time = time_dict["CreationTime"]
            time_str = str(create_time)  # "2020-12-26 00:59:33.948000+00:00"
            time_str = time_str[:19]  # "2020-12-26 00:59:33"
            time_hwnd_dict[time_str] = hwnd
        time_list = [time_str for time_str in time_hwnd_dict]
        time_list.sort()
        ret_list = []
        for time_str in time_list:
            hwnd = time_hwnd_dict[time_str]
            ret_list.append(hwnd)
        return ret_list

    # 设置显示输入, 若mode="pic", 则xxx~"C\1.bmp", 若mode="mem", 则xxx~"addr"
    def set_display_input(self, mode: str, xxx=""):
        locker = QMutexLocker(self.mutex)
        if mode not in ("screen", "pic", "mem"):
            return
        if mode in ("pic", "mem"):
            self.obj.SetDisplayInput(xxx)
        else:
            self.obj.SetDisplayInput("0")

    # 插件版本号
    def ver(self):
        locker = QMutexLocker(self.mutex)
        ret = self.obj.ver()
        return ret

    # 启用真实鼠标
    def enable_real_mouse(self, enable: bool, delay=16, step=64):
        locker = QMutexLocker(self.mutex)
        if enable:
            self.obj.EnableRealMouse(1, delay, step)
        else:
            self.obj.EnableRealMouse(0, delay, step)

    # 显示错误信息
    def show_error_msg(self, show: bool):
        locker = QMutexLocker(self.mutex)
        self.obj.SetShowErrorMsg(show)

    # 禁用系统睡眠
    def ban_sys_sleep(self):
        locker = QMutexLocker(self.mutex)
        self.obj.DisablePowerSave()

    # 禁用屏幕保护
    def ban_screen_protect(self):
        locker = QMutexLocker(self.mutex)
        self.obj.DisableScreenSave()

    # 关机
    def exit_os(self):
        locker = QMutexLocker(self.mutex)
        self.obj.ExitOs(1)

    # ------------------------ 鼠标相关 ------------------------
    def move_to(self, x: int, y: int, is_delay=True):
        locker = QMutexLocker(self.mutex)
        self.obj.MoveTo(x, y)
        if is_delay:
            msleep(SLEEP_TIME)

    # 相对移动
    def move_relative(self, rx: int, ry: int):
        locker = QMutexLocker(self.mutex)
        self.obj.MoveR(rx, ry)

    def re_move(self, x=-1, y=-1):
        locker = QMutexLocker(self.mutex)
        if (x, y) == (-1, -1):
            x = 5 + rnd(0, 60)
            y = 45 + rnd(0, 8)
        self.obj.MoveTo(x, y)

    def left_down(self):
        locker = QMutexLocker(self.mutex)
        self.obj.LeftDown()
        msleep(SLEEP_TIME)

    def left_up(self):
        locker = QMutexLocker(self.mutex)
        self.obj.LeftUp()
        msleep(SLEEP_TIME)

    def left_click(self, re_move=True):
        locker = QMutexLocker(self.mutex)
        self.obj.LeftClick()
        msleep(SLEEP_AFTER_CLICK)
        if re_move:
            self.re_move()

    def left_db_click(self, re_move=True):
        locker = QMutexLocker(self.mutex)
        self.obj.LeftDoubleClick()
        msleep(SLEEP_AFTER_CLICK)
        if re_move:
            self.re_move()

    def right_click(self, re_move=True):
        locker = QMutexLocker(self.mutex)
        self.obj.RightClick()
        msleep(SLEEP_AFTER_CLICK)
        if re_move:
            self.re_move()

    def move_click(self, x, y, re_move=True):
        # type: (int, int, bool) -> None
        locker = QMutexLocker(self.mutex)
        self.move_to(x, y)
        self.left_click(re_move)

    def move_r_click(self, x, y, is_delay=True, re_move=True):
        # type: (int, int, bool, bool) -> None
        locker = QMutexLocker(self.mutex)
        self.move_to(x, y, is_delay)
        self.right_click(re_move)

    def move_db_click(self, x, y, re_move=True):
        # type: (int, int, bool) -> None
        locker = QMutexLocker(self.mutex)
        self.move_to(x, y)
        self.left_db_click(re_move)

    def move_wheel_down(self, x, y, count=1, re_move=True):
        # type: (int, int, int, bool) -> None
        locker = QMutexLocker(self.mutex)
        self.move_to(x, y)
        for i in range(count):
            self.obj.WheelDown()
            msleep(10)
        if re_move:
            self.re_move()

    def move_wheel_up(self, x, y, count=1, re_move=True):
        # type: (int, int, int, bool) -> None
        locker = QMutexLocker(self.mutex)
        self.move_to(x, y)
        for i in range(count):
            self.obj.WheelUp()
            msleep(10)
        if re_move:
            self.re_move()

    def move_drag_to(self, x0, y0, x, y, re_move=True):
        # type: (int, int, int, int, bool) -> None
        locker = QMutexLocker(self.mutex)
        self.move_to(x0, y0)
        msleep(SLEEP_TIME)
        self.left_down()
        self.move_to(x, y)
        msleep(SLEEP_TIME)
        self.left_up()
        if re_move:
            self.re_move()

    # ------------------------ 键盘相关 ------------------------
    def key_press(self, vk_code, num=1, delay=10):
        # type: (int, int) -> None
        locker = QMutexLocker(self.mutex)
        for i in range(num):
            self.obj.KeyPress(vk_code)
            msleep(delay)

    # 发送ASCII字符串
    def key_press_str(self, asc_str):
        locker = QMutexLocker(self.mutex)
        self.obj.KeyPressStr(asc_str, 25)

    # 按组合键
    def key_press_combo(self, vk_state: int, vk_code: int):
        locker = QMutexLocker(self.mutex)
        self.obj.KeyDown(vk_state)
        msleep(10, 30)
        self.obj.KeyPress(vk_code)
        msleep(10, 30)
        self.obj.KeyUp(vk_state)

    # 按下键
    def key_down(self, vk_code: int):
        locker = QMutexLocker(self.mutex)
        self.obj.KeyDown(vk_code)

    # 抬起键
    def key_up(self, vk_code: int):
        locker = QMutexLocker(self.mutex)
        self.obj.KeyUp(vk_code)

    # 发送任意字符串
    def send_string(self, string):
        locker = QMutexLocker(self.mutex)
        self.obj.SendString(string, 1)  # lw默认向绑定的窗口发送, 用模式2

    # ------------------------ 找图相关 ------------------------
    # 找图, 找到返回True, 未找到返回False
    def find_pic(self, x1, y1, x2, y2, pic, delta_color="101010", sim=0.95, order=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> bool
        locker = QMutexLocker(self.mutex)
        while True:
            ret = self.obj.FindPic(x1, y1, x2, y2, pic,
                                   delta_color, sim, order)
            if ret or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        return ret

    # 找图扩展, 同时找多个图, 得到形如[(0,100,20), (1,30,40)]的列表
    def find_pic_ex(self, x1, y1, x2, y2, pic, delta_color="101010", sim=0.95, order=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> []
        locker = QMutexLocker(self.mutex)
        while True:
            ret_str = self.obj.FindPicEx(
                x1, y1, x2, y2, pic, delta_color, sim, order)
            if ret_str or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        # "1,100,20|2,30,40" -> [(0,100,20), (1,30,40)]
        ret_list = []
        if ret_str:
            pos_list = ret_str.split("|")  # ["1,100,20", "2,30,40"]
            for pos in pos_list:  # "1,100,20"
                kk = pos.split(",")  # ["1", "100", "20"]
                idx, x, y = int(kk[0]) - 1, int(kk[1]), int(kk[2])
                ret_list.append((idx, x, y))
        return ret_list

    # 找图左键点击, 找到返回True, 未找到返回False
    def find_pic_click(self, x1, y1, x2, y2, pic, delta_color="101010", sim=0.95, order=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> bool
        locker = QMutexLocker(self.mutex)
        while True:
            ret = self.obj.FindPic(x1, y1, x2, y2, pic,
                                   delta_color, sim, order)
            if ret or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        if ret:
            self.move_click(self.obj.x() + rnd(2, 4), self.obj.y() + rnd(2, 4))
        return ret

    # 找图右键点击, 找到返回True, 未找到返回False
    def find_pic_r_click(self, x1, y1, x2, y2, pic, delta_color="101010", sim=0.95, order=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> bool
        locker = QMutexLocker(self.mutex)
        while True:
            ret = self.obj.FindPic(x1, y1, x2, y2, pic,
                                   delta_color, sim, order)
            if ret or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        if ret:
            self.move_r_click(self.obj.x() + rnd(2, 4),
                              self.obj.y() + rnd(2, 4))
        return ret

    # 找图左键双击, 找到返回True, 未找到返回False
    def find_pic_db_click(self, x1, y1, x2, y2, pic, delta_color="101010", sim=0.95, order=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> bool
        locker = QMutexLocker(self.mutex)
        while True:
            ret = self.obj.FindPic(x1, y1, x2, y2, pic,
                                   delta_color, sim, order)
            if ret or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        if ret:
            self.move_db_click(self.obj.x() + rnd(2, 4),
                               self.obj.y() + rnd(2, 4))
        return ret

    # 找图shift+鼠标右击, 找到返回True, 未找到返回False
    def find_pic_shift_r_click(self, x1, y1, x2, y2, pic, delta_color="101010", sim=0.95, order=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> bool
        locker = QMutexLocker(self.mutex)
        while True:
            ret = self.obj.FindPic(x1, y1, x2, y2, pic,
                                   delta_color, sim, order)
            if ret or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        if ret:
            VK_SHIFT = 16
            self.key_down(VK_SHIFT)
            self.move_r_click(self.obj.x() + rnd(2, 4),
                              self.obj.y() + rnd(2, 4))
            self.key_up(VK_SHIFT)
        return ret

    # 返回图片所在窗口的坐标, 没找到返回-1,-1
    def get_pic_pos(self, x1, y1, x2, y2, pic, delta_color="101010", sim=0.95, order=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> (int, int)
        locker = QMutexLocker(self.mutex)
        while True:
            ret = self.obj.FindPic(x1, y1, x2, y2, pic,
                                   delta_color, sim, order)
            if ret or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        ret_x, ret_y = -1, -1
        if ret:
            ret_x, ret_y = self.obj.x(), self.obj.y()
        return ret_x, ret_y

    # 返回找到的图片的序号,从0开始索引.如果没找到返回-1
    def get_pic_idx(self, x1, y1, x2, y2, pic, delta_color="101010", sim=0.95, order=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> int
        locker = QMutexLocker(self.mutex)
        while True:
            ret = self.obj.FindPic(x1, y1, x2, y2, pic,
                                   delta_color, sim, order)
            if ret or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        if not ret:  # self.obj.idx()可能不会自动置为-1
            return -1
        return self.obj.idx() - 1  # lw插件内的所有序号都是从1开始数的

    # 返回找到的图片的数量
    def get_pic_num(self, x1, y1, x2, y2, pic, delta_color="101010", sim=0.95, order=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> int
        tuple_list = self.find_pic_ex(
            x1, y1, x2, y2, pic, delta_color, sim, order, timeout)
        ret = len(tuple_list)
        return ret

    # 返回找到的图片名"物_驱魔香", 未找到返回""(注意:没有图片后缀名)
    def get_pic_name(self, x1, y1, x2, y2, pic, delta_color="101010", sim=0.95, order=0, timeout=0, dir=""):
        # type: (int, int, int, int, str, str, float, int, int) -> str
        locker = QMutexLocker(self.mutex)
        if dir != "":  # 设置指定路径
            self.obj.SetPath(dir)
        while True:
            ret = self.obj.FindPic(x1, y1, x2, y2, pic,
                                   delta_color, sim, order)
            if ret or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        ret_str = ""
        if ret:
            ret_str = self.obj.GetFindedPicName()
            ret_str = ret_str.rstrip(".bmp")
        if dir != "":  # 设置回原路径
            self.obj.SetPath(DIR_RES)
        return ret_str

    # 找出距离某点最近的图片位置
    def find_pic_nearest_pos(self, x1, y1, x2, y2, pic, cx, cy, delta_color="101010", sim=0.95, order=0,
                             timeout=0):
        # type: (int, int, int, int, str, int, int, str, float, int, int) -> (int, int)
        locker = QMutexLocker(self.mutex)
        while True:
            all_pos = self.obj.FindPicEx(
                x1, y1, x2, y2, pic, delta_color, sim, order)
            if all_pos or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        ret_x, ret_y = -1, -1
        if all_pos:
            id_x_y = self.obj.FindNearestPos(all_pos, 0, cx, cy)  # "0,100,200"
            _, ret_x, ret_y = id_x_y.split(",")
            ret_x, ret_y = int(ret_x), int(ret_y)
        return ret_x, ret_y

    # ------------------------ 找色相关 ------------------------
    # 找色, 找到返回True, 未找到返回False
    def find_color(self, x1, y1, x2, y2, color, sim=1.0, order=0, timeout=0):
        # type: (int, int, int, int, str, float, int, int) -> bool
        locker = QMutexLocker(self.mutex)
        while True:
            ret = self.obj.FindColor(x1, y1, x2, y2, color, sim, order)
            if ret or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        return ret

    # 找色左键点击, 找到返回True, 未找到返回False
    def find_color_click(self, x1, y1, x2, y2, color, sim=1.0, order=0, timeout=0):
        # type: (int, int, int, int, str, float, int, int) -> bool
        locker = QMutexLocker(self.mutex)
        while True:
            ret = self.obj.FindColor(x1, y1, x2, y2, color, sim, order)
            if ret or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        if ret:
            self.move_click(self.obj.x() + rnd(2, 4), self.obj.y() + rnd(2, 4))
        return ret

    # 返回颜色所在窗口坐标, 没找到返回-1,-1
    def get_color_pos(self, x1, y1, x2, y2, color, sim=1.0, order=0, timeout=0):
        # type: (int, int, int, int, str, float, int, int) -> (int, int)
        locker = QMutexLocker(self.mutex)
        while True:
            ret = self.obj.FindColor(x1, y1, x2, y2, color, sim, order)
            if ret or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        ret_x, ret_y = -1, -1
        if ret:
            ret_x, ret_y = self.obj.x(), self.obj.y()
        return ret_x, ret_y

    # 返回指定坐标的颜色, "RRGGBB"全小写
    def get_pos_color(self, x: int, y: int):
        locker = QMutexLocker(self.mutex)
        ret = self.obj.GetColor(x, y)
        return ret

    # ------------------------ 文字相关 ------------------------
    # 找字, 找到返回True, 未找到返回False
    def find_str(self, x1, y1, x2, y2, string, color, sim=0.95, zk=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> bool
        locker = QMutexLocker(self.mutex)
        self.obj.UseDict(zk)
        while True:
            ret = self.obj.FindStrFast(x1, y1, x2, y2, string, color, sim)
            if ret or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        return ret

    # 找字扩展, 找到形如[(0,100,20), (1,30,40)]的列表, 一个都没找到返回[]
    def find_str_ex(self, x1, y1, x2, y2, string, color, sim=0.95, zk=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> []
        locker = QMutexLocker(self.mutex)
        self.obj.UseDict(zk)
        while True:
            ret_str = self.obj.FindStrFastEx(
                x1, y1, x2, y2, string, color, sim)
            if ret_str or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        # "1,100,20|2,30,40" -> [(0,100,20), (1,30,40)]
        ret_list = []
        if ret_str:
            pos_list = ret_str.split("|")  # ["1,100,20", "2,30,40"]
            for pos in pos_list:
                kk = pos.split(",")  # ["1", "100", "20"]
                idx, x, y = int(kk[0]) - 1, int(kk[1]), int(kk[2])
                ret_list.append((idx, x, y))
        return ret_list

    # 找字左键点击, 找到返回True, 未找到返回False
    def find_str_click(self, x1, y1, x2, y2, string, color, sim=0.95, zk=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> bool
        locker = QMutexLocker(self.mutex)
        self.obj.UseDict(zk)
        while True:
            ret = self.obj.FindStrFast(x1, y1, x2, y2, string, color, sim)
            if ret or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        if ret:
            self.move_click(self.obj.x() + rnd(2, 4), self.obj.y() + rnd(2, 4))
        return ret

    # 返回字所在窗口坐标, 没找到返回-1,-1
    def get_str_pos(self, x1, y1, x2, y2, string, color, sim=0.95, zk=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> (int, int)
        locker = QMutexLocker(self.mutex)
        self.obj.UseDict(zk)
        while True:
            ret = self.obj.FindStrFast(x1, y1, x2, y2, string, color, sim)
            if ret or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        ret_x, ret_y = -1, -1
        if ret:
            ret_x, ret_y = self.obj.x(), self.obj.y()
        return ret_x, ret_y

    # 找出距离某点最近的字位置
    def find_str_nearest_pos(self, x1, y1, x2, y2, string, color, cx, cy, sim=0.95, zk=0, timeout=0):
        # type: (int, int, int, int, str, str, int, int, float, int, int) -> (int, int)
        locker = QMutexLocker(self.mutex)
        self.obj.UseDict(zk)
        while True:
            all_pos = self.obj.FindStrFastEx(
                x1, y1, x2, y2, string, color, sim)
            if all_pos or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        ret_x, ret_y = -1, -1
        if all_pos:
            id_x_y = self.obj.FindNearestPos(all_pos, 0, cx, cy)  # "0,100,200"
            _, ret_x, ret_y = id_x_y.split(",")
            ret_x, ret_y = int(ret_x), int(ret_y)
        return ret_x, ret_y

    # 识别文字, 未识别出返回""
    def ocr(self, x1, y1, x2, y2, color, sim=1.0, zk=0, timeout=0):
        # type: (int, int, int, int, str, float, int, int) -> str
        locker = QMutexLocker(self.mutex)
        self.obj.UseDict(zk)
        while True:
            ret_str = self.obj.Ocr(x1, y1, x2, y2, color, sim)  # 未识别出返回None
            if ret_str or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        if ret_str is None:
            ret_str = ""
        return ret_str


class Dm():
    def __init__(self, obj: BaseObj):
        # com组件对象
        self.obj = obj
        # 线程锁
        self.mutex = QMutex(QMutex.Recursive)

    def reg(self, reg_code: str, add_code: str) -> bool:
        ret = self.obj.Reg(reg_code, add_code+"q")
        return ret

    # 版本号
    def ver(self):
        locker = QMutexLocker(self.mutex)
        ret = self.obj.Ver()
        return ret

    def set_path(self, path_res: str):
        # 设置资源路径
        self.obj.SetPath(path_res)

    def set_dict(self, idx: int, file_zk: str, zk_pwd=""):
        # 设置字库序号
        self.obj.SetDict(idx, file_zk)

    def set_pic_pwd(self, pic_pwd=""):
        pic_pwd = pic_pwd.center(10, "*")
        self.obj.SetPicPwd(pic_pwd)

    def set_dict_pwd(self, zk_pwd=""):
        zk_pwd = zk_pwd.center(10, "*")
        self.obj.SetDictPwd(zk_pwd)

    # 绑定成功, 返回1, 未绑定成功, 返回错误码
    def bind_window(self, hwnd: int) -> int:
        locker = QMutexLocker(self.mutex)
        ret = self.obj.BindWindowEx(
            hwnd, mode_display, mode_mouse, mode_keypad, mode_public, mode_back)
        if ret == 1:  # 绑定窗口成功后激活窗口才能运行
            activate_wnd(hwnd)
        else:
            ret = self.obj.GetLastError()
        return ret

    # 获取子窗口句柄, 没找到返回0
    def get_son_hwnd(self, hwnd: int) -> int:
        locker = QMutexLocker(self.mutex)
        son = self.obj.GetWindow(hwnd, 1)
        if son == 0:
            return 0
        son_son = self.obj.GetWindow(son, 1)
        son_son_son = self.obj.GetWindow(son_son, 1)
        return son_son_son

    def unbind_window(self):
        locker = QMutexLocker(self.mutex)
        self.obj.UnBindWindow()

    # 切换绑定检测窗口
    def switch_bind_detect_window(self, hwnd: int):
        locker = QMutexLocker(self.mutex)
        self.obj.UnBindWindow()
        self.obj.BindWindow(hwnd, "gdi", "windows", "windows", 0)

    # 切换绑定游戏窗口
    def switch_bind_game_window(self, hwnd: int):
        locker = QMutexLocker(self.mutex)
        self.obj.UnBindWindow()
        self.obj.BindWindowEx(hwnd, mode_display, mode_mouse,
                              mode_keypad, mode_public, mode_back)
        activate_wnd(hwnd)  # 过完验证要激活窗口

    def lock_input(self, state: str):
        locker = QMutexLocker(self.mutex)
        map_dict = {"关闭锁定": 0, "锁定键鼠": 1, "锁定鼠标": 2, "锁定键盘": 3}
        flag = map_dict[state]
        self.obj.LockInput(flag)

    # 截图bmp
    def capture(self, x1, y1, x2, y2, save_path):
        # type: (int, int, int, int, str) -> None
        locker = QMutexLocker(self.mutex)
        self.obj.Capture(x1, y1, x2, y2, save_path)

    # 获取通配符对应的文件集合，每个图片以|分割
    def match_pic(self, pic: str, dir="") -> str:
        locker = QMutexLocker(self.mutex)
        if dir != "":  # 设置指定路径
            self.obj.SetPath(dir)
        ret = self.obj.MatchPicName(pic)
        if dir != "":  # 设置回原路径
            self.obj.SetPath(DIR_RES)
        return ret

    # 枚举窗口, 枚举到返回一个整数列表, 没枚举出返回空列表
    def enum_window(self) -> [int, ...]:
        locker = QMutexLocker(self.mutex)
        hwnds = self.obj.EnumWindowByProcess(
            PROC_NAME, WND_TITLE, WND_CLASS, 1 + 2 + 8 + 32)
        if hwnds is None or hwnds == "":
            return []
        hwnd_list = hwnds.split(",")
        hwnd_list = [int(hwnd) for hwnd in hwnd_list]
        return hwnd_list

    # 设置显示输入, 若mode="pic", 则xxx~"C\1.bmp", 若mode="mem", 则xxx~"addr,size"
    def set_display_input(self, mode: str, xxx=""):
        locker = QMutexLocker(self.mutex)
        if mode not in ("screen", "pic", "mem"):
            return
        if mode == "pic":
            self.obj.SetDisplayInput(f"pic:{xxx}")
        elif mode == "mem":
            self.obj.SetDisplayInput(f"mem:{xxx}")
        else:
            self.obj.SetDisplayInput("screen")

    # 启用真实鼠标
    def enable_real_mouse(self, enable: bool, delay=16, step=64):
        locker = QMutexLocker(self.mutex)
        if enable:
            self.obj.EnableRealMouse(2, delay, step)
        else:
            self.obj.EnableRealMouse(0, delay, step)

    # 显示错误信息
    def show_error_msg(self, show: bool):
        locker = QMutexLocker(self.mutex)
        self.obj.SetShowErrorMsg(show)

    # 禁用系统睡眠
    def ban_sys_sleep(self):
        locker = QMutexLocker(self.mutex)
        self.obj.DisablePowerSave()

    # 禁用屏幕保护
    def ban_screen_protect(self):
        locker = QMutexLocker(self.mutex)
        self.obj.DisableScreenSave()

    # 关机
    def exit_os(self):
        locker = QMutexLocker(self.mutex)
        self.obj.ExitOs(1)

    #  ------------------------- 鼠标相关 -------------------------
    def move_to(self, x: int, y: int, is_delay=True):
        locker = QMutexLocker(self.mutex)
        self.obj.MoveTo(x, y)
        if is_delay:
            msleep(SLEEP_TIME)

    # 相对移动
    def move_relative(self, rx: int, ry: int):
        locker = QMutexLocker(self.mutex)
        self.obj.MoveR(rx, ry)

    def re_move(self, x=-1, y=-1):
        locker = QMutexLocker(self.mutex)
        if (x, y) == (-1, -1):
            x = 5 + rnd(0, 60)
            y = 45 + rnd(0, 8)
        self.obj.MoveTo(x, y)

    def left_down(self):
        locker = QMutexLocker(self.mutex)
        self.obj.LeftDown()
        msleep(SLEEP_TIME)

    def left_up(self):
        locker = QMutexLocker(self.mutex)
        self.obj.LeftUp()
        msleep(SLEEP_TIME)

    def left_click(self, re_move=True):
        locker = QMutexLocker(self.mutex)
        self.obj.LeftClick()
        msleep(SLEEP_AFTER_CLICK)
        if re_move:
            self.re_move()

    def left_db_click(self, re_move=True):
        locker = QMutexLocker(self.mutex)
        self.obj.LeftClick()
        msleep(SLEEP_TIME)
        self.obj.LeftClick()
        if re_move:
            self.re_move()

    def right_click(self, re_move=True):
        locker = QMutexLocker(self.mutex)
        self.obj.RightClick()
        msleep(SLEEP_AFTER_CLICK)
        if re_move:
            self.re_move()

    def move_click(self, x, y, re_move=True):
        # type: (int, int, bool) -> None
        locker = QMutexLocker(self.mutex)
        self.move_to(x, y)
        self.left_click(re_move)

    def move_r_click(self, x, y, is_delay=True, re_move=True):
        # type: (int, int, bool, bool) -> None
        locker = QMutexLocker(self.mutex)
        self.move_to(x, y, is_delay)
        self.right_click(re_move)

    def move_db_click(self, x, y, re_move=True):
        # type: (int, int, bool) -> None
        locker = QMutexLocker(self.mutex)
        self.move_to(x, y)
        self.left_db_click(re_move)

    def move_wheel_down(self, x, y, count=1, re_move=True):
        # type: (int, int, int, bool) -> None
        locker = QMutexLocker(self.mutex)
        self.move_to(x, y)
        for i in range(count):
            self.obj.WheelDown()
            msleep(10)
        if re_move:
            self.re_move()

    def move_wheel_up(self, x, y, count=1, re_move=True):
        # type: (int, int, int, bool) -> None
        locker = QMutexLocker(self.mutex)
        self.move_to(x, y)
        for i in range(count):
            self.obj.WheelUp()
            msleep(10)
        if re_move:
            self.re_move()

    def move_drag_to(self, x0, y0, x, y, re_move=True):
        # type: (int, int, int, int, bool) -> None
        locker = QMutexLocker(self.mutex)
        self.move_to(x0, y0)
        msleep(SLEEP_TIME)
        self.left_down()
        self.move_to(x, y)
        msleep(SLEEP_TIME)
        self.left_up()
        if re_move:
            self.re_move()

    # ------------------------- 键盘相关 -------------------------
    def key_press(self, vk_code: int, num=1, delay=10):
        locker = QMutexLocker(self.mutex)
        for i in range(num):
            self.obj.KeyPress(vk_code)
            msleep(delay)

    # 发送ASCII字符串
    def key_press_str(self, asc_str):
        locker = QMutexLocker(self.mutex)
        self.obj.KeyPressStr(asc_str, 25)

    # 按组合键
    def key_press_combo(self, vk_state: int, vk_code: int):
        locker = QMutexLocker(self.mutex)
        self.obj.KeyDown(vk_state)
        msleep(10, 30)
        self.obj.KeyPress(vk_code)
        msleep(10, 30)
        self.obj.KeyUp(vk_state)

    # 按下键
    def key_down(self, vk_code: int):
        locker = QMutexLocker(self.mutex)
        self.obj.KeyDown(vk_code)

    # 抬起键
    def key_up(self, vk_code: int):
        locker = QMutexLocker(self.mutex)
        self.obj.KeyUp(vk_code)

    # 发送任意字符串
    def send_string(self, string):
        locker = QMutexLocker(self.mutex)
        hwnd = self.obj.GetBindWindow()
        self.obj.SendString(hwnd, string)

    # ------------------------- 找图相关 -------------------------
    # 找图, 找到返回True, 未找到返回False
    def find_pic(self, x1, y1, x2, y2, pic, delta_color="101010", sim=0.95, order=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> bool
        locker = QMutexLocker(self.mutex)
        while True:
            # ret = (0, 43, 31)  或 (-1, -1, -1)
            ret = self.obj.FindPic(x1, y1, x2, y2, pic,
                                   delta_color, sim, order)
            if ret[0] >= 0 or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        ret = True if ret[0] >= 0 else False
        return ret

    # 找图扩展, 同时找多个图, 得到形如[(0,100,20), (1,30,40)]的列表, 一个都未找到返回[]
    def find_pic_ex(self, x1, y1, x2, y2, pic, delta_color="101010", sim=0.95, order=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> []
        locker = QMutexLocker(self.mutex)
        while True:
            ret_str = self.obj.FindPicEx(
                x1, y1, x2, y2, pic, delta_color, sim, order)
            if ret_str or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        # "0,100,20|1,30,40" -> [(0,100,20), (1,30,40)]
        ret_list = []
        if ret_str:
            pos_list = ret_str.split("|")  # ["1,100,20", "2,30,40"]
            for pos in pos_list:  # "1,100,20"
                kk = pos.split(",")  # ["1", "100", "20"]
                idx, x, y = int(kk[0]), int(kk[1]), int(kk[2])
                ret_list.append((idx, x, y))
        return ret_list

    # 找图左键点击, 找到返回True, 未找到返回False
    def find_pic_click(self, x1, y1, x2, y2, pic, delta_color="101010", sim=0.95, order=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> bool
        locker = QMutexLocker(self.mutex)
        while True:
            # ret = (0, 43, 31) 或 (-1, -1, -1)
            ret = self.obj.FindPic(x1, y1, x2, y2, pic,
                                   delta_color, sim, order)
            if ret[0] >= 0 or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        if ret[0] >= 0:
            self.move_click(ret[1] + rnd(2, 4), ret[2] + rnd(2, 4))
        ret = True if ret[0] >= 0 else False
        return ret

    # 找图右键点击, 找到返回True, 未找到返回False
    def find_pic_r_click(self, x1, y1, x2, y2, pic, delta_color="101010", sim=0.95, order=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> bool
        locker = QMutexLocker(self.mutex)
        while True:
            # ret = (0, 43, 31) 或 (-1, -1, -1)
            ret = self.obj.FindPic(x1, y1, x2, y2, pic,
                                   delta_color, sim, order)
            if ret[0] >= 0 or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        if ret[0] >= 0:
            self.move_r_click(ret[1] + rnd(2, 4), ret[2] + rnd(2, 4))
        ret = True if ret[0] >= 0 else False
        return ret

    # 找图shift+鼠标右击, 找到返回True, 未找到返回False
    def find_pic_shift_r_click(self, x1, y1, x2, y2, pic, delta_color="101010", sim=0.95, order=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> bool
        locker = QMutexLocker(self.mutex)
        while True:
            # ret = (0, 43, 31) 或 (-1, -1, -1)
            ret = self.obj.FindPic(x1, y1, x2, y2, pic,
                                   delta_color, sim, order)
            if ret[0] >= 0 or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        if ret[0] >= 0:
            VK_SHIFT = 16
            self.key_down(VK_SHIFT)
            self.move_r_click(ret[1] + rnd(2, 4), ret[2] + rnd(2, 4))
            self.key_up(VK_SHIFT)
        ret = True if ret[0] >= 0 else False
        return ret

    # 找图左键双击, 找到返回True, 未找到返回False
    def find_pic_db_click(self, x1, y1, x2, y2, pic, delta_color="101010", sim=0.95, order=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> bool
        locker = QMutexLocker(self.mutex)
        while True:
            # ret = (0, 43, 31) 或 (-1, -1, -1)
            ret = self.obj.FindPic(x1, y1, x2, y2, pic,
                                   delta_color, sim, order)
            if ret[0] >= 0 or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        if ret[0] >= 0:
            self.move_db_click(ret[1] + rnd(2, 4), ret[2] + rnd(2, 4))
        ret = True if ret[0] >= 0 else False
        return ret

    # 返回图片所在窗口在坐标, 找到返回相应坐标, 没找到返回-1, -1
    def get_pic_pos(self, x1, y1, x2, y2, pic, delta_color="101010", sim=0.95, order=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> (int, int)
        locker = QMutexLocker(self.mutex)
        while True:
            # ret = (0, 43, 31) 或 (-1, -1, -1)
            ret = self.obj.FindPic(x1, y1, x2, y2, pic,
                                   delta_color, sim, order)
            if ret[0] >= 0 or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        return ret[1], ret[2]

    # 返回找到的图片的索引, 从0开始, 如果没找到返回-1
    def get_pic_idx(self, x1, y1, x2, y2, pic, delta_color="101010", sim=0.95, order=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> int
        locker = QMutexLocker(self.mutex)
        while True:
            # ret = (0, 43, 31) 或 (-1, -1, -1)
            ret = self.obj.FindPic(x1, y1, x2, y2, pic,
                                   delta_color, sim, order)
            if ret[0] >= 0 or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        return ret[0]

    # 返回找到的图片名"物_驱魔香", 未找到返回""(注意:没有图片后缀名)
    def get_pic_name(self, x1, y1, x2, y2, pic, delta_color="101010", sim=0.95, order=0, timeout=0, dir=""):
        # type: (int, int, int, int, str, str, float, int, int) -> str
        locker = QMutexLocker(self.mutex)
        if dir != "":  # 设置指定路径
            self.obj.SetPath(dir)
        ret_str = ""
        while True:
            # ret = ("物_驱魔香.bmp", 364, 302) 或 ("", -1, -1)
            ret = self.obj.FindPicS(
                x1, y1, x2, y2, pic, delta_color, sim, order)
            if ret[0] != "" or timeout <= 0:
                ret_str = ret[0].rstrip(".bmp")
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        if dir != "":  # 设置回原路径
            self.obj.SetPath(DIR_RES)
        return ret_str

    # 返回找到的图片的数量
    def get_pic_num(self, x1, y1, x2, y2, pic, delta_color="101010", sim=0.95, order=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> (int, int)
        tuple_list = self.find_pic_ex(
            x1, y1, x2, y2, pic, delta_color, sim, order, timeout)
        ret = len(tuple_list)
        return ret

    # 找出距离某点最近的图片位置
    def find_pic_nearest_pos(self, x1, y1, x2, y2, pic, cx, cy, delta_color="101010", sim=0.95, order=0,
                             timeout=0):
        # type: (int, int, int, int, str, int, int, str, float, int, int) -> (int, int)
        locker = QMutexLocker(self.mutex)
        while True:
            all_pos = self.obj.FindPicEx(
                x1, y1, x2, y2, pic, delta_color, sim, order)
            if all_pos or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        ret_x, ret_y = -1, -1
        if all_pos:
            id_x_y = self.obj.FindNearestPos(all_pos, 0, cx, cy)  # "0,100,200"
            _, ret_x, ret_y = id_x_y.split(",")
            ret_x, ret_y = int(ret_x), int(ret_y)
        return ret_x, ret_y

    # -------------------------找色相关 -------------------------
    # 找色, 找到返回True, 未找到返回False
    def find_color(self, x1, y1, x2, y2, color, sim=1.0, order=0, timeout=0):
        # type: (int, int, int, int, str, float, int, int) -> bool
        locker = QMutexLocker(self.mutex)
        while True:
            # ret = (1, 33, 227) 或 (0, -1, -1)
            ret = self.obj.FindColor(x1, y1, x2, y2, color, sim, order)
            if ret[0] or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        return ret[0]

    # 找色左键点击, 找到返回True, 未找到返回False
    def find_color_click(self, x1, y1, x2, y2, color, sim=1.0, order=0, timeout=0):
        # type: (int, int, int, int, str, float, int, int) -> bool
        locker = QMutexLocker(self.mutex)
        while True:
            # ret = (1, 33, 227) 或 (0, -1, -1)
            ret = self.obj.FindColor(x1, y1, x2, y2, color, sim, order)
            if ret[0] or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        if ret[0]:
            self.move_click(ret[1] + rnd(2, 4), ret[2] + rnd(2, 4))
        return ret[0]

    # 返回颜色所在窗口坐标, 没找到返回-1,-1
    def get_color_pos(self, x1, y1, x2, y2, color, sim=1.0, order=0, timeout=0):
        # type: (int, int, int, int, str, float, int, int) -> (int, int)
        locker = QMutexLocker(self.mutex)
        while True:
            # ret = (1, 33, 227) 或 (0, -1, -1)
            ret = self.obj.FindColor(x1, y1, x2, y2, color, sim, order)
            if ret[0] or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        return ret[1], ret[2]

    # 返回指定坐标的颜色, "RRGGBB"全小写
    def get_pos_color(self, x: int, y: int):
        locker = QMutexLocker(self.mutex)
        ret = self.obj.GetColor(x, y)
        return ret

    # ------------------------文字相关 ------------------------
    # 找到字返回True, 没找到返回False
    def find_str(self, x1, y1, x2, y2, string, color, sim=0.95, zk=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> bool
        locker = QMutexLocker(self.mutex)
        self.obj.UseDict(zk)
        while True:
            # ret = (0, 26, 263) 或 (-1, -1, -1)
            ret = self.obj.FindStrFast(x1, y1, x2, y2, string, color, sim)
            if ret[0] >= 0 or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        ret = True if ret[0] >= 0 else False
        return ret

    # 找字扩展, 找到形如[(0,100,20), (1,30,40)]的列表, 一个都没找到返回[]
    def find_str_ex(self, x1, y1, x2, y2, string, color, sim=0.95, zk=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> []
        locker = QMutexLocker(self.mutex)
        self.obj.UseDict(zk)
        while True:
            ret_str = self.obj.FindStrFastEx(
                x1, y1, x2, y2, string, color, sim)
            if ret_str or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        # "1,100,20|2,30,40" -> [(0,100,20), (1,30,40)]
        ret_list = []
        if ret_str:
            pos_list = ret_str.split("|")  # ["1,100,20", "2,30,40"]
            for pos in pos_list:
                kk = pos.split(",")  # ["1", "100", "20"]
                idx, x, y = int(kk[0]), int(kk[1]), int(kk[2])
                ret_list.append((idx, x, y))
        return ret_list

    # 找字左键点击, 找到返回True, 未找到返回False
    def find_str_click(self, x1, y1, x2, y2, string, color, sim=0.95, zk=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> bool
        self.obj.UseDict(zk)
        while True:
            # ret = (0, 26, 263) 或 (-1, -1, -1)
            ret = self.obj.FindStrFast(x1, y1, x2, y2, string, color, sim)
            if ret[0] >= 0 or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        if ret[0] >= 0:
            self.move_click(ret[1] + rnd(2, 4), ret[2] + rnd(2, 4))
        ret = True if ret[0] >= 0 else False
        return ret

    # 返回字所在窗口坐标, 没找到返回-1,-1
    def get_str_pos(self, x1, y1, x2, y2, string, color, sim=0.95, zk=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> (int, int)
        locker = QMutexLocker(self.mutex)
        self.obj.UseDict(zk)
        while True:
            # ret = (0, 26, 263) 或 (-1, -1, -1)
            ret = self.obj.FindStrFast(x1, y1, x2, y2, string, color, sim)
            if ret[0] >= 0 or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        return ret[1], ret[2]

    # 找出距离某点最近的字位置
    def find_str_nearest_pos(self, x1, y1, x2, y2, string, color, cx, cy, sim=0.95, zk=0, timeout=0):
        # type: (int, int, int, int, str, str, int, int, float, int, int) -> (int, int)
        locker = QMutexLocker(self.mutex)
        self.obj.UseDict(zk)
        while True:
            all_pos = self.obj.FindStrFastEx(
                x1, y1, x2, y2, string, color, sim)
            if all_pos or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        ret_x, ret_y = -1, -1
        if all_pos:
            id_x_y = self.obj.FindNearestPos(all_pos, 0, cx, cy)  # "0,100,200"
            _, ret_x, ret_y = id_x_y.split(",")
            ret_x, ret_y = int(ret_x), int(ret_y)
        return ret_x, ret_y

    # 识别文字,未识别出返回""
    def ocr(self, x1, y1, x2, y2, color, sim=1.0, zk=0, timeout=0):
        # type: (int, int, int, int, str, float, int, int) -> str
        locker = QMutexLocker(self.mutex)
        self.obj.UseDict(zk)
        while True:
            # ret = "制" 或 ""
            ret = self.obj.Ocr(x1, y1, x2, y2, color, sim)
            if ret or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        return ret

# ---------------------- 日志操作 ----------------------


class Log():
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        # 创建handler对象
        self.handler_info = TimedRotatingFileHandler(filename=PATH_CLIENT_LOG, when="midnight", interval=1,
                                                     backupCount=3)
        self.handler_info.setFormatter(
            logging.Formatter("%(asctime)s  %(message)s"))
        self.handler_info.setLevel(logging.INFO)
        # 添加handler
        self.logger.addHandler(self.handler_info)

    def info(self, msg: str):
        self.logger.info(msg)

    def warn(self, msg: str):
        self.logger.warning(msg)


class TimeMsgBox(QMessageBox):
    def __init__(self, title: str, text: str, timeout=5):
        super().__init__()
        self.timeout = timeout
        self.setWindowTitle(title)
        self.setText(text)

        self.btn_accept = QPushButton(f"确 定 ({self.timeout})")
        self.btn_reject = QPushButton("取 消")
        self.addButton(self.btn_accept, QMessageBox.ButtonRole.AcceptRole)
        self.addButton(self.btn_reject, QMessageBox.ButtonRole.RejectRole)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.on_timer_timeout)
        self.timer.start(1000)

    def on_timer_timeout(self):
        self.timeout -= 1
        self.btn_accept.setText(f"确 定 ({self.timeout})")
        if self.timeout <= 0:
            self.btn_accept.click()


class MyMsgBox(QMessageBox):
    def __init__(self, title: str, text: str, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setText(text)
        self.btn_accept = QPushButton("确 定")
        self.btn_reject = QPushButton("取 消")
        self.addButton(self.btn_accept, QMessageBox.ButtonRole.AcceptRole)
        self.addButton(self.btn_reject, QMessageBox.ButtonRole.RejectRole)


# ---------------------- 窗口操作 ----------------------
def get_wnd_pos(hwnd):
    rect = GetWindowRect(hwnd)
    x, y = rect[0], rect[1]
    return x, y


def set_wnd_pos(hwnd, x, y):
    ret = SetWindowPos(hwnd, HWND_TOP, x, y, 0, 0, SWP_NOSIZE)
    return ret


def activate_wnd(hwnd):
    # pythoncom.CoInitialize()
    # 在该函数调用前，需要先发送一个其他键给屏幕，如ALT键, 否则可能报错
    # shell = Dispatch("WScript.Shell")
    # shell.SendKeys("%")  # 发送ALT键，ALT-%, CTRL-^, SHIFT-+, ENTER-~
    try:
        SetForegroundWindow(hwnd)
    except:
        pass


def terminate_wnd(hwnd):
    tid, pid = GetWindowThreadProcessId(hwnd)
    hProcess = OpenProcess(PROCESS_ALL_ACCESS, False, pid)
    TerminateProcess(hProcess, 0)


# ---------------------- 时间相关 ----------------------
# 随机数
def rnd(min: int, max: int):
    return random.randint(min, max)


# 随机返回序列中的一个元素
def rnd_choice(seq: list):
    return random.choice(seq)


# 间隔秒数
def delta_sec(start_sec: int, end_sec: int):
    gap_sec = end_sec - start_sec
    return gap_sec


# 间隔分数
def delta_minute(start_sec: int, end_sec: int):
    gap_sec = end_sec - start_sec
    gap_min = gap_sec // 60
    return gap_min


# 线程阻塞毫秒
def msleep(min_ms: int, max_ms=None):
    if max_ms is None:
        t_ms = min_ms
    else:
        t_ms = rnd(min_ms, max_ms)
    QThread.msleep(t_ms)


# ---------------------- 文件操作 ----------------------
def path_exist(path: str):
    # 路径是否存在
    if os.path.exists(path):
        return True
    return False


def dir_create(dir: str):
    # 创建目录, 不存在才创建
    if not path_exist(dir):
        os.makedirs(dir)


def dir_get_files(dir: str):
    # 获取目录中的文件
    ret = ""
    for root, dirs, files in os.walk(dir):
        ret = files
        break
    return ret


def file_create(path: str, content=""):
    # 创建文件
    with open(path, "a") as f:
        f.write(content)


def file_remove(path: str):
    # 删除文件, 存在才删除
    if path_exist(path):
        os.remove(path)


def file_rename(dir: str, old_file: str, new_file: str):
    # 文件重命名
    try:
        os.rename(f"{dir}\\{old_file}", f"{dir}\\{new_file}")
    except:
        log.warn("file_rename error")
        raise OSError


def file_clear_content(path: str):
    # 清空文件内容, 若没有文件会自动创建文件
    with open(path, "w+") as f:  # 打开文件并将光标置于开头
        f.truncate()  # 截断文件光标后的内容


def file_read_content(path: str) -> str:
    # 读取文件内容
    if not path_exist(path):
        file_create(path)
    content = ""
    with open(path, "r") as f:
        content = f.read()
    return content


def file_append_content(path: str, content: str):
    # 添加文件内容, 若没有文件会自动创建文件
    with open(path, "a") as f:
        f.write(content)


# json文件 -> py字典
def json_file_to_dict(path_cfg: str, default_cfg={}):
    try:
        # 若文件不存在, 则用默认的配置字典先创建json文件
        if not path_exist(path_cfg):
            with open(path_cfg, "w", encoding="utf-8") as f:
                json.dump(default_cfg, f, ensure_ascii=False,
                          sort_keys=True, indent=4)
        with open(path_cfg, "r", encoding="utf-8") as f:
            cfg_load = json.load(f)
    except:
        log.warn(f"json decode error! {path_cfg} {default_cfg}")
        cfg_load = {}
    return cfg_load


# json字符串 -> py字典
def json_str_to_dict(json_str: str):
    try:
        cfg_load = json.loads(json_str)
    except:
        log.warn(f"json decode error! {json_str}")
        cfg_load = {}
    return cfg_load


# py对象 -> json文件
def dict_to_json_file(py_dict: dict, path_cfg: str):
    try:
        with open(path_cfg, "w", encoding="utf-8") as f:
            json.dump(py_dict, f, ensure_ascii=False, sort_keys=True, indent=4)
    except:
        log.warn(f"json encode error! {py_dict} {path_cfg}")


# py对象 -> json字符串
def dict_to_json_str(py_dict: dict):
    try:
        json_str = json.dumps(py_dict, ensure_ascii=False, sort_keys=True)
    except:
        log.warn(f"json encode error! {py_dict}")
        json_str = "{}"
    return json_str

# ------------------ COM组件操作 -----------------------
# 注册组件到系统


def reg_com_to_system(obj_name: str) -> bool:
    obj_dll_dict = {COM_NAME_LW: DLL_LW_NAME,
                    COM_NAME_DM: DLL_DM_NAME, COM_NAME_TR: DLL_TR_NAME}
    dll_name = obj_dll_dict[obj_name]
    path_dll = f"{DIR_DLL}\\{dll_name}"
    if obj_name == COM_NAME_DM:
        DmReg = ctypes.WinDLL(f"dll\\{DLL_REGDM_NAME}")
        ret = DmReg.cquBe(path_dll, 1)  # SetDllPathW
    else:  # 此种注册方式需要以管理员运行
        start_info = subprocess.STARTUPINFO()
        start_info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        ret = subprocess.call(
            f"C:\\Windows\\System32\\regsvr32 {path_dll} /s", startupinfo=start_info)
        ret = True if ret == 0 else False
    if ret:
        return True
    return False


# 创建com组件对象
def create_com_obj(com_name: str):
    obj = None
    try:
        if com_name == COM_NAME_LW:
            obj = CreateObject(com_name)  # lw
        else:
            obj = Dispatch(com_name)  # dm, tr, op
    except:
        log.info(f"创建com对象{com_name}失败")
    return obj


# ------------------------- 安全相关 -------------------------
def is_user_dangerous():
    global action_code
    ret = False

    ret1 = anti_vm()
    if ret1:
        print("检测到虚拟机")
        action_code = action_code_dict["检测到虚拟机"]
        ret = True
    ret2 = anti_debug1()
    ret3 = anti_debug2()
    ret4 = anti_debug3()
    ret5 = anti_anti_debug4()
    if True in [ret2, ret3, ret4, ret5]:
        action_code = action_code_dict["检测到调试器"]
        ret = True
    return ret

# 检测多开, 检测到返回真


def detect_multi_run():
    global hMutex
    hMutex = CreateMutex(None, False, "TX_DETT_MR")  # 若存在, 会使该互斥体引用量加1
    if GetLastError() == ERROR_ALREADY_EXISTS:
        CloseHandle(hMutex)  # 使该互斥体引用量减1
        return True
    return False

# ------------------------- 网络验证相关 -------------------------
# 获取机器码(主板序列号+硬盘序列号)


def get_machine_code():
    pythoncom.CoInitialize()
    c = wmi.WMI()
    try:
        board_serial = c.Win32_BaseBoard()[0].SerialNumber
        disk_serial = c.Win32_DiskDrive()[0].SerialNumber
        disk_serial = disk_serial.strip(".").replace("_", "")
        machine_code = board_serial + disk_serial
        machine_code = machine_code[12:] + machine_code[:12]
        machine_code = machine_code[::-1]
    except:
        machine_code = ""
    return machine_code


# 获取操作系统
def get_operation_system() -> str:
    return platform.platform()


# 连接服务端tcp
def connect_server_tcp():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    err_no = tcp_socket.connect_ex((server_ip, server_port))
    if err_no != 0:
        return None
    return tcp_socket


# 发送数据给服务端
def send_to_server(tcp_socket: socket.socket, client_info_dict: dict):
    # 内容 转 json字符串
    client_info_dict["内容"] = dict_to_json_str(client_info_dict["内容"])
    # 根据消息类型决定是否对内容aes加密
    if client_info_dict["消息类型"] != "初始":
        # 对json内容进行aes加密
        client_info_dict["内容"] = aes.encrypt(client_info_dict["内容"])
    # 把整个客户端信息字典 转 json字符串
    json_str = dict_to_json_str(client_info_dict)
    # json字符串 base85编码
    send_bytes = base64.b85encode(json_str.encode())
    try:
        tcp_socket.send(send_bytes)
        print(f"客户端数据, 发送成功: {json_str}")
    except Exception as e:
        log.info(f"客户端数据, 发送失败: {e}")


# 从服务端接收数据
def recv_from_server(tcp_socket: socket.socket):
    tcp_socket.settimeout(5)  # 设置为非阻塞接收, 只等5秒
    recv_bytes = ""
    try:  # 若等待服务端发出消息时, 客户端套接字关闭会异常
        recv_bytes = tcp_socket.recv(4096)
    except:
        ...
    tcp_socket.settimeout(None)  # 重新设置为阻塞模式
    if not recv_bytes:  # 若客户端退出,会收到一个空str
        return "", {}
    # base85解码
    json_str = base64.b85decode(recv_bytes).decode()
    print(f"收到服务端的消息: {json_str}")
    # json字符串 转 py字典
    server_info_dict = json_str_to_dict(json_str)
    msg_type = server_info_dict["消息类型"]
    server_content_str = server_info_dict["内容"]
    # 把内容json字符串 转 py字典
    if msg_type != "初始":  # 若不为初始类型的消息, 要先aes解密
        # 先aes解密, 获取json字符串
        server_content_str = aes.decrypt(server_content_str)
    # json字符串 转 py字典
    server_content_dict = json_str_to_dict(server_content_str)
    return msg_type, server_content_dict


def is_wnd_in_list(hwnd: int) -> bool:
    for wk in worker_list:
        if wk is None:
            continue
        if wk.hwnd == hwnd:
            return True
    return False


# 获取 主屏幕 宽高
def get_main_screen_wh():
    pri_screen = QApplication.primaryScreen()
    rect = pri_screen.geometry()
    w = rect.width()
    h = rect.height()
    return w, h


# 排列所有窗口
def arrange_all_wnd(idx):
    if idx == 0:
        return
    screen_w, screen_h = get_main_screen_wh()
    if screen_h <= 670 or screen_w <= 870:
        return
    # 获取 游戏窗口数
    wnd_num = 0
    for wk in worker_list:
        if wk is None:
            continue
        wnd_num += 1
    if wnd_num < 2:
        return
    group_num = ((wnd_num - 1) // 5) + 1
    if idx == 1:  # 垂直排列
        # (group_num-1)*delta_x + 800(末窗宽) + 70(左侧预留) = screen_w
        delta_x = (screen_w - 870) // (group_num - 1) if group_num > 1 else 0
        for group in range(group_num):
            gap_num = 4 if group < group_num - 1 else (wnd_num - 1) % 5
            pos_x = 70 + group * delta_x
            # gap_num*delta_y + 600(末窗高) + 40(状态栏) + 30(末窗标题栏) = screen_h
            delta_y = (screen_h - 670) // gap_num if gap_num > 0 else 0
            start, end = group * 5, group * 5 + gap_num + 1
            for row in range(start, end):
                wk = worker_list[row]
                pos_y = (row % 5) * delta_y
                set_wnd_pos(wk.hwnd, pos_x, pos_y)
                wk.x, wk.y = pos_x, pos_y

    elif idx == 2:  # 水平排列
        # (group_num-1)*delta_y + 600(末窗高) + 40(状态栏) + 30(末窗标题栏) = screen_h
        delta_y = (screen_h - 670) // (group_num - 1) if group_num > 1 else 0
        for group in range(group_num):
            gap_num = 4 if group < group_num - 1 else (wnd_num - 1) % 5
            pos_y = group * delta_y
            # gap_num*delta_x + 800(末窗宽) + 70(左侧预留) = screen_w
            delta_x = (screen_w - 870) // gap_num if gap_num > 0 else 0
            start, end = group * 5, group * 5 + gap_num + 1
            for row in range(start, end):
                wk = worker_list[row]
                pos_x = 70 + (row % 5) * delta_x
                set_wnd_pos(wk.hwnd, pos_x, pos_y)
                wk.x, wk.y = pos_x, pos_y

    elif idx == 3:  # 斜排列
        delta_x = int((screen_w - 870) / (wnd_num - 1))
        delta_y = int((screen_h - 670) / (wnd_num - 1))
        for wk in worker_list:
            if wk is None:
                continue
            pos_x = wk.row * delta_x + 70
            pos_y = wk.row * delta_y
            set_wnd_pos(wk.hwnd, pos_x, pos_y)
            wk.x, wk.y = pos_x, pos_y


# 时间串 转 时间戳, "2020-12-26 00:59:30" -> 1608915570
def time_str_to_time_stamp(time_str: str):
    format_time = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    time_stamp = int(time.mktime(format_time))
    return time_stamp


# 过大漠VIP
def pass_dm_vip():
    ver = com_obj.ver()
    print(ver)
    dwDllBase = GetModuleHandle(f"dll\\{DLL_DM_NAME}")
    ret = True
    if ver == "6.1538":
        WriteProcessMemory(-1, dwDllBase + int(addr_crack, base=16), b"\x01")
    elif ver == "5.1423":
        WriteProcessMemory(-1, dwDllBase + int("0x1063d0", base=16), b"\x01")
    else:  # 其它收费版本
        ret = com_obj.reg("ws164899ee5cf5278a39f6d936bcff32f4497a", add_code)
    log.info(f"com组件2注册结果: {ret}")


hMutex = None

DIR_WORK = os.getcwd()
DIR_RES = "\\".join([DIR_WORK, "res"])
DIR_DLL = "\\".join([DIR_WORK, "dll"])
DIR_MAP = "\\".join([DIR_RES, "map"])
DIR_PT = "\\".join([DIR_RES, "pt"])

DIR_SAVE = "C:\\Tx_Tech"
DIR_LOG = "\\".join([DIR_SAVE, "log"])
DIR_TEMP = "\\".join([DIR_SAVE, "temp"])
dir_create(DIR_SAVE)
dir_create(DIR_LOG)
dir_create(DIR_TEMP)

PATH_CLIENT_LOG = "\\".join([DIR_LOG, "client.log"])
PATH_JSON_LOGIN = "\\".join([DIR_SAVE, "login.json"])
PATH_JSON_MAIN = "\\".join([DIR_SAVE, "main.json"])
PATH_JSON_PLAN = "\\".join([DIR_SAVE, "plan.json"])

log = Log()

# dll名称
DLL_DM_NAME = "Qt5Sqd.dll"  # dm.dll
DLL_REGDM_NAME = "Qt5Xmr.dll"  # DmReg.dll
DLL_REG_NAME = "Regdll.dll"
DLL_LW_NAME = "lw.dll"
DLL_TR_NAME = "tr.dll"
DLL_MY_NAME = "yth.dll"

# COM组件1-图灵
COM_NAME_TR = "TURING.FISR"
# COM组件2-大漠(或乐玩)
COM_NAME_LW = "lw.lwsoft3"
is_custom = False  # 是否为定制插件
if is_custom:
    COM_NAME_DM = "pb.sft"
else:
    COM_NAME_DM = "dm.dmsoft"

# 注册com组件1到系统
if reg_com_to_system(COM_NAME_TR):
    log.info("注册com组件1到系统, 成功")
else:
    log.info("注册com组件1到系统, 失败")

# 确定使用哪个插件作为com组件2
CLS_NAME = Dm
COM_NAME = COM_NAME_LW if CLS_NAME == Lw else COM_NAME_DM

# 注册com组件2到系统
if reg_com_to_system(COM_NAME):
    log.info("注册com组件2到系统, 成功")
else:
    log.info("注册com组件2到系统, 失败")

# 创建com原生对象
ori_obj = create_com_obj(COM_NAME)
# 若为定制插件, 封装一层以修改自定义函数名为方便理解的函数名
if is_custom:
    ori_obj = BaseObj(ori_obj)
# 把 原生对象 再封装一层, 以统一不同插件接口函数名
com_obj = Lw(ori_obj) if COM_NAME == COM_NAME_LW else Dm(ori_obj)


SLEEP_TIME = 100  # 等待时间ms, 越大执行速度越慢, 占用CPU越少
SLEEP_AFTER_CLICK = 150  # 点击后的等待时间ms

wnd_login = None  # 登录窗口对象
wnd_main = None  # 主窗口对象

cur_time_stamp = int(time.time())
cur_time_fmt = time.strftime("%H:%M:%S")


my_dll = ctypes.WinDLL(f"dll\\{DLL_MY_NAME}")
anti_vm = my_dll.fn1
anti_debug1 = my_dll.fn2
anti_debug2 = my_dll.fn3
anti_debug3 = my_dll.fn4
anti_anti_debug4 = my_dll.fn5
show_task_bar_icon = my_dll.fn6

# ------------------------- 网络验证相关 -------------------------
server_ip = "127.0.0.1"
server_port = 47123
machine_code = get_machine_code()

action_code_dict = {
    "正常": "*d#fl1I@34rt7%gh.",
    "检测到改数据": "*d#flI1@34rt7%gh.",
    "检测到虚拟机": "*d#flI2@34rt7%gh.",
    "检测到调试器": "*d#flI3@34rt7%gh.",
}

action_code = action_code_dict["正常"]

# 从服务端获取的数据
aes_key = "*d#f1Il@34rt7%gh."  # AES密钥, 登录界面初始化时获取, 先随机写一个迷惑破解者
user_account = "aaa"  # 用户账号, 登录成功才获取
pwd_pic = "1234"  # 图片密码, 先随机写一个迷惑破解者
pwd_zk = "5678"  # 字库密码, 先随机写一个迷惑破解者
addr_crack = "0x9073E4"  # CRACK内存地址, 先随机写一个迷惑破解者
add_code = "abcdefg"  # 附加码, 先随机写一个迷惑破解者
due_time = "2030-01-01 00:00:00"

notice = "加载公告失败..."  # 公告
url_update = "https://www.baidu.com"  # 更新网址
allow_login = False  # 允许登录
allow_reg = False  # 允许注册
allow_unbind = False  # 允许解绑
latest_ver = "0.0.0"  # 最新客户端版本

# 构造加密类实例化对象
aes = crypto.AesEncryption(aes_key)  # 先构造一个假的

# ------------------------- 控件相关 ---------------------------
TBE_CONSOLE_ROW = 15
TBE_CONSOLE_COL = 7
COL_HWND = 0
COL_PLAN = 1
COL_SCHOOL = 2
COL_RUN = 3
COL_PAUSE = 4
COL_END = 5
COL_LOG = 6
SELECTED = "√"
HIDE_X = 7680

# ------------------------- 业务相关 ---------------------------
WND_TITLE = "SW4"
WND_CLASS = "GLFW30"
PROC_NAME = "sw4main_multi.dll"
worker_list = [None for _ in range(TBE_CONSOLE_ROW)]  # 存放所有窗口工人对象的列表
cmb_plan_list = [None for _ in range(TBE_CONSOLE_ROW)]  # 方案下拉框对象列表


# 乐玩专用映射字典
mode_diplay_dict = {"normal": 0, "gdi": 1,
                    "gdi2": 2, "dx2": 3, "dx": 4, "opengl": 5}
mode_mouse_dict = {"normal": 0, "windows": 1, "windows3": 2, "dx": 3, "dx2": 4}
mode_keypad_dict = {"normal": 0, "windows": 1,
                    "windows3": 2, "dx": 3, "dx2": 4}
# 大漠专用映射字典
mode_back_dict = {0: 0, 1: 1, 2: 101, 3: 103, 4: 5}

mode_display = mode_diplay_dict["dx2"] if CLS_NAME == Lw else "dx2"
mode_mouse = mode_mouse_dict["windows3"] if CLS_NAME == Lw else "dx2"
mode_keypad = mode_keypad_dict["windows"] if CLS_NAME == Lw else "dx"
mode_public = 1+2+4+8+256+512 if CLS_NAME == Lw else "dx.public.active.api|dx.public.active.message|dx.public.active.api2|dx.public.graphic.protect|dx.public.anti.api"
mode_back = 0 if CLS_NAME == Lw else mode_back_dict[3]

# -------------------------------------------- 配置相关 --------------------------------------------
cfg_login = {  # 登录窗口
    "账号": "", "密码": "", "提示更新版本": True, "记住账号密码": True,
}

cfg_main = {  # 配置_主界面
    # 界面设置
    "绑定模式": "模式2", "工具栏方向": "垂直",
    # 基本设置
    "人宠自动补血": True, "人宠自动补蓝": True, "补充宠物忠诚": True, "自动买药": True,
    "加血药数量": "50", "加蓝药数量": "50", "伤势药数量": "50", "高宠粮数量": "50",
    "血药购买地点": "天仙店铺", "蓝药购买地点": "天仙店铺", "伤药购买地点": "天仙店铺", "宠粮购买地点": "天仙店铺",
    "自动使用驱魔香": True, "自动购买驱魔香": True, "自动购买传送符": True, "自动补充飞行旗包": True,
    "自制家具和庭院装饰": True, "优先使用还童丹买宠": False, "自动排队回到原服": False,
    "购物货币": "信誉", "开宝箱": "左",
    "禁用系统睡眠": False, "禁用屏幕保护": False, "定时": False, "定时运行全部窗口": True, "定时关闭计算机": True,
    "定时运行全部窗口时间": "00:01", "定时关闭计算机时间": "03:00", "获取窗口后排列方式": "0",
    "获取窗口后设置方案": "0", "双击方案列设置方案": "1",
    # 单人相关
    "师门次数": "20", "修炼次数": "30", "疯道人预言截图": True, "寻物用帮贡完成": False, "运镖次数": "20",
    "宝图次数": "10", "经商角色": "妮妮", "经商难度": "简单", "捐献装备等级": "70", "捐献装备数量": "8",
    "捐献贵重装备": False, "清理背包藏宝图": "自动挖宝", "清理背包现金": "上架寄售", "清理背包SW币": "商城出售",
    "任务链环数": "60", "玄武次数": "40", "青龙次数": "20", "经商次数": "2", "官职次数": "20",
    "烹饪次数": "20", "化龙鼎额外修炼": False, "化龙鼎兑换龙魂": False, "修炼宝箱地图": "长安城外",
    "天降宝箱地图": "长安城外",
    # 组队相关
    "捉鬼次数": "40", "打千年老妖": True, "打野地图": "当前地图", "打野时间": "600",
    "跟随队长领双": True, "跟随队长解双": True, "跟随队长冻双": True, "跟随队长退队": True,
    "自动关闭对话框": True, "钓鱼地图": "傲来国", "钓鱼次数": "1", "钓鱼抛竿": "S评分", "钓鱼处理": "兑换积分",
    "副本一名称": "三打白骨精", "副本一次数": "4", "副本二名称": "玄武门之变", "副本二次数": "4",
    "领取双倍时间": "2小时", "边境次数": "3", "封妖地图": "神弃平原", "封妖次数": "20", "蛮洞次数": "5",
}

cfg_plan = {  # 配置_默认方案
    "执行列表": [], "宝宝策略": "捕捉", "富裕发财": True, "普攻大肉山": True, "自动召唤": True,
    "地府拉环": True, "辅助救队友": True, "天魔买暗器": True, "首个回合技能": "自动",
    "首个回合目标": "敌方", "剩余回合技能": "自动", "剩余回合目标": "敌方",
}

cfg_plan_dict = {
    "0内置默认": copy.deepcopy(cfg_plan),
}

# 任务次数字典
task_count_dict = {}
