
from flask import Flask, 

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)

   #number = int(request.args.get('num1'))
    #temp = number
    #rev = 0
    #while (number > 0):
        #dig = number % 10
        #rev = rev * 10 + dig
        #number = number // 10
    #if (temp == rev):
        #return "The number is a palindrome!"
    #else:
        #return "The number isn't a palindrome!"

        #create a routing rule
        #GET, POST, PUT, DELETE

        