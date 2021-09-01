# Just putting this little thing here for future reference.
# Dogs take keyword arguments too, it turns out. What do you know?

class Dog():
    def __init__(self, **kwargs):
        self.name = kwargs["name"]
        self.age = kwargs["age"]
        self.attitude = kwargs["attitude"]
        
    def showName(self):
        print("Dog's name is " + self.name + ".")
        
    def showAge(self):
        # Note the explicit conversion. I miss Lua.
        print("Dog's age is " + str(self.age) + ".")
        
    def showAttitude(self):
        print("Dog's attitude is " + self.attitude + ".")

# Testing stuff. He's been eating way too much recently. Not my fault though.        
bunio = Dog(name="Bunio", age = 3, attitude = "hongry")
bunio.showName()
bunio.showAge()
bunio.showAttitude()
