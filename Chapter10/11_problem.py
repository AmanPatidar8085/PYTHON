from random import randint

class Train:
    

    def __init__(slf,trainno):
        slf.trainno=trainno
    
    def book(slf,fro,to):
        print(f"Ticket is booked in train no:{slf.trainno} from {fro}t0{to}")
    
    def getstatus(slf):
        print(f"Train no: {slf.trainno}is ruuning on time")
     
    def getfare(slf,fro,to):
        print(f"Ticket is fare in train no:{slf.trainno} from {fro}t0{to}")
        {randint(222,44565)}


t=Train(12399)
t.book("Rampur","Delhi")
t.getstatus()
t.getfare("Rampur","delhi")
