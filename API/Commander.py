import subprocess
import inspect
import time

CResults = {}

def run_command(cmd, shell=False, cwd=None, env=None, op_name=''):
    global CResults
    if op_name == '':
        op_name = inspect.stack()[1].function
    if op_name not in CResults:
        CResults[op_name] = {}
    op = CResults[op_name]
    op['cmd'] = cmd
    op['shell'] = shell
    op['cwd'] = cwd
    op['env'] = env
    op['start_time'] = time.time()
    try:
        if shell:
            spr = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd, env=env)
        else:
            spr = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd, env=env)
        op['status'] = spr.returncode
        op['output'] = spr.stdout.strip()
    except Exception as exMessage:
        op['status'] = -1
        op['output'] = str(e)
    finally:
        op['end_time'] = time.time()
        return op_name, op['status'], op['output']

# Example usage
op_name, status, output = run_command(['powershell','-Command',"echo welcomeTo PythonCommander via QaYeDev."])

# Accessing the results
print(CResults[op_name]['cmd'])
print(CResults[op_name]['output'])