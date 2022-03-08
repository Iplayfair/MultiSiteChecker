FROM python
COPY requirements.txt /home/app/requirements.txt
WORKDIR /home/app

COPY . /home/app

CMD ["python","/home/app/src/MultiSiteChecker_Classes.py"]