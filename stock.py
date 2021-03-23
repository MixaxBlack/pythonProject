MAX=0
currency1=0
Stock1=0
Stock2=0
currency2=0
STOCK=['poloxex','ceixio','bitfinex']
CURR=['ETH','ZCASH','LITECOIN']
ETH=[1890.32,1912.3,1888.2]
ZCASH=[412,398.3,415.1]
LITECOIN=[612.4,578.7,590.5]
currency=[ETH,ZCASH,LITECOIN]
I = 0
while I < 3:
    J = 0
    while J < 3:
        P1 =currency[I][J]
        K = 0
        if K==J:
            K = K+1
        while K < 3:
            P2 = currency[I][K]
            N = 0
            if N==I:
                N=N+1
            while N < 3:
                P3 = currency[N][K]
                P4 = currency[N][J]
                Result = (P2 * P4) /(P1 * P3)
                if (Result) > (MAX):
                    MAX,currency1,Stock1,currency2,Stock2 = Result, I, J, N, K
                N = N + 1
            K = K + 1
        J = J + 1
    I = I + 1
#print ("рентабельность:", MAX, "покупаем ", currency1, "на бирже ", Stock1, "продаем на бирже",Stock2, "на ней же покупаем", currency2, "и продаем на бирже", Stock1  )
print ("рентабельность:", MAX, "покупаем ", CURR[currency1], "на бирже ", STOCK[Stock1], "продаем на бирже",STOCK[Stock2], "на ней же покупаем", CURR[currency2], "и продаем на бирже", STOCK[Stock1]  )
