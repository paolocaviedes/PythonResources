from SparkModule import SendSparkMessage,SeeSparkRooms,SeeSparkTokens,listSparkMessages,seeMessagesId,deleteMessage


Token="MmRhNTAyMTAtOGJkOS00NDE2LTgwZGQtYWYyNDIyOTY3YTA0ODQyODA3MTEtMzdh"
TokenBot="OTIxMjg0ZDYtM2NmMy00NDA4LWI4NDgtYmIzN2U2MTkyYjQ5MGUzNTEwYzktOWQ2"
TokenTeam="Y2lzY29zcGFyazovL3VzL1JPT00vMzFjODE4YTAtNDc3ZC0xMWU2LTg0YWMtOGYxZDhjMGU0YTNk"
Tokengabo="Y2lzY29zcGFyazovL3VzL1JPT00vNmMyZWJkODctYTViMi0zMDM1LTg2NTItODUwMTViMDM4NDg4"
mitoken= "ZTVmYWMwODAtYWJkNS00NzM2LWI1NGUtODY4NWZhYjE0NTk2YzhmYjQ3ZDUtMTI2"
tokenhienglish="NzZhYjljMTktYTNmNi00MWFmLTg4ZmUtNzQ1OTE5ZDU5YjE4MDk4NDBkOGYtZTY1"
tokenint='Y2lzY29zcGFyazovL3VzL1JPT00vMDI5YTU4MjAtNWQ4Mi0xMWU2LTg0MWYtYzc2ZWQ1NjgyYzg0'
#IdRoom="Y2lzY29zcGFyazovL3VzL1JPT00vMTQ1NWQyNDYtMTdkMS0zYzJmLThkZjAtNTQ3ZTVlNTFkMTEw"
#IdRoom="Y2lzY29zcGFyazovL3VzL1JPT00vODRkOWY1YTgtYjU5Ni0zNDRkLWFlMzAtY2ZkODcwOTdlNWQ2"

SendSparkMessage(Token,Tokengabo,"11 de agosto")


"""
rooms= SeeSparkRooms(mitoken)

for room in rooms:
	print room
"""

"""
identificadores= SeeSparkTokens(tokenhienglish)

for tupla in identificadores:
	print tupla
"""
"""
lista=SeeSparkTokens(mitoken)
for tupla in lista:
	print str(tupla)+"\n"
"""
"""
lista=seeMessagesId(mitoken,Tokengabo)
for ide in lista:
	print ide
"""
#print deleteMessage(mitoken,"Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMDlmZTUzYTAtNWQ3OC0xMWU2LWFiNmUtYmQyYmIwZGI5OTc3")
