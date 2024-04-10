# Image: serenashah/ml-proj3-api

FROM python:3.11

RUN pip install tensorflow==2.15
RUN pip install Flask==3.0
COPY api.py /api.py
COPY models /models


CMD ["python", "api.py"]