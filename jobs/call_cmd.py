from dagster import job, op, repository
import subprocess


@op
def run_script():
    # 調用命令列指令來執行 script.py
    project_path = r"C:/Users/data-taipei/Documents/dagster_tutorial"
    file_name = r"C:/Users/data-taipei/Documents/dagster_tutorial/reports/etl1.py"
    command = f"cd {file_name} && C:/Users/data-taipei/Documents/dagster_tutorial/venv/Scripts/python.exe {file_name}"
    result = subprocess.run(["python", "script.py"], capture_output=True, text=True)

    # 打印輸出結果
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)


@job
def run_python_script_job():
    run_script()


@repository
def run_python_script():
    return [run_python_script_job]
