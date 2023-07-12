import pandas as pd
from datetime import datetime

StudentList=pd.read_excel("Student List.xlsx","Sheet1")
del StudentList['Name']
StudentList.index=list(StudentList.N)
del StudentList['N']
#Student List
StudentList
data=pd.DataFrame({'Reg':list(StudentList['Reg'])})

def myfunction(fileName,StudentList,Attname,data):

    Nov = pd.read_excel(fileName, "Sheet1")
    del Nov ['Unnamed: 0']
    Nov .drop([0], inplace=True)
    # print(Nov_12)
    # print(type(Nov_12.Timestamp[1]))#firstRow+Str

    '''Nov_12_index=Nov_12.index
    Nov_12.sort_values(by=['Reg'],inplace=True)
    Nov_12.index=Nov_12_index'''

    Reg = []
    Attendance_Nov12 = []
    for i in range(1, 31):
        if StudentList.Reg[i] in list(Nov .Reg):

            j = 1
            while j >= 1 and j < ((Nov .Reg.count()) + 1):
                if StudentList.Reg[i] == Nov .Reg[j]:
                    n = j + 1
                    if n != ((Nov .Reg.count()) + 1) and StudentList.Reg[i] == Nov .Reg[n]:
                        x1 = Nov .Timestamp[j]
                        y1 = str(x1).split(',')
                        minutes1 = str((y1[1]).split()[0])
                        minutes1 = datetime.strptime(minutes1, '%H:%M:%S')

                        x2 = Nov .Timestamp[n]
                        y2 = str(x2).split(',')
                        minutes2 = str((y2[1]).split()[0])
                        minutes2 = datetime.strptime(minutes2, '%H:%M:%S')


                        sub = ((minutes2 - minutes1).seconds) / 60
                        Reg.append(StudentList.Reg[i])
                        if sub > 50:
                            sub = 50
                        Attendance_Nov12.append(round(sub, 2))
                        j = j + 2
                    else:
                        x1 = Nov .Timestamp[j]
                        y1 = str(x1).split(',')
                        minutes1 = str((y1[1]).split()[0])
                        minutes1 = datetime.strptime(minutes1, '%H:%M:%S')

                        minutes2 = datetime.strptime('10:20:00', '%H:%M:%S')
                        sub = ((minutes2 - minutes1).seconds) / 60
                        if sub > 50:
                            sub = 50
                        Reg.append(StudentList.Reg[i])
                        Attendance_Nov12.append(round(sub, 2))
                        j = j + 1
                else:
                    j = j + 1

        else:
            Reg.append(StudentList.Reg[i])
            Attendance_Nov12.append("absent")

    Reg1 = list(StudentList['Reg'])
    Reg
    New1 = []
    New2 = []
    for j in Reg1:
        sum = 0
        for i in range(0, len(Reg)):
            if Reg[i] == j and Attendance_Nov12[i] != 'absent':
                sum = sum + Attendance_Nov12[i]
            else:
                if Reg[i] == j and Attendance_Nov12[i] == 'absent':
                    sum = 'absent'
        if sum!='absent' and sum<25:
            New1.append('absent')
        else:
            New1.append(sum)

    data[Attname] = New1

myfunction("meetingAttendanceList_Nov_12.xlsx",StudentList,"Nov_12",data)
myfunction("meetingAttendanceList_Nov_15.xlsx",StudentList,"Nov_15",data)
myfunction("meetingAttendanceList_Nov_17.xlsx",StudentList,"Nov_17",data)
myfunction("meetingAttendanceList_Nov_19.xlsx",StudentList,"Nov_19",data)
myfunction("meetingAttendanceList_Nov_22.xlsx",StudentList,"Nov_22",data)
myfunction("meetingAttendanceList_Nov_24.xlsx",StudentList,"Nov_24",data)
myfunction("meetingAttendanceList_Nov_26.xlsx",StudentList,"Nov_26",data)
print(data)
data.to_excel('Attendance1.xlsx')
