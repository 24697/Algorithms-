import networkx as nx

test = nx.Graph()
test.add_edge('Kevin Bacon','Lasco Atkins')
test.add_edge('Kevin Bacon','Scott Cann')
test.add_edge('Kevin Bacon','Richard Frice')
test.add_edge('Kevin Bacon','James McAvoy')
test.add_edge('Kevin Bacon','Michael Fassbender')
test.add_edge('Kevin Bacon','David Crow')

test.add_edge('Lasco Atkins','Noomi Rapace')

test.add_edge('Scott Cann','Vicent Cassel')

test.add_edge('Richard Frice','Rasario Dawson')

test.add_edge('James McAvoy','Vicent Cassel')
test.add_edge('James McAvoy','Rasario Dawson')

test.add_edge('Michael Fassbender','Noomi Rapace')
test.add_edge('Michael Fassbender','Idris Elba')

test.add_edge('David Crow','Idris Elba')


print(nx.neighbors(test,'Kevin Bacon'))
print(nx.degree(test,'Kevin Bacon'))
