from time import sleep
import tkinter as tk
from turtle import*
import turtle
import pyautogui as py
from keyboard import press_and_release as par
def drawing():
        elements = ["Hydrogen","Helium","Lithium","Beryllium","Boron","Carbon","Nitrogen","Oxygen","Fluorine",
                    "Neon","Sodium","Magnesium","Aluminum","Silicon","Phosphorus","Sulfur","Chlorine","Argon",
                    "Potassium","Calcium","Scandium","Titanium","Vanadium","Chromium","Manganese","Iron",
                    "Cobalt","Nickel","Copper","Zinc","Gallium","Germanium","Arsenic","Selenium","Bromine","Krypton",
                    "Rubidium","Strontium","Yttrium","Zirconium","Niobium","Molybdenum","Technetium","Ruthenium",
                    "Rhodium","Palladium","Silver","Cadmium","Indium","Tin","Antimony","Tellurium","Iodine","Xenon",
                    "Cesium","Barium","Lanthanum","Cerium","Praseodymium","Neodymium","Promethium","Samarium",
                    "Europium","Gadolinium","Terbium","Dysprosium","Holmium","Erbium","Thulium","Ytterbium",
                    "Lutetium","Hafnium","Tantalum","Tungsten","Rhenium","Osmium","Iridium","Platinum", "Gold",
                    "Mercury","Thallium","Lead","Bismuth","Polonium","Astatine","Radon","Francium","Radium",
                    "Actinium","Thorium","Protactinium","Uranium","Neptunium","Plutonium","Americium","Curium",
                    "Berkelium", "Californium","Einsteinium","Fermium","Mendelevium","Nobelium","Lawrencium",
                    "Rutherfordium","Dubnium","Seaborgium","Bohrium","Hassium","Meitnerium","Darmstadtium",
                    "Roentgenium","Copernicium","Nihonium","Flerovium","Moscovium","Livermorium","Tennessine",
                    "Oganesson"]

        l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47,
         48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82,
         83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118]

        levels = ["1s", "2s", "2p", "3s", "3p", "4s", "3d", "4p", "5s", "4d", "5p", "6s", "4f", "5d", "6p",
                  "7s", "5f", "6d", "7p"]
        ele = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl',
               'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As',
               'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In',
               'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb',
               'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl',
               'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk',
               'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh',
               'Fl', 'Mc', 'Lv', 'Ts', 'Og']
        def maxi():
                py.keyDown('winleft')
                py.press('up')
                py.keyUp('winleft')
                
        def diag():
                a=int(input("Enter the atomic number: "))
                par("Enter",do_press = True)
                sleep(5)
                l={}
                l1={}
                w=a
                for i in levels:
                        if w==0:
                            break
                        elif i[1]=="s":
                            s=0
                            while s<2:
                                s=s+1
                                w=w-1
                                if w==0:
                                    break            
                            l[i]=s
                        elif i[1]=="p":
                            p = 0
                            while p<6:
                                p=p+1
                                w=w-1
                                if w==0:
                                    break           
                            l[i]=p
                        elif i[1]=="d":
                            d=0
                            while d<10:
                                d=d+1
                                w=w-1
                                if w==0:
                                    break           
                            l[i]=d
                        elif i[1]=="f":
                            f=0
                            while f<14:
                                f=f+1
                                w=w-1
                                if w==0:
                                    break        
                            l[i]=f
                
                K,L,M,N,O,P,Q=0,0,0,0,0,0,0
                for i in l:
                    if i[0]=="1":
                        K=K+l[i]
                    elif i[0]=="2":
                        L=L+l[i]
                    elif i[0]=="3":
                        M=M+l[i]
                    elif i[0]=="4":
                        N=N+l[i]
                    elif i[0]=="5":
                        O=O+l[i]
                    elif i[0]=="6":
                        P = P+l[i]
                    elif i[0]=="7":
                        Q=Q+l[i]
                if K!=0:
                        l1["K"]=K
                if L!=0:
                        l1["L"]=L
                if M!=0:
                        l1["M"]=M
                if N!=0:
                        l1["N"]=N
                if O!=0:
                        l1["O"]=O
                if P!=0:
                        l1["P"]=P

                if Q!=0:
                        l1["Q"]=Q
                
                k,l,m,n,o,p,q = K,L,M,N,O,P,Q
                t = turtle.Turtle()
                t.penup()
                t.goto(-705,100)
                t.pendown()
                t.write("Electron shell Diagram is:-",font=("Jokerman", 25, "bold"))
                t.hideturtle()
                up()
                fd(100)
                backward(100)
                down()
                speed(0)
                pensize(2)
                shape("circle")
                shapesize(.2)
                maxi()
                up()
                goto(0,-100)
                seth(90)
                fd(12)
                down()
                write(ele[a-1],align  = "center", font = ("Javanese text",25))
                up()
                seth(-90)
                fd(14)
                down()
                write(elements[a-1],align="center", font = ("Javanese text",13))
                up()
                goto(0,-100)
                seth(-90)
                fd(50)
                seth(180)
                down()
                while K>0:
                    circle(-80)
                    dot(11)
                    circle(-80,(360/k))
                    K = K-1
                    if K == 0:
                        up()
                        goto(0,-150)
                        seth(-90)
                        fd(30)
                        seth(180)
                        down()
                while L>0:
                    circle(-110)
                    dot(11)
                    circle(-110,(360/l))
                    L = L-1
                    if L == 0:
                        up()
                        goto(0,-180)
                        seth(-90)
                        fd(30)
                        seth(180)
                        down()
                while M>0:
                    circle(-140)
                    dot(11)
                    circle(-140,(360/m))
                    M = M-1
                    if M == 0:
                        up()
                        goto(0,-210)
                        seth(-90)
                        fd(30)
                        seth(180)
                        down()
                while N>0:
                    circle(-170)
                    dot(11)
                    circle(-170,(360/n))
                    N = N-1
                    if N == 0:
                        up()
                        goto(0,-240)
                        seth(-90)
                        fd(30)
                        seth(180)
                        down()
                while O>0:
                    circle(-200)
                    dot(11)
                    circle(-200,(360/o))
                    O = O-1
                    if O == 0:
                        up()
                        goto(0,-270)
                        seth(-90)
                        fd(30)
                        seth(180)
                        down()
                while P>0:
                    circle(-230)
                    dot(11)
                    circle(-230,(360/p))
                    P = P-1
                    if P== 0:
                        up()
                        goto(0,-300)
                        seth(-90)
                        fd(30)
                        seth(180)
                        down()
                
                while Q>0:
                    circle(-260)
                    dot(11)
                    circle(-260,(360/q))
                    Q = Q-1
                    if Q == 0:
                        up()
                        goto(0,-330)
                        seth(-90)
                        fd(30)
                        seth(180)
                        down()
                        hideturtle()
        diag()
        sleep(1)

#Data Sourced from Wikipedia
Element={1:{
            "Name": "Hydrogen",
            "Appearance": "colorless gas",
            "Atomic Mass": 1.008,
            "Boil": 20.271,
            "Category": "diatomic nonmetal",
            "Density": 0.08988,
            "Discovered by": "Henry Cavendish",
            "Melt": 13.99,
            "Molar heat": 28.836,
            "Named by": "Antoine Lavoisier",
            "Number": 1,
            "Period": 1,
            "Group": 1,
            "Phase": "Gas",
            "Electronic configuration": "1s1",
            "Block": "s"},
        2:{ "Name": "Helium",
            "Appearance": "colorless gas, exhibiting a red-orange glow when placed in a high-voltage electric field",
            "Atomic Mass": 4.0026022,
            "Boil": 4.222,
            "Category": "noble gas",
            "Density": 0.1786,
            "Discovered by": "Pierre Janssen",
            "Melt": 0.95,
            "Molar heat": "null",
            "Named by": "null",
            "Number": 2,
            "Period": 1,
            "Group": 18,
            "Phase": "Gas",
            "Electronic configuration": "1s2",
            "Electron configuration semantic": "1s2",
            "Block": "s"},
        3:{"Name": "Lithium",
            "Appearance": "silvery-white",
            "Atomic Mass": 6.94,
            "Boil": 1603,
            "Category": "alkali metal",
            "Density": 0.534,
            "Discovered by": "Johan August Arfwedson",
            "Melt": 453.65,
            "Molar heat": 24.86,
            "Named by": "null",
            "Number": 3,
            "Period": 2,
            "Group": 1,
            "Phase": "Solid",
            "Block": "s"},
        4:{"Name": "Beryllium",
            "Appearance": "white-gray metallic",
            "Atomic Mass": 9.01218315,
            "Boil": 2742,
            "Category": "alkaline earth metal",
            "Density": 1.85,
            "Discovered by": "Louis Nicolas Vauquelin",
            "Melt": 1560,
            "Molar heat": 16.443,
            "Named by": "null",
            "Number": 4,
            "Period": 2,
            "Group": 2,
            "Phase": "Solid",
            "Summary": "Beryllium is a chemical element with Symbol Be and atomic Number 4. It is created through stellar nucleosynthesis and is a relatively rare element in the universe. It is a divalent element which occurs naturally only in combination with other elements in minerals.",
            "Symbol": "Be",
            "Electronic configuration": "1s2 2s2",
           
            "Block": "s"},
        5:{"Name": "Boron",
            "Appearance": "black-brown",
            "Atomic Mass": 10.81,
            "Boil": 4200,
            "Category": "metalloid",
            "Density": 2.08,
            "Discovered by": "Joseph Louis Gay-Lussac",
            "Melt": 2349,
            "Molar heat": 11.087,
            "Named by": "null",
            "Number": 5,
            "Period": 2,
            "Group": 13,
            "Phase": "Solid",
            "spectral_img": "null",
            "Summary": "Boron is a metalloid chemical element with Symbol B and atomic Number 5. Produced entirely by cosmic ray spallation and supernovae and not by stellar nucleosynthesis, it is a low-abundance element in both the Solar system and the Earth's crust. Boron is concentrated on Earth by the water-solubility of its more common naturally occurring compounds, the borate minerals.",
            "Symbol": "B",
            "Shells": [
                2,
                3
            ],
            "Electronic configuration": "1s2 2s2 2p1",
            "Electron configuration semantic": "[He] 2s2 2p1",
            
            "Block": "p"},
        6:{"Name": "Carbon",
            "Appearance": "null",
            "Atomic Mass": 12.011,
            "Boil": "null",
            "Category": "polyatomic nonmetal",
            "Density": 1.821,
            "Discovered by": "Ancient Egypt",
            "Melt": "null",
            "Molar heat": 8.517,
            "Named by": "null",
            "Number": 6,
            "Period": 2,
            "Group": 14,
            "Phase": "Solid",
            "Summary": "Carbon (from Latin:carbo \"coal\") is a chemical element with Symbol C and atomic Number 6. On the Periodic table, it is the first (row 2) of six elements in column (Group) 14, which have in common the composition of their outer electron shell. It is nonmetallic and tetravalent—making four electrons available to form covalent chemical bonds.",
            "Symbol": "C",
            "Shells": [
                2,
                4
            ],
            "Electronic configuration": "1s2 2s2 2p2",
            "Electron configuration semantic": "[He] 2s2 2p2",
            
            "Block": "p"},
        7:{"Name": "Nitrogen",
            "Appearance": "colorless gas, liquid or solid",
            "Atomic Mass": 14.007,
            "Boil": 77.355,
            "Category": "diatomic nonmetal",
            "Density": 1.251,
            "Discovered by": "Daniel Rutherford",
            "Melt": 63.15,
            "Molar heat": "null",
            "Named by": "Jean-Antoine Chaptal",
            "Number": 7,
            "Period": 2,
            "Group": 15,
            "Phase": "Gas",
    
            "Summary": "Nitrogen is a chemical element with Symbol N and atomic Number 7. It is the lightest pnictogen and at room temperature, it is a transparent, odorless diatomic gas. Nitrogen is a common element in the universe, estimated at about seventh in total abundance in the Milky Way and the Solar System.",
            "Symbol": "N",
            "Shells": [
                2,
                5
            ],
            "Electronic configuration": "1s2 2s2 2p3",
            "Electron configuration semantic": "[He] 2s2 2p3",
            
            "Block": "p"
        },
        8:{
            "Name": "Oxygen",
            "Appearance": "null",
            "Atomic Mass": 15.999,
            "Boil": 90.188,
            "Category": "diatomic nonmetal",
            "Density": 1.429,
            "Discovered by": "Carl Wilhelm Scheele",
            "Melt": 54.36,
            "Molar heat": "null",
            "Named by": "Antoine Lavoisier",
            "Number": 8,
            "Period": 2,
            "Group": 16,
            "Phase": "Gas",
            "Summary": "Oxygen is a chemical element with Symbol O and atomic Number 8. It is a member of the chalcogen Group on the Periodic table and is a highly reactive nonmetal and oxidizing agent that readily forms compounds (notably oxides) with most elements. By mass, oxygen is the third-most abundant element in the universe, after hydrogen and helium.",
            "Symbol": "O",
           
            "Shells": [
                2,
                6
            ],
            "Electronic configuration": "1s2 2s2 2p4",
            "Electron configuration semantic": "[He] 2s2 2p4",
            
        
            "Block": "p"
        },
        9:{
            "Name": "Fluorine",
            "Appearance": "null",
            "Atomic Mass": 18.9984031636,
            "Boil": 85.03,
            "Category": "diatomic nonmetal",
            "Density": 1.696,
            "Discovered by": "André-Marie Ampère",
            "Melt": 53.48,
            "Molar heat": "null",
            "Named by": "Humphry Davy",
            "Number": 9,
            "Period": 2,
            "Group": 17,
            "Phase": "Gas",
            
            "Summary": "Fluorine is a chemical element with Symbol F and atomic Number 9. It is the lightest halogen and exists as a highly toxic pale yellow diatomic gas at standard conditions. As the most electronegative element, it is extremely reactive:almost all other elements, including some noble gases, form compounds with fluorine.",
            "Symbol": "F",
           
            "Shells": [
                2,
                7
            ],
            "Electronic configuration": "1s2 2s2 2p5",
            "Electron configuration semantic": "[He] 2s2 2p5",
            
           
            "Block": "p"
        },
        10:{
            "Name": "Neon",
            "Appearance": "colorless gas exhibiting an orange-red glow when placed in a high voltage electric field",
            "Atomic Mass": 20.17976,
            "Boil": 27.104,
            "Category": "noble gas",
            "Density": 0.9002,
            "Discovered by": "Morris Travers",
            "Melt": 24.56,
            "Molar heat": "null",
            "Named by": "null",
            "Number": 10,
            "Period": 2,
            "Group": 18,
            "Phase": "Gas",
        
            "Summary": "Neon is a chemical element with Symbol Ne and atomic Number 10. It is in Group 18 (noble gases) of the Periodic table. Neon is a colorless, odorless, inert monatomic gas under standard conditions, with about two-thirds the Density of air.",
            "Symbol": "Ne",
            
            "Shells": [
                2,
                8
            ],
            "Electronic configuration": "1s2 2s2 2p6",
            "Electron configuration semantic": "[He] 2s2 2p6",
            
            "Block": "p"
        },
        11:{
            "Name": "Sodium",
            "Appearance": "silvery white metallic",
            "Atomic Mass": 22.989769282,
            "Boil": 1156.09,
            "Category": "alkali metal",
            "Density": 0.968,
            "Discovered by": "Humphry Davy",
            "Melt": 370.944,
            "Molar heat": 28.23,
            "Named by": "null",
            "Number": 11,
            "Period": 3,
            "Group": 1,
            "Phase": "Solid",
        
            "Summary": "Sodium /ˈsoʊdiəm/ is a chemical element with Symbol Na (from Ancient Greek Νάτριο) and atomic Number 11. It is a soft, silver-white, highly reactive metal. In the Periodic table it is in column 1 (alkali metals), and shares with the other six elements in that column that it has a single electron in its outer shell, which it readily donates, creating a positively charged atom - a cation.",
            "Symbol": "Na",
            
            "Shells": [
                2,
                8,
                1
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s1",
            "Electron configuration semantic": "[Ne] 3s1",
            
                       "Block": "s"
        },
        12:{
            "Name": "Magnesium",
            "Appearance": "shiny grey solid",
            "Atomic Mass": 24.305,
            "Boil": 1363,
            "Category": "alkaline earth metal",
            "Density": 1.738,
            "Discovered by": "Joseph Black",
            "Melt": 923,
            "Molar heat": 24.869,
            "Named by": "null",
            "Number": 12,
            "Period": 3,
            "Group": 2,
            "Phase": "Solid",
            
            "Summary": "Magnesium is a chemical element with Symbol Mg and atomic Number 12. It is a shiny gray solid which bears a close physical resemblance to the other five elements in the second column (Group 2, or alkaline earth metals) of the Periodic table:they each have the same Electronic configuration in their outer electron shell producing a similar crystal structure. Magnesium is the ninth most abundant element in the universe.",
            "Symbol": "Mg",
           
            "Shells": [
                2,
                8,
                2
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2",
            "Electron configuration semantic": "[Ne] 3s2",
            
            
            "Block": "s"
        },
        13:{
            "Name": "Aluminium",
            "Appearance": "silvery gray metallic",
            "Atomic Mass": 26.98153857,
            "Boil": 2743,
            "Category": "post-transition metal",
            "Density": 2.7,
            "Discovered by": "null",
            "Melt": 933.47,
            "Molar heat": 24.2,
            "Named by": "Humphry Davy",
            "Number": 13,
            "Period": 3,
            "Group": 13,
            "Phase": "Solid",
            
            "Summary": "Aluminium (or aluminum; see different endings) is a chemical element in the boron Group with Symbol Al and atomic Number 13. It is a silvery-white, soft, nonmagnetic, ductile metal. Aluminium is the third most abundant element (after oxygen and silicon), and the most abundant metal, in the Earth's crust.",
            "Symbol": "Al",
            "xpos": 13,
            
            "Shells": [
                2,
                8,
                3
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p1",
            "Electron configuration semantic": "[Ne] 3s2 3p1",
           
            "Block": "p"
        },
        14:{
            "Name": "Silicon",
            "Appearance": "crystalline, reflective with bluish-tinged faces",
            "Atomic Mass": 28.085,
            "Boil": 3538,
            "Category": "metalloid",
            "Density": 2.329,
            "Discovered by": "Jöns Jacob Berzelius",
            "Melt": 1687,
            "Molar heat": 19.789,
            "Named by": "Thomas Thomson (chemist)",
            "Number": 14,
            "Period": 3,
            "Group": 14,
            "Phase": "Solid",
            
            "Summary": "Silicon is a chemical element with Symbol Si and atomic Number 14. It is a tetravalent metalloid, more reactive than germanium, the metalloid directly below it in the table. Controversy about silicon's character dates to its discovery.",
            "Symbol": "Si",
            
            "Shells": [
                2,
                8,
                4
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p2",
            "Electron configuration semantic": "[Ne] 3s2 3p2",
            
          
            "Block": "p"
        },
        15:{
            "Name": "Phosphorus",
            "Appearance": "colourless, waxy white, yellow, scarlet, red, violet, black",
            "Atomic Mass": 30.9737619985,
            "Boil": "null",
            "Category": "polyatomic nonmetal",
            "Density": 1.823,
            "Discovered by": "Hennig Brand",
            "Melt": "null",
            "Molar heat": 23.824,
            "Named by": "null",
            "Number": 15,
            "Period": 3,
            "Group": 15,
            "Phase": "Solid",
           
            "Summary": "Phosphorus is a chemical element with Symbol P and atomic Number 15. As an element, phosphorus exists in two major forms—white phosphorus and red phosphorus—but due to its high reactivity, phosphorus is never found as a free element on Earth. Instead phosphorus-containing minerals are almost always present in their maximally oxidised state, as inorganic phosphate rocks.",
            "Symbol": "P",
            
            "Shells": [
                2,
                8,
                5
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p3",
            "Electron configuration semantic": "[Ne] 3s2 3p3",
          
            "Block": "p"
        },
        16:{
            "Name": "Sulfur",
            "Appearance": "lemon yellow sintered microcrystals",
            "Atomic Mass": 32.06,
            "Boil": 717.8,
            "Category": "polyatomic nonmetal",
            "Density": 2.07,
            "Discovered by": "Ancient china",
            "Melt": 388.36,
            "Molar heat": 22.75,
            "Named by": "null",
            "Number": 16,
            "Period": 3,
            "Group": 16,
            "Phase": "Solid",
           
            "Summary": "Sulfur or sulphur (see spelling differences) is a chemical element with Symbol S and atomic Number 16. It is an abundant, multivalent non-metal. Under normal conditions, sulfur atoms form cyclic octatomic molecules with chemical formula S8.",
            "Symbol": "S",
            
            "Shells": [
                2,
                8,
                6
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p4",
            "Electron configuration semantic": "[Ne] 3s2 3p4",
            
            "Block": "p"
        },
        17:{
            "Name": "Chlorine",
            "Appearance": "pale yellow-green gas",
            "Atomic Mass": 35.45,
            "Boil": 239.11,
            "Category": "diatomic nonmetal",
            "Density": 3.2,
            "Discovered by": "Carl Wilhelm Scheele",
            "Melt": 171.6,
            "Molar heat": "null",
            "Named by": "null",
            "Number": 17,
            "Period": 3,
            "Group": 17,
            "Phase": "Gas",
           
            "Summary": "Chlorine is a chemical element with Symbol Cl and atomic Number 17. It also has a relative Atomic Mass of 35.5. Chlorine is in the halogen Group (17) and is the second lightest halogen following fluorine.",
            "Symbol": "Cl",
            
            "Shells": [
                2,
                8,
                7
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p5",
            "Electron configuration semantic": "[Ne] 3s2 3p5",
            
            "Block": "p"
        },
        18:{
            "Name": "Argon",
            "Appearance": "colorless gas exhibiting a lilac/violet glow when placed in a high voltage electric field",
            "Atomic Mass": 39.9481,
            "Boil": 87.302,
            "Category": "noble gas",
            "Density": 1.784,
            "Discovered by": "Lord Rayleigh",
            "Melt": 83.81,
            "Molar heat": "null",
            "Named by": "null",
            "Number": 18,
            "Period": 3,
            "Group": 18,
            "Phase": "Gas",
           
            "Summary": "Argon is a chemical element with Symbol Ar and atomic Number 18. It is in Group 18 of the Periodic table and is a noble gas. Argon is the third most common gas in the Earth's atmosphere, at 0.934% (9,340 ppmv), making it over twice as abundant as the next most common atmospheric gas, water vapor (which averages about 4000 ppmv, but varies greatly), and 23 times as abundant as the next most common non-condensing atmospheric gas, carbon dioxide (400 ppmv), and more than 500 times as abundant as the next most common noble gas, neon (18 ppmv).",
            "Symbol": "Ar",
            
            "Shells": [
                2,
                8,
                8
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6",
            "Electron configuration semantic": "[Ne] 3s2 3p6",
          
            "Block": "p"
        },
        19:{
            "Name": "Potassium",
            "Appearance": "silvery gray",
            "Atomic Mass": 39.09831,
            "Boil": 1032,
            "Category": "alkali metal",
            "Density": 0.862,
            "Discovered by": "Humphry Davy",
            "Melt": 336.7,
            "Molar heat": 29.6,
            "Named by": "null",
            "Number": 19,
            "Period": 4,
            "Group": 1,
            "Phase": "Solid",
            
            "Summary": "Potassium is a chemical element with Symbol K (derived from Neo-Latin, kalium) and atomic Number 19. It was first isolated from potash, the ashes of plants, from which its Name is derived. In the Periodic table, potassium is one of seven elements in column (Group) 1 (alkali metals):they all have a single valence electron in their outer electron shell, which they readily give up to create an atom with a positive charge - a cation, and combine with anions to form salts.",
            "Symbol": "K",
           
            "Shells": [
                2,
                8,
                8,
                1
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s1",
            "Electron configuration semantic": "[Ar] 4s1",
           
            "Block": "s"
        },
        20:{
            "Name": "Calcium",
            "Appearance": "null",
            "Atomic Mass": 40.0784,
            "Boil": 1757,
            "Category": "alkaline earth metal",
            "Density": 1.55,
            "Discovered by": "Humphry Davy",
            "Melt": 1115,
            "Molar heat": 25.929,
            "Named by": "null",
            "Number": 20,
            "Period": 4,
            "Group": 2,
            "Phase": "Solid",
            
            "Summary": "Calcium is a chemical element with Symbol Ca and atomic Number 20. Calcium is a soft gray alkaline earth metal, fifth-most-abundant element by mass in the Earth's crust. The ion Ca2+ is also the fifth-most-abundant dissolved ion in seawater by both molarity and mass, after sodium, chloride, magnesium, and sulfate.",
            "Symbol": "Ca",
           
            "Shells": [
                2,
                8,
                8,
                2
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2",
            "Electron configuration semantic": "[Ar] 4s2",
           
            "Block": "s"
        },
        21:{
            "Name": "Scandium",
            "Appearance": "silvery white",
            "Atomic Mass": 44.9559085,
            "Boil": 3109,
            "Category": "transition metal",
            "Density": 2.985,
            "Discovered by": "Lars Fredrik Nilson",
            "Melt": 1814,
            "Molar heat": 25.52,
            "Named by": "null",
            "Number": 21,
            "Period": 4,
            "Group": 3,
            "Phase": "Solid",
           
            "Summary": "Scandium is a chemical element with Symbol Sc and atomic Number 21. A silvery-white metallic d-Block element, it has historically been sometimes classified as a rare earth element, together with yttrium and the lanthanoids. It was discovered in 1879 by spectral analysis of the minerals euxenite and gadolinite from Scandinavia.",
            "Symbol": "Sc",
           
            "Shells": [
                2,
                8,
                9,
                2
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d1",
            "Electron configuration semantic": "[Ar] 3d1 4s2",
           
            "Block": "d"
        },
        22:{
            "Name": "Titanium",
            "Appearance": "silvery grey-white metallic",
            "Atomic Mass": 47.8671,
            "Boil": 3560,
            "Category": "transition metal",
            "Density": 4.506,
            "Discovered by": "William Gregor",
            "Melt": 1941,
            "Molar heat": 25.06,
            "Named by": "Martin Heinrich Klaproth",
            "Number": 22,
            "Period": 4,
            "Group": 4,
            "Phase": "Solid",
           
            "Summary": "Titanium is a chemical element with Symbol Ti and atomic Number 22. It is a lustrous transition metal with a silver color, low Density and high strength. It is highly resistant to corrosion in sea water, aqua regia and chlorine.",
            "Symbol": "Ti",
            
            "Shells": [
                2,
                8,
                10,
                2
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d2",
            "Electron configuration semantic": "[Ar] 3d2 4s2",
            
            "Block": "d"
        },
        23:{
            "Name": "Vanadium",
            "Appearance": "blue-silver-grey metal",
            "Atomic Mass": 50.94151,
            "Boil": 3680,
            "Category": "transition metal",
            "Density": 6,
            "Discovered by": "Andrés Manuel del Río",
            "Melt": 2183,
            "Molar heat": 24.89,
            "Named by": "Isotopes of vanadium",
            "Number": 23,
            "Period": 4,
            "Group": 5,
            "Phase": "Solid",
           
            "Summary": "Vanadium is a chemical element with Symbol V and atomic Number 23. It is a hard, silvery grey, ductile and malleable transition metal. The element is found only in chemically combined form in nature, but once isolated artificially, the formation of an oxide layer stabilizes the free metal somewhat against further oxidation.",
            "Symbol": "V",
           
            "Shells": [
                2,
                8,
                11,
                2
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d3",
            "Electron configuration semantic": "[Ar] 3d3 4s2",
            
            "Block": "d"
        },
        24:{
            "Name": "Chromium",
            "Appearance": "silvery metallic",
            "Atomic Mass": 51.99616,
            "Boil": 2944,
            "Category": "transition metal",
            "Density": 7.19,
            "Discovered by": "Louis Nicolas Vauquelin",
            "Melt": 2180,
            "Molar heat": 23.35,
            "Named by": "null",
            "Number": 24,
            "Period": 4,
            "Group": 6,
            "Phase": "Solid",
            "Summary": "Chromium is a chemical element with Symbol Cr and atomic Number 24. It is the first element in Group 6. It is a steely-gray, lustrous, hard and brittle metal which takes a high polish, resists tarnishing, and has a high Melting point.",
            "Symbol": "Cr",
           
            "Shells": [
                2,
                8,
                13,
                1
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s1 3d5",
            "Electron configuration semantic": "[Ar] 3d5 4s1",
           
            "Block": "d"
        },
        25:{
            "Name": "Manganese",
            "Appearance": "silvery metallic",
            "Atomic Mass": 54.9380443,
            "Boil": 2334,
            "Category": "transition metal",
            "Density": 7.21,
            "Discovered by": "Torbern Olof Bergman",
            "Melt": 1519,
            "Molar heat": 26.32,
            "Named by": "null",
            "Number": 25,
            "Period": 4,
            "Group": 7,
            "Phase": "Solid",
            
            "Summary": "Manganese is a chemical element with Symbol Mn and atomic Number 25. It is not found as a free element in nature; it is often found in combination with iron, and in many minerals. Manganese is a metal with important industrial metal alloy uses, particularly in stainless steels.",
            "Symbol": "Mn",
           
            "Shells": [
                2,
                8,
                13,
                2
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d5",
            "Electron configuration semantic": "[Ar] 3d5 4s2",
          
            "Block": "d"
        },
        26:{
            "Name": "Iron",
            "Appearance": "lustrous metallic with a grayish tinge",
            "Atomic Mass": 55.8452,
            "Boil": 3134,
            "Category": "transition metal",
            "Density": 7.874,
            "Discovered by": "5000 BC",
            "Melt": 1811,
            "Molar heat": 25.1,
            "Named by": "null",
            "Number": 26,
            "Period": 4,
            "Group": 8,
            "Phase": "Solid",
            
            "Summary": "Iron is a chemical element with Symbol Fe (from Latin:ferrum) and atomic Number 26. It is a metal in the first transition series. It is by mass the most common element on Earth, forming much of Earth's outer and inner core.",
            "Symbol": "Fe",
           
            "Shells": [
                2,
                8,
                14,
                2
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d6",
            "Electron configuration semantic": "[Ar] 3d6 4s2",
            
            "Block": "d"
        },
        27:{
            "Name": "Cobalt",
            "Appearance": "hard lustrous gray metal",
            "Atomic Mass": 58.9331944,
            "Boil": 3200,
            "Category": "transition metal",
            "Density": 8.9,
            "Discovered by": "Georg Brandt",
            "Melt": 1768,
            "Molar heat": 24.81,
            "Named by": "null",
            "Number": 27,
            "Period": 4,
            "Group": 9,
            "Phase": "Solid",
            
            "Summary": "Cobalt is a chemical element with Symbol Co and atomic Number 27. Like nickel, cobalt in the Earth's crust is found only in chemically combined form, save for small deposits found in alloys of natural meteoric iron. The free element, produced by reductive sMelting, is a hard, lustrous, silver-gray metal.",
            "Symbol": "Co",
            
            "Shells": [
                2,
                8,
                15,
                2
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d7",
            "Electron configuration semantic": "[Ar] 3d7 4s2",
            
            "Block": "d"
        },
        28:{
            "Name": "Nickel",
            "Appearance": "lustrous, metallic, and silver with a gold tinge",
            "Atomic Mass": 58.69344,
            "Boil": 3003,
            "Category": "transition metal",
            "Density": 8.908,
            "Discovered by": "Axel Fredrik Cronstedt",
            "Melt": 1728,
            "Molar heat": 26.07,
            "Named by": "null",
            "Number": 28,
            "Period": 4,
            "Group": 10,
            "Phase": "Solid",
            
            "Summary": "Nickel is a chemical element with Symbol Ni and atomic Number 28. It is a silvery-white lustrous metal with a slight golden tinge. Nickel belongs to the transition metals and is hard and ductile.",
            "Symbol": "Ni",
            
            "Shells": [
                2,
                8,
                16,
                2
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d8",
            "Electron configuration semantic": "[Ar] 3d8 4s2",
            
            "Block": "d"
        },
        29:{
            "Name": "Copper",
            "Appearance": "red-orange metallic luster",
            "Atomic Mass": 63.5463,
            "Boil": 2835,
            "Category": "transition metal",
            "Density": 8.96,
            "Discovered by": "Middle East",
            "Melt": 1357.77,
            "Molar heat": 24.44,
            "Named by": "null",
            "Number": 29,
            "Period": 4,
            "Group": 11,
            "Phase": "Solid",
            
            "Summary": "Copper is a chemical element with Symbol Cu (from Latin:cuprum) and atomic Number 29. It is a soft, malleable and ductile metal with very high thermal and electrical conductivity. A freshly exposed surface of pure copper has a reddish-orange color.",
            "Symbol": "Cu",
            
            "Shells": [
                2,
                8,
                18,
                1
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s1 3d10",
            "Electron configuration semantic": "[Ar] 3d10 4s1",
            
            "Block": "d"
        },
        30:{
            "Name": "Zinc",
            "Appearance": "silver-gray",
            "Atomic Mass": 65.382,
            "Boil": 1180,
            "Category": "transition metal",
            "Density": 7.14,
            "Discovered by": "India",
            "Melt": 692.68,
            "Molar heat": 25.47,
            "Named by": "null",
            "Number": 30,
            "Period": 4,
            "Group": 12,
            "Phase": "Solid",
            
            "Summary": "Zinc, in commerce also spelter, is a chemical element with Symbol Zn and atomic Number 30. It is the first element of Group 12 of the Periodic table. In some respects zinc is chemically similar to magnesium:its ion is of similar size and its only common oxidation state is +2.",
            "Symbol": "Zn",
            
            "Shells": [
                2,
                8,
                18,
                2
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10",
            "Electron configuration semantic": "[Ar] 3d10 4s2",
            
            "Block": "d"
        },
        31:{
            "Name": "Gallium",
            "Appearance": "silver-white",
            "Atomic Mass": 69.7231,
            "Boil": 2673,
            "Category": "post-transition metal",
            "Density": 5.91,
            "Discovered by": "Lecoq de Boisbaudran",
            "Melt": 302.9146,
            "Molar heat": 25.86,
            "Named by": "null",
            "Number": 31,
            "Period": 4,
            "Group": 13,
            "Phase": "Solid",
            
            "Summary": "Gallium is a chemical element with Symbol Ga and atomic Number 31. Elemental gallium does not occur in free form in nature, but as the gallium(III) compounds that are in trace amounts in zinc ores and in bauxite. Gallium is a soft, silvery metal, and elemental gallium is a brittle solid at low temperatures, and Melts at 29.76 °C (85.57 °F) (slightly above room temperature).",
            "Symbol": "Ga",
            
            "Shells": [
                2,
                8,
                18,
                3
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p1",
            "Electron configuration semantic": "[Ar] 3d10 4s2 4p1",
            
            "Block": "p"
        },
       32:{
            "Name": "Germanium",
            "Appearance": "grayish-white",
            "Atomic Mass": 72.6308,
            "Boil": 3106,
            "Category": "metalloid",
            "Density": 5.323,
            "Discovered by": "Clemens Winkler",
            "Melt": 1211.4,
            "Molar heat": 23.222,
            "Named by": "null",
            "Number": 32,
            "Period": 4,
            "Group": 14,
            "Phase": "Solid",
            
            "Summary": "Germanium is a chemical element with Symbol Ge and atomic Number 32. It is a lustrous, hard, grayish-white metalloid in the carbon Group, chemically similar to its Group neighbors tin and silicon. Purified germanium is a semiconductor, with an Appearance most similar to elemental silicon.",
            "Symbol": "Ge",
           
            "Shells": [
                2,
                8,
                18,
                4
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p2",
            "Electron configuration semantic": "[Ar] 3d10 4s2 4p2",
            
            "Block": "p"
        },
        33:{
            "Name": "Arsenic",
            "Appearance": "metallic grey",
            "Atomic Mass": 74.9215956,
            "Boil": "null",
            "Category": "metalloid",
            "Density": 5.727,
            "Discovered by": "Bronze Age",
            "Melt": "null",
            "Molar heat": 24.64,
            "Named by": "null",
            "Number": 33,
            "Period": 4,
            "Group": 15,
            "Phase": "Solid",
            
            "Summary": "Arsenic is a chemical element with Symbol As and atomic Number 33. Arsenic occurs in many minerals, usually in conjunction with sulfur and metals, and also as a pure elemental crystal. Arsenic is a metalloid.",
            "Symbol": "As",
           
            "Shells": [
                2,
                8,
                18,
                5
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p3",
            "Electron configuration semantic": "[Ar] 3d10 4s2 4p3",
            
            "Block": "p"
        },
        34:{
            "Name": "Selenium",
            "Appearance": "black, red, and gray (not pictured) allotropes",
            "Atomic Mass": 78.9718,
            "Boil": 958,
            "Category": "polyatomic nonmetal",
            "Density": 4.81,
            "Discovered by": "Jöns Jakob Berzelius",
            "Melt": 494,
            "Molar heat": 25.363,
            "Named by": "null",
            "Number": 34,
            "Period": 4,
            "Group": 16,
            "Phase": "Solid",
            
            "Summary": "Selenium is a chemical element with Symbol Se and atomic Number 34. It is a nonmetal with properties that are intermediate between those of its Periodic table column-adjacent chalcogen elements sulfur and tellurium. It rarely occurs in its elemental state in nature, or as pure ore compounds.",
            "Symbol": "Se",
            
            "Shells": [
                2,
                8,
                18,
                6
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p4",
            "Electron configuration semantic": "[Ar] 3d10 4s2 4p4",
            
            "Block": "p"
        },
        35:{
            "Name": "Bromine",
            "Appearance": "null",
            "Atomic Mass": 79.904,
            "Boil": 332,
            "Category": "diatomic nonmetal",
            "Density": 3.1028,
            "Discovered by": "Antoine Jérôme Balard",
            "Melt": 265.8,
            "Molar heat": "null",
            "Named by": "null",
            "Number": 35,
            "Period": 4,
            "Group": 17,
            "Phase": "Liquid",
            
            "Summary": "Bromine (from Ancient Greek:βρῶμος, brómos, meaning \"stench\") is a chemical element with Symbol Br, and atomic Number 35. It is a halogen. The element was isolated independently by two chemists, Carl Jacob Löwig and Antoine Jerome Balard, in 1825–1826.",
            "Symbol": "Br",
            
            "Shells": [
                2,
                8,
                18,
                7
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p5",
            "Electron configuration semantic": "[Ar] 3d10 4s2 4p5",
                        "Block": "p"
        },
        36:{
            "Name": "Krypton",
            "Appearance": "colorless gas, exhibiting a whitish glow in a high electric field",
            "Atomic Mass": 83.7982,
            "Boil": 119.93,
            "Category": "noble gas",
            "Density": 3.749,
            "Discovered by": "William Ramsay",
            "Melt": 115.78,
            "Molar heat": "null",
            "Named by": "null",
            "Number": 36,
            "Period": 4,
            "Group": 18,
            "Phase": "Gas",
            
            "Summary": "Krypton (from Greek:κρυπτός kryptos \"the hidden one\") is a chemical element with Symbol Kr and atomic Number 36. It is a member of Group 18 (noble gases) elements. A colorless, odorless, tasteless noble gas, krypton occurs in trace amounts in the atmosphere, is isolated by fractionally distilling liquefied air, and is often used with other rare gases in fluorescent lamps.",
            "Symbol": "Kr",
            
            "Shells": [
                2,
                8,
                18,
                8
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6",
            "Electron configuration semantic": "[Ar] 3d10 4s2 4p6",
           
            "Block": "p"
        },
        37:{
            "Name": "Rubidium",
            "Appearance": "grey white",
            "Atomic Mass": 85.46783,
            "Boil": 961,
            "Category": "alkali metal",
            "Density": 1.532,
            "Discovered by": "Robert Bunsen",
            "Melt": 312.45,
            "Molar heat": 31.06,
            "Named by": "null",
            "Number": 37,
            "Period": 5,
            "Group": 1,
            "Phase": "Solid",
            
            "Summary": "Rubidium is a chemical element with Symbol Rb and atomic Number 37. Rubidium is a soft, silvery-white metallic element of the alkali metal Group, with an Atomic Mass of 85.4678. Elemental rubidium is highly reactive, with properties similar to those of other alkali metals, such as very rapid oxidation in air.",
            "Symbol": "Rb",
            
            "Shells": [
                2,
                8,
                18,
                8,
                1
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1",
            "Electron configuration semantic": "[Kr] 5s1",
           
            "Block": "s"
        },
        38:{
            "Name": "Strontium",
            "Appearance": "null",
            "Atomic Mass": 87.621,
            "Boil": 1650,
            "Category": "alkaline earth metal",
            "Density": 2.64,
            "Discovered by": "William Cruickshank (chemist)",
            "Melt": 1050,
            "Molar heat": 26.4,
            "Named by": "null",
            "Number": 38,
            "Period": 5,
            "Group": 2,
            "Phase": "Solid",
            
            "Summary": "Strontium is a chemical element with Symbol Sr and atomic Number 38. An alkaline earth metal, strontium is a soft silver-white or yellowish metallic element that is highly reactive chemically. The metal turns yellow when it is exposed to air.",
            "Symbol": "Sr",
           
            "Shells": [
                2,
                8,
                18,
                8,
                2
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2",
            "Electron configuration semantic": "[Kr] 5s2",
           
            "Block": "s"
        },
        39:{
            "Name": "Yttrium",
            "Appearance": "silvery white",
            "Atomic Mass": 88.905842,
            "Boil": 3203,
            "Category": "transition metal",
            "Density": 4.472,
            "Discovered by": "Johan Gadolin",
            "Melt": 1799,
            "Molar heat": 26.53,
            "Named by": "null",
            "Number": 39,
            "Period": 5,
            "Group": 3,
            "Phase": "Solid",
         
            "Summary": "Yttrium is a chemical element with Symbol Y and atomic Number 39. It is a silvery-metallic transition metal chemically similar to the lanthanides and it has often been classified as a \"rare earth element\". Yttrium is almost always found combined with the lanthanides in rare earth minerals and is never found in nature as a free element.",
            "Symbol": "Y",
            
            "Shells": [
                2,
                8,
                18,
                9,
                2
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d1",
            "Electron configuration semantic": "[Kr] 4d1 5s2",
           
            "Block": "d"
        },
        40:{
            "Name": "Zirconium",
            "Appearance": "silvery white",
            "Atomic Mass": 91.2242,
            "Boil": 4650,
            "Category": "transition metal",
            "Density": 6.52,
            "Discovered by": "Martin Heinrich Klaproth",
            "Melt": 2128,
            "Molar heat": 25.36,
            "Named by": "null",
            "Number": 40,
            "Period": 5,
            "Group": 4,
            "Phase": "Solid",
            
            "Summary": "Zirconium is a chemical element with Symbol Zr and atomic Number 40. The Name of zirconium is taken from the Name of the mineral zircon, the most important source of zirconium. The word zircon comes from the Persian word zargun زرگون, meaning \"gold-colored\".",
            "Symbol": "Zr",
            
            "Shells": [
                2,
                8,
                18,
                10,
                2
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d2",
            "Electron configuration semantic": "[Kr] 4d2 5s2",
           
            "Block": "d"
        },
        41:{
            "Name": "Niobium",
            "Appearance": "gray metallic, bluish when oxidized",
            "Atomic Mass": 92.906372,
            "Boil": 5017,
            "Category": "transition metal",
            "Density": 8.57,
            "Discovered by": "Charles Hatchett",
            "Melt": 2750,
            "Molar heat": 24.6,
            "Named by": "null",
            "Number": 41,
            "Period": 5,
            "Group": 5,
            "Phase": "Solid",
            
            "Summary": "Niobium, formerly columbium, is a chemical element with Symbol Nb (formerly Cb) and atomic Number 41. It is a soft, grey, ductile transition metal, which is often found in the pyrochlore mineral, the main commercial source for niobium, and columbite. The Name comes from Greek mythology:Niobe, daughter of Tantalus since it is so similar to tantalum.",
            "Symbol": "Nb",
            
            "Shells": [
                2,
                8,
                18,
                12,
                1
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d4",
            "Electron configuration semantic": "[Kr] 4d4 5s1",
            
            "Block": "d"
        },
        42:{
            "Name": "Molybdenum",
            "Appearance": "gray metallic",
            "Atomic Mass": 95.951,
            "Boil": 4912,
            "Category": "transition metal",
            "Density": 10.28,
            "Discovered by": "Carl Wilhelm Scheele",
            "Melt": 2896,
            "Molar heat": 24.06,
            "Named by": "null",
            "Number": 42,
            "Period": 5,
            "Group": 6,
            "Phase": "Solid",
           
            "Summary": "Molybdenum is a chemical element with Symbol Mo and atomic Number 42. The Name is from Neo-Latin molybdaenum, from Ancient Greek Μόλυβδος molybdos, meaning lead, since its ores were confused with lead ores. Molybdenum minerals have been known throughout history, but the element was discovered (in the sense of differentiating it as a new entity from the mineral salts of other metals) in 1778 by Carl Wilhelm Scheele.",
            "Symbol": "Mo",
            
            "Shells": [
                2,
                8,
                18,
                13,
                1
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d5",
            "Electron configuration semantic": "[Kr] 4d5 5s1",
          
            "Block": "d"
        },
        43:{
            "Name": "Technetium",
            "Appearance": "shiny gray metal",
            "Atomic Mass": 98,
            "Boil": 4538,
            "Category": "transition metal",
            "Density": 11,
            "Discovered by": "Emilio Segrè",
            "Melt": 2430,
            "Molar heat": 24.27,
            "Named by": "null",
            "Number": 43,
            "Period": 5,
            "Group": 7,
            "Phase": "Solid",
            
            "Summary": "Technetium (/tɛkˈniːʃiəm/) is a chemical element with Symbol Tc and atomic Number 43. It is the element with the lowest atomic Number in the Periodic table that has no stable isotopes:every form of it is radioactive. Nearly all technetium is produced synthetically, and only minute amounts are found in nature.",
            "Symbol": "Tc",
         
            "Shells": [
                2,
                8,
                18,
                13,
                2
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d5",
            "Electron configuration semantic": "[Kr] 4d5 5s2",
          
            "Block": "d"
        },
        44:{
            "Name": "Ruthenium",
            "Appearance": "silvery white metallic",
            "Atomic Mass": 101.072,
            "Boil": 4423,
            "Category": "transition metal",
            "Density": 12.45,
            "Discovered by": "Karl Ernst Claus",
            "Melt": 2607,
            "Molar heat": 24.06,
            "Named by": "null",
            "Number": 44,
            "Period": 5,
            "Group": 8,
            "Phase": "Solid",
          
            "Summary": "Ruthenium is a chemical element with Symbol Ru and atomic Number 44. It is a rare transition metal belonging to the platinum Group of the Periodic table. Like the other metals of the platinum Group, ruthenium is inert to most other chemicals.",
            "Symbol": "Ru",
           
            "Shells": [
                2,
                8,
                18,
                15,
                1
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d7",
            "Electron configuration semantic": "[Kr] 4d7 5s1",
           
            "Block": "d"
        },
        45:{
            "Name": "Rhodium",
            "Appearance": "silvery white metallic",
            "Atomic Mass": 102.905502,
            "Boil": 3968,
            "Category": "transition metal",
            "Density": 12.41,
            "Discovered by": "William Hyde Wollaston",
            "Melt": 2237,
            "Molar heat": 24.98,
            "Named by": "null",
            "Number": 45,
            "Period": 5,
            "Group": 9,
            "Phase": "Solid",
          
            "Summary": "Rhodium is a chemical element with Symbol Rh and atomic Number 45. It is a rare, silvery-white, hard, and chemically inert transition metal. It is a member of the platinum Group.",
            "Symbol": "Rh",
            
            "Shells": [
                2,
                8,
                18,
                16,
                1
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d8",
            "Electron configuration semantic": "[Kr] 4d8 5s1",
       
            "Block": "d"
        },
        46:{
            "Name": "Palladium",
            "Appearance": "silvery white",
            "Atomic Mass": 106.421,
            "Boil": 3236,
            "Category": "transition metal",
            "Density": 12.023,
            "Discovered by": "William Hyde Wollaston",
            "Melt": 1828.05,
            "Molar heat": 25.98,
            "Named by": "null",
            "Number": 46,
            "Period": 5,
            "Group": 10,
            "Phase": "Solid",
           
            "Summary": "Palladium is a chemical element with Symbol Pd and atomic Number 46. It is a rare and lustrous silvery-white metal discovered in 1803 by William Hyde Wollaston. He Named it after the asteroid Pallas, which was itself Named after the epithet of the Greek goddess Athena, acquired by her when she slew Pallas.",
            "Symbol": "Pd",
            
            "Shells": [
                2,
                8,
                18,
                18
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 4d10",
            "Electron configuration semantic": "[Kr] 4d10",
           
            "Block": "d"
        },
        47:{
            "Name": "Silver",
            "Appearance": "lustrous white metal",
            "Atomic Mass": 107.86822,
            "Boil": 2435,
            "Category": "transition metal",
            "Density": 10.49,
            "Discovered by": "unknown, before 5000 BC",
            "Melt": 1234.93,
            "Molar heat": 25.35,
            "Named by": "null",
            "Number": 47,
            "Period": 5,
            "Group": 11,
            "Phase": "Solid",
            
            "Summary": "Silver is a chemical element with Symbol Ag (Greek:άργυρος árguros, Latin:argentum, both from the Indo-European root *h₂erǵ- for \"grey\" or \"shining\") and atomic Number 47. A soft, white, lustrous transition metal, it possesses the highest electrical conductivity, thermal conductivity and reflectivity of any metal. The metal occurs naturally in its pure, free form (native silver), as an alloy with gold and other metals, and in minerals such as argentite and chlorargyrite.",
            "Symbol": "Ag",
           
            "Shells": [
                2,
                8,
                18,
                18,
                1
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d10",
            "Electron configuration semantic": "[Kr] 4d10 5s1",
            
            "Block": "d"
        },
        48:{
            "Name": "Cadmium",
            "Appearance": "silvery bluish-gray metallic",
            "Atomic Mass": 112.4144,
            "Boil": 1040,
            "Category": "transition metal",
            "Density": 8.65,
            "Discovered by": "Karl Samuel Leberecht Hermann",
            "Melt": 594.22,
            "Molar heat": 26.02,
            "Named by": "Isotopes of cadmium",
            "Number": 48,
            "Period": 5,
            "Group": 12,
            "Phase": "Solid",
          
            "Summary": "Cadmium is a chemical element with Symbol Cd and atomic Number 48. This soft, bluish-white metal is chemically similar to the two other stable metals in Group 12, zinc and mercury. Like zinc, it prefers oxidation state +2 in most of its compounds and like mercury it shows a low Melting point compared to transition metals.",
            "Symbol": "Cd",
            
            "Shells": [
                2,
                8,
                18,
                18,
                2
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10",
            "Electron configuration semantic": "[Kr] 4d10 5s2",
            
            "Block": "d"
        },
        49:{
            "Name": "Indium",
            "Appearance": "silvery lustrous gray",
            "Atomic Mass": 114.8181,
            "Boil": 2345,
            "Category": "post-transition metal",
            "Density": 7.31,
            "Discovered by": "Ferdinand Reich",
            "Melt": 429.7485,
            "Molar heat": 26.74,
            "Named by": "null",
            "Number": 49,
            "Period": 5,
            "Group": 13,
            "Phase": "Solid",
           
            "Summary": "Indium is a chemical element with Symbol In and atomic Number 49. It is a post-transition metallic element that is rare in Earth's crust. The metal is very soft, malleable and easily fusible, with a Melting point higher than sodium, but lower than lithium or tin.",
            "Symbol": "In",
           
            "Shells": [
                2,
                8,
                18,
                18,
                3
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p1",
            "Electron configuration semantic": "[Kr] 4d10 5s2 5p1",
          
            "Block": "p"
        },
        50:{
            "Name": "Tin",
            "Appearance": "silvery-white (beta, β) or gray (alpha, α)",
            "Atomic Mass": 118.7107,
            "Boil": 2875,
            "Category": "post-transition metal",
            "Density": 7.365,
            "Discovered by": "unknown, before 3500 BC",
            "Melt": 505.08,
            "Molar heat": 27.112,
            "Named by": "null",
            "Number": 50,
            "Period": 5,
            "Group": 14,
            "Phase": "Solid",
          
            "Summary": "Tin is a chemical element with the Symbol Sn (for Latin:stannum) and atomic Number 50. It is a main Group metal in Group 14 of the Periodic table. Tin shows a chemical similarity to both neighboring Group-14 elements, germanium and lead, and has two possible oxidation states, +2 and the slightly more stable +4.",
            "Symbol": "Sn",
           
            "Shells": [
                2,
                8,
                18,
                18,
                4
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p2",
            "Electron configuration semantic": "[Kr] 4d10 5s2 5p2",
           
            "Block": "p"
        },
        51:{
            "Name": "Antimony",
            "Appearance": "silvery lustrous gray",
            "Atomic Mass": 121.7601,
            "Boil": 1908,
            "Category": "metalloid",
            "Density": 6.697,
            "Discovered by": "unknown, before 3000 BC",
            "Melt": 903.78,
            "Molar heat": 25.23,
            "Named by": "null",
            "Number": 51,
            "Period": 5,
            "Group": 15,
            "Phase": "Solid",
          
            "Summary": "Antimony is a chemical element with Symbol Sb (from Latin:stibium) and atomic Number 51. A lustrous gray metalloid, it is found in nature mainly as the sulfide mineral stibnite (Sb2S3). Antimony compounds have been known since ancient times and were used for cosmetics; metallic antimony was also known, but it was erroneously identified as lead upon its discovery.",
            "Symbol": "Sb",
            
            "Shells": [
                2,
                8,
                18,
                18,
                5
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p3",
            "Electron configuration semantic": "[Kr] 4d10 5s2 5p3",
            
            "Block": "p"
        },
        52:{
            "Name": "Tellurium",
            "Appearance": "null",
            "Atomic Mass": 127.603,
            "Boil": 1261,
            "Category": "metalloid",
            "Density": 6.24,
            "Discovered by": "Franz-Joseph Müller von Reichenstein",
            "Melt": 722.66,
            "Molar heat": 25.73,
            "Named by": "null",
            "Number": 52,
            "Period": 5,
            "Group": 16,
            "Phase": "Solid",
           
            "Summary": "Tellurium is a chemical element with Symbol Te and atomic Number 52. It is a brittle, mildly toxic, rare, silver-white metalloid. Tellurium is chemically related to selenium and sulfur.",
            "Symbol": "Te",
           
            "Shells": [
                2,
                8,
                18,
                18,
                6
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p4",
            "Electron configuration semantic": "[Kr] 4d10 5s2 5p4",
           
            "Block": "p"
        },
        53:{
            "Name": "Iodine",
            "Appearance": "lustrous metallic gray, violet as a gas",
            "Atomic Mass": 126.904473,
            "Boil": 457.4,
            "Category": "diatomic nonmetal",
            "Density": 4.933,
            "Discovered by": "Bernard Courtois",
            "Melt": 386.85,
            "Molar heat": "null",
            "Named by": "null",
            "Number": 53,
            "Period": 5,
            "Group": 17,
            "Phase": "Solid",
           
            "Summary": "Iodine is a chemical element with Symbol I and atomic Number 53. The Name is from Greek ἰοειδής ioeidēs, meaning violet or purple, due to the color of iodine vapor. Iodine and its compounds are primarily used in nutrition, and industrially in the production of acetic acid and certain polymers.",
            "Symbol": "I",
           
            "Shells": [
                2,
                8,
                18,
                18,
                7
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p5",
            "Electron configuration semantic": "[Kr] 4d10 5s2 5p5",
           
            "Block": "p"
        },
        54:{
            "Name": "Xenon",
            "Appearance": "colorless gas, exhibiting a blue glow when placed in a high voltage electric field",
            "Atomic Mass": 131.2936,
            "Boil": 165.051,
            "Category": "noble gas",
            "Density": 5.894,
            "Discovered by": "William Ramsay",
            "Melt": 161.4,
            "Molar heat": "null",
            "Named by": "null",
            "Number": 54,
            "Period": 5,
            "Group": 18,
            "Phase": "Gas",
          
            "Summary": "Xenon is a chemical element with Symbol Xe and atomic Number 54. It is a colorless, dense, odorless noble gas, that occurs in the Earth's atmosphere in trace amounts. Although generally unreactive, xenon can undergo a few chemical reactions such as the formation of xenon hexafluoroplatinate, the first noble gas compound to be synthesized.",
            "Symbol": "Xe",
            
            "Shells": [
                2,
                8,
                18,
                18,
                8
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6",
            "Electron configuration semantic": "[Kr] 4d10 5s2 5p6",
           
            "Block": "p"
        },
        55:{
            "Name": "Cesium",
            "Appearance": "silvery gold",
            "Atomic Mass": 132.905451966,
            "Boil": 944,
            "Category": "alkali metal",
            "Density": 1.93,
            "Discovered by": "Robert Bunsen",
            "Melt": 301.7,
            "Molar heat": 32.21,
            "Named by": "null",
            "Number": 55,
            "Period": 6,
            "Group": 1,
            "Phase": "Solid",
           
            "Summary": "Caesium or cesium is a chemical element with Symbol Cs and atomic Number 55. It is a soft, silvery-gold alkali metal with a Melting point of 28 °C (82 °F), which makes it one of only five elemental metals that are liquid at or near room temperature. Caesium is an alkali metal and has physical and chemical properties similar to those of rubidium and potassium.",
            "Symbol": "Cs",
         
            "Shells": [
                2,
                8,
                18,
                18,
                8,
                1
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s1",
            "Electron configuration semantic": "[Xe] 6s1",
           
            "Block": "s"
        },
        56:{
            "Name": "Barium",
            "Appearance": "null",
            "Atomic Mass": 137.3277,
            "Boil": 2118,
            "Category": "alkaline earth metal",
            "Density": 3.51,
            "Discovered by": "Carl Wilhelm Scheele",
            "Melt": 1000,
            "Molar heat": 28.07,
            "Named by": "null",
            "Number": 56,
            "Period": 6,
            "Group": 2,
            "Phase": "Solid",
          
            "Summary": "Barium is a chemical element with Symbol Ba and atomic Number 56. It is the fifth element in Group 2, a soft silvery metallic alkaline earth metal. Because of its high chemical reactivity barium is never found in nature as a free element.",
            "Symbol": "Ba",
            
            "Shells": [
                2,
                8,
                18,
                18,
                8,
                2
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2",
            "Electron configuration semantic": "[Xe] 6s2",
          
            "Block": "s"
        },
        57:{
            "Name": "Lanthanum",
            "Appearance": "silvery white",
            "Atomic Mass": 138.905477,
            "Boil": 3737,
            "Category": "lanthanide",
            "Density": 6.162,
            "Discovered by": "Carl Gustaf Mosander",
            "Melt": 1193,
            "Molar heat": 27.11,
            "Named by": "null",
            "Number": 57,
            "Period": 6,
            "Group": 3,
            "Phase": "Solid",
          
            "Summary": "Lanthanum is a soft, ductile, silvery-white metallic chemical element with Symbol La and atomic Number 57. It tarnishes rapidly when exposed to air and is soft enough to be cut with a knife. It gave its Name to the lanthanide series, a Group of 15 similar elements between lanthanum and lutetium in the Periodic table:it is also sometimes considered the first element of the 6th-Period transition metals.",
            "Symbol": "La",
          
            "Shells": [
                2,
                8,
                18,
                18,
                9,
                2
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d1",
            "Electron configuration semantic": "[Xe] 5d16s2",
          
            "Block": "f"
        },
        58:{
            "Name": "Cerium",
            "Appearance": "silvery white",
            "Atomic Mass": 140.1161,
            "Boil": 3716,
            "Category": "lanthanide",
            "Density": 6.77,
            "Discovered by": "Martin Heinrich Klaproth",
            "Melt": 1068,
            "Molar heat": 26.94,
            "Named by": "null",
            "Number": 58,
            "Period": 6,
            "Group": 3,
            "Phase": "Solid",
           
            "Summary": "Cerium is a chemical element with Symbol Ce and atomic Number 58. It is a soft, silvery, ductile metal which easily oxidizes in air. Cerium was Named after the dwarf planet Ceres (itself Named after the Roman goddess of agriculture).",
            "Symbol": "Ce",
           
            "Shells": [
                2,
                8,
                18,
                19,
                9,
                2
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d1 4f1",
            "Electron configuration semantic": "[Xe] 4f1 5d1 6s2",
           
            "Block": "f"
        },
        59:{
            "Name": "Praseodymium",
            "Appearance": "grayish white",
            "Atomic Mass": 140.907662,
            "Boil": 3403,
            "Category": "lanthanide",
            "Density": 6.77,
            "Discovered by": "Carl Auer von Welsbach",
            "Melt": 1208,
            "Molar heat": 27.2,
            "Named by": "null",
            "Number": 59,
            "Period": 6,
            "Group": 3,
            "Phase": "Solid",
          
            "Summary": "Praseodymium is a chemical element with Symbol Pr and atomic Number 59. Praseodymium is a soft, silvery, malleable and ductile metal in the lanthanide Group. It is valued for its magnetic, electrical, chemical, and optical properties.",
            "Symbol": "Pr",
           
            "Shells": [
                2,
                8,
                18,
                21,
                8,
                2
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f3",
            "Electron configuration semantic": "[Xe] 4f3 6s2",
           
            "Block": "f"
        },
        60:{
            "Name": "Neodymium",
            "Appearance": "silvery white",
            "Atomic Mass": 144.2423,
            "Boil": 3347,
            "Category": "lanthanide",
            "Density": 7.01,
            "Discovered by": "Carl Auer von Welsbach",
            "Melt": 1297,
            "Molar heat": 27.45,
            "Named by": "null",
            "Number": 60,
            "Period": 6,
            "Group": 3,
            "Phase": "Solid",
            
            "Summary": "Neodymium is a chemical element with Symbol Nd and atomic Number 60. It is a soft silvery metal that tarnishes in air. Neodymium was discovered in 1885 by the Austrian chemist Carl Auer von Welsbach.",
            "Symbol": "Nd",
           
            "Shells": [
                2,
                8,
                18,
                22,
                8,
                2
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f4",
            "Electron configuration semantic": "[Xe] 4f4 6s2",
           
            "Block": "f"
        },
        61:{
            "Name": "Promethium",
            "Appearance": "metallic",
            "Atomic Mass": 145,
            "Boil": 3273,
            "Category": "lanthanide",
            "Density": 7.26,
            "Discovered by": "Chien Shiung Wu",
            "Melt": 1315,
            "Molar heat": "null",
            "Named by": "Isotopes of promethium",
            "Number": 61,
            "Period": 6,
            "Group": 3,
            "Phase": "Solid",
            
            "Summary": "Promethium, originally prometheum, is a chemical element with the Symbol Pm and atomic Number 61. All of its isotopes are radioactive; it is one of only two such elements that are followed in the Periodic table by elements with stable forms, a distinction shared with technetium. Chemically, promethium is a lanthanide, which forms salts when combined with other elements.",
            "Symbol": "Pm",
            
            "Shells": [
                2,
                8,
                18,
                23,
                8,
                2
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f5",
            "Electron configuration semantic": "[Xe] 4f5 6s2",
           
            "Block": "f"
        },
        62:{
            "Name": "Samarium",
            "Appearance": "silvery white",
            "Atomic Mass": 150.362,
            "Boil": 2173,
            "Category": "lanthanide",
            "Density": 7.52,
            "Discovered by": "Lecoq de Boisbaudran",
            "Melt": 1345,
            "Molar heat": 29.54,
            "Named by": "null",
            "Number": 62,
            "Period": 6,
            "Group": 3,
            "Phase": "Solid",
           
            "Summary": "Samarium is a chemical element with Symbol Sm and atomic Number 62. It is a moderately hard silvery metal that readily oxidizes in air. Being a typical member of the lanthanide series, samarium usually assumes the oxidation state +3.",
            "Symbol": "Sm",
          
            "Shells": [
                2,
                8,
                18,
                24,
                8,
                2
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f6",
            "Electron configuration semantic": "[Xe] 4f6 6s2",
          
            "Block": "f"
        },
        63:{
            "Name": "Europium",
            "Appearance": "null",
            "Atomic Mass": 151.9641,
            "Boil": 1802,
            "Category": "lanthanide",
            "Density": 5.264,
            "Discovered by": "Eugène-Anatole Demarçay",
            "Melt": 1099,
            "Molar heat": 27.66,
            "Named by": "null",
            "Number": 63,
            "Period": 6,
            "Group": 3,
            "Phase": "Solid",
            
            "Summary": "Europium is a chemical element with Symbol Eu and atomic Number 63. It was isolated in 1901 and is Named after the continent of Europe. It is a moderately hard, silvery metal which readily oxidizes in air and water.",
            "Symbol": "Eu",
           
            "Shells": [
                2,
                8,
                18,
                25,
                8,
                2
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f7",
            "Electron configuration semantic": "[Xe] 4f7 6s2",
           
            "Block": "f"
        },
        64:{
            "Name": "Gadolinium",
            "Appearance": "silvery white",
            "Atomic Mass": 157.253,
            "Boil": 3273,
            "Category": "lanthanide",
            "Density": 7.9,
            "Discovered by": "Jean Charles Galissard de Marignac",
            "Melt": 1585,
            "Molar heat": 37.03,
            "Named by": "null",
            "Number": 64,
            "Period": 6,
            "Group": 3,
            "Phase": "Solid",
            
            "Summary": "Gadolinium is a chemical element with Symbol Gd and atomic Number 64. It is a silvery-white, malleable and ductile rare-earth metal. It is found in nature only in combined (salt) form.",
            "Symbol": "Gd",
            
            "Shells": [
                2,
                8,
                18,
                25,
                9,
                2
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f7 5d1",
            "Electron configuration semantic": "[Xe] 4f7 5d1 6s2",
          
            "Block": "f"
        },
        65:{
            "Name": "Terbium",
            "Appearance": "silvery white",
            "Atomic Mass": 158.925352,
            "Boil": 3396,
            "Category": "lanthanide",
            "Density": 8.23,
            "Discovered by": "Carl Gustaf Mosander",
            "Melt": 1629,
            "Molar heat": 28.91,
            "Named by": "null",
            "Number": 65,
            "Period": 6,
            "Group": 3,
            "Phase": "Solid",
            
            "Summary": "Terbium is a chemical element with Symbol Tb and atomic Number 65. It is a silvery-white rare earth metal that is malleable, ductile and soft enough to be cut with a knife. Terbium is never found in nature as a free element, but it is contained in many minerals, including cerite, gadolinite, monazite, xenotime and euxenite.",
            "Symbol": "Tb",
           
            "Shells": [
                2,
                8,
                18,
                27,
                8,
                2
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f9",
            "Electron configuration semantic": "[Xe] 4f9 6s2",
            
            "Block": "f"
        },
        66:{
            "Name": "Dysprosium",
            "Appearance": "silvery white",
            "Atomic Mass": 162.5001,
            "Boil": 2840,
            "Category": "lanthanide",
            "Density": 8.54,
            "Discovered by": "Lecoq de Boisbaudran",
            "Melt": 1680,
            "Molar heat": 27.7,
            "Named by": "null",
            "Number": 66,
            "Period": 6,
            "Group": 3,
            "Phase": "Solid",
           
            "Summary": "Dysprosium is a chemical element with the Symbol Dy and atomic Number 66. It is a rare earth element with a metallic silver luster. Dysprosium is never found in nature as a free element, though it is found in various minerals, such as xenotime.",
            "Symbol": "Dy",
           
            "Shells": [
                2,
                8,
                18,
                28,
                8,
                2
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f10",
            "Electron configuration semantic": "[Xe] 4f10 6s2",
            
            "Block": "f"
        },
        67:{
            "Name": "Holmium",
            "Appearance": "silvery white",
            "Atomic Mass": 164.930332,
            "Boil": 2873,
            "Category": "lanthanide",
            "Density": 8.79,
            "Discovered by": "Marc Delafontaine",
            "Melt": 1734,
            "Molar heat": 27.15,
            "Named by": "null",
            "Number": 67,
            "Period": 6,
            "Group": 3,
            "Phase": "Solid",
            
            "Summary": "Holmium is a chemical element with Symbol Ho and atomic Number 67. Part of the lanthanide series, holmium is a rare earth element. Holmium was discovered by Swedish chemist Per Theodor Cleve.",
            "Symbol": "Ho",
           
            "Shells": [
                2,
                8,
                18,
                29,
                8,
                2
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f11",
            "Electron configuration semantic": "[Xe] 4f11 6s2",
          
            "Block": "f"
        },
        68:{
            "Name": "Erbium",
            "Appearance": "silvery white",
            "Atomic Mass": 167.2593,
            "Boil": 3141,
            "Category": "lanthanide",
            "Density": 9.066,
            "Discovered by": "Carl Gustaf Mosander",
            "Melt": 1802,
            "Molar heat": 28.12,
            "Named by": "null",
            "Number": 68,
            "Period": 6,
            "Group": 3,
            "Phase": "Solid",
          
            "Summary": "Erbium is a chemical element in the lanthanide series, with Symbol Er and atomic Number 68. A silvery-white solid metal when artificially isolated, natural erbium is always found in chemical combination with other elements on Earth. As such, it is a rare earth element which is associated with several other rare elements in the mineral gadolinite from Ytterby in Sweden, where yttrium, ytterbium, and terbium were discovered.",
            "Symbol": "Er",
           
            "Shells": [
                2,
                8,
                18,
                30,
                8,
                2
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f12",
            "Electron configuration semantic": "[Xe] 4f12 6s2",
            
            "Block": "f"
        },
        69:{
            "Name": "Thulium",
            "Appearance": "silvery gray",
            "Atomic Mass": 168.934222,
            "Boil": 2223,
            "Category": "lanthanide",
            "Density": 9.32,
            "Discovered by": "Per Teodor Cleve",
            "Melt": 1818,
            "Molar heat": 27.03,
            "Named by": "null",
            "Number": 69,
            "Period": 6,
            "Group": 3,
            "Phase": "Solid",
          
            "Summary": "Thulium is a chemical element with Symbol Tm and atomic Number 69. It is the thirteenth and antepenultimate (third-last) element in the lanthanide series. Like the other lanthanides, the most common oxidation state is +3, seen in its oxide, halides and other compounds.",
            "Symbol": "Tm",
           
            "Shells": [
                2,
                8,
                18,
                31,
                8,
                2
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f13",
            "Electron configuration semantic": "[Xe] 4f13 6s2",
           
            "Block": "f"
        },
        70:{
            "Name": "Ytterbium",
            "Appearance": "null",
            "Atomic Mass": 173.0451,
            "Boil": 1469,
            "Category": "lanthanide",
            "Density": 6.9,
            "Discovered by": "Jean Charles Galissard de Marignac",
            "Melt": 1097,
            "Molar heat": 26.74,
            "Named by": "null",
            "Number": 70,
            "Period": 6,
            "Group": 3,
            "Phase": "Solid",
           
            "Summary": "Ytterbium is a chemical element with Symbol Yb and atomic Number 70. It is the fourteenth and penultimate element in the lanthanide series, which is the basis of the relative stability of its +2 oxidation state. However, like the other lanthanides, its most common oxidation state is +3, seen in its oxide, halides and other compounds.",
            "Symbol": "Yb",
          
            "Shells": [
                2,
                8,
                18,
                32,
                8,
                2
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14",
            "Electron configuration semantic": "[Xe] 4f14 6s2",
           
            "Block": "f"
        },
        71:{
            "Name": "Lutetium",
            "Appearance": "silvery white",
            "Atomic Mass": 174.96681,
            "Boil": 3675,
            "Category": "lanthanide",
            "Density": 9.841,
            "Discovered by": "Georges Urbain",
            "Melt": 1925,
            "Molar heat": 26.86,
            "Named by": "null",
            "Number": 71,
            "Period": 6,
            "Group": 3,
            "Phase": "Solid",
           
            "Summary": "Lutetium is a chemical element with Symbol Lu and atomic Number 71. It is a silvery white metal, which resists corrosion in dry, but not in moist air. It is considered the first element of the 6th-Period transition metals and the last element in the lanthanide series, and is traditionally counted among the rare earths.",
            "Symbol": "Lu",
           
            "Shells": [
                2,
                8,
                18,
                32,
                9,
                2
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d1",
            "Electron configuration semantic": "[Xe] 4f14 5d1 6s2",
           
            "Block": "d"
        },
        72:{
            "Name": "Hafnium",
            "Appearance": "steel gray",
            "Atomic Mass": 178.492,
            "Boil": 4876,
            "Category": "transition metal",
            "Density": 13.31,
            "Discovered by": "Dirk Coster",
            "Melt": 2506,
            "Molar heat": 25.73,
            "Named by": "null",
            "Number": 72,
            "Period": 6,
            "Group": 4,
            "Phase": "Solid",
           
            "Summary": "Hafnium is a chemical element with Symbol Hf and atomic Number 72. A lustrous, silvery gray, tetravalent transition metal, hafnium chemically resembles zirconium and is found in zirconium minerals. Its existence was predicted by Dmitri Mendeleev in 1869, though it was not identified until 1923, making it the penultimate stable element to be discovered (rhenium was identified two years later).",
            "Symbol": "Hf",
          
            "Shells": [
                2,
                8,
                18,
                32,
                10,
                2
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d2",
            "Electron configuration semantic": "[Xe] 4f14 5d2 6s2",
            
            "Block": "d"
        },
        73:{
            "Name": "Tantalum",
            "Appearance": "gray blue",
            "Atomic Mass": 180.947882,
            "Boil": 5731,
            "Category": "transition metal",
            "Density": 16.69,
            "Discovered by": "Anders Gustaf Ekeberg",
            "Melt": 3290,
            "Molar heat": 25.36,
            "Named by": "null",
            "Number": 73,
            "Period": 6,
            "Group": 5,
            "Phase": "Solid",
          
            "Summary": "Tantalum is a chemical element with Symbol Ta and atomic Number 73. Previously known as tantalium, its Name comes from Tantalus, an antihero from Greek mythology. Tantalum is a rare, hard, blue-gray, lustrous transition metal that is highly corrosion-resistant.",
            "Symbol": "Ta",
            
            "Shells": [
                2,
                8,
                18,
                32,
                11,
                2
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d3",
            "Electron configuration semantic": "[Xe] 4f14 5d3 6s2",
           
            "Block": "d"
        },
        74:{
            "Name": "Tungsten",
            "Appearance": "grayish white, lustrous",
            "Atomic Mass": 183.841,
            "Boil": 6203,
            "Category": "transition metal",
            "Density": 19.25,
            "Discovered by": "Carl Wilhelm Scheele",
            "Melt": 3695,
            "Molar heat": 24.27,
            "Named by": "null",
            "Number": 74,
            "Period": 6,
            "Group": 6,
            "Phase": "Solid",
            
            "Summary": "Tungsten, also known as wolfram, is a chemical element with Symbol W and atomic Number 74. The word tungsten comes from the Swedish language tung sten, which directly translates to heavy stone. Its Name in Swedish is volfram, however, in order to distinguish it from scheelite, which in Swedish is alternatively Named tungsten.",
            "Symbol": "W",
          
            "Shells": [
                2,
                8,
                18,
                32,
                12,
                2
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d4",
            "Electron configuration semantic": "[Xe] 4f14 5d4 6s2",
           
            "Block": "d"
        },
        75:{
            "Name": "Rhenium",
            "Appearance": "silvery-grayish",
            "Atomic Mass": 186.2071,
            "Boil": 5869,
            "Category": "transition metal",
            "Density": 21.02,
            "Discovered by": "Masataka Ogawa",
            "Melt": 3459,
            "Molar heat": 25.48,
            "Named by": "Walter Noddack",
            "Number": 75,
            "Period": 6,
            "Group": 7,
            "Phase": "Solid",
         
            "Summary": "Rhenium is a chemical element with Symbol Re and atomic Number 75. It is a silvery-white, heavy, third-row transition metal in Group 7 of the Periodic table. With an estimated average concentration of 1 part per billion (ppb), rhenium is one of the rarest elements in the Earth's crust.",
            "Symbol": "Re",
            
            "Shells": [
                2,
                8,
                18,
                32,
                13,
                2
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d5",
            "Electron configuration semantic": "[Xe] 4f14 5d5 6s2",
          
            "Block": "d"
        },
        76:{
            "Name": "Osmium",
            "Appearance": "silvery, blue cast",
            "Atomic Mass": 190.233,
            "Boil": 5285,
            "Category": "transition metal",
            "Density": 22.59,
            "Discovered by": "Smithson Tennant",
            "Melt": 3306,
            "Molar heat": 24.7,
            "Named by": "null",
            "Number": 76,
            "Period": 6,
            "Group": 8,
            "Phase": "Solid",
           
            "Summary": "Osmium (from Greek osme (ὀσμή) meaning \"smell\") is a chemical element with Symbol Os and atomic Number 76. It is a hard, brittle, bluish-white transition metal in the platinum Group that is found as a trace element in alloys, mostly in platinum ores. Osmium is the densest naturally occurring element, with a Density of 22.59 g/cm3.",
            "Symbol": "Os",
            
            "Shells": [
                2,
                8,
                18,
                32,
                14,
                2
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d6",
            "Electron configuration semantic": "[Xe] 4f14 5d6 6s2",
          
            "Block": "d"
        },
        77:{
            "Name": "Iridium",
            "Appearance": "silvery white",
            "Atomic Mass": 192.2173,
            "Boil": 4403,
            "Category": "transition metal",
            "Density": 22.56,
            "Discovered by": "Smithson Tennant",
            "Melt": 2719,
            "Molar heat": 25.1,
            "Named by": "null",
            "Number": 77,
            "Period": 6,
            "Group": 9,
            "Phase": "Solid",
          
            "Summary": "Iridium is a chemical element with Symbol Ir and atomic Number 77. A very hard, brittle, silvery-white transition metal of the platinum Group, iridium is generally credited with being the second densest element (after osmium) based on measured Density, although calculations involving the space lattices of the elements show that iridium is denser. It is also the most corrosion-resistant metal, even at temperatures as high as 2000 °C. Although only certain molten salts and halogens are corrosive to solid iridium, finely divided iridium dust is much more reactive and can be flammable.",
            "Symbol": "Ir",
               
            "Shells": [
                2,
                8,
                18,
                32,
                15,
                2
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d7",
            "Electron configuration semantic": "[Xe] 4f14 5d7 6s2",
   
            "Block": "d"
        },
        78:{
            "Name": "Platinum",
            "Appearance": "silvery white",
            "Atomic Mass": 195.0849,
            "Boil": 4098,
            "Category": "transition metal",
            "Density": 21.45,
            "Discovered by": "Antonio de Ulloa",
            "Melt": 2041.4,
            "Molar heat": 25.86,
            "Named by": "null",
            "Number": 78,
            "Period": 6,
            "Group": 10,
            "Phase": "Solid",
          
            "Summary": "Platinum is a chemical element with Symbol Pt and atomic Number 78. It is a dense, malleable, ductile, highly unreactive, precious, gray-white transition metal. Its Name is derived from the Spanish term platina, which is literally translated into \"little silver\".",
            "Symbol": "Pt",
           
            "Shells": [
                2,
                8,
                18,
                32,
                17,
                1
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s1 4f14 5d9",
            "Electron configuration semantic": "[Xe] 4f14 5d9 6s1",
           
            "Block": "d"
        },
        79:{
            "Name": "Gold",
            "Appearance": "metallic yellow",
            "Atomic Mass": 196.9665695,
            "Boil": 3243,
            "Category": "transition metal",
            "Density": 19.3,
            "Discovered by": "Middle East",
            "Melt": 1337.33,
            "Molar heat": 25.418,
            "Named by": "null",
            "Number": 79,
            "Period": 6,
            "Group": 11,
            "Phase": "Solid",
          
            "Summary": "Gold is a chemical element with Symbol Au (from Latin:aurum) and atomic Number 79. In its purest form, it is a bright, slightly reddish yellow, dense, soft, malleable and ductile metal. Chemically, gold is a transition metal and a Group 11 element.",
            "Symbol": "Au",
           
            "Shells": [
                2,
                8,
                18,
                32,
                18,
                1
            ],
            "Electronic configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s1 4f14 5d10",
            "Electron configuration semantic": "[Xe] 4f14 5d10 6s1",
          
            "Block": "d"
        },

            80:{
                 "Name": "Mercury",
                 "Appearance": "silvery",
                 "atomic_mass": 200.5923,
                 "Boil": 629.88,
                 "Category": "transition metal",
                 "Density": 13.534,
                 "Discovered By": "unknown, before 2000 BCE",
                 "Melt": 234.321,
                 "Molar heat": 27.983,
                 "Named_by": "null",
                 "Number": 80,
                 "Period": 6,
                 "Group": 12,
                 "Phase": "Liquid",
                 "Summary": "Mercury is a chemical element with Symbol Hg and atomic Number 80. It is commonly known as quicksilver and was formerly Named hydrargyrum (/haɪˈdrɑːrdʒərəm/). A heavy, silvery d-block element, mercury is the only metallic element that is liquid at standard conditions for temperature and pressure; the only other element that is liquid under these conditions is bromine, though metals such as caesium, gallium, and rubidium Melt just above room temperature.",
                 "Symbol": "Hg",
                 "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10",
                 "block": "d"},
             81:{
                 "Name": "Thallium",
                 "Appearance": "silvery white",
                 "atomic_mass": 204.38,
                 "Boil": 1746,
                 "Category":"post-transition metal",
                 "Density": 11.85,
                 "Discovered By": "William Crookes",
                 "Melt": 577,
                 "Molar heat": 26.32,
                 "Number": 81,
                 "Period": 6,
                 "Group": 13,
                 "Phase": "Solid",
                 "Summary": "Thallium is a chemical element with Symbol Tl and atomic Number 81. This soft gray post-transition metal is not found free in nature. When isolated, it resembles tin, but discolors when exposed to air.",
                 "Symbol": "Tl",
                 "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p1",
                 "block": "p"},
             82:{
                 "Name":"Lead",
                 "Appearance": "metallic gray",
                 "atomic_mass": 207.21,
                 "Boil": 2022,
                 "Category": "post-transition metal",
                 "Density": 11.34,
                 "Discovered By": "Middle East",
                 "Melt": 600.61,
                 "Molar heat": 26.65,
                 "Named_by": "null",
                 "Number": 82,
                 "Period": 6,
                 "Group": 14,
                 "Phase":"Solid",
                 "Summary": "Lead (/lɛd/) is a chemical element in the carbon Group with Symbol Pb (from Latin:plumbum) and atomic Number 82. Lead is a soft, malleable and heavy post-transition metal. Metallic lead has a bluish-white color after being freshly cut, but it soon tarnishes to a dull grayish color when exposed to air.",
                 "Symbol": "Pb",
                 "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p2",
                 "block": "p"},
             83:{
                 "Name": "Bismuth",
                 "Appearance": "lustrous silver",
                 "atomic_mass": 208.980401,
                 "Boil": 1837,
                 "Category": "post-transition metal",
                 "Density": 9.78,
                 "Discovered By": "Claude François Geoffroy",
                 "Melt": 544.7,
                 "Molar heat": 25.52,
                 "Number": 83,
                 "Period": 6,
                 "Group": 15,
                 "Phase": "Solid",
                 "Summary": "Bismuth is a chemical element with Symbol Bi and atomic Number 83. Bismuth, a pentavalent post-transition metal, chemically resembles arsenic and antimony. Elemental bismuth may occur naturally, although its sulfide and oxide form important commercial ores.",
                 "Symbol": "Bi",
                 "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p3",
                 "block": "p"},
             84:{"Name":"Polonium",
                 "Appearance": "silvery",
                 "atomic_mass": 209,
                 "Boil": 1235,
                 "Category": "post-transition metal",
                 "Density": 9.196,
                 "Discovered By": "Pierre Curie",
                 "Melt": 527,
                 "Molar heat": 26.4,
                 "Number": 84,
                 "Period": 6,
                 "Group": 16,
                 "Phase": "Solid",
                 "Summary": "Polonium is a chemical element with Symbol Po and atomic Number 84, discovered in 1898 by Marie Curie and Pierre Curie. A rare and highly radioactive element with no stable isotopes, polonium is chemically similar to bismuth and tellurium, and it occurs in uranium ores. Applications of polonium are few.",
                 "Symbol": "Po",
                 "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p4",
                 "block": "p"},
          
           85:{
                "Name": "Astatine",
                "Appearance": "unknown, probably metallic",
                "atomic_mass": 210,
                "Boil": 610,
                "Category": "metalloid",
                "Density": 6.35,
                "Discovered By": "Dale R. Corson",
                "Melt": 575,
                "Number": 85,
                "Period": 6,
                "Group": 17,
                "Phase": "Solid",
                "Summary": "Astatine is a very rare radioactive chemical element with the chemical Symbol At and atomic Number 85. It occurs on Earth as the decay product of various heavier elements. All its isotopes are short-lived; the most stable is astatine-210, with a half-life of 8.1 hours.",
                "Symbol": "At",
                "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p5",
                "block": "p"
            },

            86:{
                "Name": "Radon",
                "Appearance": "colorless gas, occasionally glows green or red in discharge tubes",
                "atomic_mass": 222,
                "Boil": 211.5,
                "Category": "noble gas",
                "Density": 9.73,
                "Discovered By": "Friedrich Ernst Dorn",
                "Melt": 202,
                "Molar heat": "null",
                "Named_by": "null",
                "Number": 86,
                "Period": 6,
                "Group": 18,
                "Phase": "Gas",
                "Summary": "Radon is a chemical element with Symbol Rn and atomic Number 86. It is a radioactive, colorless, odorless, tasteless noble gas, occurring naturally as a decay product of radium. Its most stable isotope, 222Rn, has a half-life of 3.8 days.",
                "Symbol": "Rn",
                "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6",
                "block": "p"
            },

           87: {
                "Name": "Francium",
                "Appearance": "null",
                "atomic_mass": 223,
                "Boil": 950,
                "Category": "alkali metal",
                "Density": 1.87,
                "Discovered By": "Marguerite Perey",
                "Melt": 300,
                "Molar heat": "null",
                "Named_by": "null",
                "Number": 87,
                "Period": 7,
                "Group": 1,
                "Phase": "Solid",
                "Summary": "Francium is a chemical element with Symbol Fr and atomic Number 87. It used to be known as eka-caesium and actinium K. It is the second-least electronegative element, behind only caesium. Francium is a highly radioactive metal that decays into astatine, radium, and radon.",
                "Symbol": "Fr",
                "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s1",
                "block": "s"
            },
            88:{
                "Name": "Radium",
                "Appearance": "silvery white metallic",
                "atomic_mass": 226,
                "Boil": 2010,
                "Category": "alkaline earth metal",
                "Density": 5.5,
                "Discovered By": "Pierre Curie",
                "Melt": 1233,
                "Molar heat": "null",
                "Named_by": "null",
                "Number": 88,
                "Period": 7,
                "Group": 2,
                "Phase": "Solid",
                "Summary": "Radium is a chemical element with Symbol Ra and atomic Number 88. It is the sixth element in Group 2 of the Periodic table, also known as the alkaline earth metals. Pure radium is almost colorless, but it readily combines with nitrogen (rather than oxygen) on exposure to air, forming a black surface layer of radium nitride (Ra3N2).",
                "Symbol": "Ra",
                "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2",
                "block": "s"
            },
            89:{
                "Name": "Actinium",
                "Appearance": "null",
                "atomic_mass": 227,
                "Boil": 3500,
                "Category": "actinide",
                "Density": 10,
                "Discovered By": "Friedrich Oskar Giesel",
                "Melt": 1500,
                "Molar heat": 27.2,
                "Number": 89,
                "Period": 7,
                "Group": 3,
                "Phase": "Solid",
                "Summary": "Actinium is a radioactive chemical element with Symbol Ac (not to be confused with the abbreviation for an acetyl Group) and atomic Number 89, which was discovered in 1899. It was the first non-primordial radioactive element to be isolated. Polonium, radium and radon were observed before actinium, but they were not isolated until 1902.",
                "Symbol": "Ac",
                "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 6d1",
                "block": "f"
            },
           90: {
                "Name": "Thorium",
                "Appearance": "silvery, often with black tarnish",
                "atomic_mass": 232.03774,
                "Boil": 5061,
                "Category": "actinide",
                "Density": 11.724,
                "Discovered By": "Jöns Jakob Berzelius",
                "Melt": 2023,
                "Molar heat": 26.23,
                "Named_by": "null",
                "Number": 90,
                "Period": 7,
                "Group": 3,
                "Phase": "Solid",
                "Summary": "Thorium is a chemical element with Symbol Th and atomic Number 90. A radioactive actinide metal, thorium is one of only two significantly radioactive elements that still occur naturally in large quantities as a primordial element (the other being uranium). It was discovered in 1828 by the Norwegian Reverend and amateur mineralogist Morten Thrane Esmark and identified by the Swedish chemist Jöns Jakob Berzelius, who Named it after Thor, the Norse god of thunder.",
                "Symbol": "Th",
                "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 6d2",
                    "block": "f"
            },
           91: {
                "Name": "Protactinium",
                "Appearance": "bright, silvery metallic luster",
                "atomic_mass": 231.035882,
                "Boil": 4300,
                "Category": "actinide",
                "Density": 15.37,
                "Discovered By": "William Crookes",
                "Melt": 1841,
                "Molar heat": "null",
                "Named_by": "Otto Hahn",
                "Number": 91,
                "Period": 7,
                "Group": 3,
                "Phase": "Solid",
                "Summary": "Protactinium is a chemical element with Symbol Pa and atomic Number 91. It is a dense, silvery-gray metal which readily reacts with oxygen, water vapor and inorganic acids. It forms various chemical compounds where protactinium is usually present in the oxidation state +5, but can also assume +4 and even +2 or +3 states.",
                "Symbol": "Pa",
                "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f2 6d1",
                "block": "f"
            },
            92:{
                "Name": "Uranium",
                "Appearance": "null",
                "atomic_mass": 238.028913,
                "Boil": 4404,
                "Category": "actinide",
                "Density": 19.1,
                "Discovered By": "Martin Heinrich Klaproth",
                "Melt": 1405.3,
                "Molar heat": 27.665,
                "Named_by": "null",
                "Number": 92,
                "Period": 7,
                "Group": 3,
                "Phase": "Solid",
                "Summary": "Uranium is a chemical element with Symbol U and atomic Number 92. It is a silvery-white metal in the actinide series of the Periodic table. A uranium atom has 92 protons and 92 electrons, of which 6 are valence electrons.",
                "Symbol": "U",
                "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f3 6d1",
                "block": "f"
            },
            93:{
                "Name": "Neptunium",
                "Appearance": "silvery metallic",
                "atomic_mass": 237,
                "Boil": 4447,
                "Category": "actinide",
                "Density": 20.45,
                "Discovered By": "Edwin McMillan",
                "Melt": 912,
                "Molar heat": 29.46,
                "Number": 93,
                "Period": 7,
                "Group": 3,
                "Phase": "Solid",
                "Summary": "Neptunium is a chemical element with Symbol Np and atomic Number 93. A radioactive actinide metal, neptunium is the first transuranic element. Its position in the Periodic table just after uranium, Named after the planet Uranus, led to it being Named after Neptune, the next planet beyond Uranus.",
                "Symbol": "Np",
                "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f4 6d1",
                "block": "f"
            },
            94:{
                "Name": "Plutonium",
                "Appearance": "silvery white, tarnishing to dark gray in air",
                "atomic_mass": 244,
                "Boil": 3505,
                "Category": "actinide",
                "Density": 19.816,
                "Discovered By": "Glenn T. Seaborg",
                "Melt": 912.5,
                "Molar heat": 35.5,
                "Number": 94,
                "Period": 7,
                "Group": 3,
                "Phase": "Solid",
                "Summary": "Plutonium is a transuranic radioactive chemical element with Symbol Pu and atomic Number 94. It is an actinide metal of silvery-gray Appearance that tarnishes when exposed to air, and forms a dull coating when oxidized. The element normally exhibits six allotropes and four oxidation states.",
                "Symbol": "Pu",
                "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f6",
                "block": "f"
            },
            95:{
                "Name": "Americium",
                "Appearance": "silvery white",
                "atomic_mass": 243,
                "Boil": 2880,
                "Category": "actinide",
                "Density": 12,
                "Discovered By": "Glenn T. Seaborg",
                "Melt": 1449,
                "Molar heat": 62.7,
                "Named_by": "null",
                "Number": 95,
                "Period": 7,
                "Group": 3,
                "Phase": "Solid",
                "Summary": "Americium is a radioactive transuranic chemical element with Symbol Am and atomic Number 95. This member of the actinide series is located in the Periodic table under the lanthanide element europium, and thus by analogy was Named after the Americas. Americium was first produced in 1944 by the Group of Glenn T.Seaborg from Berkeley, California, at the metallurgical laboratory of University of Chicago.",
                "Symbol": "Am",
                "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f7",
                "block": "f"
            },
            96:{
                "Name": "Curium",
                "Appearance": "silvery metallic, glows purple in the dark",
                "atomic_mass": 247,
                "Boil": 3383,
                "Category": "actinide",
                "Density": 13.51,
                "Discovered By": "Glenn T. Seaborg",
                "Melt": 1613,
                "Molar heat": "null",
                "Named_by": "null",
                "Number": 96,
                "Period": 7,
                "Group": 3,
                "Phase": "Solid",
                "Summary": "Curium is a transuranic radioactive chemical element with Symbol Cm and atomic Number 96. This element of the actinide series was Named after Marie and Pierre Curie – both were known for their research on radioactivity. Curium was first intentionally produced and identified in July 1944 by the Group of Glenn T. Seaborg at the University of California, Berkeley.",
                "Symbol": "Cm",
                "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f7 6d1",
                "block": "f"
            },
            97:{
                "Name": "Berkelium",
                "Appearance": "silvery",
                "atomic_mass": 247,
                "Boil": 2900,
                "Category": "actinide",
                "Density": 14.78,
                "Discovered By": "Lawrence Berkeley National Laboratory",
                "Melt": 1259,
                "Molar heat": "null",
                "Named_by": "null",
                "Number": 97,
                "Period": 7,
                "Group": 3,
                "Phase": "Solid",
                "Summary": "Berkelium is a transuranic radioactive chemical element with Symbol Bk and atomic Number 97. It is a member of the actinide and transuranium element series. It is Named after the city of Berkeley, California, the location of the University of California Radiation Laboratory where it was discovered in December 1949.",
                "Symbol": "Bk",
                "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f9",
                "block": "f"
            },
            98:{
                "Name": "Californium",
                "Appearance": "silvery",
                "atomic_mass": 251,
                "Boil": 1743,
                "Category": "actinide",
                "Density": 15.1,
                "Discovered By": "Lawrence Berkeley National Laboratory",
                "Melt": 1173,
                "Molar heat": "null",
                "Named_by": "null",
                "Number": 98,
                "Period": 7,
                "Group": 3,
                "Phase": "Solid",
                "Summary": "Californium is a radioactive metallic chemical element with Symbol Cf and atomic Number 98. The element was first made in 1950 at the University of California Radiation Laboratory in Berkeley, by bombarding curium with alpha particles (helium-4 ions). It is an actinide element, the sixth transuranium element to be synthesized, and has the second-highest Atomic Mass of all the elements that have been produced in amounts large enough to see with the unaided eye (after einsteinium).",
                "Symbol": "Cf",
                "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f10",
                "block": "f"
            },
           99:{
                "Name": "Einsteinium",
                "Appearance": "silver-colored",
                "atomic_mass": 252,
                "Boil": 1269,
                "Category": "actinide",
                "Density": 8.84,
                "Discovered By": "Lawrence Berkeley National Laboratory",
                "Melt": 1133,
                "Molar heat": "null",
                "Named_by": "null",
                "Number": 99,
                "Period": 7,
                "Group": 3,
                "Phase": "Solid",
                "Summary": "Einsteinium is a synthetic element with Symbol Es and atomic Number 99. It is the seventh transuranic element, and an actinide. Einsteinium was discovered as a component of the debris of the first hydrogen bomb explosion in 1952, and Named after Albert Einstein.",
                "Symbol": "Es",
                "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f11",
                "block": "f"
            },
           100:{
                "Name": "Fermium",
                "Appearance": "null",
                "atomic_mass": 257,
                "Boil": "null",
                "Category": "actinide",
                "Density": "null",
                "Discovered By": "Lawrence Berkeley National Laboratory",
                "Melt": 1800,
                "Molar heat": "null",
                "Named_by": "null",
                "Number": 100,
                "Period": 7,
                "Group": 3,
                "Phase": "Solid",
                "Summary": "Fermium is a synthetic element with Symbol Fm and atomic Number 100. It is a member of the actinide series. It is the heaviest element that can be formed by neutron bombardment of lighter elements, and hence the last element that can be prepared in macroscopic quantities, although pure fermium metal has not yet been prepared.",
                "Symbol": "Fm",
                "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f12",
                "block": "f"
            },
           101:{
                "Name": "Mendelevium",
                "Appearance": "null",
                "atomic_mass": 258,
                "Boil": "null",
                "Category": "actinide",
                "Density": "null",
                "Discovered By": "Lawrence Berkeley National Laboratory",
                "Melt": 1100,
                "Molar heat": "null",
                "Named_by": "null",
                "Number": 101,
                "Period": 7,
                "Group": 3,
                "Phase": "Solid",
                "Summary": "Mendelevium is a synthetic element with chemical Symbol Md (formerly Mv) and atomic Number 101. A metallic radioactive transuranic element in the actinide series, it is the first element that currently cannot be produced in macroscopic quantities through neutron bombardment of lighter elements. It is the antepenultimate actinide and the ninth transuranic element.",
                "Symbol": "Md",
                "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f13",
                "block": "f"
            },
           102:{
                "Name": "Nobelium",
                "Appearance": "null",
                "atomic_mass": 259,
                "Boil": "null",
                "Category": "actinide",
                "Density": "null",
                "Discovered By": "Joint Institute for Nuclear Research",
                "Melt": 1100,
                "Molar heat": "null",
                "Named_by": "null",
                "Number": 102,
                "Period": 7,
                "Group": 3,
                "Summary": "Nobelium is a synthetic chemical element with Symbol No and atomic Number 102. It is Named in honor of Alfred Nobel, the inventor of dynamite and benefactor of science. A radioactive metal, it is the tenth transuranic element and is the penultimate member of the actinide series.",
                "Symbol": "No",
                "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14",
                "block": "f"
            },
            103:{
                "Name": "Lawrencium",
                "Appearance": "null",
                "atomic_mass": 266,
                "Boil": "null",
                "Category": "actinide",
                "Density": "null",
                "Discovered By": "Lawrence Berkeley National Laboratory",
                "Melt": 1900,
                "Molar heat": "null",
                "Named_by": "null",
                "Number": 103,
                "Period": 7,
                "Group": 3,
                "Phase": "Solid",
                "Summary": "Lawrencium is a synthetic chemical element with chemical Symbol Lr (formerly Lw) and atomic Number 103. It is Named in honor of Ernest Lawrence, inventor of the cyclotron, a device that was used to discover many artificial radioactive elements. A radioactive metal, lawrencium is the eleventh transuranic element and is also the final member of the actinide series.",
                "Symbol": "Lr",
                "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 7p1",
                "block": "d"
            },
            104:{
                "Name": "Rutherfordium",
                "Appearance": "null",
                "atomic_mass": 267,
                "Boil": 5800,
                "Category": "transition metal",
                "Density": 23.2,
                "Discovered By": "Joint Institute for Nuclear Research",
                "Melt": 2400,
                "Molar heat": "null",
                "Named_by": "null",
                "Number": 104,
                "Period": 7,
                "Group": 4,
                "Phase": "Solid",
                "Summary": "Rutherfordium is a chemical element with Symbol Rf and atomic Number 104, Named in honor of physicist Ernest Rutherford. It is a synthetic element (an element that can be created in a laboratory but is not found in nature) and radioactive; the most stable known isotope, 267Rf, has a half-life of approximately 1.3 hours. In the Periodic table of the elements, it is a d - block element and the second of the fourth - row transition elements.",
                "Symbol": "Rf",
                "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d2",
                    "block": "d"
            },
            105:{
                "Name": "Dubnium",
                "Appearance": "null",
                "atomic_mass": 268,
                "Boil": "null",
                "Category": "transition metal",
                "Density": 29.3,
                "Discovered By": "Joint Institute for Nuclear Research",
                "Melt": "null",
                "Molar heat": "null",
                "Named_by": "null",
                "Number": 105,
                "Period": 7,
                "Group": 5,
                "Phase": "Solid",
                "Summary": "Dubnium is a chemical element with Symbol Db and atomic Number 105. It is Named after the town of Dubna in Russia (north of Moscow), where it was first produced. It is a synthetic element (an element that can be created in a laboratory but is not found in nature) and radioactive; the most stable known isotope, dubnium-268, has a half-life of approximately 28 hours.",
                "Symbol": "Db",
                "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d3",
                "block": "d"
            },
            106:{
                "Name": "Seaborgium",
                "Appearance": "null",
                "atomic_mass": 269,
                "Boil": "null",
                "Category": "transition metal",
                "Density": 35,
                "Discovered By": "Lawrence Berkeley National Laboratory",
                "Melt": "null",
                "Molar heat": "null",
                "Named_by": "null",
                "Number": 106,
                "Period": 7,
                "Group": 6,
                "Phase": "Solid",
                "Summary": "Seaborgium is a synthetic element with Symbol Sg and atomic Number 106. Its most stable isotope 271Sg has a half-life of 1.9 minutes. A more recently discovered isotope 269Sg has a potentially slightly longer half-life (ca.",
                "Symbol": "Sg",
                "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d4",
                "block": "d"
            },
            107:{
                "Name": "Bohrium",
                "Appearance": "null",
                "atomic_mass": 270,
                "Boil": "null",
                "Category": "transition metal",
                "Density": 37.1,
                "Discovered By": "Gesellschaft für Schwerionenforschung",
                "Melt": "null",
                "Molar heat": "null",
                "Named_by": "null",
                "Number": 107,
                "Period": 7,
                "Group": 7,
                "Phase": "Solid",
                "Summary": "Bohrium is a chemical element with Symbol Bh and atomic Number 107. It is Named after Danish physicist Niels Bohr. It is a synthetic element (an element that can be created in a laboratory but is not found in nature) and radioactive; the most stable known isotope, 270Bh, has a half-life of approximately 61 seconds.",
                "Symbol": "Bh",
                "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d5",
                "block": "d"
            },
            108:{
                "Name": "Hassium",
                "Appearance": "null",
                "atomic_mass": 269,
                "Boil": "null",
                "Category": "transition metal",
                "Density": 40.7,
                "Discovered By": "Gesellschaft für Schwerionenforschung",
                "Melt": 126,
                "Molar heat": "null",
                "Named_by": "null",
                "Number": 108,
                "Period": 7,
                "Group": 8,
                "Phase": "Solid",
                "Summary": "Hassium is a chemical element with Symbol Hs and atomic Number 108, Named after the German state of Hesse. It is a synthetic element (an element that can be created in a laboratory but is not found in nature) and radioactive; the most stable known isotope, 269Hs, has a half-life of approximately 9.7 seconds, although an unconfirmed metastable state, 277mHs, may have a longer half-life of about 130 seconds. More than 100 atoms of hassium have been synthesized to date.",
                "Symbol": "Hs",
                    "ectron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d6",
                "block": "d"
            },
            109:{
                "Name": "Meitnerium",
                "Appearance": "null",
                "atomic_mass": 278,
                "Boil": "null",
                "Category": "unknown, probably transition metal",
                "Density": 37.4,
                "Discovered By": "Gesellschaft für Schwerionenforschung",
                "Melt": "null",
                "Molar heat": "null",
                "Named_by": "null",
                "Number": 109,
                "Period": 7,
                "Group": 9,
                "Phase": "Solid",
                "Summary": "Meitnerium is a chemical element with Symbol Mt and atomic Number 109. It is an extremely radioactive synthetic element (an element not found in nature that can be created in a laboratory). The most stable known isotope, meitnerium-278, has a half-life of 7.6 seconds.",
                "Symbol": "Mt",
                "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d7",
                "block": "d"
            },
            110:{
                "Name": "Darmstadtium",
                "Appearance": "null",
                "atomic_mass": 281,
                "Boil": "null",
                "Category": "unknown, probably transition metal",
                "Density": 34.8,
                "Discovered By": "Gesellschaft für Schwerionenforschung",
                "Melt": "null",
                "Molar heat": "null",
                "Number": 110,
                "Period": 7,
                "Group": 10,
                "Phase": "Solid",
                "Summary": "Darmstadtium is a chemical element with Symbol Ds and atomic Number 110. It is an extremely radioactive synthetic element. The most stable known isotope, darmstadtium-281, has a half-life of approximately 10 seconds.",
                "Symbol": "Ds",
                "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d8",
                "block": "d"
            },
           111:{
                "Name": "Roentgenium",
                "Appearance": "null",
                "atomic_mass": 282,
                "Boil": "null",
                "Category": "unknown, probably transition metal",
                "Density": 28.7,
                "Discovered By": "Gesellschaft für Schwerionenforschung",
                "Melt": "null",
                "Molar heat": "null",
                "Named_by": "null",
                "Number": 111,
                "Period": 7,
                "Group": 11,
                "Phase": "Solid",
                "Summary": "Roentgenium is a chemical element with Symbol Rg and atomic Number 111. It is an extremely radioactive synthetic element (an element that can be created in a laboratory but is not found in nature); the most stable known isotope, roentgenium-282, has a half-life of 2.1 minutes. Roentgenium was first created in 1994 by the GSI Helmholtz Centre for Heavy Ion Research near Darmstadt, Germany.",
                "Symbol": "Rg",
                "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d9",
                "block": "d"
            },
            112:{
                "Name": "Copernicium",
                "Appearance": "null",
                "atomic_mass": 285,
                "Boil": 3570,
                "Category": "transition metal",
                "Density": 14.0,
                "Discovered By": "Gesellschaft für Schwerionenforschung",
                "Melt": "null",
                "Molar heat": "null",
                "Named_by": "null",
                "Number": 112,
                "Period": 7,
                "Group": 12,
                "Phase": "Liquid",
                "Summary": "Copernicium is a chemical element with Symbol Cn and atomic Number 112. It is an extremely radioactive synthetic element that can only be created in a laboratory. The most stable known isotope, copernicium-285, has a half-life of approximately 29 seconds, but it is possible that this copernicium isotope may have a nuclear isomer with a longer half-life, 8.9 min.",
                "Symbol": "Cn",
                "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10",
                "block": "d"
            },
            113:{
                "Name": "Nihonium",
                "Appearance": "null",
                "atomic_mass": 286,
                "Boil": 1430,
                "Category": "unknown, probably transition metal",
                "Density": 16,
                "Discovered By": "RIKEN",
                "Melt": 700,
                "Molar heat": "null",
                "Named_by": "null",
                "Number": 113,
                "Period": 7,
                "Group": 13,
                "Phase": "Solid",
                "Summary": "Nihonium is a chemical element with atomic Number 113. It has a Symbol Nh. It is a synthetic element (an element that can be created in a laboratory but is not found in nature) and is extremely radioactive; its most stable known isotope, nihonium-286, has a half-life of 20 seconds.",
                "Symbol": "Nh",
                "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10 7p1",
                "block": "p"
            },
            114:{
                "Name": "Flerovium",
                "Appearance": "null",
                "atomic_mass": 289,
                "Boil": 420,
                "Category": "post-transition metal",
                "Density": 14,
                "Discovered By": "Joint Institute for Nuclear Research",
                "Melt": 340,
                "Molar heat": "null",
                "Named_by": "null",
                "Number": 114,
                "Period": 7,
                "Group": 14,
                "Phase": "Solid",
                "Summary": "Flerovium is a superheavy artificial chemical element with Symbol Fl and atomic Number 114. It is an extremely radioactive synthetic element. The element is Named after the Flerov Laboratory of Nuclear Reactions of the Joint Institute for Nuclear Research in Dubna, Russia, where the element was discovered in 1998.",
                "Symbol": "Fl",
                "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10 7p2",
                "block": "p"
            },
            115:{
                "Name": "Moscovium",
                "Appearance": "null",
                "atomic_mass": 289,
                "Boil": 1400,
                "Category": "unknown, probably post-transition metal",
                "Density": 13.5,
                "Discovered By": "Joint Institute for Nuclear Research",
                "Melt": 670,
                "Molar heat": "null",
                "Named_by": "null",
                "Number": 115,
                "Period": 7,
                "Group": 15,
                "Phase": "Solid",
                "Summary": "Moscovium is the Name of a synthetic superheavy element in the Periodic table that has the Symbol Mc and has the atomic Number 115. It is an extremely radioactive element; its most stable known isotope, moscovium-289, has a half-life of only 220 milliseconds. It is also known as eka-bismuth or simply element 115.",
                "Symbol": "Mc",
                "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10 7p3",
                "block": "p"
            },
            116:{
                "Name": "Livermorium",
                "Appearance": "null",
                "atomic_mass": 293,
                "Boil": 1085,
                "Category": "unknown, probably post-transition metal",
                "Density": 12.9,
                "Discovered By": "Joint Institute for Nuclear Research",
                "Melt": 709,
                "Molar heat": "null",
                "Named_by": "null",
                "Number": 116,
                "Period": 7,
                "Group": 16,
                "Phase": "Solid",
                "Summary": "Livermorium is a synthetic superheavy element with Symbol Lv and atomic Number 116. It is an extremely radioactive element that has only been created in the laboratory and has not been observed in nature. The element is Named after the Lawrence Livermore National Laboratory in the United States, which collaborated with the Joint Institute for Nuclear Research in Dubna, Russia to discover livermorium in 2000.",
                "Symbol": "Lv",
                "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10 7p4",
                "block": "p"
            },
            117:{
                "Name": "Tennessine",
                "Appearance": "null",
                "atomic_mass": 294,
                "Boil": 883,
                "Category": "unknown, probably metalloid",
                "Density": 7.17,
                "Discovered By": "Joint Institute for Nuclear Research",
                "Melt": 723,
                "Molar heat": "null",
                "Named_by": "null",
                "Number": 117,
                "Period": 7,
                "Group": 17,
                "Phase": "Solid",
                "Summary": "Tennessine is a superheavy artificial chemical element with an atomic Number of 117 and a Symbol of Ts. Also known as eka-astatine or element 117, it is the second-heaviest known element and penultimate element of the 7th Period of the Periodic table. As of 2016, fifteen tennessine atoms have been observed: six when it was first synthesized in 2010, seven in 2012, and two in 2014.",
                "Symbol": "Ts",
                "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10 7p5",
                "block": "p"
            },
            118:{
                "Name": "Oganesson",
                "Appearance": "null",
                "atomic_mass": 294,
                "Boil": 350,
                "Category": "unknown, predicted to be noble gas",
                "Density": 4.95,
                "Discovered By": "Joint Institute for Nuclear Research",
                "Melt": "null",
                "Molar heat": "null",
                "Named_by": "null",
                "Number": 118,
                "Period": 7,
                "Group": 18,
                "Phase": "Solid",
                "Summary": "Oganesson is IUPAC's Name for the transactinide element with the atomic Number 118 and element Symbol Og. It is also known as eka-radon or element 118, and on the Periodic table of the elements it is a p-block element and the last one of the 7th Period. Oganesson is currently the only synthetic member of Group 18.",
                "Symbol": "Og",
                "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10 7p6",
                "block": "p"
            },
            119:{
                "Name": "Ununennium",
                "Appearance": "null",
                "atomic_mass": 315,
                "Boil": 630,
                "Category": "unknown, but predicted to be an alkali metal",
                "Density": 3,
                "Discovered By": "GSI Helmholtz Centre for Heavy Ion Research",
                "Melt": "null",
                "Molar heat": "null",
                "Named_by": "null",
                "Number": 119,
                "Period": 8,
                "Group": 1,
                "Phase": "Solid",
                "Summary": "Ununennium, also known as eka-francium or simply element 119, is the hypothetical chemical element with Symbol Uue and atomic Number 119. Ununennium and Uue are the temporary systematic IUPAC Name and Symbol respectively, until a permanent Name is decided upon. In the Periodic table of the elements, it is expected to be an s-block element, an alkali metal, and the first element in the eighth Period.",
                "Symbol": "Uue",
                "electron_configuration": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10 7p6 8s1",
                "block": "s"}}



def AllDetails():
    if z in Element:
        for key, value in Element[z].items():
            print(f'"{key}": {value}')
            
    else:
        print(f"No Element found for atomic Number {z}")

def Particular_Detail():
    key=input("Enter the Key:")
    a=key.lower()
    b=a.capitalize()
    print(b+ ":" + str(Element[z][b]))
    




print("What you want to print")
print("Press 1 to print All detail about Element")
print("Press 2 to print paricular detail about Element")
print("Press 3 to draw Electron Shell Diagram of given Atomic No.")
n=int(input("Enter value"))
if n==1:
    z = int(input("Enter Atomic No.:"))
    AllDetails()
    
elif n==2:
    z = int(input("Enter Atomic No.:"))
    print("What do you want to print")
    all=["Name","Appearance","Atomic Mass","Boil","Category","Density","Discovered By","Melt","Molar heat","Named_by","Number","Period",
         "Group","Phase","Summary","Symbol","Electron confriguration"]
    print(all)
    
    Particular_Detail()
elif n==3:
    drawing()


