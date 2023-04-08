# RUN
pytest Naufal.py -v
pytest Naufal.py -v -s
pytest Naufal.py -v --html=report.html
python3 -m pytest -s -v mobile_setup.py
pytest -p no:warnings -s -v mobile_setup.py