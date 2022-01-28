
from email import header
from wsgiref import headers


try:

    import unittest
    from run import app

except Exception as e:
    print("Some Modules are Missing {} ".format(e))

class FlaskTest(unittest.TestCase):
    def test_get_books(self):
        tester = app.test_client(self)
        response = tester.get("/books")
        status_code = response.status_code
        # self.assertEqual(status_code, 200)
        self.assertEqual(response.content_type, "application/json")
    
    def test_put_book(self):
        tester = app.test_client(self)
        data = {"title": "test book"}
        response = tester.put("/books/book9", data=data)
        status_code = response.status_code
        print(response)
        self.assertEqual(status_code, 201)
    
    def test_post_book(self):
        tester = app.test_client(self)
        data = {"title": "test book"}
        response = tester.post("/books", data=data)
        print(response)
        status_code = response.status_code
        self.assertEqual(status_code, 201)
    
    def test_delete_book(self):
        tester = app.test_client(self)
        response = tester.delete("/books/ghkk")
        print(response)
        status_code = response.status_code
        self.assertEqual(status_code, 404)

if __name__ == '__main__':
    unittest.main()