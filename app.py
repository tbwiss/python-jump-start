from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        'name': 'Green eggs and ham',
        'price': 7.99,
        'isbn': 3495738534
    },
        {
        'name': 'In the sky',
        'price': 12.33,
        'isbn': 34957385423
    }
]


def validBookObject(bookObject):
    if ('name' in bookObject and 'price' in bookObject and 'isbn' in bookObject):
        return True
    else:
      return False


# GET /books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({'books': books})


# GET /books/:isdn
@app.route('/books/<int:isbn>')
def get_book_by_isdn(isbn):
    return_value = {}
    for book in books:
        if book['isbn'] == isbn:
          return_value = {
            'name': book['name'],
            'price': book['price']
          }
    return jsonify(return_value)


# POST /books
@app.route('/books', methods=['POST'])
def add_book():
    return jsonify(request.get_json())


if __name__ == '__main__':
  app.run(port=5000)