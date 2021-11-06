import tkinter.colorchooser
from tkinter import *
from tkinter import ttk





def zax():
    import tkinter as tk
    from tkinter import scrolledtext
    from tkinter.ttk import Combobox
    from tkinter import messagebox
    from tkinter import filedialog

    window = tk.Tk()
    window.geometry('900x400')
    window.title("Фрактальные деревья")
    tab_control = ttk.Notebook(window)
    tab1 = ttk.Frame(tab_control)
    tab2 = ttk.Frame(tab_control)
    tab3 = ttk.Frame(tab_control)
    tab_control.add(tab1, text='Основная')
    tab_control.add(tab2, text='Информация о l-истеме')
    tab_control.add(tab3, text='Словарь для данной программы')
    tab_control.pack(expand=1, fill='both')
    lis_ru = []
    rule_pas = dict()

    def tl_run(axi, rule_pas, nangl, thick, ch_d, col_st, col_ls, itr, angl, dl,fn ):
        import turtle as tl
        from random import randint
        def fon1():
            tl.Screen().bgcolor(fn)
        def fon2():
            tl.Screen().bgpic(fn)
        if ch_d==1:
            fon1()
        elif ch_d==2:
            fon2()

        tl.hideturtle()
        tl.tracer(0)
        tl.penup()
        tl.setposition(-100, -390)
        tl.left(nangl)
        tl.pendown()
        thick=thick
        tl.pensize(thick)
        tl.pencolor(col_st)
        axiom = axi
        axmTemp = ""
        dl=dl


        stc = []
        translate=rule_pas

        for _ in range(itr):
            for ch in axiom:
                if ch in translate:
                    axmTemp += translate[ch]
                else:
                    axmTemp += ch
            axiom = axmTemp
            axmTemp = ""

        for i in axiom:
            if i == "-":
                tl.left(angl)
            elif i == "+":
                tl.right(angl)
            elif i == "[":
                thick = thick * 0.75
                tl.pensize(thick)
                stc.append(thick)
                stc.append(tl.xcor())
                stc.append(tl.ycor())
                stc.append(tl.heading())
            elif i == "]":
                tl.penup()
                tl.setheading(stc.pop())
                tl.sety(stc.pop())
                tl.setx(stc.pop())
                thick = stc.pop()
                tl.pensize(thick)
                tl.pendown()
            elif i == "b":
                tl.penup()
                tl.forward(dl)
                tl.pendown()
            elif i == '0':
                tl.pencolor(col_ls)
                tl.pensize(2)
                tl.forward(dl-2)
                tl.pencolor(col_st)
            else:
                tl.forward(dl)

        #def print_screen():
            #ts = tl.getscreen()
            #ts.getcanvas().postscript(file=input("введите название") + ".eps")

        def vivod_tl():
            tl.update()
            t=tl.Turtle()
            t.screen.exitonclick()
            tl.TurtleScreen._RUNNING=True

        soh=1
        if soh == 1:
            #print_screen()
            vivod_tl()

    def vklad1():
        def prover_rule(event):
            rule = entry2.get()
            entry2.delete(0, tk.END)
            rule_s = label12.get()[0]

            for i in rule:
                if i not in "F+-b[]0":
                    res1 = messagebox.askquestion('Внимание',
                                                  f"Правило содержит символы которых нет в алфавит. Они будут работать как и F\n\n"
                                                  f"Добавить?")
                    break
            else:
                res1 = messagebox.askquestion('Внимание', f"Правило впорядке\n\n"
                                                          f"Добавить?")

            def add_ru(res1):
                if res1 == "yes" and len(rule) != 0:
                    lis_ru.append(rule_s + "->" + rule)
                    combo1['values'] = lis_ru
                    rule_pas[rule_s] = rule

            add_ru(res1)

        def prover_axiom(event):

            axi_p = entry1.get()

            for i in axi_p:
                if i not in "F+-b[]":
                    res2 = messagebox.askquestion('Внимание',
                                                  f"Аксиома содержит символы которых нет в алфавит. Они будут работать как и F\n\n"
                                                  f"Добавить?")

                    break
            else:
                res2 = messagebox.askquestion('Внимание', f"Аксиома впорядке\n\n"
                                                          f"Добавить?")
            if res2=="yes":
                global axi
                axi=axi_p


        def start_tl(event):
            itr=spin1.get()
            angl=spin3.get()
            thick=spin2.get()
            dl=spin5.get()
            nangl=spin4.get()

            print(int(itr))
            print(int(angl))
            print(int(thick))
            print(int(dl))
            print(int(nangl))
            print(axi)
            print(rule_pas)
            print(int(ch_d))
            print(col_st)
            print(col_ls)
            print(fn)
            tl_run(itr=int(itr),
                   angl=int(angl),
                   thick=int(thick),
                   dl=int(dl),
                   nangl=int(nangl),
                   axi=axi,
                   rule_pas=rule_pas,
                   ch_d=int(ch_d),
                   col_ls=col_ls,
                   col_st=col_st,
                   fn=fn)




        but1 = tk.Button(tab1, text="Начать")
        but1.bind("<Button-1>", start_tl)
        label=tk.Label(tab1, text=f"Чтобы запустить повторно:\n"
                                  f"1.Закройте старый рисунок\n"
                                  f"2.Нажмите дважды 'Начать'")
        label.grid(row=10, column=1, sticky=W)

        lebel_erorr_ru1 = tk.Label(tab1, text=f"Первое - правило. Второе - для какого символа ")
        lebel_erorr_ru1.grid(row=1, column=3, padx=5, pady=5)
        label1 = tk.Label(tab1, text=f"Аксиома")
        entry1 = tk.Entry(tab1, width=40)
        label1.grid(row=0, column=0, padx=5, pady=5)
        entry1.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        label2 = tk.Label(tab1, text=f"правило")
        entry2 = tk.Entry(tab1, width=40)

        label2.grid(row=1, column=0, padx=5, pady=5)
        entry2.grid(row=1, column=1, padx=5, pady=5)

        #combo = Combobox(tab1, state="readonly", width=1)

        #combo['values'] = ["F", "b", "+", "-", "[", "]"]
        label12=tk.Entry(tab1, width=2)
        label12.grid(row=1, column=2, padx=5, pady=5, sticky=W)

        but2 = tk.Button(tab1, text="Добавить")
        but2.bind("<Button-1>", prover_rule)
        but2.grid(row=1, column=2, sticky=E)

        but3 = tk.Button(tab1, text="Проверить")
        but3.bind("<Button-1>", prover_axiom)
        but3.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        but1.grid(row=10, column=0, padx=5, pady=5)
        label3 = tk.Label(tab1, text=f"Списока правил")
        label3.grid(row=2, column=0, padx=5, pady=5, sticky=W)

        label4 = tk.Label(tab1, text=f"Внимание! Однин символ-одно правило")
        label4.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        combo1 = Combobox(tab1, state="readonly")

        combo1.grid(row=2, column=1, sticky=W)

        label5 = tk.Label(tab1, text=f"Кол-во интераций")
        label5.grid(row=4, column=0, padx=5, pady=5, sticky=W)
        spin1 = Spinbox(tab1, from_=0, to=100, width=5)
        spin1.grid(row=5, column=0, padx=5, pady=5, sticky=W)

        label6 = tk.Label(tab1, text=f"толщина стебля в начале:")
        label6.grid(row=4, column=1, padx=5, pady=5, sticky=W)
        spin2 = Spinbox(tab1, from_=0, to=100, width=5)
        spin2.grid(row=5, column=1, padx=5, pady=5, sticky=W)

        label7 = tk.Label(tab1, text=f"Изменять угол на:")
        label7.grid(row=4, column=2)
        spin3 = Spinbox(tab1, from_=0, to=100, width=5)
        spin3.grid(row=5, column=2, sticky=W)

        label8 = tk.Label(tab1, text=f"Начальный угол")
        label8.grid(row=4, column=3, padx=5, pady=5)
        spin4 = Spinbox(tab1, from_=0, to=100, width=5)
        spin4.grid(row=5, column=3, padx=5, pady=5)

        label9 = tk.Label(tab1, text=f"Длинна шага")
        label9.grid(row=4, column=4, padx=5, pady=5)
        spin5 = Spinbox(tab1, from_=0, to=100, width=5)
        spin5.grid(row=5, column=4, padx=5, pady=5, sticky=W)

        def vib_st(event):
            global col_st
            col_st=tkinter.colorchooser.askcolor()[-1]
            entry3.delete(0, tk.END)
            entry3.insert(0, col_st)
        label10 = tk.Label(tab1, text=f" Впишите или выберите цвет стебля")
        label10.grid(row=6, column=1, padx=5, pady=5)
        but4=tk.Button(tab1, text="Выбрать")
        but4.bind("<Button-1>", vib_st)
        but4.grid( row=7, column=1, sticky=E)
        entry3=tk.Entry(tab1, width=10)
        entry3.grid(row=7, column=1)

        def vib_ls(event):
            global col_ls
            col_ls=tkinter.colorchooser.askcolor()[-1]
            entry4.delete(0, tk.END)
            entry4.insert(0, col_ls)
        label10 = tk.Label(tab1, text=f" Впишите или выберите цвет листа")
        label10.grid(row=6, column=3, padx=5, pady=5)
        but5 = tk.Button(tab1, text="Выбрать")
        but5.bind("<Button-1>", vib_ls)
        but5.grid(row=7, column=3, sticky=E)
        entry4 = tk.Entry(tab1, width=10)
        entry4.grid(row=7, column=3)


        def vib_fn(event):
            global fn
            fn = tkinter.colorchooser.askcolor()[-1]
            entry5.delete(0, tk.END)
            entry5.insert(0, fn)
        but6 = tk.Button(tab1, text="Выбрать")
        but6.bind("<Button-1>", vib_fn)
        but6.grid(row=9, column=1, sticky=E)
        entry5 = tk.Entry(tab1, width=10)
        entry5.grid(row=9, column=1, )

        def vib_photo(event):
            global fn
            fn = filedialog.askopenfilename(filetypes=(("gif files","*.gif"),("all files","*.*")))
            entry6.delete(0, tk.END)
            entry6.insert(0, fn)

        but7 = tk.Button(tab1, text="Выбрать")
        but7.bind("<Button-1>", vib_photo)
        but7.grid(row=9, column=3, sticky=E)
        entry6 = tk.Entry(tab1, width=10)
        entry6.grid(row=9, column=3)

        def clicked1():
            global ch_d
            ch_d=1

        def clicked2():
            global ch_d
            ch_d = 2




        selected = IntVar()
        rad1 = Radiobutton(tab1, text='Однотонный фон', value=1, variable=selected, command=clicked1)
        rad2 = Radiobutton(tab1, text='Фото  под  фон', value=2, variable=selected, command=clicked2)
        rad1.grid(row=8, column=1)
        rad2.grid(row=8, column=3)


    vklad1()

    def vklad2():

        txt = scrolledtext.ScrolledText(tab2, width=100, height=20)
        txt.grid(column=0, row=0, padx=5, pady=5)
        txt.insert(INSERT, "Немного информация о l-системе\n\n"
                           "Понятие L-систем появилось в 1968 году благодаря Аристриду Линденмайеру, датскому "
                           "математику и биологу. "
                           "При этом вначале их предполагалось использовать лишь при изучении формальных языков и в "
                           "некоторых биологических моделях селекции. Однако выяснилось, "
                           "что на основе L-систем могут быть построены многие известные фракталы, такие как ковер "
                           "Серпинского, снежинка Коха, и другие.\n\n "
                           "Несколько позже L-системы стали использовать для генерации растительных форм, таких как "
                           "листья, кусты и деревья (в большинстве компьютерных игр растения ландшафтов генерируются "
                           "именно L-системами).\n\n "
                           "При графической реализации L-систем используется turtle-графика – так называемая "
                           "'черепашья' графика. "
                           " Правила в этой графике весьма просты, и заключаются в следующем."
                           "Точка (черепашка) дискретными шагами движется по экрану и прочерчивает за собой след, "
                           "при необходимости возможно перемещение точки без оставления следа. "
                           "В каждый момент времени координаты и состояние точки определяется тремя параметрами на "
                           "плоскости: координаты точки и направление, в котором будет двигаться точка. "
                           "Точка может распознавать и выполнять некоторую последовательность команд, состоящую из "
                           "последовательностей символов (или групп символов в более сложном случае), читающихся "
                           "слева направо. "
                           "Ниже в таблице 1 приведены наиболее часто используемые символы последовательности и их "
                           "назначение.\n\n "
                           "")
        txt.configure(state='disabled')

    vklad2()

    def vklad3():
        txt = scrolledtext.ScrolledText(tab3, width=100, height=20)
        txt.grid(column=4, row=5, padx=5, pady=5)
        txt.insert(INSERT, "  Символ последовательности       Назначение (интерпретация)\n"
                           "  F                               Перемещение на 1 шаг вперед с прорисовкой следа.\n"
                           "  b                               Перемещение на 1 шаг вперед без прорисовки следа.\n"
                           "  [                               Открыть ветвь.\n"
                           "  ]                               Закрыть ветвь.\n"
                           "  +                               Увеличение угла на указанную величину.\n"
                           "  -                               Уменьшение угла на указанную величину.\n"
                           "  0                               Нарисовать лист\n")
        txt.configure(state='disabled')

    vklad3()
    window.resizable(width=False, height=False)
    window.mainloop()


zax()
