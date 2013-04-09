import sys
from xml.dom import minidom


class RSLParser(object):
    def __init__(self):
        pass

    def parse(self, path):
        xmldoc = minidom.parse(path)
        print(xmldoc)
        motions = xmldoc.getElementsByTagName('rrs2_PureMotionStatement')
        for motion in motions:
            print("Motion is: ", motion)
            targets = xmldoc.getElementsByTagName('PtpTarget')
            for target in targets:
                print("Target is: ", target)
                params = target.getElementsByTagName('TargetParameters')
                print("params is: ", params)
                for p in params:
                    vals = p.getElementsByTagName('VALUE')
                    for val in vals:
                        print(val.attributes.items())
                        if val.attributes['name'].value == "Target":
                            print("Got a new ptp target to ", val.attributes["ay"].value, val.attributes["ay"].value)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = "samples/simple.rsl"
    parser = RSLParser()
    parser.parse(path)
    from IPython.frontend.terminal.embed import InteractiveShellEmbed
    ipshell = InteractiveShellEmbed( banner1="\nStarting IPython shell, available objects are:\n ")
    ipshell(local_ns=locals())

