def main():
  tasks=[]
  while True: 
      try:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark as done")
        print("5. mark as pending again")
        print("6. Exit")
        ins=int(input("Instruction: "))
       
      except ValueError:
        print("Invalid instruction!")
        continue
#Add task
      if ins==1:
          x=input("Add Task: ")
          if x.strip()=="":
             print("No task entered!")
             continue
          else:
             
             tasks.append({"task":x,"status":"pending"})
#VIEW TASK LIST
      elif ins==2:
       return_list(tasks)
# Removing a task      
      elif ins==3:
        if check_empty(tasks):
           continue
        else:
          return_list(tasks)

          try:
            z= int(input("Enter Task to be removed: "))
            if 0<z<=len(tasks):
                z-=1
                tasks.pop(z)
                print("Updated task list:")
                return_list(tasks)

            else:
              print("enter a valid task number!")
              continue
          except ValueError:
            print("Enter valid instruction!")
            continue
  #mark as done
      elif ins==4:
       
       if check_empty(tasks):
           continue
        
       else:
          return_list(tasks)
          try:
            y=int(input("Enter task number to mark as done: "))
            if 0<y<=len(tasks) :
                y-=1
                if tasks[y]["status"]=="done":
                   print("Already done!")
                   continue
                else:
                    tasks[y]["status"]="done"
                    print("Updated list:")
                    return_list(tasks)
            else:
                print("Invalid task no!") 
                continue          
          except ValueError:
            print("Not a valid input!")
            continue
        #mark as pending again
      elif ins==5:
         if check_empty(tasks):
           continue
        
         else:  
          return_list(tasks)
          try:
            q=int(input("Enter task number to mark as pending again: "))
            if 0<q<=len(tasks) :
                q-=1
                if tasks[q]["status"]=="pending":
                   print("Already pending!")
                   continue
                else:
                    tasks[q]["status"]="pending"
                    print("Updated list:")
                    return_list(tasks)
            else:
                print("task not found") 
                continue          
          except ValueError:
            print("Not a valid input!")
            continue
    #Exit
      elif ins==6:
         print("Final todo list")
         return_list(tasks)
         break
          
      else:
        print("command not found!")
        continue

  # i need error cheking for segments acepting index of a list element  
  # enumerate passkeys
  #     

def  return_list(x):
     if not x:
           print("No task available!")
           
     else:
      for i,tsk in enumerate(x,start=1):
          if tsk["status"]== "done":     
            print(f'{i}. {strike(tsk["task"])} ({tsk["status"]}) ')
          else:
            print(f'{i}. {tsk["task"]} ({tsk["status"]}) ') 
              
def strike(text):
        return ''.join([u'\u0336{}'.format(c) for c in text])
def check_empty(tasks):
    if not tasks:
        print("No task available!")
        return True
    return False

      
if __name__=="__main__":     
    main() 

