import subprocess
def runcmd(cmd)->list:
    out=[]
    err=[]
    for i in cmd:
        print(i)
        p1=subprocess.Popen(i ,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True,universal_newlines=True)
        out1,err1=p1.communicate()
        print(out1,err1)
        out.append(out1)
        err.append(err1)
    return out,err
