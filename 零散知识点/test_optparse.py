__author__ = 'solomn'

from optparse import OptionParser
#
#
# parser = OptionParser()
#
#
#
# parser.add_option("-f", "--file","--ff","--fuckfilename",dest="filename",type= "int",
#                   help="write report to FILE", metavar="FILE")
#
# parser.add_option("-q", "--quiet",
#                   action="store_false", dest="verbose", default=True,
#                   help="don't print status messages to stdout")
#
#
#
# parser.add_option("-v", action="store_true", dest="verbose")
# # parser.add_option("-q", action="store_false", dest="verbose")
#
# parser.add_option("-a","--append",action="append",dest="append",help= "fuck apeend help")
#
# parser.add_option("-c","--const",action="store_const",help = "fuck const ",default = "fuck")
#
#
# (options, args) = parser.parse_args()
#
# if __name__ == "__main__":
#     print "options:",options
#     print "-------------------------"
#     print "args:",args




from optparse import OptionGroup

parser = OptionParser()

group = OptionGroup(parser, "Dangerous Options",
                    "Caution: use these options at your own risk.  "
                    "It is believed that some of them bite.")
group.add_option("-g", action="store_true", help="Group option.")
parser.add_option_group(group)

(options, args) = parser.parse_args()

# if __name__ == "__main__":
#     print "options:",options
#     print "-------------------------"
#     print "args:",args







