import tkinter as tk
import pandas as pd
import numpy as np
from pandas import DataFrame

root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=300)
canvas1.pack()

input_word = tk.Entry(root)
canvas1.create_window(200, 140, window=input_word)


def get_data():
    my_input = tk.Label(root, text=input_word.get())                # label for text input
    word = input_word.get()                                         # save input text in word variable
    length = len(word)                                              # length of input
    df = []
    with open('C:/Alphabets/main.src', 'w'):                        # clear the .src file
        pass
    with open('C:/Alphabets/main.dat', 'w'):                        # clear the .dat file
        pass

    # For loop that iterates over length of input and save csv data for each letter in df from database
    for x in range(length):
        PATH = r'C:\Alphabets\c' + word[x] + '.csv'
        read_points = pd.read_csv(PATH, skip_blank_lines=False)     # read the csv file using the 'PATH' variable
        df.append(DataFrame(read_points, columns=['m', 'x', 'y']))  # assign column names

        print(df[x])

    P = 1
    D = 32

    # For loop that iterates over length of input and create main.src file
    for x in range(length):

        with open('C:/Alphabets/main.src', 'a') as f:               # create/modify main.src
            f.write('SPTP XP' + str(P) + ', $TOOL = STOOL2(FP1), $BASE = SBASE(FP1.BASE_NO),')
            f.write('\n')
            P += 1

            # For loop that iterates over length of single letter and write commands in src file
            for i in range(len(df[x])-1):                           # one less iteration since base command written before the loop

                if np.isnan(df[x]['x'].values[i]):                  # condition to detect empty cell
                    f.write('SPTP XP' + str(P) + ' WITH $VEL_AXIS[1] = SVEL_JOINT(100.0), $TOOL = STOOL2(FP' + str(
                        P) + '), $BASE = SBASE(FP' + str(P) + '.BASE_NO), $IPO_MODE = SIPO_MODE(FP' + str(
                        P) + '.IPO_FRAME), $LOAD = SLOAD(FP' + str(
                        P) + '.TOOL_NO), $ACC_AXIS[1] = SACC_JOINT(PPDAT' + str(
                        P) + '), $APO = SAPO_PTP(PPDAT' + str(P) + '), $GEAR_JERK[1] = SGEAR_JERK(PPDAT' + str(
                        P) + '), $COLLMON_TOL_PRO[1] = USE_CM_PRO_VALUES(0)')

                elif df[x]['m'].values[i+1] == 'c':                 # condition to identify flag for circular movement
                    f.write('SCIRC XP' + str(P) + ', XP' + str(
                        P + 1) + ' WITH $VEL = SVEL_CP(2.0, , LCPDAT14), $TOOL = STOOL2(FP18), $BASE = SBASE(FP18.BASE_NO)')
                    P += 1

                else:                                               # for linear movement
                    f.write('SLIN XP' + str(P) + ' WITH $VEL = SVEL_CP(2.0, , LCPDAT' + str(
                        D) + '), $TOOL = STOOL2(FP' + str(P) + '), $BASE = SBASE(FP' + str(
                        P) + '.BASE_NO), $IPO_MODE = SIPO_MODE(FP' + str(P) + '.IPO_FRAME), $LOAD = SLOAD(FP' + str(
                        P) + '.TOOL_NO), $ACC = SACC_CP(LCPDAT' + str(D) + '), $ORI_TYPE = SORI_TYP(LCPDAT' + str(
                        D) + '), $APO = SAPO(LCPDAT' + str(D) + '), $JERK = SJERK(LCPDAT' + str(
                        D) + '), $COLLMON_TOL_PRO[1] = USE_CM_PRO_VALUES(0)')
                    D += 1

                f.write('\n')
                P += 1

    Po = 1

    # For loop that iterates over length of input and create main.dat file
    for x in range(length):
        space = x * 12
        with open('C:/Alphabets/main.dat', 'a') as f:               # create/modify main.dat

            # For loop that iterates over length of single letter and write commands in dat file
            for i in range(len(df[x])):                             # length of each letter
                if np.isnan(df[x]['x'].values[i]):                  # condition to detect empty cell
                    f.write('DECL E6POS XP' + str(Po) + ' = { X ' + str((df[x]['x'].values[i + 1]) + space) + ', Y ' + str(
                        df[x]['y'].values[
                            i + 1]) + ', Z 0.0, A 0.0, B 90.0, C 90.000018, S 2, T 10, E1 0.0, E2 0.0, E3 0.0, E4 0.0, E5 0.0, E6 0.0 }')
                else:
                    f.write('DECL E6POS XP' + str(Po) + ' = { X ' + str((df[x]['x'].values[i]) + space) + ', Y ' + str(
                        df[x]['y'].values[
                            i]) + ', Z 0.0, A 0.0, B 90.0, C 90.000018, S 2, T 10, E1 0.0, E2 0.0, E3 0.0, E4 0.0, E5 0.0, E6 0.0 }')

                f.write('\n')
                Po += 1

    canvas1.create_window(200, 230, window=my_input)                # create input window


button1 = tk.Button(text='Enter', command=get_data)                 # create input field
canvas1.create_window(200, 180, window=button1)                     # create input button

root.mainloop()
