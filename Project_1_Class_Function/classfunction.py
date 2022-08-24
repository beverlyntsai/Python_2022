class  human:
    def  jump(self):
       print('I can jump.')
    def  run(self):
        print('I can run.')
    def  behave(self):
       self.jump()
       self.run()

class  woman(human):
    def  sing(self):
        print('I can sing.')
    def  behave(self):
       self.sing()



lady=woman()
lady.jump()

