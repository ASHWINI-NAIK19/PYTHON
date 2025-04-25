class Company():
    cname='Infosys'
    cloc='Bangalore'
    CEO='Salil Parikh'
    def __init__(self,name,id,loc,sal):
        self.name=name
        self.id=id
        self.loc=loc
        self.sal=sal
e1=Company('Ashwini',124,'RAM',10000)
e2=Company('Ravi',125,'RT',12000)
print(e1.name,e1.id,e1.loc,e1.sal)
print(e2.name,e2.id,e2.loc,e2.sal)
