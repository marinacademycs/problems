import check50

@check50.check()
def exists():
    """password_checker.py exists"""
    check50.exists("password_checker.py")

@check50.check(exists)
def testHelloWorld():
    """Input of all lowercase and less than 15 characters long"""
    output = check50.run("python3 password_checker.py").stdin("helloworld", prompt=False).stdout("Weak").exit()

@check50.check(exists)
def testHackorz():
    """input of 8 chars and meets all other requirements"""
    output = check50.run("python3 password_checker.py").stdin("h4cK0rz!", prompt=False).stdout("Strong").exit()

@check50.check(exists)
def testLessThanEight():
    """Input of less than 8 characters"""
    output = check50.run("python3 password_checker.py").stdin("He11!o", prompt=False).stdout("Weak").exit()


@check50.check(exists)
def test2and8():
    """input of 9 chars but meets only 2 other requirements"""
    output = check50.run("python3 password_checker.py").stdin("Password!", prompt=False).stdout("Weak").exit()

@check50.check(exists)
def test10and2():
    """input of 10 chars and meets 2 other requirements"""
    output = check50.run("python3 password_checker.py").stdin("Jackknife!", prompt=False).stdout("Strong").exit()

@check50.check(exists)
def itsMeMario():
    """input of 15+ characters long"""
    output = check50.run("python3 password_checker.py").stdin("helloworlditsmemario", prompt=False).stdout("Strong").exit()

@check50.check(exists)
def test14and1():
    """input of 14 chars and meets 1 other requirement"""
    output = check50.run("python3 password_checker.py").stdin("Crocodiletears", prompt=False).stdout("Strong").exit()

@check50.check(exists)
def flyToTheMoon():
    """input of 14 chars and meets 0 other requirements"""
    output = check50.run("python3 password_checker.py").stdin("flymetothemoon", prompt=False).stdout("Weak").exit()
