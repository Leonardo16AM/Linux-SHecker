from termcolor import colored
import pandas as pd 
import subprocess
import os
from grader import grader
import time

class testcase:
    def __init__(self,code_name,tc_id,io_format,t_limit,m_limit):
        self.code_name=code_name
        self.code='Code/'+code_name
        self.id=tc_id
        self.format=io_format
        self.t_limit=t_limit
        self.path = os.path.dirname(os.path.realpath('__file__'))+'/'
        self.veredict=0

        self.ifile=self.path+'Input/'
        self.ofile=self.path+'Output/'
        if io_format==1:
            self.ifile=f"{self.ifile}{self.code_name}.{tc_id}.in"
            self.ofile=f"{self.ofile}{self.code_name}.{tc_id}.out"
        if io_format==2:
            self.ifile=f"{self.ifile}{tc_id}.in"
            self.ofile=f"{self.ofile}{tc_id}.out"
        if io_format==3:
            self.ifile=f"{self.ifile}{self.code_name}.in.{tc_id}"
            self.ofile=f"{self.ofile}{self.code_name}.out.{tc_id}"

    def evaluate(self):
        ''' Function to evaluate if the testcase is correct'''
        
        ifile=self.ifile
        ofile=self.ofile

        #Copy files from testcase file to input.in
        with open(ifile) as infile1:
            with open(self.path+"input.in", "w") as infile2:
                for line in infile1:
                    infile2.write(line)


        #Runing code
        
        os.system(f'./{self.code}&' )

        crun=subprocess.check_output(f"pgrep {self.code_name}", shell=True)
        crun=crun.decode("utf-8").split('\n')[0]
        time.sleep(self.t_limit+0.05)
        


        #Checking if TLE
        try:
            is_run=subprocess.check_output(f"ps {crun}", shell=True)
            is_run=is_run.decode("utf-8").split(' ')
            self.veredict=3
            print(colored("Time Limit Exceeded","red"))
            return self.veredict
        except Exception:
            pass
  
        ifile=str(open(ifile,'r+t').read())
        ofile=str(open(ofile,'r+t').read())
        afile=str(open(self.path+"/output.out",'r+t').read())
        self.veredict=int(grader(ifile,ofile,afile))
        if self.veredict==0:
            print(colored("Wrong Answer","red"))
        else:
            print(colored("Accepted","green"))
        return self.veredict


class tests:
    def __init__(self):
        self.code_name=input(colored("Enter the name of the problem (without extension)\n",'blue'))
        ftc=int(input(colored("Enter the first testcase number\n",'blue')))
        ltc=int(input(colored("Enter the last testcase number\n",'blue')))
        self.iot=input(colored("Enter the type of input/output: \n (1) file.[num].in \n (2) [num].in \n (3) file.in.[num]\n",'blue'))
        self.tl=input(colored("Enter the time limit in seconds. Example: 2.5 \n",'blue'))
        print(colored("In case of an error in the data provided the checker probably will crash, it is your fault, so be carefull",'cyan'))
        self.ml=1000
        time.sleep(2)
        

        print(colored("Building code",'blue'))
        os.system(f'make Code/{self.code_name}>file.log')
        log=open("file.log","r+").read()
        
        
        if os.path.isfile(f"Code/{self.code_name}"): 
            print(colored("Code builded succesfully",'green'))
        else:
            print(colored("Compilation Error",'red'))
            return

        num_tc=ltc-ftc+1
        num_ok=0

        self.testcases=[]
        for i in range(int(ftc),int(ltc)+1):
            self.testcases.append(testcase(self.code_name,i,int(self.iot),int(self.tl),int(self.ml) ))
            print(f"Runing testcase {i} :",end="")
            res=self.testcases[i-1].evaluate()
            if res==1:
                num_ok+=1

        os.remove(f"Code/{self.code_name}")
        percent=num_ok*100/num_tc
        print("Total:",end=" ")
        if percent==100:
            print(colored(percent,'green'))
        elif percent==0:
            print(colored(percent,'red'))
        else:
            print(colored(percent,'yellow'))
        
if __name__=="__main__":
    ds=tests()
    input(colored("Press a enter to close SHecker",'magenta'))
