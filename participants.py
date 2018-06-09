from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Participant

engine = create_engine('sqlite:///competitionround2.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

#participants of category 1
category1 = Category(name = "Category 1: Juz 30")
session.add(category1)
session.commit()

participant1 = Participant(name="Aaliyah Naina", age = 10 ,category = category1)
session.add(participant1)
session.commit()

participant2 = Participant(name="Habiba Khan", age = 14, category = category1)
session.add(participant2)
session.commit()

participant3 = Participant(name="Sami Terra", age = 8, category = category1)
session.add(participant3)
session.commit()

participant4 = Participant(name="Mohammad Bhatti", age = 0 , category = category1)
session.add(participant4)
session.commit()



#participants of category 2
category2 = Category(name = "Category 2: Juz 29 and 30")
session.add(category2)
session.commit()

participant1 = Participant(name="Noor Khan", age = 14,category = category2)
session.add(participant1)
session.commit()

participant2 = Participant(name="Asma Sebkhaoui", age = 10, category = category2)
session.add(participant2)
session.commit()

participant3 = Participant(name="Hasnain Kaurejo", age = 0 , category = category2)
session.add(participant3)
session.commit()


#participants of category 3
category3 = Category(name = "Category 3: Juz 28, 29, and 30")
session.add(category3)
session.commit()

participant1 = Participant(name="Rashad Hattak", age = 8,category = category3)
session.add(participant1)
session.commit()

participant2 = Participant(name="Zakar Pirzada", age = 0, category = category3)
session.add(participant2)
session.commit()

participant3 = Participant(name="Ibraheem Ropri", age = 0, category = category3)
session.add(participant3)
session.commit()


#participants of category 4
category4 = Category(name = "Category 4: Quarter of the Qur'an")
session.add(category4)
session.commit()

participant1 = Participant(name="Abdelrahman Sherif Mohamed", age = 0,category = category4)
session.add(participant1)
session.commit()

participant2 = Participant(name="Tnzil Abdalla", age = 13, category = category4)
session.add(participant2)
session.commit()

participant3 = Participant(name="Mohammed Azfar Bin Mohammed Azman", age = 0, category = category4)
session.add(participant3)
session.commit()

#participants of category 10
category10 = Category(name = "Category 10: Best Recitation")
session.add(category10)
session.commit()

participant1 = Participant(name="Zakar Pirzada", age = 0,category = category10)
session.add(participant1)
session.commit()

participant2 = Participant(name="Aaliyah Naina", age = 10 , category = category10)
session.add(participant2)
session.commit()

participant3 = Participant(name="Ali Bawla", age = 7, category = category10)
session.add(participant3)
session.commit()

print "participants added!"
