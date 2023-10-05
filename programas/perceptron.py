from PIL import Image
import random as rd
rd.seed(42)

def gen_weight_vector(len):
    W = [float(round(rd.uniform(-1.0,1.0),2)) for w in range(1,len + 1)]
    return W

def vector_product2d(X,W):
    return [x*w for x,w in zip(X,W)]

def step_function(suma):
    if suma >= 0: 
        return 1
    else:
        return 0     

def update_weights(W,e):
    alpha = 1 #learning rate
    return [(w + alpha*e) for w in W]

def perceptron_training(pics,size):
    b = round(rd.uniform(-1.0,1.0),2)
    W = gen_weight_vector(size)
    W2 = []
    j = 1
    
    for pic in pics:
        print("ya en pics train")
        #print(W) 
        #print(W2)   
        #if j > 1: W = W2
        output = 0
        X = list(pic.getdata())
        iterator = 1
        y = 1
        while output != y:
            suma = sum(vector_product2d(X,W)) + b
            
            output = step_function(suma)
            print("ya sumao")
            #print("antes de update")
            #print(W)
            print("haciendo updates")
            W = update_weights(W,y - output)
            print("termino updates")
            #print("despues")
            #print(W)
            iterator += 1
            #W2 = W
            #print(W)
            #print(W2)
        print("Last iteration: " + str(iterator))
        #print(j)
        j += 1
        #print(j)
        #print(W2)
    return W,b

def perceptron_testing(pics,W,b):
    i = 1
    for pic in pics:
        X = list(pic.getdata())
        suma = sum(vector_product2d(X,W)) + b
        output = step_function(suma)
        if output:
            print("La imagen " + str(i) + " es un cero")
        else:
            print("La imagen " + str(i) + " no es un cero")
        i += 1

img = Image.open("../img/numbers/zero1.jpg")
img2 = Image.open("../img/numbers/zero2.jpg")
img3 = Image.open("../img/numbers/zero3.jpg")
img4 = Image.open("../img/numbers/zero.jpg")

#t_img = Image.open("../img/numbers/zero3.jpg")
t_img2 = Image.open("../img/numbers/zero4.jpg")
t_img3 = Image.open("../img/numbers/zero5.jpg")
t_img4 = Image.open("../img/numbers/one.jpg")
t_img5 = Image.open("../img/numbers/two.jpg")
t_img6 = Image.open("../img/numbers/three.jpg")
t_img7 = Image.open("../img/numbers/four.jpg")
t_img8 = Image.open("../img/numbers/five.jpg")
t_img9 = Image.open("../img/numbers/six.jpg")
t_img10 = Image.open("../img/numbers/seven.jpg")
t_img11 = Image.open("../img/numbers/eight.jpg")
t_img12 = Image.open("../img/numbers/nine.jpg")



img.load()
img2.load()
img3.load()
img4.load()

#t_img.load()
t_img2.load()
t_img3.load()
t_img4.load()
t_img5.load()
t_img6.load()
t_img7.load()
t_img8.load()
t_img9.load()
t_img10.load()
t_img11.load()
t_img12.load()

gray_img = img.convert("L")
gray_img2 = img2.convert("L")
gray_img3 = img3.convert("L")
gray_img4 = img4.convert("L")

#t_gray_img = t_img.convert("L")
t_gray_img2 = t_img2.convert("L")
t_gray_img3 = t_img3.convert("L")
t_gray_img4 = t_img4.convert("L")
t_gray_img5 = t_img5.convert("L")
t_gray_img6 = t_img6.convert("L")
t_gray_img7 = t_img7.convert("L")
t_gray_img8 = t_img8.convert("L")
t_gray_img9 = t_img9.convert("L")
t_gray_img10 = t_img10.convert("L")
t_gray_img11 = t_img11.convert("L")
t_gray_img12 = t_img12.convert("L")

pics = [gray_img,gray_img2,gray_img3,gray_img4]
testing_pics = [t_gray_img2,t_gray_img3,t_gray_img4,t_gray_img5,t_gray_img6,t_gray_img7,t_gray_img8
                ,t_gray_img9,t_gray_img10,t_gray_img11,t_gray_img12]
width,height = gray_img.size
size = width * height
W,b = perceptron_training(pics, size)
perceptron_testing(testing_pics,W,b)

img.close()
img2.close()
img3.close()

#t_img.close()
t_img2.close()
t_img3.close()
t_img4.close()  