class SerVivo: 
    """
    This class represents a SerVivo with the single attribute indicating if it is dead or alive

    Attributes
    ----------
    public: 
    None

    protected:
    _vivo: represents if the SerVivo is dead or alive. 

    Private: They should not be docummented, they are part of the hidden implementation

    Methods 
    -------
    die()
    The SerVivo dies
    """
    def __init__(self):
        print("")

    def is_vivo(self):
        return -1


    def die(self):
        return -1

    ''' TODO IF NEEDED OVERRIDE METHODS TO STR, EQUALITY, COMPARISON, HASH , etc.
    '''

def main():
    """TESTS!
    """
    print("=======================================================.")
    print(">Test Case 1: isVivo().")
    print("=======================================================.")
    serVivo = SerVivo()
    if(serVivo.is_vivo() == True):
        print("OK: Test PASS. TEST ISVIVO PASSED.")
    else:
        print("KO: Check Constructor.")
    serVivo.die()
    print("=======================================================.")
    print(">Test Case 2: die().")
    print("=======================================================.")
    if(serVivo.is_vivo()):
        print("KO: TEST DIE FAILED.")
    else:
        print("OK: Test PASS. TEST DIE PASSED.")

if __name__=="__main__":
    main()