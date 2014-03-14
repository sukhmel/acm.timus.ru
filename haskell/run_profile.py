import time
import subprocess

task  = 1787
cwd   = r'.'
stdin = cwd + r'\%i.txt' % task

done  = 1
tries = 5

while done and tries:
    done = subprocess.call(['ghc', '%i.hs' % task], cwd=cwd, shell=True)
    tries -= 1

with open(stdin) as inFile:
    start = time.clock()
    process = subprocess.Popen( [cwd + r'\%i.exe' % task]
                              , stdout=subprocess.PIPE
                              , stdin=inFile
                              , shell=True
                              )
    out, err = process.communicate()
    stop  = time.clock()
    print(out)
    print('elapsed time = %2.4f sec' % (stop - start))
