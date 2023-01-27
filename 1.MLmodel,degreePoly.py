import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)
from sklearn.model_selection import train_test_split
x = numpy.random.normal(3,1,100)
print(x)
y = numpy.random.normal(150,40,100)/x
print(y)

plt.scatter(x,y)
plt.show()

train_x, test_x, train_y, test_y = train_test_split(x,y,test_size=0.3)

plt.scatter(train_x,train_y)
plt.show()

plt.scatter(test_x,test_y)
plt.show()

# Draw a Polynomial Regression line through the data points with training data
mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))
myline = numpy.linspace(0,6,100)
plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()

# Draw a Polynomial Regression line through the data points with test data
mymodel = numpy.poly1d(numpy.polyfit(test_x, test_y, 4))
myline = numpy.linspace(0,6,100)
plt.scatter(test_x, test_y)
plt.plot(myline, mymodel(myline))
plt.show()

#It measures the relationship between the x axis and y axis
#where 0 means no relationship, and 1 means totally related.
import numpy
from sklearn.metrics import r2_score
numpy.random.seed(2)
r2 = r2_score(train_y, mymodel(train_x))
print(r2)

#Predict the values
#Now that we have established that our model is OK, we can start prediction
print(mymodel(5))
