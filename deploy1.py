import os
from flask import Flask ,request,render_template

FLOWER_FOLDER = os.path.join('static', 'flower_photo')
# FLOWER_FOLDER = os.path('static')
app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = FLOWER_FOLDER
print(f"FLOWER_FOLDER is {FLOWER_FOLDER}")
full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'Iris.jpeg')
print(f"full_filename is {full_filename}")
