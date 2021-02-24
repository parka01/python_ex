import matplotlib.pyplot as pyplot

years=[1950,1960,1970,1980,1990,2000,2010]
gdp=[67.0,80.0,257.0,1686.0,6505,11865.3,22105.3]

pyplot.plot(years,gdp,color='green',marker='o',linestyle='solid')
pyplot.title('GDP per capita')

pyplot.ylabel('dollars')
pyplot.savefig('gdp.png',dpi=300)
pyplot.show()