import check50

@check50.check()
def exists():
    """password_checker.py exists"""
    check50.exists("password_checker.py")

@check50.check(exists)
def testHelloWorld():
    """All lowercase and less than 15 characters long"""
    output = check50.run("python3 password_checker.py").stdin("helloworld", prompt=False).stdout("Weak").exit()

@check50.check(exists)
def testHackorz():
    """8 chars and meets all requirements"""
    output = check50.run("python3 password_checker.py").stdin("h4cK0rz!", prompt=False).stdout("Strong").exit()

@check50.check(exists)
def testLessThanEight():
    """Input of ess than 8 characters"""
    output = check50.run("python3 password_checker.py").stdin("Hello", prompt=False).stdout("Weak").exit()