
Set-ExecutionPolicy Unrestricted
echo Setup MyProject
Invoke-WebRequest "https://archive.org/download/mp_20221212_202212/MP.zip" -OutFile MP.zip
mkdir C:\MP
Expand-Archive MP.zip C:\MP -Force
cd c:\MP
Invoke-WebRequest "https://archive.org/download/mt-5-app/MT5Data.zip" -OutFile MT5Data.zip
Expand-Archive  MT5Data.zip .QaYeApps\MT5 -Force
mkdir API
Invoke-WebRequest "https://raw.githubusercontent.com/QaYeProg/MTFullScript/main/API/__main__.py" -OutFile API\__main__.py
Invoke-WebRequest "https://raw.githubusercontent.com/QaYeProg/MTFullScript/main/env" -OutFile ".env"
Invoke-WebRequest "https://raw.githubusercontent.com/QaYeProg/MTFullScript/main/MTFullScript.py" -OutFile MTFullScript.py
Invoke-WebRequest "https://raw.githubusercontent.com/QaYeProg/MTFullScript/main/%3DRun.cmd" -OutFile "=Run.cmd"
echo Running Project.
.\scripts\activate
python .\MTFullScript.py
echo Done
