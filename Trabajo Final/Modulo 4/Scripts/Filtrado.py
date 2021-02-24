import pandas as pd
airbnb = pd.read_csv("./data/pandas/airbnb.csv")
print(airbnb)

# ordenar por puntacion mas de 4
#de mayor a menor
#mostrar las que tienen mas reviews
x= airbnb[(airbnb.overall_satisfaction>= 4)]
x

y= x.sort_values(by=['reviews'], ascending = False)
y.head(3)

x= airbnb [(airbnb.room_id== 97503)]
print(x)

y= airbnb [(airbnb.room_id== 90387)]
print(y)

airbnb = pd.read_csv("./data/pandas/airbnb.csv")
x= airbnb[(airbnb.price<=50)]
y= x[(x.room_type == 'Shared room')]
z=y.sort_values(by=['overall_satisfaction'], ascending = False)
print(z.head(10))
