# importing some modules
import requests
from bs4 import BeautifulSoup
import lxml
import smtplib



# constant
URL_OF_THE_WEB = 'https://www.startech.com.bd/lg-lg34wk95u-w-ultrawide-5k2k-ips-led-monitor'

PRICE = []

MY_GMAAIL ="rpg736tanvir@gmail.com"
MY_PASSWORD ="01955005706#@"
MAIL_RECIVER ="tanzin736@gmail.com"
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587


# main program will start from here

def find_the_price(soup) -> int:
    price_of_the_product = soup.find(name='span',class_='price').getText().split(',')
    print(price_of_the_product)
    result = price_of_the_product[1].split('৳')[0]
    solve = price_of_the_product[0]
    PRICE.append(solve)
    PRICE.append(result)
    print("".join(PRICE))
    real_price = int("".join(PRICE))/85
    return real_price

# creating another method that will hendle the mailing
def send_the_mail(mail,message):
    # now i am going to conenct with the mail server
    with smtplib.SMTP(MAIL_SERVER,port=MAIL_PORT) as connection:
        # for the secure connection
        connection.starttls()
        # we are going to login to our account
        connection.login(user=MY_GMAAIL,password=MY_PASSWORD,initial_response_ok=True)
        # now I am going to send mail
        connection.sendmail(from_addr=MY_GMAAIL,to_addrs=mail,msg=f"Subject:Startech Price Alert!\n\n\n{message}")
    print("Mail is sended...!!")


# for the calculation of the price
def isLowerd(price) -> bool:
    if price<1000:
        return True
    else:
        return False


# now lets send a request to the url
response = requests.get(url=URL_OF_THE_WEB)

# check the response with print
print(response.status_code)

# now we are going to triger an error if something goes wrong
response.raise_for_status()

# now i am going to print out the html 
data = response.text

# now i am going to create the instance of the bs4 object
soup = BeautifulSoup(data,'html.parser')

# print(soup.title.string)
price = find_the_price(soup)
title = soup.title.string
message = f"the Price rate of {title} is decresed to :{price}$"

# now we are going to check if the
# price is lowerd or not
if isLowerd(price):
    send_the_mail(MAIL_RECIVER,message)
else:
    print("The prices isn't decreased...!!")
    pass