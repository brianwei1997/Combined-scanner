# Combined-scanner
Just a scanning script that founding fingerprints that lead to vulnerabilities. Concluded from daily works

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
