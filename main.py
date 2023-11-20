from flask import Flask, jsonify, request
from db import get, create

app = Flask(__name__)