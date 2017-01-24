class Fraction(object):

    """Docstring for Fraction. """

    def __init__(self,nom,denom):
        """This class will take nominator and denominator

        :nom: TODO
        :denom: TODO

        """
        self._nom = nom
        self._denom = denom

    def common_divisor(self):
        for n in range(2,10):
            if self._nom / n >= 1:
                if self._denom / n >= 1:
                    print(n)
                    break




f = Fraction(2,3)
f.common_divisor()
