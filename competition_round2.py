from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Participant

engine = create_engine('sqlite:///competitionround2.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

app = Flask(__name__)

#show all categories
@app.route('/')
@app.route('/categories')
def showCategories():
    categories = session.query(Category).all()
    return render_template('categories.html', categories = categories)
#show participants of a Category
@app.route('/categories/<int:category_id>/participants')
@app.route('/categories/<int:category_id>')
def showParticipants(category_id):
    category = session.query(Category).filter_by(id = category_id).one()
    participants = session.query(Participant).filter_by(category_id = category_id).all()
    return render_template('participants.html', category = category, participants = participants)

#Rubric for Each category
@app.route('/categories/<int:category_id>/participants/<int:participant_id>/rubric', methods = ['GET', 'POST'])
def rubricCategory(category_id, participant_id):
    category = session.query(Category).filter_by(id = category_id).one()
    participant = session.query(Participant).filter_by(id = participant_id).one()
    if category.id == 1:
        return render_template('rubric1.html', participant = participant, category = category)
    if category.id == 2:
        return render_template('rubric1.html', participant = participant, category = category)
    if category.id == 3:
        return render_template('rubric2.html', participant = participant, category = category)
    if category.id == 4:
        return render_template('rubric2.html', participant = participant, category = category)
    if category.id == 5:
        return render_template('rubric3.html', participant = participant, category = category)

if __name__ == '__main__':
    app.debug = True
    app.run()
