from Bio.Seq import Seq
import SeqRecord
file = r"C:\Users\Siddhi\Downloads\b.bacterialongum\ncbi_dataset\data\GCF_000196555.1\GCF_000196555.1_ASM19655v1_genomic.fna"
my_dna = file.open(file, "FASTA")
str = my_dna[0:100]
print(my_dna.read())
print (str)
