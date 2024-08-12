# import subprocess
# if __name__ == '__main__':
# #command line args along with error capture on failure with check true
#       s = subprocess.run('behave --no-capture',shell=True, check=True)

import subprocess

# from Testing6 import *

# if __name__ == '__main__':
# p = argparse.ArgumentParser()
# # --testdir command line argument added
# # p.add_argument('--testdir', required=False, help="File path")
# p.add_argument('testdir', help="File path")
# a = p.parse_args()
# testdir = a.testdir
# complete command
# c= f'behave --no-capture {testdir}'
c = f'behave -f allure_behave.formatter:AllureFormatter -o Reports --no-capture'
s = subprocess.run(c, shell=True, check=True)
