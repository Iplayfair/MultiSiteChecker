FROM python
WORKDIR /home/app

COPY . /home/app

CMD ["python","/home/app/src/MultiSiteChecker_Classes.py"]