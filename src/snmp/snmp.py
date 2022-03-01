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


def getComputerUpTime(server):

    iterator = getCmd(SnmpEngine(),
                      CommunityData('public'),
                      UdpTransportTarget((server, 161)),
                      ContextData(),
                      ObjectType(ObjectIdentity('1.3.6.1.2.1.1.3.0')))

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


def getComputerServices(server):
    iterator = getCmd(SnmpEngine(),
                      CommunityData('public'),
                      UdpTransportTarget((server, 161)),
                      ContextData(),
                      ObjectType(ObjectIdentity('1.3.6.1.2.1.1.7.0')))

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


def getMACAdress(server):

    iterator = getCmd(SnmpEngine(),
                      CommunityData('public'),
                      UdpTransportTarget((server, 161)),
                      ContextData(),
                      ObjectType(ObjectIdentity('1.3.6.1.2.1.3.1.1.2.3')))

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:  # SNMP engine errors
        print(errorIndication)
    else:
        if errorStatus:  # SNMP agent errors
            print('%s at %s' % (errorStatus.prettyPrint(),
                  varBinds[int(errorIndex)-1] if errorIndex else '?'))
        else:
            for varBind in varBinds:  # SNMP response contents
                print(varBind.split('='))

            return varBind


iterator = getCmd(SnmpEngine(),
                  CommunityData('public'),
                  UdpTransportTarget(("172.17.11.94", 161)),
                  ContextData(),
                  ObjectType(ObjectIdentity('1.3.6.1.2.1.25.3.2.1.5')))

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
