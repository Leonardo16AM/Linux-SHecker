# To create a custom grader create a function grader(str input,str answer,str output) who returns a boolean if it is a correct answer 
import re

def grader(input,answer,output):
    try:
        ansli=re.split(' |\n',answer)
        outli=re.split(' |\n',output)
        answer=[]
        output=[]
        for i in ansli:
            if i!='' : answer.append(i)
        for i in outli:
            if i!='' : output.append(i)
        # print(answer)
        # print(output)
        return answer==output
    except Exception:
        return False
