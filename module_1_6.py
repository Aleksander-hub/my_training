

my_dict={'Sonia':2000,'Sasha':2010,'Masha':2015}
print(my_dict['Sonia'])
my_dict['Sonia']=12345
my_dict['Vasia']=1990#не существующий
my_dict.update({'Ira':2003,'Tania':1985})
print(my_dict)
del my_dict['Masha']
print(my_dict)

my_set={'a':1,'b':2,'c':3}
print(my_set['c'])
my_set.update({'d':4,'e':5})
print(my_set)
del my_set['b']
print(my_set)