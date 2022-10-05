"""
this program suspends gta.exe process for ten seconds then resumes it. The reason for this is because when the 
process is resumed you will be in a lobby by yourself.
"""

import psutil, time

def findProcessIdByName(processName):
    '''
    Get a list of all the PIDs of a all the running process whose name contains
    the given string processName
    '''
    listOfProcessObjects = []
    #Iterate over the all the running process
    for proc in psutil.process_iter():
       try:
           pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
           # Check if process name contains the given name string.
           if processName.lower() in pinfo['name'].lower() :
               listOfProcessObjects.append(pinfo)
       except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
           pass
    return listOfProcessObjects

process_id = findProcessIdByName("GTA5")[0]['pid']

p = psutil.Process(process_id)
p.suspend()
print('process is suspended')

for i in range(1,11):
    print(11-i)
    time.sleep(1)

p.resume()
print("process is resumed")



