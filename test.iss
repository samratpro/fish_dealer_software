; Define installer name and output directory
[Setup]
AppName=Fish Dealer Software
AppVersion=1.0
DefaultDirName={localappdata}\FishDealerSoftware
DefaultGroupName=Fish Dealer Software
OutputBaseFilename=FishDealerSetup
Compression=lzma
SolidCompression=yes
SetupIconFile=C:\Users\pc\Desktop\pyhton\fish\static\logo.ico

; Wizard images (if needed)
WizardImageFile=C:\Users\pc\Desktop\pyhton\fish\static\appbanner.bmp
WizardSmallImageFile=C:\Users\pc\Desktop\pyhton\fish\static\logo.bmp

; Silent installation option
DisableDirPage=no
DisableProgramGroupPage=yes

; Include Python interpreter and app files
[Files]
Source: "C:\Users\pc\Desktop\pyhton\fish\*"; DestDir: "{app}"; Flags: recursesubdirs
Source: "C:\Users\pc\Desktop\pyhton\fish\venv\*"; DestDir: "{app}\venv"; Flags: recursesubdirs
Source: "C:\Users\pc\Desktop\pyhton\fish\font\*"; DestDir: "{app}\font"; Flags: recursesubdirs
Source: "C:\Users\pc\Desktop\pyhton\fish\icons\*"; DestDir: "{app}\icons"; Flags: recursesubdirs
Source: "C:\Users\pc\Desktop\pyhton\fish\images\*"; DestDir: "{app}\images"; Flags: recursesubdirs

; Create necessary folders
[Dirs]
Name: "{app}"; Permissions: everyone-full
Name: "{localappdata}\FishDealerSoftware"; Permissions: everyone-full

; Registry settings (optional)
[Registry]
Root: HKCU; Subkey: "Software\FishDealerSoftware2"; Flags: uninsdeletekey

; Shortcuts
[Icons]
Name: "{group}\Fish Dealer Software"; Filename: "{app}\venv\Scripts\pythonw.exe"; Parameters: """{app}\main.py"""; WorkingDir: "{app}"; IconFilename: "{app}\static\logo.ico"
Name: "{group}\Uninstall Fish Dealer Software"; Filename: "{uninstallexe}"; IconFilename: "{app}\static\logo.ico"
Name: "{commondesktop}\Fish Dealer Software"; Filename: "{app}\venv\Scripts\pythonw.exe"; Parameters: """{app}\main.py"""; WorkingDir: "{app}"; IconFilename: "{app}\static\logo.ico"; Tasks: desktopicon

; Run the application after installation
[Run]
Filename: "{app}\venv\Scripts\pythonw.exe"; Parameters: """{app}\main.py"""; WorkingDir: "{app}"; Flags: nowait postinstall

; Uninstaller (removes everything)
[UninstallDelete]
Type: filesandordirs; Name: "{app}"
Type: filesandordirs; Name: "{localappdata}\FishDealerSoftware"

; Optional tasks
[Tasks]
Name: desktopicon; Description: "Create a &desktop icon"; GroupDescription: "Additional icons:"; Flags: unchecked