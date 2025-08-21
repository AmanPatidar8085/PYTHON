from random import randint

class Train:
    

    def __init__(self,trainno):
        self.trainno=trainno
    
    def book(self,fro,to):
        print(f"Ticket is booked in train no:{self.trainno} from {fro}t0{to}")
    
    def getstatus(self):
        print(f"Train no: {self.trainno}is ruuning on time")
     
    def getfare(self,fro,to):
        print(f"Ticket is fare in train no:{self.trainno} from {fro}t0{to}")
        {randint(222,44565)}


t=Train(12399)
t.book("Rampur","Delhi")
t.getstatus()
t.getfare("Rampur","delhi")
