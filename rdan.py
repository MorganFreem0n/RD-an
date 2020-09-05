import requests
import os
import sys
import time
from colored import fg, bg, attr
tokens = []
funcs = []
Vars = []
def Start(filename):
  time.sleep(2)
  f = open(filename + '.rdan')
  for line in f:
    if line.startswith("print "):
      print(line.split(" ", 1)[1])
      tokens.append("print")

 
    
    if line.startswith("spam "):
      tokens.append("spam")
      while True:
        print(line.split(" ", 1)[1])

    if line.startswith("// "):
      tokens.append("//")

    if line.startswith("writeImage "):
      img = line.split(" ", 1)[1]
      name = line.split(" ", 2)[2]
      r = requests.get(img)
      tokens.append("writeImage")
      with open(name, 'wb') as qs:
        qs.write(r.content)

    if line.startswith("warn "):
      text = line.split(" ", 1)[1]
      print(fg("light_yellow"), text)
      tokens.append("warn")

    if line.startswith("error "):
      text = line.split(" ", 1)[1]
      print(fg("red"), text)
      tokens.append("error")

    if line.startswith("info "):
      text = line.split(" ", 1)[1]
      print(fg("light_blue"), text)
      tokens.append("info")

    if line.startswith("exit"):
      sys.exit() 
      tokens.append("exit")

    if line.startswith("wait "):
      Time = line.split(" ", 1)[1]
      time.sleep(int(Time))
      tokens.append("wait")
    # Var create
    if line.startswith("var.create "):
      var_name = line.split(" ")[1]
      contents = line.split(" ", 2)[2]
      Vars.append(var_name + " : " + contents)
      tokens.append("var.create")

    if line.startswith("input.get "):
     in_put = input(line.split(" ", 1)[1])
     tokens.append("input.get")
    
    if line.startswith("input.print "):
      print(in_put)
      tokens.append("input.print")


    if line.startswith("var.print "):
      varp = line.split(" ")[1]
      for object in Vars:
        if str(object).split(" : ")[0] == varp:
          print(str(object).split(" : ")[1])
      tokens.append("var.print")

    if line.startswith(". "):
      func_name = line.split(" ")[1]
      code = line.split(" ", 2)[2]
      tokens.append(".")
      funcs.append(func_name + ":" + code)

    
def lex(filename):
  time.sleep(3)
  f = open(filename + '.rdan')
  for line in f:
    check = line.split(" ")[0]
    if check not in tokens:
      if line == "\n":
        pass
      else:
        print(fg("red"), "Invalid: " + line)
        print(" ")
        sys.exit()
def debug():
  print(tokens)
# look at this fuggin clown