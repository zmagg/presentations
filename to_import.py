from threading import Thread
import imp

class Bob(Thread):
    def run(self):
        print "import lock is already held:" + str(imp.lock_held())
        imp.release_lock()
        import urllib
        print "My name is Bob!"

bar = Bob()
bar.start()
bar.join()
