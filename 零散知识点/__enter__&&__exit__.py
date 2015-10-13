#coding:utf-8
__author__ = 'solomn'

class A(object):
    def __init__(self):
        print "initializing ...."

    def __del__(self):
        print "deleting...."


    def __enter__(self):#必须用于with中
        print "entering...."

    def __exit__(self, exc_type, exc_val, exc_tb):#必须用于with中
        print "exiting...."
        pass

    def test_fun(self):
        print "doing test function..."

if __name__=="__main__":
    with A() as a:
        print 111
    print "------------------------"
    A()
