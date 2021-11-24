from pysnmp.hlapi import *


def getComputerName(server):
    iterator = getCmd(SnmpEngine(),
                      CommunityData('public'),
                      UdpTransportTarget((server, 161)),
                      ContextData(),
                      ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.5.0')))

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:  # SNMP engine errors
        print(errorIndication)
    else:
        if errorStatus:  # SNMP agent errors
            print('%s at %s' % (errorStatus.prettyPrint(),
                  varBinds[int(errorIndex)-1] if errorIndex else '?'))
        else:
            for varBind in varBinds:  # SNMP response contents
                print(varBind)
            
            return varBind



def getComputerRam(server):
    iterator = getCmd(SnmpEngine(),
                      CommunityData('public'),
                      UdpTransportTarget((server, 161)),
                      ContextData(),
                      ObjectType(ObjectIdentity('.1.3.6.1.2.1.25.2.2.0')))

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:  # SNMP engine errors
        print(errorIndication)
    else:
        if errorStatus:  # SNMP agent errors
            print('%s at %s' % (errorStatus.prettyPrint(),
                  varBinds[int(errorIndex)-1] if errorIndex else '?'))
        else:
            for varBind in varBinds:  # SNMP response contents
                print(varBind)
            
            return varBind