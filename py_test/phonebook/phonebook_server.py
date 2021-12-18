# A simple client-server phonebook
# - The program will load the data (name and phone number) from a text file
#   and start the server.
# - When the server receive a input name from the client, the server will look for
#   that name and return the phone number.
# - Make the server to handle multiple connections and process multiple request from
# - the clients.
import csv

class PhonebookServer:
    def __init__(self):
        self.data_list = list()

    def load_data_from_file(self):
        ''' Load data from CSV file and store in a list for '''
        with open('data.csv', mode='r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.data_list.append(row)

    def print_data(self):
        for data in self.data_list:
            print("Name: {}\nPhone: {}\n".format(data['name'], data['phone']))

    def run(self):
        self.load_data_from_file()
        self.print_data()

if __name__ == '__main__':
    server = PhonebookServer()
    server.run()
