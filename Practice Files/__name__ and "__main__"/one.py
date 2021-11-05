#python one.py

def func():
	print("FUNCTION() in one.py")

print("TOP LEVEL IN ONE.PY")

if __name__ == "__main__": 
	print("ONE.PY is being run directly!")
else: 
	print("ONE.PY has been imported!")