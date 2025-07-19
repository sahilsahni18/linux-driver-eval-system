import subprocess

def compile_driver(file_path):
    try:
        compile_cmd = ["gcc", "-Wall", "-Wextra", "-c", file_path]
        result = subprocess.run(compile_cmd, capture_output=True, text=True)
        success = result.returncode == 0
        warnings = result.stderr.count("warning:")
        errors = result.stderr.count("error:")
        return success, warnings, errors
    except Exception as e:
        return False, 0, 1

def run_static_analysis(file_path):
    try:
        result = subprocess.run(["clang-tidy", file_path, "--"], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)
