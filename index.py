import jenkins
import csv
import time
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

#clear the spreadsheet
sheet.clear()

# Push the data of csv to spreadsheet
row = 1
column = 1
requestCount = 0
#limit for write request per 100 seconds
writeQuota = 90 
Fi = []
Fi = open("jenkins.csv",'r')
for value in Fi:
    items = value.strip().split(',')
    for item in items:
        if(requestCount == writeQuota):
            time.sleep(100)
            requestCount = 0
        sheet.update_cell(row, column, item)
        requestCount += 1
        column += 1
    row += 1
    column = 1

Fi.close()

if __name__ == "__main__":
 
    get_server_instance()
    build_details()
