import os
import subprocess
import time

def run_pytest():
    """Run pytest with specified arguments."""
    pytest_args = [
        'pytest',
        '-v',
        '--html=Result/Report/report.html',
        'backend/tests/test_frontend.py'  # Path to the test file
    ]
    result = subprocess.run(pytest_args, cwd=os.path.abspath(os.path.dirname(__file__)))
    if result.returncode != 0:
        raise RuntimeError("pytest failed")

def run_locust():
    """Run Locust with specified arguments."""
    locust_args = [
        'locust',
        '-f',
        'backend/tests/test_performance.py',  # Path to the Locust file
    ]
    result = subprocess.run(locust_args, cwd=os.path.abspath(os.path.dirname(__file__)))
    if result.returncode != 0:
        raise RuntimeError("Locust failed")

if __name__ == "__main__":
    run_locust()
    run_pytest()
    # locust_process = run_locust()
    # time.sleep(5)  # Give Locust some time to start
    # # pytest_process = run_pytest()
    #
    # # pytest_process.wait()
    # locust_process.terminate()

    print("Tests completed.")
