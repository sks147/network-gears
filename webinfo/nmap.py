import os

#nmap -options -target server ip
def get_nmap(options, ip):
  command = "nmap "+options+" "+ip
  process = os.popen(command)
  results = str(process.read())
  return results
