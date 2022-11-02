from copy import deepcopy

class Star_Cinema:
    _hall_list =[]
    def entry_hall(self,hall):
        self._hall_list.append(hall)
#1 end
class Hall(Star_Cinema):

    def __init__(self,rows,cols,hall_no) -> None: #,seats,show_list.rows,cols,hall_no
        self.seats={}
        self.show_list=[]
        self.rows=rows
        self.cols=cols
        self.hall_no=hall_no
        self.id_list=[]
        self.total_seat=rows*cols
        super().__init__()
        self.entry_hall(self)
          
    
    def entry_show(self,id,movie_name,time):
        self.id=id
        self.movie_name=movie_name
        self.time=time
        self.id_list.append(self.id)
        self.show_list.append((self.id,self.movie_name,self.time))
        self.seat_arr = [["Free" for i in range(self.cols)] for j in range(self.rows)]  
        self.seats['id']=self.seat_arr

    def check_and_finalize(self,a,seatn): 
        self.a=deepcopy(a)
        self.seatn=seatn
        self.s=''.join(self.seatn)
        con=False

        for i,v in enumerate(self.a):                 #check this seat index is valid or not
            for j,h in enumerate(v):
                self.a[i][j]=f'{chr(i+65)}{j+1}'
                if self.a[i][j]==self.s:
                    con=True

        if con: #if valid 
            x=ord(self.s[0])-66
            y=ord(self.s[1])-49
            if self.seats['id'][x][y]=="Free":
                self.seats['id'][x][y]=self.name
                self.total_seat-=1
                print("Seat booked successfully")
            else:
                print("No sir,This seat is already booked")    


        else:
            print("Invalid seat number")     

    def book_seats(self,name,ph,id_of_show,seat_no):
        self.name=name
        self.ph=ph
        self.id_of_show=id_of_show
        self.seat_no=seat_no  #this is tuple and a lot of work remaining
        if self.id_of_show in self.id_list:
           self.check_and_finalize(self.seats['id'],self.seat_no)  
        else:
            print("Invalid show id,Sir\n\n")   
 
    def view_show_list(self):
        print("\n\n")
        print('_'*85)
        print('_'*85)
        print("\n")
        print("Show Id\t\t\t\tMovie name\t\t\t\tShow time")
        #print(self.show_list)  
        for i in self.show_list:
            for j in i:
                print(j,end='\t\t\t\t')
            print("\n") 
        print('_'*85)
        print('_'*85)  
        print("\n")         

    def view_available_seats(self):
        print("\n\n")
        print("'X'- for unavailable seats")
        print('_'*40)
        print('_'*40)
        print("\n")
        for i,v in enumerate(self.seat_arr):                 #check this index is valid or not
            for j,h in enumerate(v):
                if self.seat_arr[i][j]!="Free":
                    print("X",end="     ")
                else:
                    print(f'{chr(i+65)}{j+1}',end='    ')
            print("\n")     
        print('_'*40)
        print('_'*40) 
        print("\n")                

#Problem in no.7


S=Star_Cinema()
H1=Hall(5,6,"HL23")
H1.entry_hall(H1)
H1.entry_show("M09","Black Panther 2","09.00 AM")
H1.entry_show("N12","Bullet Train ","12.00 PM")
H1.entry_show("AF03","Men in Black","03.00 PM")
H1.entry_show("AF06","Hawa(Bangla)","06.00 PM")
H1.entry_show("N09","Rosaline(22)","09.00 PM")

while True:
    print("Choose an option-------")
    print("\n1.Show available\n2.Ticket available\n3.Book a ticket")
    x=int(input())
    print("\n")
    if x==1:
        H1.view_show_list()
    if x==2:
        H1.view_available_seats()
    if x==3:
        n=int(input("How many tickets you want to buy??? "))
        if n>H1.total_seat:
            print("Sorry sir, ",n," Seats are Not available")
        else:
            name=input("Please input your name: ")
            ph=input("Please enter your phone number: ")
            id_of_show=input("Plase enter the show id: ")
            for i in range(n):
                seat_no=input("Please enter the seat number: ")
                print("\n")
                H1.book_seats(name,ph,id_of_show,seat_no)  
