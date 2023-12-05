import os, sys, re, time
inputText = open(os.path.join(sys.path[0], 'input'), 'r')
lines = inputText.readlines()

binaryString = ""
for i in range(0, len(lines[0].strip()), 2):
  binaryString += bin(int(lines[0].strip()[i:i+2], 16))[2:].zfill(8)

def getBinaryLength(length):
  if length% 4 > 0:
    return length + (3-((length)%4))
  return length

def getPacketVersion(packet):
  return int(packet[:3],2)
def getPacketType(packet):
  return int(packet[3:6],2)
def getLiteralValue(packet):
  bitString = ""
  startIndex = 6
  while True:
    currentBitString = packet[startIndex+1: startIndex+5]
    bitString += currentBitString
    if packet[startIndex:startIndex+1] == "0":
      break
    startIndex += 5
  return (int(bitString, 2), startIndex+5)
def getSubPackets(packet):
  lengthType: bool = packet[6:7] == "0"
  number = int(packet[7:7+(15 if lengthType else 11)], 2)
  returnStr = ""
  if (lengthType):
    returnStr = packet[22:22+number]
  else:
    returnStr = packet[18:]
  return (returnStr, lengthType, number)


def decodePacket(packet, spaces):
  global versionNumberSum
  if len(packet)<6:
    return len(packet)
  version = getPacketVersion(packet)
  type = getPacketType(packet)
  if type == 4:
    literalValue, usedBits = getLiteralValue(packet)
    print(f"{spaces} [{literalValue}]")
    return (usedBits, literalValue)
  else:
    subStr, lengthType, endOfString = getSubPackets(packet)
    
    returnCounter = 0
    values = []
    if lengthType:
      startIndex = 0
      while startIndex < len(subStr):
        current, value = decodePacket(subStr[startIndex:], spaces + "  ")
        startIndex += current
        values.append(value)
      returnCounter = 22 + endOfString
    else:
      startIndex = 0
      for i in range(endOfString):
        current, value = decodePacket(subStr[startIndex:], spaces + "  ")
        startIndex += current
        values.append(value)
      returnCounter = 18 + startIndex
    if type == 0:
      print(f"{spaces} +")
      return (returnCounter, sum(values))
    if type == 1:
      product = 1
      for value in values:
        product *= value
      print(f"{spaces} *")
      return (returnCounter, product)
    if type == 2:
      print(f"{spaces} min")
      return (returnCounter, min(values))
    if type == 3:
      print(f"{spaces} max")
      return (returnCounter, max(values))
    if type == 5:
      print(f"{spaces} >")
      return(returnCounter, 1 if values[0]>values[1] else 0)
    if type == 6:
      print(f"{spaces} <")
      return(returnCounter, 1 if values[0]<values[1] else 0)
    if type == 7:
      print(f"{spaces} ==")
      return(returnCounter, 1 if values[0] == values[1] else 0)

counter, value = decodePacket(binaryString, "")
print("Result =", value)