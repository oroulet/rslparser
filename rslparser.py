import sys
from xml.dom import minidom
import xml.etree.ElementTree as et


class RSLParser(object):
    def __init__(self):
        pass

    def parse(self, path):
        tree = et.parse(path)
        root = tree.getroot()
        main = root.find("rrs2_MainRoutine")
        body = main.find("rrs2_RoutineBody")
        for cmd in body:
            print("cmd is: ", cmd)
            if cmd.tag == "rrs2_PureMotionStatement":
                target = cmd.find("PtpTarget")
                if target:
                    params = target.find("TargetParameters")
                    #print("params is: ", params)
                    for val in params:
                        if val.get('name') == "Target":
                            print("Got a new ptp target to ", val.get("ay"), val.get("ay"))
                            #val.set("ay", "00000000000000000000")
        #tree.write("output.xml")


    def parse2(self, path):
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
    #from IPython.frontend.terminal.embed import InteractiveShellEmbed
    #ipshell = InteractiveShellEmbed( banner1="\nStarting IPython shell, available objects are:\n ")
    #ipshell(local_ns=locals())

