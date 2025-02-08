# Flashcards App

## Project Overview

This Django-based backend application allows users to create, manage, and use flashcards as a learning tool.  [the Leitner system] help with memorizing topics or learning new languages by presenting questions on one side and answers on the other in flashcards. The app organizes cards into boxes, and users can test themselves by flipping through the flashcards.

---

## Features

- **Create Flashcards:** Add new cards with questions and answers.
- **Edit Flashcards:** Update existing card content as needed.
- **Organize by Box:** Cards are categorized by boxes to support the spaced repetition learning technique.
- **Check Card Progress:** Mark cards as solved or unsolved to promote better memorization.
- **Random Card Selection:** Review a random card from a specific box.

---

## Project Structure

### Card Model

- **Methods:**
    - `move(self, solved)`: Moves the card to the next box if solved, or resets it to the first box.
    - `__str__(self)`: Returns a string representation of the flashcard (e.g., showing the question).

---

### Views

This app uses Django **class-based views (CBVs)** to handle requests and responses efficiently.

- **CardListView:** Displays a list of all flashcards ordered by box.
    - Inherits from `ListView`
    - Provides `get_queryset()` to retrieve and order all cards by their box.
- **CardCreateView:** Provides a form to create new flashcards.
    - Inherits from `CreateView`
    - Automatically redirects to the creation page upon success.
- **CardEditView:** Allows updating existing flashcards.
    - Inherits from `UpdateView`
    - Redirects to the card list after a successful edit.
- **BoxView:** Displays cards for a specific box and selects one at random for testing.
    - Inherits from `ListView`
    - Methods include:
        - `get_queryset()`: Retrieves cards for a specific box.
        - `get_context_data()`: Adds context including the box number and a randomly selected card.
        - `post()`: Handles form submission to mark cards as solved or unsolved and move them to the appropriate box.

---

### Usage Instructions

1. Navigate to `http://localhost:8000/card-list` to view all cards.
2. Create a new card at `http://localhost:8000/create-card`.
3. Edit existing cards by visiting `http://localhost:8000/edit-card/<card-id>`.
4. Test your memory using `http://localhost:8000/box/<box-number>`.

---

## Setup Instructions

1. **Clone the repository:**
    
    ```bash
    git clone <repository-url>
    cd <repository-folder>
    
    ```
    
2. **Install dependencies:**
    
    ```bash
    pip install -r requirements.txt
    ```
    
3. **Apply migrations:**
    
    ```bash
    python manage.py migrate
    ```
    
4. **Run the server:**
    
    ```bash
    python manage.py runserver
    ```
    
5. **Access the app:** Open [http://localhost:8000](http://localhost:8000/) in your browser.

---

## Future Improvements

- User authentication for personalized flashcard sets.
- Advanced statistics on user performance.
- Support for multimedia cards.

---

## Contribution Guidelines

Feel free to fork the project and submit pull requests for improvements or new features. Please ensure all changes are properly documented.