# DNA_SeqAnalyzer

The analyzer is a single HTML file with no external dependencies — all logic runs in the browser using vanilla JavaScript.
When you paste a DNA sequence and hit Analyze, the input is sanitized (whitespace stripped, uppercased) and validated against [ATGCN] characters before any processing begins.
GC Content — counts occurrences of G and C bases, divides by total sequence length, and expresses it as a percentage. Also tallies individual base counts (A, T, G, C) displayed as colored pills.
Complement Strand — maps each base to its Watson-Crick pair (A↔T, G↔C) to generate the 3'→5' complement. The reverse complement (used in replication and primer design) is produced by reversing that result, giving the antiparallel 5'→3' strand.
ORF Detection — scans all 3 reading frames of the sense strand for ATG start codons, then walks forward in triplets until a stop codon (TAA, TAG, or TGA) is encountered. Any resulting sequence ≥ 30bp is reported as an ORF, along with its frame, position, length in bp, and predicted amino acid count. Results are sorted by length, longest first.
Codon Frequency — splits the entire sequence into non-overlapping triplets starting from position 0, counts each unique codon, and renders them as cards with a mini bar chart scaled relative to the most frequent codon. Codons are color-coded — green for standard, amber for Met (start), red for stop codons — using the standard genetic code lookup table hardcoded in the script.

this also works offline after downloading the code file
ai script has been used in this as it is a learning project
