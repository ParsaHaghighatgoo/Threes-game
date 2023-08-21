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
    sum = []
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
                    sum += [3]
                    break
            
            elif temp[i] == 2 :
                if temp[i+1] == 1 :
                    temp[i] = 3
                    temp[i+1] = 0
                    sum += [3]
                    break

            else :
                if temp[i] == temp[i+1]:
                    sum += [temp[i]+temp[i]]
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

    if len(sum) == 0 :
        sum += [0]
    total_sum = max(sum)
    return [mt , total_sum]   

def Up(mt):
    sum = []
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
                    sum += [3]
                    break
            
            elif temp[i] == 2 :
                if temp[i+1] == 1 :
                    temp[i] = 3
                    temp[i+1] = 0
                    sum += [3]
                    break

            else :
                if temp[i] == temp[i+1]:
                    sum += [temp[i]+temp[i]]
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

    if len(sum) == 0 :
        sum += [0]
    total_sum = max(sum)
    return mt , total_sum  

def Left(mt):
    sum = []
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
                    sum += [3]
                    break
            
            elif temp[i] == 2 :
                if temp[i+1] == 1 :
                    temp[i] = 3
                    temp[i+1] = 0
                    sum += [3]
                    break

            else :
                if temp[i] == temp[i+1]:
                    sum += [temp[i]+temp[i]]
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
        
    if len(sum) == 0 :
        sum += [0]
    total_sum = max(sum)
    return mt , total_sum

def Right(mt):
    sum = []
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
                    sum += [3]
                    break
            
            elif temp[i] == 2 :
                if temp[i+1] == 1 :
                    temp[i] = 3
                    temp[i+1] = 0
                    sum += [3]
                    break

            else :
                if temp[i] == temp[i+1]:
                    sum += [temp[i]+temp[i]]
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
        
    if len(sum) == 0 :
        sum += [0]
    total_sum = max(sum)
    return mt , total_sum   
    
#input mat :
size = int(input())
mat = []
for i in range(size):
    avlie = input().split()
    for i in range(size):
        avlie[i] = int(avlie[i])
    mat += [avlie]

#-------------------------------------------------------------------------------------------------------------------------------

#input k d :    
tedad_harkat = int(input())
counter = 0 
harkat = ''
matmax_shift = [ 'L' , 'D' , 'U' , 'R' ]
while counter < tedad_harkat :
    mat_max = []
    
    mat_tmp = [i[:] for i in mat]
    mat_tmp = Left(mat_tmp)
    mat_max += [mat_tmp[1]]
    
    mat_tmp = [i[:] for i in mat]
    mat_tmp = Down(mat_tmp)
    mat_max += [mat_tmp[1]]

    
    mat_tmp = [i[:] for i in mat]
    mat_tmp = Up(mat_tmp)
    mat_max += [mat_tmp[1]]

    mat_tmp = [i[:] for i in mat]
    mat_tmp = Right(mat_tmp)
    mat_max += [mat_tmp[1]]

    Flag1_3 = True
    for i in range(len(mat_max)):
        for j in range(i,len(mat_max)):
            if mat_max[i] == mat_max [j]:
                Flag1_3 = False


    #---------------------------------------------------------------------------------------------------------
    if Flag1_3 :
        max_matmax = max(mat_max)
        index_max_matmax = 0
        for i in range(len(mat_max)):
           if mat_max[i] == max_matmax:
                index_max_matmax = i
                break
        shift1_3 = matmax_shift[index_max_matmax]
    else :
        if max(mat_max) == 0 :
            mat = Left(mat)[0]
            kd = input().split()
            k = int(kd[0])
            d = int(kd[1])
            mat = L_kd(mat,k,d)
            shift1_3 = 'none'
            harkat += 'L'
        else :
            max_matmax = max(mat_max)
            index_max_matmax = 0
            for i in range(len(mat_max)):
                if mat_max[i] == max_matmax:
                    index_max_matmax = i
                    break
            shift1_3 = matmax_shift[index_max_matmax]

    #---------------------------------------------------------------------------------------------------            

    if shift1_3 == 'none' :
        hs = 0
    elif shift1_3 == 'R' : 
        mat = Right(mat)[0]
        kd = input().split()
        k = int(kd[0])
        d = int(kd[1])
        mat = R_kd(mat,k,d)
        harkat += 'R' 
    elif shift1_3 == 'D' :
        mat = Down(mat)[0]
        kd = input().split()
        k = int(kd[0])
        d = int(kd[1])
        mat = D_kd(mat,k,d)
        harkat += 'D'
        
    elif shift1_3 == 'U' :
        mat = Up(mat)[0]
        kd = input().split()
        k = int(kd[0])
        d = int(kd[1])
        mat = U_kd(mat,k,d)
        harkat += 'U'
    elif shift1_3 == 'L' :
        mat = Left(mat)[0]
        kd = input().split()
        k = int(kd[0])
        d = int(kd[1])
        mat = L_kd(mat,k,d)
        harkat += 'L'

    
    
    
    
    
    
    counter += 1    

#----------------------------------------------------------------------------------------------------------------------------
#output :
print(harkat)
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
    