class Parent:
    # Creating Constructors
    def __init__(self):
        # Here are initializing the initial variables
        """
            Working of Constructors is to initialize the instance variable of class and the Constructors called when the
            object of its class is created. No need to call explicitly while normal function needs to be called.
        """
        self.example()

        self.dominant_hand = 'right'
        self.hair_color = 'black'
        self.avg_hight = '5ft'
        self.eye_color = 'black'
        print(self.dominant_hand, self.hair_color, self.eye_color, self.avg_hight)

        def example(self):
            print('this is an example')

parent_obj = Parent()

# open terminall : ctrl + `
# rever tab: Shift+tab
# ctrl+shift+z
# ctrl+d  : multiple same thing picker
