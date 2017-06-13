echo "Tests should not be run pathpipe-farm3" 
python3 -m unittest discover -s prokka/tests/ -p '*_test.py'
