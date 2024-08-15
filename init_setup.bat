@echo off
echo [ %date% %time% ]: START

@REM echo [ %date% %time% ]: Creating virtual env
@REM python -m venv venv/
@REM echo [ %date% %time% ]: activate venv
@REM call venv\Scripts\activate
@REM echo [ %date% %time% ]: installing the requirements
@REM pip install -r requirements.txt

echo [ %date% %time% ]: creating folders and files
python template-automation.py

echo [ %date% %time% ]: END
