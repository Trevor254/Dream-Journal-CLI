from models import session, Category, Dream

def seed_database():
    # Clear existing data
    session.query(Dream).delete()
    session.query(Category).delete()
    
    # Creating categories
    lucid = Category(name="Lucid Dream")
    nightmare = Category(name="Nightmare")
    fantasy = Category(name="Fantasy")
    
    session.add_all([lucid, nightmare, fantasy])
    session.commit()

    # Creation of  dreams
    dream1 = Dream(title="Flying Above Cities", description="I was flying over a futuristic city.", category=lucid)
    dream2 = Dream(title="Chased by Shadows", description="Dark shadows were chasing me in a maze.", category=nightmare)
    dream3 = Dream(title="Talking Animals", description="I had a conversation with a talking cat.", category=fantasy)
    
    session.add_all([dream1, dream2, dream3])
    session.commit()

    print("Database seeded successfully!")

if __name__ == "__main__":
    seed_database()
