import os

if (not os.path.exists('data')):
    os.mkdir('data')

print(os.getcwd())