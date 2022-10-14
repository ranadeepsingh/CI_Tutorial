## Continuous Integration Tutorial with Github Actions

#### Setup:
```bash
git clone https://github.com/ranadeepsingh/CI_Tutorial.git

python -m pip install -r requirements.txt
```

#### Run PyTest:

```bash
coverage run -m pytest 
coverage report -m 
```

To Save and See Reports:
```bash
coverage run -m pytest | tee reports/unittest_report.txt
coverage report -m | tee reports/coverage_report.txt
coverage html
```


