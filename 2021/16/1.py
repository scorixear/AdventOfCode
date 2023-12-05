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
  versionNumberSum += version
  type = getPacketType(packet)
  if type == 4:
    literalValue, usedBits = getLiteralValue(packet)
    print(f"{spaces}[{version}] [{type}] [{literalValue}]")
    return usedBits
  else:
    subStr, lengthType, endOfString = getSubPackets(packet)
    print(f"{spaces}[{version}] [{type}] [{lengthType}] [{endOfString}]")
    if lengthType:
      startIndex = 0
      while startIndex < len(subStr):
        startIndex += decodePacket(subStr[startIndex:], spaces + "  ")
      return 22 + endOfString
    else:
      startIndex = 0
      for i in range(endOfString):
        startIndex += decodePacket(subStr[startIndex:], spaces + "  ")
      return 18 + startIndex

versionNumberSum = 0

decodePacket(binaryString, "")

print("\nSum:", versionNumberSum)