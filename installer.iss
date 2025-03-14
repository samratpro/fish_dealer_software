; Define installer name and output directory
[Setup]
AppName=Fish Dealer Software
AppVersion=1.0
DefaultDirName={localappdata}\FishDealerSoftware
DefaultGroupName=Fish Dealer Software
OutputBaseFilename=FishDealerSetup
Compression=lzma
SolidCompression=yes
SetupIconFile=C:\Users\pc\Desktop\pyhton\fish_dealer_software\static\logo.ico

; Wizard images (if needed)
WizardImageFile=C:\Users\pc\Desktop\pyhton\fish_dealer_software\static\appbanner.bmp
WizardSmallImageFile=C:\Users\pc\Desktop\pyhton\fish_dealer_software\static\logo.bmp

; Silent installation option
DisableDirPage=no
DisableProgramGroupPage=yes

; Include Python interpreter and app files
[Files]
Source: "C:\Users\pc\Desktop\pyhton\fish_dealer_software\*"; DestDir: "{app}"; Flags: recursesubdirs
Source: "C:\Users\pc\Desktop\pyhton\fish_dealer_software\python\*"; DestDir: "{app}\python"; Flags: recursesubdirs
Source: "C:\Users\pc\Desktop\pyhton\fish_dealer_software\font\*"; DestDir: "{app}\font"; Flags: recursesubdirs
Source: "C:\Users\pc\Desktop\pyhton\fish_dealer_software\icons\*"; DestDir: "{app}\icons"; Flags: recursesubdirs
Source: "C:\Users\pc\Desktop\pyhton\fish_dealer_software\images\*"; DestDir: "{app}\images"; Flags: recursesubdirs
Source: "C:\Users\pc\Desktop\pyhton\fish_dealer_software\run.vbs"; DestDir: "{app}"

; Create necessary folders
[Dirs]
Name: "{app}"; Permissions: everyone-full
Name: "{localappdata}\FishDealerSoftware"; Permissions: everyone-full

; Registry settings (optional)
[Registry]
Root: HKCU; Subkey: "Software\FishDealerSoftware2"; Flags: uninsdeletekey

; Shortcuts
[Icons]
Name: "{group}\Fish Dealer Software"; Filename: "{app}\run.vbs"; WorkingDir: "{app}"; IconFilename: "{app}\static\logo.ico"
Name: "{group}\Uninstall Fish Dealer Software"; Filename: "{uninstallexe}"; IconFilename: "{app}\static\logo.ico"
Name: "{commondesktop}\Fish Dealer Software"; Filename: "{app}\run.vbs"; WorkingDir: "{app}"; IconFilename: "{app}\static\logo.ico"; Tasks: desktopicon

; Run the application after installation
[Run]
Filename: "{app}\run.vbs"; Description: "{cm:LaunchProgram, Fish Dealer Software}"; Flags: nowait postinstall skipifsilent

; Uninstaller (removes everything)
[UninstallDelete]
Type: filesandordirs; Name: "{app}"
Type: filesandordirs; Name: "{localappdata}\FishDealerSoftware"

; Optional tasks
[Tasks]
Name: desktopicon; Description: "Create a &desktop icon"; GroupDescription: "Additional icons:"; Flags: unchecked