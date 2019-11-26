

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
        print(fs)
    return fs

def main():
    fs = count()
    print(fs[0]())

if __name__ == '__main__':
    main()