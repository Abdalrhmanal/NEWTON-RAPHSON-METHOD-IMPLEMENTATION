# class person:
#     def _init_(self, n, ln, id=-1):
#         self.name = n
#         self.lname = ln
#         if id == -1:
#             self.Id = self.getMaxId()
#         else:
#             self.Id = id

#     def getMaxId(self):
#         f = open("personId.text", "r")
#         id = f.read()
#         f.close()
#         return  int(id.strip())+1
#     def savePerson(self):
#         f = open("person.csv", "a")
#         try:
#             f.write("%s,%s,%s\n" % (self.Id, self.name, self.lname))
#         except Exception as exp:
#             print(exp)
#         else:
#             f1 = open("personId.text", "w")
#             f1.write("%s"%self.Id)
#             f1.close()
#         finally:
#             f.close()

#     def getAllPersons():
#         lstPerson = []
#         file = open("person.csv", "r")
#         try:
#             lstlines = file.readlines()
#             for line in lstlines:
#                 lstPersonLine = line.split(",")
#                 Id = lstPersonLine[0].strip()
#                 name = lstPersonLine[1].strip()
#                 lname = lstPersonLine[2].strip()
#                 per = person(name, lname, Id)
#                 lstPerson.append(per)
#             return lstPerson
#         except Exception as exp:
#             print(exp)
#         finally:
#             file.close()
#         return lstlines

# per = person("khaled", "khlef", 1)
# per1 = person("sgg", "dfh",2)
# per2 = person("sgsg", "sgsg",3)
# per3 = person("sgsgd", "khsgslef",4)
# per4 = person("khalsgded", "khsglef",5)
# per4 = person("khalsgded", "khsglef")
# per1.savePerson()
# per2.savePerson()
# per3.savePerson()
# per4.savePerson()
# lst=person.getAllPersons()
class Person:
    def _init_(self,n,ln):
         self.name=n
         self.lname=ln
         self.Id=self.getMaxId()+1
    def getMaxId(self):
        f=open("person.csv","r")
        alllines=f.readlines()
        f.close()
        lastline=alllines[len(alllines)-1]
        lst=lastline.strip(",")
        id=lst[0]
        return int(id.strip())#+1
    def savePerson(self):
        try:
            f=open("person.csv","a")
            f.write("%s,%s,%s\n"%(self.Id,self.namem,self.lname))
        except Exception as exp:
            print(exp)
        finally:
            f.close()
    def getAllPerson():
        file=open("person.csv","r",encode="utf-8")
        lstlines=file.readlines()
        file.close()
        return lstlines
lst=Person.getAllPerson()
    
per=Person("ahmad", "aldali")