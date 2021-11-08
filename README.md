```
export AWS_ACCESS_KEY_ID=<key_id>
export AWS_SECRET_ACCESS_KEY=<secret>
export AWS_DEFAULT_REGION=ap-southeast-2

brew install virtualenv
brew tap aws/tap
brew install aws-sam-cli
which python3.9

virtualenv -p /usr/local/bin/python3.9 ~/venv-sam-tut
source ~/venv-sam-tut/bin/activate
```