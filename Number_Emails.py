import pandas as p
def name(data): 
    name_col=data.get('Name')  
    list_of_name=list(name_col) 
    print(list_of_name)
def number(data):
    number_col=data.get('Number')
    list_of_Number=list(number_col)   
    print(list_of_Number) 

def email(data):
    email_col=data.get('Email')
    Emails=list(email_col)
    print(Emails)

if __name__ == '__main__':
    data = p.read_excel("Files//Email_numbers.xlsx")
    name(data)
    number(data)
    email(data)
    


