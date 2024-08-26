import check50

@check50.check()
def hw_exists():
    """helloworld.py exists."""
    check50.exists("helloworld.py")

def hn_exists():
    """helloname.py exists."""
    check50.exists("helloname.py")
