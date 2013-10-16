from threading import Thread
import imp
import pdb

class Alice(Thread):
    def run(self):
        print "import lock is already held:" + str(imp.lock_held())
        import to_import
        print "My name is Alice!"

foo = Alice()
foo.start()
foo.join()
