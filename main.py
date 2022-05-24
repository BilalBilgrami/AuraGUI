import tkinter as tk
import pandas as pd
import numpy as np
from pandas import DataFrame
# import csv

root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=300)
canvas1.pack()

input_word = tk.Entry(root)
canvas1.create_window(200, 140, window=input_word)


def get_data():
    my_input = tk.Label(root, text=input_word.get())
    word = input_word.get()
    length = len(word)
    df = []
    with open('C:/Alphabets/main.src', 'w'):
        pass
    with open('C:/Alphabets/main.dat', 'w'):
        pass

    for x in range(len(word)):
        PATH = r'C:\Alphabets\c' + word[x] + '.csv'
        read_points = pd.read_csv(PATH, skip_blank_lines=False)  # read the csv file using the 'PATH' variable
        df.append(DataFrame(read_points, columns=['m', 'x', 'y']))  # assign column names

        # print(empty[0])
        val = df[x]['x'].values[0]
        print(val)
        print(df[x])

    P = 1
    D = 32
    # z = 0
    # print(word[1]) for x in range(len(df[-1]['x'].index)):
    for x in range(length):
        z = 0
        with open('C:/Alphabets/main.src', 'a') as f:
            f.write('SPTP XP' + str(P) + ', $TOOL = STOOL2(FP1), $BASE = SBASE(FP1.BASE_NO),')
            f.write('\n')
            P += 1
            for i in range(len(df[x])-1):

                if np.isnan(df[x]['x'].values[z]):
                    f.write('SPTP XP' + str(P) + ' WITH $VEL_AXIS[1] = SVEL_JOINT(100.0), $TOOL = STOOL2(FP' + str(
                        P) + '), $BASE = SBASE(FP' + str(P) + '.BASE_NO), $IPO_MODE = SIPO_MODE(FP' + str(
                        P) + '.IPO_FRAME), $LOAD = SLOAD(FP' + str(
                        P) + '.TOOL_NO), $ACC_AXIS[1] = SACC_JOINT(PPDAT' + str(
                        P) + '), $APO = SAPO_PTP(PPDAT' + str(P) + '), $GEAR_JERK[1] = SGEAR_JERK(PPDAT' + str(
                        P) + '), $COLLMON_TOL_PRO[1] = USE_CM_PRO_VALUES(0)')
                    # z+=1

                elif df[x]['m'].values[i+1] == 'c':
                    f.write('SCIRC XP' + str(P) + ', XP' + str(
                        P + 1) + ' WITH $VEL = SVEL_CP(2.0, , LCPDAT14), $TOOL = STOOL2(FP18), $BASE = SBASE(FP18.BASE_NO)')
                    P += 1
                    # z+=1

                else:
                    f.write('SLIN XP' + str(P) + ' WITH $VEL = SVEL_CP(2.0, , LCPDAT' + str(
                        D) + '), $TOOL = STOOL2(FP' + str(P) + '), $BASE = SBASE(FP' + str(
                        P) + '.BASE_NO), $IPO_MODE = SIPO_MODE(FP' + str(P) + '.IPO_FRAME), $LOAD = SLOAD(FP' + str(
                        P) + '.TOOL_NO), $ACC = SACC_CP(LCPDAT' + str(D) + '), $ORI_TYPE = SORI_TYP(LCPDAT' + str(
                        D) + '), $APO = SAPO(LCPDAT' + str(D) + '), $JERK = SJERK(LCPDAT' + str(
                        D) + '), $COLLMON_TOL_PRO[1] = USE_CM_PRO_VALUES(0)')
                    D += 1
                    # z += 1

                f.write('\n')
                P += 1
                z += 1

    Po = 1
    for x in range(length):
        # r = 0
        space = x * 12
        with open('C:/Alphabets/main.dat', 'a') as f:

            for i in range(len(df[x])):
                if np.isnan(df[x]['x'].values[i]):
                    f.write('DECL E6POS XP' + str(Po) + ' = { X ' + str((df[x]['x'].values[i + 1]) + space) + ', Y ' + str(
                        df[x]['y'].values[
                            i + 1]) + ', Z 0.0, A 0.0, B 90.0, C 90.000018, S 2, T 10, E1 0.0, E2 0.0, E3 0.0, E4 0.0, E5 0.0, E6 0.0 }')
                else:
                    f.write('DECL E6POS XP' + str(Po) + ' = { X ' + str((df[x]['x'].values[i]) + space) + ', Y ' + str(
                        df[x]['y'].values[
                            i]) + ', Z 0.0, A 0.0, B 90.0, C 90.000018, S 2, T 10, E1 0.0, E2 0.0, E3 0.0, E4 0.0, E5 0.0, E6 0.0 }')

                f.write('\n')
                Po += 1
                # r += 1

    canvas1.create_window(200, 230, window=my_input)


button1 = tk.Button(text='Enter', command=get_data)
canvas1.create_window(200, 180, window=button1)

root.mainloop()
