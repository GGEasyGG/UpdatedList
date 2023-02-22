FROM python:3.10

RUN pip install pipenv

RUN mkdir /root/Updated_List

WORKDIR /root/Updated_List

COPY Pipfile Pipfile.lock Updated_List.py Test.py ./

RUN pipenv install --system --deploy

ENTRYPOINT ["python", "Test.py"]
