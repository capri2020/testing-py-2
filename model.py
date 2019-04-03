from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""
    # FIXME: write a function that creates a game and adds it to the database.
    Game.query.delete()

    gm1 = Game(name='Monopoly', description='Board game using paper money')
    gm2 = Game(name='Candy Land', description='Simple racing board game')
    gm3 = Game(name='Angry Bird', description='Casual puzzle video game')
    gm4 = Game(name='Jewels', description='Matching gems')

    db.session.add_all([gm1, gm2, gm3, gm4])
    db.session.commit()
    
    # print("FIXME")


if __name__ == '__main__':
    from party import app

    connect_to_db(app)
    print("Connected to DB.")
