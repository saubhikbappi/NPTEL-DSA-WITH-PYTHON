#What is the value of endmsg after executing the following lines?



startmsg = "hello"
endmsg = ""
for i in range(0,len(startmsg)):
    endmsg = startmsg[i]+endmsg
print(endmsg)


#OUTPUT--- ollehh