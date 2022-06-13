Why is it called Log4Shell

Put application url as input to the application to be logged by log4j

Analyse URL and log4j --> vulnerable application reaches malicious LDAP server looking for an exploit payload object

attacker's ldap server redirects vulnerable application to http://attackerserver.com/exploitpayload.class

vulnerable applocation load then executes. attacker gain remote code exec privileges


log4j intention is for this library to just save the log
but hackers use jndi to remote change and control


threats:
- social engineering
- ransomware
- ddos
- cryptojacking

trends
- biometrics
- blockchain
- cloud
- IoT
- mobile
- finance