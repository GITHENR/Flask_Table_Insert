from flask import Flask, render_template
from azure.storage.table import TableService, Entity

table_service = TableService(account_name='cloudshell340965605', account_key='OB0MNBHAL4EEDPbUleI3vuEjTGsEzmB82BZiCFXjPJRhzNFp6+g9kM0YPeWgPzydVnhUQy1MiXqNzJVvnHnQ6w==')
task = {'PartitionKey': 'First', 'RowKey': '1000',
        'description': 'customer1', 'priority': 200}
table_service.update_entity('customer', task)
app = Flask(__name__)


@app.route("/")
def index():
    return "hi from home page"

@app.route("/user/<name>")
def profile(name):
    task = {'PartitionKey': 'First', 'RowKey': '1000','description': 'product1', 'priority': 200}
    table_service.insert_entity('product', task)
    return render_template('hello.html', name=name)

if __name__ == "__main__":
    app.run()