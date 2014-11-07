import getopt, sys
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from spiders.mmspider import MmspiderSpider
from scrapy.utils.project import get_project_settings

class startSpider(object):
    def __init__(self):
        super(startSpider, self).__init__()
        self.file = ''
        self.num = 0
    def help_text(self):
        print """
    main.py [-h HELP] [-n NUM] [-f FILE] [-v] [-s START]

    optional arguments:
        -h, --help      get this help and exit
        -n, --num       concurrent_requests (default is 16)
        -f, --file      pic save location(default is ./pics)
        -v              show versions and exit
        -s, --start     start spider
        """

    def main(self):
        try:
            opts, args = getopt.getopt(
            	sys.argv[1:], 
            	"hsn:f:v", 
            	["help", "start", "num=", "file="])
        except getopt.GetoptError as err:
            # print help information and exit:
            print str(err) # will print something like "option -a not recognized"
            sys.exit(2)
        for o, a in opts:
            if o in ("-h", "--help"):
                self.help_text()
                sys.exit()
            elif o in ("-n", "--num"):
                try:
                    self.num = int(a)
                except ValueError as err:
                    print 'invalid input'
                    sys.exit()
            elif o in ("-f", "--file"):
            	   self.file = a
            elif o == "-v":
                print '0.0.1'
                sys.exit()
            elif o in ("-s", "--start"):
            	print 'spider running...'
                self.start()
            else:
                assert False, "unhandled option"
    
    def start(self):
        spider = MmspiderSpider()
        settings = get_project_settings()
        if self.file:
            settings.set('IMAGES_STORE', self.file)
        if self.num:
            settings.set('CONCURRENT_REQUESTS', self.num)
        print settings
        #crawler = Crawler(settings)
        # crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
        # crawler.configure()
        # crawler.crawl(spider)
        # crawler.start()
        # log.start()
        # reactor.run()

if __name__ == "__main__":
    startSpider().main()
