import pylint
import pylint.lint

def use_pylint(file_path):
    with open("static_review.txt", "a") as f:
        result=pylint.run_pylint(file_path)
        f.write(file_path+'\n'+result+'\n')
        
#use_pylint('RepoCopy\\file1.py')
