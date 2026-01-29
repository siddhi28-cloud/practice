from Bio import SeqIO
file = r"C:\Users\Siddhi\Downloads\b.bacterialongum\ncbi_dataset\data\GCA_000196555.1\GCA_000196555.1_ASM19655v1_genomic.fna"
record = next(SeqIO.parse(file, "fasta"))
gene = record[:50]
print (gene)