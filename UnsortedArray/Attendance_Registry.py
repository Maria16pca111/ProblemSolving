def Attendance_Registry(Entry):
    Count=0
    CountMax=0
    for x in range(0,10):
        if not (x==Entry):
            Entry.insert(0,x)
            print'Welcome'
            Count+=1
            print(Entry)
    for y in Entry:
        for z in Entry:
            if(y==z):
                Updated_Entry=Entry.remove(z)
                print'Bye! See you Again'               
                CountMax+=1
                print(Updated_Entry)
                print(Entry)
    print Count,CountMax
            
Entry=[20]
Attendance_Registry(Entry)
            