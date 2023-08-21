#function kd :
def R_kd(mt,k,d):
    temp = []
    m = 0
    m_dic = {}
    i0 = 0
    for i in range(len(mt)):
        temp += [mt[i][0]] 
    
    for j in range(len(temp)):
        if temp[j] == 0 :
            m_dic[i0] = j
            m += 1   
            i0 += 1

    if m == 0 :
        return mt
    else : 
        jaygah = k%m
        mt[m_dic[jaygah]][0] = d  

    return mt

def  L_kd(mt,k,d):
    temp = []
    m = 0
    m_dic = {}
    i0 = 0
    for i in range(len(mt)):
        temp += [mt[i][3]] 
    
    for j in range(len(temp)):
        if temp[j] == 0 :
            m_dic[i0] = j
            m += 1   
            i0 += 1
    
    if m == 0 :
        return mt
    else : 
        jaygah = k%m
        mt[m_dic[jaygah]][3] = d  

    return mt   

def U_kd(mt,k,d):
    temp = []
    m = 0
    m_dic = {}
    i0 = 0
    for i in range(len(mt)):
        temp += [mt[3][i]]
    
    for j in range(len(temp)):
        if temp[j] == 0 :
            m_dic[i0] = j
            m += 1   
            i0 += 1
    
    if m == 0 :
        return mt
    else : 
        jaygah = k%m
        mt[3][m_dic[jaygah]] = d  

    return mt       

def D_kd(mt,k,d):
    temp = []
    m = 0
    m_dic = {}
    i0 = 0
    for i in range(len(mt)):
        temp += [mt[0][i]]
    
    for j in range(len(temp)):
        if temp[j] == 0 :
            m_dic[i0] = j
            m += 1   
            i0 += 1
    
    if m == 0 :
        return mt
    else : 
        jaygah = k%m
        mt[0][m_dic[jaygah]] = d  

    return mt       

#funtion RLUD :
def Down(mt):  
    for u in range(len(mt)):
        temp = []
        for j in range(len(mt)):
            temp += [mt[j][u]]
        temp = temp[::-1]
        
        for i in range(len(temp)-1):
            if temp[0] == 0:
                break
            if temp[i] == 0 :
                continue
            
            elif temp[i] == 1 :
                if temp[i+1] == 2 :
                    temp[i] = 3
                    temp[i+1] = 0
                    break
            
            elif temp[i] == 2 :
                if temp[i+1] == 1 :
                    temp[i] = 3
                    temp[i+1] = 0
                    break

            else :
                if temp[i] == temp[i+1]:
                    temp[i] = temp[i]+temp[i]
                    temp[i+1] = 0
                    break
        
        
        if temp[0] != 0 :
            for m in range(1,len(temp)-1):
                if temp[m] == 0 :
                    x = temp[m]
                    y = temp[m+1]
                    temp[m] = y
                    temp[m+1] = x
        else :
            for m in range(0,len(temp)-1):
                if temp[m] == 0 :
                    x = temp[m]
                    y = temp[m+1]
                    temp[m] = y
                    temp[m+1] = x
        
        
        temp = temp[::-1]
        for j in range(len(mt)):
            mt[j][u] = temp[j]

    return mt    

def Up(mt):
    for u in range(len(mt)):
        temp = []
        for j in range(len(mt)):
            temp += [mt[j][u]]
        
        for i in range(len(temp)-1):
            if temp[0] == 0:
                break
            if temp[i] == 0 :
                continue
            
            elif temp[i] == 1 :
                if temp[i+1] == 2 :
                    temp[i] = 3
                    temp[i+1] = 0
                    break
            
            elif temp[i] == 2 :
                if temp[i+1] == 1 :
                    temp[i] = 3
                    temp[i+1] = 0
                    break

            else :
                if temp[i] == temp[i+1]:
                    temp[i] = temp[i]+temp[i]
                    temp[i+1] = 0
                    break
        
        
        if temp[0] != 0 :
            for m in range(1,len(temp)-1):
                if temp[m] == 0 :
                    x = temp[m]
                    y = temp[m+1]
                    temp[m] = y
                    temp[m+1] = x
        else :
            for m in range(0,len(temp)-1):
                if temp[m] == 0 :
                    x = temp[m]
                    y = temp[m+1]
                    temp[m] = y
                    temp[m+1] = x
        
        
        
        for j in range(len(mt)):
            mt[j][u] = temp[j]

    return mt    

def Left(mt):
    for u in range(len(mt)):
        temp = []
        for j in range(len(mt)):
            temp += [mt[u][j]]
        
        for i in range(len(temp)-1):
            if temp[0] == 0:
                break
            if temp[i] == 0 :
                continue
            
            elif temp[i] == 1 :
                if temp[i+1] == 2 :
                    temp[i] = 3
                    temp[i+1] = 0
                    break
            
            elif temp[i] == 2 :
                if temp[i+1] == 1 :
                    temp[i] = 3
                    temp[i+1] = 0
                    break

            else :
                if temp[i] == temp[i+1]:
                    temp[i] = temp[i]+temp[i]
                    temp[i+1] = 0
                    break
        
        if temp[0] != 0 :
            for m in range(1,len(temp)-1):
                if temp[m] == 0 :
                    x = temp[m]
                    y = temp[m+1]
                    temp[m] = y
                    temp[m+1] = x
        else :
            for m in range(0,len(temp)-1):
                if temp[m] == 0 :
                    x = temp[m]
                    y = temp[m+1]
                    temp[m] = y
                    temp[m+1] = x
        
        
        
        
        for j in range(len(mt)):
            mt[u][j] = temp[j]
        
    return mt    

def Right(mt):
    for u in range(len(mt)):
        temp = []
        for j in range(len(mt)):
            temp += [mt[u][j]]
        temp = temp[::-1]

        for i in range(len(temp)-1):
            if temp[0] == 0:
                break
            if temp[i] == 0 :
                continue
            
            elif temp[i] == 1 :
                if temp[i+1] == 2 :
                    temp[i] = 3
                    temp[i+1] = 0
                    break
            
            elif temp[i] == 2 :
                if temp[i+1] == 1 :
                    temp[i] = 3
                    temp[i+1] = 0
                    break

            else :
                if temp[i] == temp[i+1]:
                    temp[i] = temp[i]+temp[i]
                    temp[i+1] = 0
                    break
        
        if temp[0] != 0 :
            for m in range(1,len(temp)-1):
                if temp[m] == 0 :
                    x = temp[m]
                    y = temp[m+1]
                    temp[m] = y
                    temp[m+1] = x
        else :
            for m in range(0,len(temp)-1):
                if temp[m] == 0 :
                    x = temp[m]
                    y = temp[m+1]
                    temp[m] = y
                    temp[m+1] = x
        
        temp = temp[::-1]
        for j in range(len(mt)):
            mt[u][j] = temp[j]            
        
    
    return mt    
    
#input mat :
size = int(input())
mat = []
for i in range(size):
    avlie = input().split()
    for i in range(size):
        avlie[i] = int(avlie[i])
    mat += [avlie]

#input k d :    
harkat = input()
for i in harkat:
    if i == 'R' : 
        mat_tmp = [i[:] for i in mat]
        mat_tmp = Right(mat_tmp)
        if mat != mat_tmp :
            mat = Right(mat)
            kd = input().split()
            k = int(kd[0])
            d = int(kd[1])
            mat = R_kd(mat,k,d)
        else :
            mat = Right(mat)
    elif i == 'D' :
        mat_tmp = [i[:] for i in mat]
        mat_tmp = Down(mat_tmp)
        if  mat != mat_tmp :
            mat = Down(mat)
            kd = input().split()
            k = int(kd[0])
            d = int(kd[1])
            mat = D_kd(mat,k,d)
        else :
            mat = Down(mat)
    elif i == 'U' :
        mat_tmp = [i[:] for i in mat]
        mat_tmp = Up(mat_tmp)
        if mat != mat_tmp :
            mat = Up(mat)
            kd = input().split()
            k = int(kd[0])
            d = int(kd[1])
            mat = U_kd(mat,k,d)
        else :
            mat = Up(mat)
    elif i == 'L' :
        mat_tmp = [i[:] for i in mat]
        mat_tmp = Left(mat_tmp)
        if mat != mat_tmp :
            mat = Left(mat)
            kd = input().split()
            k = int(kd[0])
            d = int(kd[1])
            mat = L_kd(mat,k,d)
        else :
            mat = Left(mat)
#output :
for i in range(len(mat)):
    for j in range(len(mat)):
        print( mat[i][j] , end = "\t" )
    print()

#partial or final score :
Flag1 = False
for m in range(len(mat)):
    for n in range(len(mat)):
        if mat[m][n] == 0 :
            Flag1 = True
            break
    if Flag1 :
        break
if Flag1 == False :
    while True :
        mat_tmp = [i[:] for i in mat]
        mat_tmp = Right(mat_tmp)
        if mat != mat_tmp :
            Flag1 = True
            break   
        mat_tmp = [i[:] for i in mat]
        mat_tmp = Left(mat_tmp)
        if mat != mat_tmp :
            Flag1 = True
            break
        mat_tmp = [i[:] for i in mat]
        mat_tmp = Up(mat_tmp)
        if mat != mat_tmp :
            Flag1 = True
            break  
        mat_tmp = [i[:] for i in mat]
        mat_tmp = Down(mat_tmp)
        if mat != mat_tmp :
            Flag1 = True
            break      

score = 0 
for o in range(len(mat)):
    for p in range(len(mat)):
        if mat[o][p] == 0 or mat[o][p] == 1 or mat[o][p] == 2 :
            continue
        else :
            tmp_sc = mat[o][p]
            if tmp_sc == 3 :
                k = 1
                score += (3)
            else :        
                tmp_sc //= 3
                k = 0 
                while True :
                    tmp_sc //= 2 
                    k += 1
                    if tmp_sc == 1 :
                        break
                k += 1
                score += (3**k)        

if Flag1 :
    print("The partial score is " + str(score) + "." )
else :
    print("The final score is " + str(score) + "." )    
    