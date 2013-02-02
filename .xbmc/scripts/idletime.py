import xbmc,xbmcgui
import subprocess,os
 
ILT = 0
IDLE_TIME_MIN = 15
s = 0
 
while(1):
  it = xbmc.getGlobalIdleTime()
  s = ((IDLE_TIME_MIN * 60) - it )
  if (s > 0):
    if (ILT == 1):
      if xbmc.Player().isPlayingVideo():
        pass
      else:
        os.system("irsend send_once led on")
        ILT = 0
 
  elif (s < 0):
    if (ILT == 0 and xbmc.Player().isPlayingVideo() == False):
      os.system("irsend send_once led off")
      ILT = 1
  xbmc.sleep(5000)
