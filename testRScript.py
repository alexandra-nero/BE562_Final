import subprocess

code = subprocess.check_call("Rscript helloworld.R", shell=True)
#code is the error message that the command prompt/terminal will return. it will be a 0 unless there is an error.
