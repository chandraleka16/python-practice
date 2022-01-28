import json
from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask('BookAPI')
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument('title', required=True)
parser.add_argument('category', required=False)

books = {
     "book1": {
        "title": "The Russian",
        "category": "fiction"

    },
    "book2": {
        "title": "The Vanishing Half",
        "category": "fiction"

    },
    "book3": {
        "title": "The Midnight Library",
        "category": "fiction"

    },
    "book4": {
        "title": "Viscount Who Loved Me",
        "category": "fiction"

    },
    "book5": {
        "title": "Just as I Am",
        "category": "non-fiction"
    },
    "book6": {
        "title": "Untamed",
        "category": "non-fiction"
    }
}

with open('books.json', 'r') as f:
    books = json.load(f)

def write_changes_to_file():
    global books
    # books = {k: v for k, v in sorted(books.items(), key=lambda book: book[1]['category'])}
    with open('books.json', 'w') as f:
        json.dump(books, f)

class BookSchedule(Resource):
    def get(self):
        return books
    
    def post(self):
        args = parser.parse_args()
        new_book = new_book = {"title": args["title"],
                    "category": args["category"]}
        book_id = max(int(b.lstrip('book')) for b in books.keys()) +1
        book_id =f"book{book_id}"
        books[book_id] = new_book
        write_changes_to_file()
        return books[book_id], 201

class Book(Resource):
    def get(self, book_id):
        if book_id == "all":
            return books
        if book_id not in books:
            return { "message": f"Book {book_id} not found!"}, 404
        return books[book_id], 201

    def put(self, book_id):
        args = parser.parse_args()
        new_book = {"title": args["title"],
                    "category": args["category"]}
        books[book_id] = new_book
        write_changes_to_file()
        return {book_id: books[book_id]}, 201

    def delete(self, book_id):
        if book_id not in books:
            return { "message": f"Book {book_id} not found!"}, 404
        del books[book_id]
        write_changes_to_file()
        return { "message": f"Book {book_id} deleted"}, 204


api.add_resource(Book, '/books/<book_id>')
api.add_resource(BookSchedule, '/books')
if __name__ == '__main__':
    app.run()