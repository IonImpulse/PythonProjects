import re
key={'Ile':['AUU','AUC','AUA'],'Leu':['CUU','CUC','CUA','CUG','UUA','UUG'],
            'Val':['GUU','GUC','GUA','GUG'],'Phe':['UUU','UUC'],'Met':['AUG'],
            'Cys':['UGU','UGC'],'Ala':['GCU','GCC','GCA','GCG'],'Gly':['GGU','GGC','GGA','GGG'],
            'Pro':['CCA', 'CCU', 'CCC', 'CCG'],'Thr':['ACU','ACC','ACA','ACG'],
            'Ser':['UCU','UCC','UCA','UCG','AGC'],'Tyr':['UAU','UAC'],
            'Trp':['UGG'],'Gln':['CAA','CAG'],'Asn':['AAU','AAC'],'His':['CAU','CAC'],
            'Glu':['GAA','GAG'],'Asp':['GAU','GAC'],'Lys':['AAA','AAG'],
            'Arg':['CGU','CGC','CGA','CGG','AGA','AGG'],'STOP':['UAA','UAG','UGA']}

def get_codon(RNA_Seq) :
    RNA_Seq = RNA_Seq.split(",")
    codon = ""

    for seq in RNA_Seq :
        for item in key :
            if seq in key[item] :
                codon += item + " "

    return codon[:-1]


while True :
    print("Input sequence:")
    
    sequence = input(":")

    if " " in sequence :
        sequence = sequence.replace(" ", ",")
    else :
        sequence = ','.join([sequence[i:i+3] for i in range(0, len(sequence), 3)])

    check = sorted(list(set([i.upper() for i in sequence.replace(",", "")])))

    
    try:
    
        if check == ['A', 'C', 'G', 'T'] :
            print("RNA: " + str(sequence.upper().replace("T", "U").replace(",", " ")))

            print("Codon: " + str(get_codon(sequence.upper().replace("T", "U"))))

        elif check == ['A', 'C', 'G', 'U'] :
            print("DNA: " + str(sequence.upper().replace("U", "T").replace(",", " ")))

            print("Codon: " + str(get_codon(sequence.upper())))

        else :
            output = ""
            
            if "-" in sequence :
                sequence = sequence.replace("-,", "")

            for index, seq in enumerate(sequence.split(",")) :
                output += str(index+1) + ": " + str(seq[:3].title()) + " - " + str(key[seq[:3].title()]) + "\n"
        
            print("RNA:")
            print(output)

            print("DNA:")
            print(output.replace('U', 'T'))
    
    except Exception as e : 
        print(e)
    print("\n====================\n")