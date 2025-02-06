from db.models import session, Dream, Category

def main_menu():
    while True:
        print("\nDream Journal CLI")
        print("1. Add a Dream")
        print("2. View All Dreams")
        print("3. Find a Dream by Title")
        print("4. Delete a Dream")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_dream()
        elif choice == "2":
            view_all_dreams()
        elif choice == "3":
            find_dream()
        elif choice == "4":
            delete_dream()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

def add_dream():
    title = input("Enter dream title: ").strip()
    description = input("Enter dream description: ").strip()

    categories = session.query(Category).all()
    if not categories:
        print("No categories found. Please add categories in the database first.")
        return

    print("Choose a category:")
    for category in categories:
        print(f"{category.id}. {category.name}")

    category_id = input("Enter category ID: ").strip()

    # Validate category selection
    category = session.query(Category).filter_by(id=category_id).first()
    if not category:
        print("Invalid category ID. Returning to main menu.")
        return

    new_dream = Dream(title=title, description=description, category=category)
    session.add(new_dream)
    session.commit()

    print(f"Dream '{title}' added successfully!")

def view_all_dreams():
    dreams = session.query(Dream).all()
    if not dreams:
        print("No dreams found.")
        return

    print("\nAll Dreams:")
    for dream in dreams:
        print(f"- {dream.id}: {dream.title} ({dream.category.name})")
        print(f"  Description: {dream.description}")
        print(f"  Date: {dream.date}\n")

def find_dream():
    title = input("Enter the dream title to search for: ").strip()
    dream = session.query(Dream).filter(Dream.title.ilike(f"%{title}%")).first()

    if dream:
        print(f"\nFound Dream: {dream.title} ({dream.category.name})")
        print(f"Description: {dream.description}")
        print(f"Date: {dream.date}\n")
    else:
        print("No dream found with that title.")

def delete_dream():
    dream_id = input("Enter the dream ID to delete: ").strip()
    
    dream = session.query(Dream).filter_by(id=dream_id).first()
    if not dream:
        print("Dream not found.")
        return

    session.delete(dream)
    session.commit()
    print(f"Dream '{dream.title}' deleted successfully.")

if __name__ == "__main__":
    main_menu()
