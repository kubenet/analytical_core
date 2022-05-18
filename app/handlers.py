from fastapi import APIRouter, Body, Depends
from app.forms import UserLoginForm
from app.models import connect_db

router = APIRouter()


@router.get('/')
def index():
    return {"Status": "OK"}


@router.get('/login', name='user: login')
def login():
    return {"Login": "null"}


@router.post('/login', name='user: login')
def login(user_form: UserLoginForm = Body(..., embed=True), database=Depends(connect_db)):
    return {"Login": "null"}


@router.post('/logout', name='user: logout')
def logout():
    return {"Logout": "OK"}


@router.get('/user', name='user: ')
def user():
    return {"Status user get": "OK"}


@router.post('/user')
def user():
    return {"Status user post": "OK"}


@router.get('/stream')
def stream():
    return {"Status stream get": "OK"}


@router.put('/stream')
def stream():
    return {"Status stream put": "OK"}


@router.post('/stream')
def stream():
    return {"Status stream post": "OK"}
