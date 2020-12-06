import os


def generate_negative_description_file(n):
    with open('data/neg'+str(n)+'.txt', 'w') as f:
        for filename in os.listdir('data/images/n'+str(n)):
            print('data/images/n'+str(n)+'/'+filename +'\n')
            f.write('data/images/n'+str(n)+'/'+filename +'\n')

def generate_positive_description_file(n):
    with open('data/pos'+str(n)+'.txt', 'w') as f:
        for filename in os.listdir('data/images/p'+str(n)):
            f.write('images/p'+str(n)+'/'+ filename + '\n')