stud_seat = [[]]
def place(s_num,row,clm):
    #query for fetching the usn of this s_num
    #usn = #query result
    #stud_seat[row][col] = usn
    #return stud_seat
    print(snum,row,clm)

def arrange(sec,rm,bool_mat):                     #sec is a list and rm is the room
    rows = rc_rooms[rm[1]],
    cols = rc_rooms[rm[2]],
    rm_bool = bool_mat[rm]
    for section in sec:
        while(j<cols):
            if (stud_no%4==0):          #student num should start from 0
                i=0
            else:
                i=1
            while(i<rows):
                if(rm_bool[i][j]):
                    print("placing a student",stud_no)
                    lists = place(stud_no,i,j)
                    stud_no+=1
                i = i+2
            j=j+2 
    print(stud_no)       
    print(lists)
sections = []
rc_rooms = {"201":[3,4],"202":[7,8]} #the rooms in the list as well as the rc_rooms dict shd be same
rooms = []
cap_total = 0
bool_rm = {"201":[[1,1,1],[0,1,1],[1,1,1]]}
print("enter the rooms")
for k in rooms:
    rooms.append(input())
print("enter the sections")
for k in sections:
    sections.append(input())
for i in room:
    rc_list = rc_rooms[i]
    cap_total+=rc_list[0]*rc_list[1]
print("the total capacity of the rooms is ",cap_total)
for room in rooms:
        arrange(sections,room,bool_rm)
