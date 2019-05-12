import base64

def main():
    inp = input('->')
    encoded = inp.encode('utf-8') #encoded the input (we need a bytes like object)
    b16encoded = base64.b16encode(encoded) #b16encoded the encoded string
    print(b16encoded)
    print(base64.b16decode(b16encoded).decode('utf-8'))#decoded it
    print("hello git")
<<<<<<< HEAD
    print("hello yesterday")
=======
    print("hello tomorrow")
>>>>>>> feature1
    print("111")

if __name__ == '__main__':
    main()
