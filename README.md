# Continuous Integration Tutorial with Github Actions

## Setup:
```bash
git clone https://github.com/ranadeepsingh/CI_Tutorial.git

python -m pip install -r requirements.txt
```

## Run PyTest:
main.py - It has the code that needs to be tested \
test_main.py - has the tests for the code

```bash
coverage run -m pytest | tee reports/unittest_report.txt
coverage report -m | tee reports/coverage_report.txt
coverage html
```

## Model Training and Evaluation
```bash
python main.py | tee reports/model_train_report.txt

python offline_eval.py | tee reports/offline_evaluation_report.txt
```

## Continuous Integration with Github Actions

See the .github/workflows
Any yml file there is an automated testing workflow.
Output can be seen in Repository's "Actions" Tab

Files:
* push_ci.yml - Runs PyTest and integration test on every push and pull request
* test_model.yml - Run model trainign and evaluation every n hours or days as specified by Cron job. See Cron time format [here](https://www.pair.com/support/kb/paircloud-using-cron/).

