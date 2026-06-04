class SeqAnalyzer:                      #class to analyze RNA sequences


    def input_seq(self, seq):                    #function to input the sequence and remove spaces and convert to uppercase
        self.seq = seq.replace(" ","").upper()


    def check_seq(self, seq):                     #function to check for invalid nucleotides and remove them from the sequence, also prints the invalid nucleotides that were removed
        invalid_nucleotides = set(seq) - set("AUCG")
        for i in seq:
            if i in invalid_nucleotides:
                seq = seq.replace(i, "")
        print("Invalid nucleotides removed:", invalid_nucleotides)        
        return seq
    


    def codon_seq(self):                              #function to convert the sequence into codons and return the corresponding amino acids, also handles stop codons and start codons
        cdSeq=""
        x={
    # U - First Base
    'UUU': 'Phe', 'UUC': 'Phe', 'UUA': 'Leu', 'UUG': 'Leu',
    'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser',
    'UAU': 'Tyr', 'UAC': 'Tyr', 'UAA': 'Stop', 'UAG': 'Stop',
    'UGU': 'Cys', 'UGC': 'Cys', 'UGA': 'Stop', 'UGG': 'Trp',
    
    # C - First Base
    'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
    'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
    'CAU': 'His', 'CAC': 'His', 'CAA': 'Gln', 'CAG': 'Gln',
    'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg',
    
    # A - First Base
    'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile', 'AUG': 'Met/start',
    'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
    'AAU': 'Asn', 'AAC': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys',
    'AGU': 'Ser', 'AGC': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg',
    
    # G - First Base
    'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val',
    'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
    'GAU': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu',
    'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly'}
        
        for i in range(0,len(self.seq),3):
            codon=self.seq[i:i+3]
            if codon in x:
                cdSeq+=x[codon]+" "
        return cdSeq
    
 
    def complementary_seq(self):                        #function to return the complementary sequence of the input sequence, also handles invalid nucleotides by ignoring them
        x={"A":"U","U":"A","C":"G","G":"C"}
        compSeq=""
        for i in self.seq:
            if i in x:
                compSeq+=x[i]
        return compSeq



    def cg_content(self):                              #function to calculate the CG content of the sequence and return it as a percentage
        c=self.seq.count("C")
        g=self.seq.count("G")
        cg=(c+g)/len(self.seq)*100
        return cg    
    


    def length_seq(self):                           #function to return the length of the sequence
        return len(self.seq)


    def refine_seq(self):                             #function to refine the sequence by removing any nucleotides that are not in the set of valid nucleotides and also ensures that the length of the sequence is a multiple of 3 for codon analysis, also prints the number of nucleotides removed
        x=len(self.seq)%3
        if x!=0:
            self.seq=self.seq[:-x]
        else:
            self.seq=self.seq  



s1=SeqAnalyzer()                            #object of the SeqAnalyzer class

s=input("Enter a sequence: ")
s1.input_seq(s)
s1.seq = s1.check_seq(s1.seq)
print("Refined sequence:",s1.seq)
s1.refine_seq()
print("Complementary sequence: ",s1.complementary_seq())
print("Codon sequence: ",s1.codon_seq())
print("CG content: ",s1.cg_content(),"%")

