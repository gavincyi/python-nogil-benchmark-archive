FROM nogil/python

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY requirements-test.txt ./
RUN pip install --no-cache-dir -r requirements.txt -r requirements-test.txt

COPY . .

CMD [ "python", "--version" ]
