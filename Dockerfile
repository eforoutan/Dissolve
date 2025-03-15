FROM python:3.9-slim

RUN pip install geopandas

WORKDIR /app

COPY dissolve_shp.py /app/dissolve_shp.py

ENTRYPOINT [ "python3", "/app/dissolve_shp.py" ]