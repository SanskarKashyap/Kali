from sympy import mod_inverse
import concurrent.futures

def base256(M):
    base = 256
    message256 = []
    sisa = M
    z = float(M)
    p = int(z).bit_length() // 8 + 1
    for _ in range(p):
        k = sisa % base
        sisa //= base
        message256.append(k)
    return message256

def Encode256(ascii):
    ascii256 = ""
    for a in ascii:
        g = int(str(a))
        ascii256 += chr(g)
    return ascii256

def factorize_range(args):
    start, end, N = args
    for i in range(start, end):
        if N % i == 0:
            return i
    return None

def factorize(N):
    num_threads = 10
    chunk_size = N // num_threads
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(factorize_range, (i*chunk_size, (i+1)*chunk_size, N)) for i in range(num_threads)]
        for future in concurrent.futures.as_completed(futures):
            factor = future.result()
            if factor is not None:
                return factor, N // factor
    return None


def calculate_phiN(N):
    # Factorize N into p and q
    # This is a simplified example, in practice factorizing N is non-trivial
    p, q = factorize(N)

    # Calculate phiN
    phiN = (p - 1) * (q - 1)

    return phiN

def main():
    N = int("21748096742659849357018698040199616792045282095099285468703513272637607311895366864257192785335233959058309060465868423951823285357297913125406449247740781187827060592914104497795045699165888211906369241532135744738704719864455623853940841947859652750123329821235383771649185149402914522002819011319590369529")
    e = int("65537")
    c = int("5035028646289403967446356090900614024724984911944639699234793220898497706186123226210199790989613849953542047021633331398057077596600815193940830692730376382829474208609200046676663440957657102570794842099284679728898437831331557960967948540809799255902703014867201045003016001267189341232653910252303505881")
    

    
    # phiN = int("21748096742659849357018698040199616792045282095099285468703513272637607311895366864257192785335233959058309060465868423951823285357297913125406449247738183679866482270532707596677244578324683864074431419149661562939376104607869781204868324933316666364155001553295827687037711471146642763970634674131635418276")

    d = mod_inverse(e, calculate_phiN(N))
    m = pow(c, d, N)

    print("d =", d)
    print("m =", m)
    
    message_256 = base256(m)
    print("m in base 256 =", message_256)
    print("Convert with ASCII \n", Encode256(message_256))

if __name__ == "__main__":
    main()
