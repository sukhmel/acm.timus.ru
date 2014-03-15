# task file must be named "task_number.hs", it is compiled here
# test data must be named "task_number.txt" and consist of separate runs,
#      concatenated with "##\n". Each run is then performed separately.

import time
import subprocess

# TASK NUMBER
task  = 1787
cwd   = r'.'
stdin = cwd + r'\%i.txt' % task

done  = 1
tries = 5

# try several times to build the task, without optimizing
while done and tries:
    done = subprocess.call(['ghc', '%i.hs' % task], cwd=cwd, shell=True)
    tries -= 1

# read file with data for runs
with open(stdin) as runs:
    tasks = runs.read().split('##\n')

# conduct separate checks, test performance
for data in tasks:
    start = time.clock()
    process = subprocess.Popen( [cwd + r'\%i.exe' % task]
                              , stdout=subprocess.PIPE
                              , stdin =subprocess.PIPE
                              , stderr=subprocess.PIPE
                              , shell=True
                              )
    out, err = process.communicate(input=data.encode())
    stop  = time.clock()

    # output result
    result = ''
    if len(data) > 0:
        result += 'in\t%s%s\n' % (data.replace('\n','\n\t')[:-1], '-'*79)

    if len(out) > 0:
        result += 'out\t%s%s\n'  % (out.decode().replace('\n','\n\t')[:-1], '-'*79)

    if len(err) > 0:
        result += 'err\t%s%s\n'  % (err.decode().replace('\n','\n\t')[:-1], '-'*79)

    result += 'time\t%2.4f sec\n%s\n' % (stop - start, '='*79)

    print(result)
