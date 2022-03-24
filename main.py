from winreg import *
import os
paths = {
    "SOFTWARE\Microsoft\Windows\CurrentVersion\Run",
    "SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Run",
    "Software\Microsoft\Windows\CurrentVersion\RunOnce",
    "Software\Microsoft\Windows\CurrentVersion\RunOnceEx",
    "System\CurrentControlSet\Services",
    "Software\Microsoft\Windows\CurrentVersion\RunServices",
    "Software\Microsoft\Windows\CurrentVersion\RunServicesOnce",
    "SOFTWARE\Microsoft\Active Setup\Installed Components",
    "SOFTWARE\Wow6432Node\Microsoft\Active Setup\Installed Components",
    "SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\SharedTaskScheduler",
    "SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\SharedTaskScheduler",
    "SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\ShellServiceObjects",
    "SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\ShellServiceObjects",
    "SOFTWARE\Microsoft\Windows\CurrentVersion\ShellServiceObjectDelayLoad",
    "SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\ShellServiceObjectDelayLoad",
    "Software\Classes\*\ShellEx\ContextMenuHandlers",
    "Software\Wow6432Node\Classes\*\ShellEx\ContextMenuHandlers",
    "Software\Classes\Drive\ShellEx\ContextMenuHandlers",
    "Software\Wow6432Node\Classes\Drive\ShellEx\ContextMenuHandlers",
    "Software\Classes\*\ShellEx\PropertySheetHandlers",
    "Software\Wow6432Node\Classes\*\ShellEx\PropertySheetHandlers",
    "Software\Classes\Directory\ShellEx\ContextMenuHandlers",
    "Software\Classes\Directory\ShellEx\ContextMenuHandlers",
    "Software\Wow6432Node\Classes\Directory\ShellEx\ContextMenuHandlers",
    "Software\Classes\Directory\Shellex\DragDropHandlers",
    "Software\Classes\Directory\Shellex\DragDropHandlers",
    "Software\Wow6432Node\Classes\Directory\Shellex\DragDropHandlers",
    "Software\Classes\Directory\Shellex\CopyHookHandlers",
    "Software\Classes\Directory\Background\ShellEx\ContextMenuHandlers",
    "Software\Classes\Directory\Background\ShellEx\ContextMenuHandlers",
    "Software\Wow6432Node\Classes\Directory\Background\ShellEx\ContextMenuHandlers",
    "Software\Classes\Folder\ShellEx\ContextMenuHandlers",
    "Software\Wow6432Node\Classes\Folder\ShellEx\ContextMenuHandlers",
    "Software\Classes\Folder\ShellEx\DragDropHandlers",
    "Software\Wow6432Node\Classes\Folder\ShellEx\DragDropHandlers",
    "Software\Microsoft\Windows\CurrentVersion\Explorer\ShellIconOverlayIdentifiers",
    "Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\ShellIconOverlayIdentifiers",
    "SOFTWARE\Microsoft\Windows NT\CurrentVersion\Font Drivers",
    "Software\Microsoft\Windows NT\CurrentVersion\Drivers32",
    "Software\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Drivers32",
    "Software\Classes\Filter",
    "Software\Classes\CLSID\{083863F1-70DE-11d0-BD40-00A0C911CE86}\Instance",
    "Software\Wow6432Node\Classes\CLSID\{083863F1-70DE-11d0-BD40-00A0C911CE86}\Instance",
    "Software\Classes\CLSID\{7ED96837-96F0-4812-B211-F13C24117ED3}\Instance",
    "Software\Wow6432Node\Classes\CLSID\{7ED96837-96F0-4812-B211-F13C24117ED3}\Instance",
    "System\CurrentControlSet\Control\Session Manager\KnownDlls",
    "Control Panel\Desktop\Scrnsave.exe",
    "System\CurrentControlSet\Services\WinSock2\Parameters\Protocol_Catalog9\Catalog_Entries",
    "System\CurrentControlSet\Services\WinSock2\Parameters\Protocol_Catalog9\Catalog_Entries64"
}


keys = []
fixed_keys = []

def local_keys(path):
    Local_Registry = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
    Local_RawKey = OpenKey(Local_Registry, path)
    try:
        i = 0
        while 1:
            name, value, type = EnumValue(Local_RawKey, i)
            output = (name, value, i)
            keys.append(str(output))
            i += 1
    except WindowsError:
        print()

for path in paths:
    try:
        local_keys(path)
    except:
        pass
for key in keys:
    if ".dll" in key:
        pass
    elif ".drv" in key:
        pass
    elif ".acm" in key:
        pass
    elif ".DLL" in key:
        pass
    elif "WebCheck" in key:
        pass
    else:
        fixed_keys.append(key)



file_startup = os.getenv('APPDATA') + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
files = os.listdir(file_startup)

print(f"[{len(fixed_keys)}] Registry Keys found")
print("===============================")
for key in fixed_keys:
    print(key)
print("===============================\n")

print(f"[{len(files)}] Files found")
print("===============================")
for file in files:
    print(f'{file_startup}\{file}')
print("===============================")
input = input("")
