FROM python 

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt

CMD [ "pytest", "./tests/test_const_mock.py", "./tests/test_slowdown_class.py", "./tests/test_slowdown_func.py"]