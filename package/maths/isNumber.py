class isNumber:

    @classmethod
    def isNumber(cls, n):
        try:
            float(n)
        except ValueError:
            return False
        return True