import base64

def main():
    inp = input('->')
    encoded = inp.encode('utf-8') #encoded the input (we need a bytes like object)
    b16encoded = base64.b16encode(encoded) #b16encoded the encoded string
    print(b16encoded)
    print(base64.b16decode(b16encoded).decode('utf-8'))#decoded it
    print("hello git")
    print("hello tomorrow")

if __name__ == '__main__':
    main()
