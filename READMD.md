# 使用專案內的python建立job 
- etl_example.py : python檔案
- asset_example.py : dagster call etl_example.py 的設定檔案
執行: 
```
venv\scripts\activate  
dagster dev -f asset_example.py 
```