import glob
import ai_response
import prompt_template
import static_analysis
import git_clone
if __name__ == "__main__":
    repo=input("paste git repo link : ")
    git_clone.clone(repo)
    file_list=glob.glob('**/*.py')
    for file in file_list:
        with open(file,'r') as read_file:
            contents = read_file.read() 
            prompt=prompt_template.review_prompt+f'{contents}'        
            f = open("code_review.txt", "a")
            f.write(read_file.name+'\n')
            f.write(ai_response.response(prompt)+'\n')
            f.close()
    ai_response.response(prompt_template.forget_prompt)
    #static_analysis.use_pylint()
#must add multithreading            

    
