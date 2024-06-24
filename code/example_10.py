# Logic. If statement.

if True:
    print("The condition was True")
    
if False:
    print("The condition was False")  # This will not be executed

dry_run_flag = True

if dry_run_flag:
    print("Dry run mode: Only showing what should happen")
else:
    print("Real run mode: Actually doing the work")
