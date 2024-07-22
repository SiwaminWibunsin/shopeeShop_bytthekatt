[Setup]
AppName=Shopee Bot
AppVersion=1.0
DefaultDirName={pf}\ShopeeBot
DefaultGroupName=Shopee Bot
OutputDir=.
OutputBaseFilename=ShopeeBotSetup

[Files]
Source: "dist\main_shopee.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Shopee Bot"; Filename: "{app}\main_shopee.exe"
Name: "{group}\Uninstall Shopee Bot"; Filename: "{uninstallexe}"
