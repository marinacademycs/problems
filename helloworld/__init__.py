import check50

@check50.check()
def hw_exists():
    """helloworld.py exists."""
    check50.exists("helloworld.py")
