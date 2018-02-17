; The name of the installer
Name "bwRenamer"

; The file to write
OutFile "installers\bwrenamer_1.0.0_installer_win32.exe"

; The default installation directory
InstallDir "$PROGRAMFILES\bwRenamer"

; Registry key to check for directory (so if you install again, it will
; overwrite the old one automatically)
InstallDirRegKey HKLM "Software\bwRenamer" "Install_Dir"

; Request application privileges for Windows Vista
RequestExecutionLevel admin

;--------------------------------

; Pages
Page components
Page directory
Page instfiles

UninstPage uninstConfirm
UninstPage instfiles

;--------------------------------

; The stuff to install
Section "bwRenamer (required)"

    SectionIn RO

    ; Set output path to the installation directory.
    SetOutPath $INSTDIR

    ; Put application files there
    File "build\*.*"

    ; Write the installation path into the registry
    WriteRegStr HKLM "SOFTWARE\bwRenamer" "Install_Dir" "$INSTDIR"

    ; Write the uninstall keys for Windows
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\bwRenamer" "DisplayName" "bwRenamer"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\bwRenamer" "UninstallString" '"$INSTDIR\Uninstall.exe"'
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\bwRenamer" "NoModify" 1
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\bwRenamer" "NoRepair" 1
    WriteUninstaller "Uninstall.exe"

SectionEnd


; Optional section (can be disabled by the user)
Section "Start Menu Shortcuts"

    CreateDirectory "$SMPROGRAMS\bwRenamer"
    CreateShortCut "$SMPROGRAMS\bwRenamer\bwRenamer.lnk" "$INSTDIR\bwRenamer.exe" "" "$INSTDIR\bwRenamer.exe" 0
    CreateShortCut "$SMPROGRAMS\bwRenamer\Uninstall.lnk" "$INSTDIR\Uninstall.exe" "" "$INSTDIR\Uninstall.exe" 0

SectionEnd

;--------------------------------

; Uninstaller
Section "Uninstall"

    ; Remove registry keys
    DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\bwRenamer"
    DeleteRegKey HKLM "SOFTWARE\bwRenamer"

    ; Remove files
    Delete "$INSTDIR\*.*"

    ; Remove shortcuts, if any
    Delete "$SMPROGRAMS\bwRenamer\*.*"

    ; Remove directories used
    RMDir "$SMPROGRAMS\bwRenamer"
    RMDir "$INSTDIR"

SectionEnd
