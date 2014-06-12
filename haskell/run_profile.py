# task file must be named "task_number.hs", it is compiled here
# test data must be named "task_number.txt" and consist of separate runs,
#      concatenated with "##\n". Each run is then performed separately.

import time
import subprocess

# TASK NUMBER
task  = 1876
cwd   = r'.'
stdin = cwd + r'\%i.txt' % task

profiling = False
output    = True

done  = 1
tries = 5

# try several times to build the task, without optimizing
while done and tries:
    cmd = [ 'ghc'
          , '%i.hs' % task
          ]
    if profiling:
        cmd += [ '-prof'
               , '-auto-all'
##               , '-O2'
               ]
        
    process = subprocess.Popen( cmd
                              , cwd=cwd
                              , shell=True
                              , stdout=subprocess.PIPE
                              , stdin =subprocess.PIPE
                              , stderr=subprocess.PIPE
                              )
    out, err = process.communicate()
    done = len(err)
    tries -= 1

# succesfull compilation
if done == 0:
    # read file with data for runs
    with open(stdin) as runs:
        tasks = runs.read().split('##\n')

    # conduct separate checks, test performance
    for data in tasks:
        start = time.clock()
        cmd = [ cwd + r'\%i.exe' % task]
        if profiling:
            cmd += [ '+RTS'
                   , '-p'
                   ]

        process = subprocess.Popen( cmd 
                                  , stdout=subprocess.PIPE
                                  , stdin =subprocess.PIPE
                                  , stderr=subprocess.PIPE
                                  , shell=True
                                  )
        out, err = process.communicate(input=data.encode())
        stop  = time.clock()

        # output result
        result = ''
        if output:
            if len(data) > 0:
                result += 'in\t%s%s\n' % (data.replace('\n','\n\t')[:-1], '-'*79)

            if len(out) > 0:
                result += 'out\t%s%s\n'  % (out.decode('866').replace('\n','\n\t')[:-1], '-'*79)

        if len(err) > 0:
            result += 'err\t%s%s\n'  % (err.decode('866').replace('\n','\n\t')[:-1], '-'*79)

        result += 'time\t%2.4f sec\n%s\n' % (stop - start, '='*79)

        print(result)
else:
    print(err.decode())
