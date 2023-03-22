from itertools import count
# Grammar Productions
productions = [
    ["P'", 'P'],
    ['P', 'S'],
    ['S', 'A'],
    ['S', 'while', 'M', 'E', 'do', 'M', 'S'],
    ['S', 'if', 'M', 'B', 'then', 'M', 'S', 'N', 'else', 'M', 'S'],
    ['S', 'for', 'A', ';', 'M', 'B', ';', 'M', 'X', 'do', ' M', 'S'],
    ['M'],
    ['N'],
    ['A', 'id', '=', 'E'],
    ['E', 'E', '+', 'T'],
    ['E', 'E', '-', 'T'],
    ['E', 'T'],
    ['T', 'T', '*', 'F'],
    ['T', 'T', '/', 'F'],
    ['T', 'F'],
    ['F', '(', 'E', ')'],
    ['F', 'id'],
    ['B', 'B', '||', 'M', 'C'],
    ['B', 'C'],
    ['C', 'C', '&&', 'M', 'D'],
    ['C', 'D'],
    ['D', '!', 'G'],
    ['D', 'G'],
    ['G', 'id'],
    ['G', 'id', "relop", 'id'],
    ['X','A']
]

# Bottom-Up Parser Table
action_table = {(0, 'for'): 's6',
 (0, 'id'): 's7',
 (0, 'if'): 's5',
 (0, 'while'): 's4',
 (1, '$'): 'acc',
 (2, '$'): 'r1',
 (3, '$'): 'r2',
 (3, 'else'): 'r2',
 (4, 'for'): 'r6',
 (4, 'id'): 'r6',
 (4, 'if'): 'r6',
 (4, 'not'): 'r6',
 (4, 'while'): 'r6',
 (5, 'for'): 'r6',
 (5, 'id'): 'r6',
 (5, 'if'): 'r6',
 (5, 'not'): 'r6',
 (5, 'while'): 'r6',
 (6, 'id'): 's7',
 (7, '='): 's11',
 (8, 'id'): 's17',
 (8, 'not'): 's15',
 (9, 'id'): 's17',
 (9, 'not'): 's15',
 (10, ';'): 's19',
 (11, '('): 's23',
 (11, 'id'): 's24',
 (12, 'do'): 's25',
 (12, 'or'): 's26',
 (13, ';'): 'r18',
 (13, 'and'): 's27',
 (13, 'do'): 'r18',
 (13, 'or'): 'r18',
 (13, 'then'): 'r18',
 (14, ';'): 'r20',
 (14, 'and'): 'r20',
 (14, 'do'): 'r20',
 (14, 'or'): 'r20',
 (14, 'then'): 'r20',
 (15, 'id'): 's17',
 (16, ';'): 'r22',
 (16, 'and'): 'r22',
 (16, 'do'): 'r22',
 (16, 'or'): 'r22',
 (16, 'then'): 'r22',
 (17, ';'): 'r23',
 (17, 'and'): 'r23',
 (17, 'do'): 'r23',
 (17, 'or'): 'r23',
 (17, 'relop'): 's29',
 (17, 'then'): 'r23',
 (18, 'or'): 's26',
 (18, 'then'): 's30',
 (19, 'for'): 'r6',
 (19, 'id'): 'r6',
 (19, 'if'): 'r6',
 (19, 'not'): 'r6',
 (19, 'while'): 'r6',
 (20, '$'): 'r8',
 (20, '+'): 's32',
 (20, '-'): 's33',
 (20, ';'): 'r8',
 (20, 'do'): 'r8',
 (20, 'else'): 'r8',
 (21, '$'): 'r11',
 (21, ')'): 'r11',
 (21, '*'): 's34',
 (21, '+'): 'r11',
 (21, '-'): 'r11',
 (21, '/'): 's35',
 (21, ';'): 'r11',
 (21, 'do'): 'r11',
 (21, 'else'): 'r11',
 (22, '$'): 'r14',
 (22, ')'): 'r14',
 (22, '*'): 'r14',
 (22, '+'): 'r14',
 (22, '-'): 'r14',
 (22, '/'): 'r14',
 (22, ';'): 'r14',
 (22, 'do'): 'r14',
 (22, 'else'): 'r14',
 (23, '('): 's23',
 (23, 'id'): 's24',
 (24, '$'): 'r16',
 (24, ')'): 'r16',
 (24, '*'): 'r16',
 (24, '+'): 'r16',
 (24, '-'): 'r16',
 (24, '/'): 'r16',
 (24, ';'): 'r16',
 (24, 'do'): 'r16',
 (24, 'else'): 'r16',
 (25, 'for'): 'r6',
 (25, 'id'): 'r6',
 (25, 'if'): 'r6',
 (25, 'not'): 'r6',
 (25, 'while'): 'r6',
 (26, 'for'): 'r6',
 (26, 'id'): 'r6',
 (26, 'if'): 'r6',
 (26, 'not'): 'r6',
 (26, 'while'): 'r6',
 (27, 'for'): 'r6',
 (27, 'id'): 'r6',
 (27, 'if'): 'r6',
 (27, 'not'): 'r6',
 (27, 'while'): 'r6',
 (28, ';'): 'r21',
 (28, 'and'): 'r21',
 (28, 'do'): 'r21',
 (28, 'or'): 'r21',
 (28, 'then'): 'r21',
 (29, 'id'): 's40',
 (30, 'for'): 'r6',
 (30, 'id'): 'r6',
 (30, 'if'): 'r6',
 (30, 'not'): 'r6',
 (30, 'while'): 'r6',
 (31, 'id'): 's17',
 (31, 'not'): 's15',
 (32, '('): 's23',
 (32, 'id'): 's24',
 (33, '('): 's23',
 (33, 'id'): 's24',
 (34, '('): 's23',
 (34, 'id'): 's24',
 (35, '('): 's23',
 (35, 'id'): 's24',
 (36, ')'): 's47',
 (36, '+'): 's32',
 (36, '-'): 's33',
 (37, 'for'): 's6',
 (37, 'id'): 's7',
 (37, 'if'): 's5',
 (37, 'while'): 's4',
 (38, 'id'): 's17',
 (38, 'not'): 's15',
 (39, 'id'): 's17',
 (39, 'not'): 's15',
 (40, ';'): 'r24',
 (40, 'and'): 'r24',
 (40, 'do'): 'r24',
 (40, 'or'): 'r24',
 (40, 'then'): 'r24',
 (41, 'for'): 's6',
 (41, 'id'): 's7',
 (41, 'if'): 's5',
 (41, 'while'): 's4',
 (42, ';'): 's52',
 (42, 'or'): 's26',
 (43, '$'): 'r9',
 (43, ')'): 'r9',
 (43, '*'): 's34',
 (43, '+'): 'r9',
 (43, '-'): 'r9',
 (43, '/'): 's35',
 (43, ';'): 'r9',
 (43, 'do'): 'r9',
 (43, 'else'): 'r9',
 (44, '$'): 'r10',
 (44, ')'): 'r10',
 (44, '*'): 's34',
 (44, '+'): 'r10',
 (44, '-'): 'r10',
 (44, '/'): 's35',
 (44, ';'): 'r10',
 (44, 'do'): 'r10',
 (44, 'else'): 'r10',
 (45, '$'): 'r12',
 (45, ')'): 'r12',
 (45, '*'): 'r12',
 (45, '+'): 'r12',
 (45, '-'): 'r12',
 (45, '/'): 'r12',
 (45, ';'): 'r12',
 (45, 'do'): 'r12',
 (45, 'else'): 'r12',
 (46, '$'): 'r13',
 (46, ')'): 'r13',
 (46, '*'): 'r13',
 (46, '+'): 'r13',
 (46, '-'): 'r13',
 (46, '/'): 'r13',
 (46, ';'): 'r13',
 (46, 'do'): 'r13',
 (46, 'else'): 'r13',
 (47, '$'): 'r15',
 (47, ')'): 'r15',
 (47, '*'): 'r15',
 (47, '+'): 'r15',
 (47, '-'): 'r15',
 (47, '/'): 'r15',
 (47, ';'): 'r15',
 (47, 'do'): 'r15',
 (47, 'else'): 'r15',
 (48, '$'): 'r3',
 (48, 'else'): 'r3',
 (49, ';'): 'r17',
 (49, 'and'): 's27',
 (49, 'do'): 'r17',
 (49, 'or'): 'r17',
 (49, 'then'): 'r17',
 (50, ';'): 'r19',
 (50, 'and'): 'r19',
 (50, 'do'): 'r19',
 (50, 'or'): 'r19',
 (50, 'then'): 'r19',
 (51, 'else'): 'r7',
 (52, 'for'): 'r6',
 (52, 'id'): 'r6',
 (52, 'if'): 'r6',
 (52, 'not'): 'r6',
 (52, 'while'): 'r6',
 (53, 'else'): 's55',
 (54, 'id'): 's7',
 (55, 'for'): 'r6',
 (55, 'id'): 'r6',
 (55, 'if'): 'r6',
 (55, 'not'): 'r6',
 (55, 'while'): 'r6',
 (56, 'do'): 's59',
 (57, 'do'): 'r25',
 (58, 'for'): 's6',
 (58, 'id'): 's7',
 (58, 'if'): 's5',
 (58, 'while'): 's4',
 (59, 'for'): 'r6',
 (59, 'id'): 'r6',
 (59, 'if'): 'r6',
 (59, 'not'): 'r6',
 (59, 'while'): 'r6',
 (60, '$'): 'r4',
 (60, 'else'): 'r4',
 (61, 'for'): 's6',
 (61, 'id'): 's7',
 (61, 'if'): 's5',
 (61, 'while'): 's4',
 (62, '$'): 'r5',
 (62,'else'):'r5'}

                

goto_table = {(0, 'A'): '3',
 (0, 'P'): '1',
 (0, 'S'): '2',
 (4, 'M'): '8',
 (5, 'M'): '9',
 (6, 'A'): '10',
 (8, 'B'): '12',
 (8, 'C'): '13',
 (8, 'D'): '14',
 (8, 'G'): '16',
 (9, 'B'): '18',
 (9, 'C'): '13',
 (9, 'D'): '14',
 (9, 'G'): '16',
 (11, 'E'): '20',
 (11, 'F'): '22',
 (11, 'T'): '21',
 (15, 'G'): '28',
 (19, 'M'): '31',
 (23, 'E'): '36',
 (23, 'F'): '22',
 (23, 'T'): '21',
 (25, 'M'): '37',
 (26, 'M'): '38',
 (27, 'M'): '39',
 (30, 'M'): '41',
 (31, 'B'): '42',
 (31, 'C'): '13',
 (31, 'D'): '14',
 (31, 'G'): '16',
 (32, 'F'): '22',
 (32, 'T'): '43',
 (33, 'F'): '22',
 (33, 'T'): '44',
 (34, 'F'): '45',
 (35, 'F'): '46',
 (37, 'A'): '3',
 (37, 'S'): '48',
 (38, 'C'): '49',
 (38, 'D'): '14',
 (38, 'G'): '16',
 (39, 'D'): '50',
 (39, 'G'): '16',
 (41, 'A'): '3',
 (41, 'S'): '51',
 (51, 'N'): '53',
 (52, 'M'): '54',
 (54, 'A'): '57',
 (54, 'X'): '56',
 (55, 'M'): '58',
 (58, 'A'): '3',
 (58, 'S'): '60',
 (59, 'M'): '61',
 (61, 'A'): '3',
 (61,'S'):'62'}

keywords = ['while', 'do', 'for', 'if', 'then', 'else', 'and', 'or', 'not']
operators = ['+', '-', '*', '/', '&&', '||', '!', 'relop', '$', '=' , ';']


class StackItem:
    def __init__(self, name, place="-", quad=None):
        self.name = name
        self.place = place
        self.quad = quad
        self.next = []
        self.true = []
        self.false = []


class TAC_generator:

    def __init__(self, input_string, productions, action_table, goto_table):
        self.code = []
        self.temp_counter = count()
        self.productions = productions
        self.action_table = action_table
        self.goto_table = goto_table
        self.input_tokens = input_string.split()

    def newtemp(self):
        return f'T{next(self.temp_counter)}'

    def nextQuad(self):
        return len(self.code)

    def backpatch(self, to_back_patch, quad):
        for line_no in to_back_patch:
            self.code[line_no] += " " + str(quad)

    def gen(self, *args):
        self.code.append(" ".join(args))

    def semantic_action(self, production_index, LHS, RHS):
        match production_index:
            case 1:
                S = RHS.pop()
                self.backpatch(S.next, self.nextQuad())
                return StackItem("P")

            case 2:
                return StackItem("S")

            case 3:

                RHS.pop()
                M1 = RHS.pop()
                B = RHS.pop()
                RHS.pop()
                M2 = RHS.pop()
                S1 = RHS.pop()

                self.backpatch(S1.next, M1.quad)
                self.backpatch(B.true, M2.quad)
                S = StackItem("S")
                S.next = B.false
                self.gen("goto", str(M1.quad))
                return S

            case 4:

                RHS.pop()
                M = RHS.pop()
                B = RHS.pop()
                RHS.pop()
                M1 = RHS.pop()
                S1 = RHS.pop()
                N = RHS.pop()
                RHS.pop()
                M2 = RHS.pop()
                S2 = RHS.pop()
                
                self.backpatch(B.true, M1.quad)
                self.backpatch(B.false, M2.quad)
                S = StackItem("S")
                S.next = list(set(S1.next + N.next + S2.next))
                return S

            case 5:
                for i in RHS:
                    print(i.name,end=" ")
                
                RHS.pop()
                A1 = RHS.pop()
                RHS.pop()
                M1 = RHS.pop()
                B = RHS.pop()
                RHS.pop()
                M2 = RHS.pop()
                X = RHS.pop()
                RHS.pop()
                M3 = RHS.pop()
                S1 = RHS.pop()
                print(M1.quad)
                
                self.backpatch(B.true,M3.quad)
                self.backpatch(X.next,M1.quad)
                S = StackItem("S")
                S.next = B.false
                self.gen("goto",str(M2.quad))
                return S

            case 6:
                return StackItem("M", quad=self.nextQuad())

            case 7:
                N = StackItem("N")
                N.next = [self.nextQuad()]
                self.gen("goto")
                return N

            case 8:
                id = RHS.pop()
                RHS.pop()
                E = RHS.pop()
                self.gen(id.place, "=", E.place)
                return StackItem("A")

            case 9:
                E1 = RHS.pop()
                RHS.pop()
                T = RHS.pop()
                E = StackItem(LHS, self.newtemp())
                self.gen(E.place, "=", E1.place, "+", T.place)
                return E

            case 10:
                E1 = RHS.pop()
                RHS.pop()
                T = RHS.pop()
                E = StackItem(LHS, self.newtemp())
                self.gen(E.place, "=", E1.place, "-", T.place)
                return E
                
            case 11:
                E = RHS.pop()
                T = StackItem(LHS, E.place)
                return T

            case 12:
                T1 = RHS.pop()
                RHS.pop()
                F = RHS.pop()
                T = StackItem(LHS, self.newtemp())
                self.gen(T.place, "=", T1.place, "*", F.place)
                return T

            case 13:
                T1 = RHS.pop()
                RHS.pop()
                F = RHS.pop()
                T = StackItem(LHS, self.newtemp())
                self.gen(T.place, "=", T1.place, "/", F.place)
                return T

            case 14:
                F = RHS.pop()
                T = StackItem(LHS, F.place)
                return T

            case 15:
                E = RHS.pop()
                F = StackItem(LHS, E.place)
                return F

            case 16:
                id = RHS.pop()
                F = StackItem(LHS, id.place)
                return F

            case 17:
                B = RHS.pop()
                RHS.pop()
                M = RHS.pop()
                C = RHS.pop()

                self.backpatch(B.false, M.quad)

                B1 = StackItem("B")
                B1.true = list(set(C.true + B.true))
                B1.false = list(C.false)
                return B1

            case 18:
                C = RHS.pop()

                B = StackItem(LHS)
                B.true = list(C.true)
                B.false = list(C.false)
                return B

            case 19:
                C = RHS.pop()
                RHS.pop()
                M = RHS.pop()
                D = RHS.pop()

                self.backpatch(C.true, M.quad)

                C1 = StackItem("C")
                C1.false = list(set(C.false + D.false))
                C1.true = list(D.true)
                return C1

            case 20:
                D = RHS.pop()

                C = StackItem(LHS)
                C.true = list(D.true)
                C.false = list(D.false)
                return C

            case 21:
                RHS.pop()
                G = RHS.pop()

                D = StackItem("D")
                D.true = list(G.false)
                D.false = list(G.true)
                return D

            case 22:
                G = RHS.pop()

                D = StackItem("D")
                D.true = list(G.true)
                D.false = list(G.false)
                return D

            case 23:
                id = RHS.pop()

                E = StackItem("E")
                E.true = [self.nextQuad()]
                E.false = [self.nextQuad()+1]

                self.gen("if", id.place, "goto")
                self.gen("goto")

                return E

            case 24:
                id1 = RHS.pop()
                RHS.pop()
                id2 = RHS.pop()

                G = StackItem("G")
                G.true = [self.nextQuad()]
                G.false = [self.nextQuad()+1]

                self.gen("if", id1.place, "relop", id2.place, "goto")
                self.gen("goto")

                return G
            case 25:
                A=RHS.pop()
                self.gen("goto")
                return StackItem("X")

    def generateTAC(self):
        output=''
        if self.parse_input_tokens():
            i = 0
            for line in self.code:
                print(f"{i:>4}:  ", end="")
                output+=str(f"{i:>4}:")
                print(line)
                output+=line+'\n'
                i += 1
            print(f"{i:>4}:  ")
            output+=str(f"{i:>4}:  ")
        return output

    def parse_input_tokens(self):
        stack = [0]
        self.input_tokens.append('$')

        i = 0
        try:
            while True:
                state = stack[-1]
                token = self.input_tokens[i]
                # print(state, token)
                if token not in keywords + operators + ['$']:
                    action = self.action_table[(state, "id")]
                else:
                    action = self.action_table[(state, token)]

                if action[0] == 's':
                    if token not in keywords + operators + ['$']:
                        stack.append(StackItem("id", token))
                    else:
                        stack.append(StackItem(token))

                    stack.append(int(action[1:]))
                    i += 1

                elif action[0] == 'r':
                    production_index = int(action[1:])
                    production = self.productions[production_index]
                    popped_items = []
                    for _ in range(len(production)-1):
                        stack.pop()
                        popped_items.append(stack.pop())

                    state = stack[-1]
                    stack.append(self.semantic_action(
                        production_index, production[0], popped_items))
                    
                    stack.append(int(self.goto_table[(state, production[0])]))

                elif action == 'acc':
                    return True

                else:
                    print("[ERROR] INVALID STREAM OF TOKENS")
                    return False

        except:
            print("[ERROR] INVAID STREAM OF TOKENS")
            return False



input_string = "for id = id + id ; id relop id ; id = id + id do id = id * id"

tac = TAC_generator(input_string, productions, action_table, goto_table)
tac.generateTAC()


# from tkinter import *
# from tkinter import ttk

# #Create an instance of Tkinter frame
# win= Tk()
# win.geometry("800x500")

# def display_text():
#    global entry
#    string= entry.get()
#    three_A_C=TAC_generator(string, productions, action_table, goto_table)
#    code=three_A_C.generateTAC()

#    label.insert('1.0',code)
   
# def clear_text():
#     label.delete("1.0",END)
# #Initialize a Label to display the User Input
# label=Text(win,font=("Courier 9 bold"))
# label.place(x=200,y=130,height=350,width=400)

# #Create an Entry widget to accept User Input
# Input_label=Label(win,text="Input",font="Courier 15 bold")
# Input_label.place(x=10,y=25)
# entry= Entry(win, width= 120)
# entry.focus_set()
# entry.place(x=100,y=30,width=600)

# #Create a Button to validate Entry Widget
# ttk.Button(win, text= "Generate",width= 20, command= display_text).place(x=200,y=80)
# ttk.Button(win,text="clear",width= 20, command= clear_text).place(x=400,y=80)
# win.mainloop()

