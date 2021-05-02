#ALGORITMA
def carirarity():
    rarity= str(input("Masukkan rarity: "))
    print("\n Hasil pencarian: \n" )
    if (rarity == "C"):
        FindBy('gadget',{'rarity':'C'})
    elif (rarity == "B"):
        FindBy('gadget',{'rarity':'B'})
    elif (rarity == "A"):
        FindBy('gadget',{'rarity':'A'})
    elif (rarity == "S"):
        FindBy('gadget',{'rarity':'S'})
    else:
        print("Input tidak valid")

ShowEachEntry(gadget_by_rarity, display= carirarity, pageSize = 2)