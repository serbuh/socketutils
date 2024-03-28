python setup.py bdist_wheel
python -m pip install .\dist\socketutils-0.0.2-py3-none-any.whl --force-reinstall
python test.py