from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(id,name,price,description,picture_link):
	    product_object = Product(
	    Id=Id,
        name=name,
        price=price,
        description=description,
        picture_link=picture_link)
    session.add(product_object)
    session.commit()

add_product(1,"vansclassic",49.99,"https://images.vans.com/is/image/Vans/D3HY28-HERO?$583x583$")
add_product(2,"vansskate",59.99,"idk")


def update_product_price(Id,price):
ther or not they have finished the lab

   product_object = session.query(
       Product).filter_by(
       Id=Id)
   product_object.price = price
   session.commit()


   update_product_price(1,39.99)


   def delete_product(Id):

   session.query(Product).filter_by(
       Id=Id).delete()
   session.commit()

delete_product(2)

def query_all():

   Products = session.query(
      Product).all()
   return Products


print(query_all())


def query_by_id(Id):
	product = session.query(
		Product).filter_by(
		Id=Id)
	return product
print(query_by_id(1))


def add_to_cart(productID):
	session.query(cart).filter_by(productID=productID).add()

    session.commit()
