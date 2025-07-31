from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from controller.user import User
from controller.account import Account
from controller.transaction import Transaction
from lib.check_password import check_user
from lib.update_money import less_money_account, more_money_account
from model.handle_db import HandleAccounts
from middleware.error_handler import ErrorHandler

app = FastAPI()

template = Jinja2Templates(directory="./view")

app.add_middleware(ErrorHandler)

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return template.TemplateResponse("index.html", {"request": request})

@app.get("/new-home", response_class=HTMLResponse)
def service_home(request: Request):
    return template.TemplateResponse("new_home.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
def root(request: Request):
    return template.TemplateResponse("index.html", {"request": request})

@app.post("/new-home", response_class=HTMLResponse)
def root(request: Request):
    return template.TemplateResponse("new_home.html", {"request": request})

@app.get("/signup", response_class=HTMLResponse)
def signup(request:Request):
    return template.TemplateResponse("signup.html", {"request":request})

@app.get("/user", response_class=HTMLResponse)
def user(req:Request):
    return RedirectResponse("/")

@app.get("/accounts", response_class=HTMLResponse)
def account(request:Request):
    return template.TemplateResponse("accounts.html", {"request":request})

@app.get("/transactions", response_class=HTMLResponse)
def transaction(request:Request):
    return template.TemplateResponse("transactions.html", {"request":request})

@app.get("/get_money", response_class=HTMLResponse)
def get_money(request:Request):
    return template.TemplateResponse("get_money.html", {"request":request})

@app.get("/money", response_class=HTMLResponse)
def money(request:Request):
    return RedirectResponse("/new-home")

@app.get("/update_money", response_class=HTMLResponse)
def update_money(request:Request):
    return template.TemplateResponse("update_money.html", {"request":request})

@app.post("/user", response_class=HTMLResponse)
def user(request:Request, username:str=Form(), password_user:str=Form() ):
    verify = check_user(username, password_user)
    if verify:
        return template.TemplateResponse("new_home.html", {"request":request, "data_user":verify})
    return RedirectResponse("/") #Esto significa que la contraseña fue incorrecta

@app.post("/data-processing", response_class=HTMLResponse)
def data_processing(firstname:str=Form(), lastname:str=Form(), username:str=Form(), country:str=Form(), password_user:str=Form()):
    data_user = {
        "firstname":firstname,
        "lastname":lastname,
        "username": username,
        "country": country,
        "password_user": password_user
    }
    db = User(data_user)
    db.create_user()
    return RedirectResponse("/")

@app.post("/account-processing", response_class=HTMLResponse)
def account_processing(type_account:str=Form(),money_account:str=Form() ,password_account:str=Form()):
    data_account = {
        "type_account":type_account,
        "money_account":money_account,
        "password_account":password_account
    }
    db = Account(data_account)
    db.create_account()
    return RedirectResponse("/new-home")

@app.post("/transaction-processing", response_class=HTMLResponse)
def transaction_processing(type_account:str=Form(),id_receive:str=Form(), money_transaction:str=Form(), password_account:str=Form()):
    data_transaction = {
        "id_receive":id_receive,
        "money_transaction":money_transaction
    } #Aqui se hace la misma validacion de contrasena y del dinero de la cuenta
    verify_money = less_money_account(money_transaction, type_account, password_account)
    if verify_money:
        db = Transaction(data_transaction)
        db.create_transaction()
        return RedirectResponse("/new-home") #Aqui la transaccion fue realizada con exito
    elif verify_money == None:
        return "No tiene el suficiente dinero para realizar la transaccion"
    elif verify_money == False:
        return "Contraseña incorrecta"

@app.post("/get_money", response_class=HTMLResponse)
def get_money(request:Request, type_account:str=Form()):
    account = HandleAccounts()
    money_account = account.get_only_account(type_account)
    return template.TemplateResponse("money.html", {"request":request, "data_account":money_account})

@app.post("/update_money", response_class=HTMLResponse)
def transaction_processing(type_account:str=Form(), money_in:str=Form() ,password_account:str=Form()):
    verify_money = more_money_account(money_in, type_account, password_account)
    if verify_money:
        return RedirectResponse("/new-home") #Aqui el ingreso fue realizado con exito
    elif verify_money == False:
        return "Contraseña incorrecta"
    