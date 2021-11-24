from pysnmp.hlapi import *


class NewWindow():
    def __init__(self) -> None:
        pass


def getComputerName():
    iterator = getCmd(SnmpEngine(),
                      CommunityData('public'),
                      UdpTransportTarget(('172.17.11.94', 161)),
                      ContextData(),
                      ObjectType(ObjectIdentity('1.3.6.1.4.1.311.1.1.3.1')))

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:  # SNMP engine errors
        print(errorIndication)
    else:
        if errorStatus:  # SNMP agent errors
            print('%s at %s' % (errorStatus.prettyPrint(),
                  varBinds[int(errorIndex)-1] if errorIndex else '?'))
        else:
            for varBind in varBinds:  # SNMP response contents
                print(' = '.join([x.prettyPrint() for x in varBind]))
