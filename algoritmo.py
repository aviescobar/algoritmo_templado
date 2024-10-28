from flask import Flask, render_template
import math
import random

app = Flask(__name__)

def distancia(coord1, coord2):
