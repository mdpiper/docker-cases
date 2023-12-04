import pymt

print("pymt version = {}".format(pymt.__version__))
for model in pymt.MODELS:
    print(model)

m = pymt.MODELS.PRMSSurface()
print("pymt component: " + m.name)
