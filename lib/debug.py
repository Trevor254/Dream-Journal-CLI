from db.models import initialize_db, session, Dream, Category

def verify_data():
    # Fetch all categories
    categories = session.query(Category).all()
    print("\nCategories:")
    for category in categories:
        print(f"- {category.id}: {category.name}")

    # Fetch all dreams
    dreams = session.query(Dream).all()
    print("\nDreams:")
    for dream in dreams:
        print(f"- {dream.id}: {dream.title} ({dream.category.name})")
        print(f"  Description: {dream.description}")
        print(f"  Date: {dream.date}\n")

if __name__ == "__main__":
    initialize_db()  # This ensures the database schema is in place
    verify_data()    # This checks the seeded data


# if __name__ == "__main__":
#     initialize_db()
#     print("Database and tables created successfully!")

# test to verify data in database
