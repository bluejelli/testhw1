# COPY PASTE YOUR FINAL HELLO WORLD CLASS IN HERE ===================================

class HelloWorld:
    # ===== Class: Hello World =======#
    # Class Variables:
    # - message: str -> message to be displayed


    # Args: None.
    # Returns: None
    def __init__(self, message :str = "Hello World!"):
        #  constructor

        self.message = message
     
    # Args: None
    # Returns: str with message 
    def __repr__(self) -> str:
       
        return self.message
