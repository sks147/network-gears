import os

def get_ip_address(url):
  command = "host "+url
  #runs the terminal command host
  process = os.popen(command)
  #runs the command on terminal
  result = str(process.read())
  #save the output in variable result
  marker = results.find('has address')
  return results[marker:].splitlines()[0]
  #get the topmost result ip
