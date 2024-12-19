from flask import Flask, request, jsonify, abort, render_template

app = Flask(__name__)
AUTH_TOKEN = 'securetoken'

# Temporary in-memory storage
books = []
members = []
book_id_counter = 1
member_id_counter = 1


@app.route('/')
def home():
    return render_template('index.html')


def require_auth():
    """Require authentication via the AUTH_TOKEN."""
    token = request.headers.get('Authorization')
    if token != AUTH_TOKEN:
        abort(403, description="Unauthorized")


@app.route('/books', methods=['GET'])
def get_books():
    """Retrieve books with optional search functionality."""
    require_auth()
    search = request.args.get('search', '').lower()
    filtered_books = [book for book in books if search in book['title'].lower() or search in book['author'].lower()]
    return jsonify(filtered_books)


@app.route('/books', methods=['POST'])
def create_book():
    """Add a new book."""
    global book_id_counter
    require_auth()
    data = request.json
    new_book = {
        "id": book_id_counter,
        "title": data['title'],
        "author": data['author'],
        "available": True
    }
    books.append(new_book)
    book_id_counter += 1
    return jsonify({"message": "Book added successfully"}), 201


@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    """Update book details."""
    require_auth()
    data = request.json
    for book in books:
        if book['id'] == id:
            book['title'] = data['title']
            book['author'] = data['author']
            return jsonify({"message": "Book updated successfully"})
    abort(404, description="Book not found")


@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    """Delete a book."""
    require_auth()
    global books
    books = [book for book in books if book['id'] != id]
    return jsonify({"message": "Book deleted successfully"})


@app.route('/members', methods=['GET'])
def get_members():
    """Retrieve all members."""
    require_auth()
    return jsonify(members)


@app.route('/members', methods=['POST'])
def create_member():
    """Add a new member."""
    global member_id_counter
    require_auth()
    data = request.json
    new_member = {
        "id": member_id_counter,
        "name": data['name'],
        "email": data['email']
    }
    members.append(new_member)
    member_id_counter += 1
    return jsonify({"message": "Member added successfully"}), 201


@app.route('/members/<int:id>', methods=['PUT'])
def update_member(id):
    """Update member details."""
    require_auth()
    data = request.json
    for member in members:
        if member['id'] == id:
            member['name'] = data['name']
            member['email'] = data['email']
            return jsonify({"message": "Member updated successfully"})
    abort(404, description="Member not found")


@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    """Delete a member."""
    require_auth()
    global members
    members = [member for member in members if member['id'] != id]
    return jsonify({"message": "Member deleted successfully"})


if __name__ == '__main__':
    app.run(debug=True)
