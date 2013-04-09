from xml.dom import minidom

if __name__ == "__main__":
    xmldoc = minidom.parse("samples/simple.rsl")
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
    #print(itemlist[0].attributes['name'].value)
    #for s in itemlist :
        #print(s.attributes['name'].value)

    from IPython.frontend.terminal.embed import InteractiveShellEmbed
    ipshell = InteractiveShellEmbed( banner1="\nStarting IPython shell, available objects are:\n ")
    ipshell(local_ns=locals())

