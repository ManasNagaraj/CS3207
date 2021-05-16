from collections import Counter


def append_dot(a):
    jj = a.replace("->", "->.")
    return jj



def closure(a):
    temp = [a]
    for it in temp:
        jj = it[it.index(".") + 1]
        if jj != len(it) - 1:
            for k in prod:
                if k[0][0] == jj and (append_dot(k)) not in temp:
                    temp.append(append_dot(k))
        else:
            for k in prod:
                if k[0][0] == jj and it not in temp:
                    temp.append(it)
                

    return temp


def shiftdot(new, pos):
    new = list(new)
    temp = new[pos]
    if pos != len(new):
        new[pos] = new[pos + 1]
        new[pos + 1] = temp
        new1 = "".join(new)
        return new1
    else:
        return "".join(new)



def goto1(x1):
    hh = []
    pos = x1.index(".")
    if pos != len(x1) - 1:
        jj = list(x1)
        kk = shiftdot(jj, pos)
        if kk.index(".") != len(kk) - 1:
            jjj = closure(kk)
            return jjj
        else:
            hh.append(kk)
            return hh
    else:
        return x1



def get_list(graph, state):
    final = []
    for g in graph:
        if int(g.split()[0]) == state:
            final.append(g)

    return final



def first(string):
    first_ = set()
    if string in non_term:
        alternatives = productions_dict[string]

        for alternative in alternatives:
            first_2 = first(alternative)
            first_ = first_ |first_2

    elif string in term:
        first_ = {string}

    else:
        first_2 = first(string[0])
        
        first_ = first_ | first_2

    return  first_

def follow(nT):
    follow_ = set()
    prods = productions_dict.items()
    if nT==starting_symbol:
        follow_ = follow_ | {'$'}
    for nt,rhs in prods:
        for alt in rhs:
            for char in alt:
                if char==nT:
                    following_str = alt[alt.index(char) + 1:]
                    if following_str=='':
                        if nt==nT:
                            continue
                        else:
                            follow_ = follow_ | follow(nt)
                    else:
                        follow_2 = first(following_str)
                        follow_ = follow_ | follow_2
    return follow_




#--------------------------------------------------------------
#----------------main------------------------------------------

term=[]
print("Enter terminals seperated by space")
term=input().strip().split(' ')
term.append('$')

non_term=[]
print("Enter non terminals seperated by space")
non_term=input().strip().split(' ')

prod = []
set_of_items = []
c = []

n = int(input('Enter no. of grammar rules: '))
print('Enter grammar rule :(A->cd) ')
for i in range(n):
    prod.append(input())
    
    
    
    
    
    
productions_dict = {}

for nT in non_term:
    productions_dict[nT] = []


#print("productions_dict",productions_dict)

for production in prod:
    nonterm_to_prod = production.split("->")
    alternatives = nonterm_to_prod[1].split("/")
    for alternative in alternatives:
        productions_dict[nonterm_to_prod[0]].append(alternative)

print("productions_dict",productions_dict)    
FIRST = {}
FOLLOW = {}

for non_terminal in non_term:
    FIRST[non_terminal] = set()

for non_terminal in non_term:
    FOLLOW[non_terminal] = set()    
    
for non_terminal in non_term:
    FIRST[non_terminal] = FIRST[non_terminal] | first(non_terminal)

print("FIRST",FIRST)
starting_symbol=prod[0][0]
FOLLOW[starting_symbol] = FOLLOW[starting_symbol] | {'$'}
for non_terminal in non_term:
    FOLLOW[non_terminal] = FOLLOW[non_terminal] | follow(non_terminal)

print("FOLLOW", FOLLOW)


    
    
    
    
a='X->.'+prod[0][0]
prod.insert(0, a)
print("---------------------------------------------------------------")
print("Augmented Grammar")
print(prod)

prod_num = {}
for i in range(1, len(prod)):
    prod_num[str(prod[i])] = i
    

j = closure(a)
set_of_items.append(j)

state_numbers = {}
dfa_prod = {}
items = 0
while True:
    if len(set_of_items) == 0:
        break

    jk = set_of_items.pop(0)
    kl = jk
    c.append(jk)
    state_numbers[str(jk)] = items
    items += 1

    if len(jk) > 1:
        for item in jk:
            jl = goto1(item)
            if jl not in set_of_items and jl != kl:
                set_of_items.append(jl)
                dfa_prod[str(state_numbers[str(jk)]) + " " + str(item)] = jl
            else:
                dfa_prod[str(state_numbers[str(jk)]) + " " + str(item)] = jl
    


for item in c:
    for j in range(len(item)):
        if goto1(item[j]) not in c:
            if item[j].index(".") != len(item[j]) - 1:
                c.append(goto1(item[j]))

print("---------------------------------------------------------------")
print("Total States: ", len(c))
for i in range(len(c)):
    print(i, ":", c[i])
print("---------------------------------------------------------------")

dfa = {}
for i in range(len(c)):
    if i in dfa:
        pass
    else:
        lst = get_list(dfa_prod, i)
        samp = {}
        for j in lst:
            s = j.split()[1].split('->')[1]
            search = s[s.index('.') + 1]
            samp[search] = state_numbers[str(dfa_prod[j])]

        if samp != {}:
            dfa[i] = samp


#print(dfa)
#---------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------


#------------------------ Generate SLR parsing table------------------------------------
table = []

table.append([''] + term + non_term)

table_dic = {}

for i in range(len(c)):
    data = [''] * (len(term) + len(non_term))
    samp = {}

    # Action
    try:
        for j in dfa[i]:
            if not j.isupper() and j != '' and j != '.':
                ind = term.index(j)
                data[ind] = 'S' + str(dfa[i][j])
                samp[term[ind]] = 'S' + str(dfa[i][j])

    except Exception:
        if i != 1:
            s = list(c[i][0])
            s.remove('.')
            s = "".join(s)
            #print(prod_num)
            lst = [i] + ['r' + str(prod_num[s])] * len(term)
            lst += [''] * len(non_term)
            table.append(lst)
            foll=FOLLOW[s[0]]
            for j in foll:
                samp[j] = 'r' + str(prod_num[s])
        else:
            lst = [i] + [''] * (len(term) + len(non_term))
            lst[-1] = 'Accept'
            table.append(lst)

    # Goto
    try:
        for j in dfa[i]:
            if j.isupper():
                ind = non_term.index(j)
                data[len(term) + ind] = dfa[i][j]

                samp[j] = str(dfa[i][j])

        table.append([i] + data)
    except Exception:
        pass

    if samp == {}:
        table_dic[i] = {'$': 'Accept'}
    else:
        table_dic[i] = samp



print("\n")
print('-----------SLR Parsing table-------------')
for i in table_dic:
    print(i,table_dic[i])
#------------------------------------------------------------------------------------





# Parse String
string = input("Enter the string to be parsed: ")
string += '$'
print("\n")

stack = [0]
pointer = 0



data = []

i = 0
accepted = False
while True:
    try:
        try:
            prods = dfa[stack[-1]]
            prod_i = prods[string[i]]  # state num
        except Exception:
            prod_i = None

        try:
            tab = table_dic[stack[-1]]
            tab_i = tab[string[i]]  # S or r
        except Exception:
            tab = table_dic[stack[-2]]
            tab_i = tab[stack[-1]]  # S or r

        if tab_i == 'Accept':
            data.append(['Action({0}, {1}) = {2}'.format(stack[-1], string[i], tab_i), i, string[i], str(stack)])
            accepted = True
            break
        else:
            if tab_i[0] == 'S' and not str(stack[-1]).isupper():
                lst = ['Action({0}, {1}) = {2}'.format(stack[-1], string[i], tab_i), i, string[i]]
                stack.append(string[i])
                stack.append(prod_i)
                lst.append(str(stack))
                data.append(lst)
                i += 1
            elif tab_i[0] == 'r':
                lst = ['Action({0}, {1}) = {2}'.format(stack[-1], string[i], tab_i), i, string[i]]
                x = None
                for i1 in prod_num:
                    if prod_num[i1] == int(tab_i[1]):
                        x = i1
                        break

                length = 2 * (len(x.split('->')[1]))
                for _ in range(length):
                    stack.pop()

                stack.append(x[0])
                lst.append(str(stack))
                data.append(lst)
            else:
                lst = ['goto({0}, {1}) = {2}'.format(stack[-2], stack[-1], tab_i), i, string[i]]
                stack.append(int(tab_i))
                lst.append(str(stack))
                data.append(lst)
    except Exception:
        accepted = False
        break

try:

    if accepted:
        print("String accepted")
    else:
        print("The string is not parsable!")
        
except Exception:

    print("Invalid string entered!")
