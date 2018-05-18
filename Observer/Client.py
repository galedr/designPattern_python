from Observer import *
from Subject import *

subject = ProcessOne()
observerOne = InsertIntoTableOne()
observerTwo = InsertIntoTableTwo()
subject.addObserver(observerOne)
subject.addObserver(observerTwo)
subject.notify()

observerOne.response()
observerTwo.response()
