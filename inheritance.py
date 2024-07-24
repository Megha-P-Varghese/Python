class Course:
    def __init__(self,cname):
      self.cname = cname

    def dispcourse(self):
        print(self.cname)

class Subject(Course):
    def __init__(self,cname):
        Course.__init__(self,cname)
        #super().__init__(cname)

obj = Subject("MCA")
obj.dispcourse()
