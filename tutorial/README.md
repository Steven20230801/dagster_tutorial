# Tutorial Template Project

This is a [Dagster](https://dagster.io/) project made to be used alongside the official [Dagster tutorial](https://docs.dagster.io/tutorial).

# Windows設立環境變數
setx DAGSTER_HOME "C:\Users\Steven\Documents\Python\Dagster" /M
Write-Host $env:DAGSTER_HOME # Power-shell

echo %DAGSTER_HOME%

venv\scripts\activate
dagster dev

Error: No arguments given and no [tool.dagster] block in pyproject.toml found.
```
[tool.dagster]
storage = "sqlite"
```