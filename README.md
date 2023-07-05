# Combined-scanner
Just a scanning script that founding fingerprints that lead to vulnerabilities. Concluded from daily works
Issues welcomed!

# Disclaimer
By using this script, you should obey the laws and rules of your current countries or regions, illegal cyber attacks may lead to serious crimes.

This project does not responsible or encourage for any illegal cyber attacks

This project is aiming for authorized penetration tests, security construction of business companies or cybersecurity researches.

# Abilities

- Scanning XXL-JOB Admin Center,unauthorized access of Admin Center API(XXL-JOB<2.0.2), unauthorized access of XXL-JOB Executors
- Scanning unauthorized access of Flink Console
- Scanning unauthorized access of k8s api
- Scanning unauthorized access of swagger documents
- Scanning nacos console

# Preparation
  pip3 install -r requirements

# Usage
  - Single Target mode:
  python3 main.py -t [url]

  - Multi Targets mode:
  > python3 main.py -f [filepath]

  - Target File example:
  > http://test.com
>  
  > https://test1.com

You may check the result.txt under the script folder after scanning.


# Thanks

Inspired by Rabbitmask's scanning script, convert it into the usage of other vulns

Refers to:

https://github.com/rabbitmask/SB-Actuator
