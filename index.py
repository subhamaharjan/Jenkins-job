import jenkins
import csv
from secrets import gc, sheet, token

# Connect to the Jenkins server
def get_server_instance():
    jenkins_url = 'https://cc-p-jenkins.ckan.io/'
    username = 'subha.maharjan@datopian.com'
    server = jenkins.Jenkins(jenkins_url, username, password=token)
    return server

# Get job info and  loop over builds
def build_details():
    server = get_server_instance()
    job_name = 'simplified list instances'
    info = server.get_job_info(job_name)
    lastCompletedBuild = info['lastCompletedBuild']
    number = lastCompletedBuild['number']
    consoleOutput = server.get_build_console_output(job_name, number)


    # create a file and write the value of consoleOutput
    with open("consoledata.txt","w") as f:
        f.write(consoleOutput)

    return f

# Iterating over lines and appending the lines
mylines = []
routeData = []
clientData= []
data = []
client = ""
with open('consoledata.txt', 'rt') as rf:
    for myline in rf:
        mylines.append(myline)


    for line in mylines:
        if line[0:2] == '==':
            client = line.replace('== ','')

        if line[0] == '-':
            routeData.append(line.replace('- ','').replace('\n',''))
            clientData.append(client.replace('\n',''))

# Zip the list
data = zip(clientData, routeData)


# Headers for CSV File
header = ['Client List', 'Routes']

#Convert zipped data into csv file
with open('jenkins.csv', 'w', newline="\n") as output:  
    writer = csv.writer(output, delimiter = ',')
    writer.writerow(i for i in header)
    for j in data:
        writer.writerow(j)
       
# Upload csv file to google sheets
content = open("jenkins.csv",'r').read()
gc.import_csv('1jbhuF3gyLs7NLrRZRLprzm52Aa68FiYZ3cC3BuKHldU',content)



if __name__ == "__main__":
 
    get_server_instance()
    build_details()
