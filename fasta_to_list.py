# Here, I am reading fasta files using pufaidx library and reading protein sequences line by line

from pyfaidx import Fasta
genes = Fasta('data/training.fasta')

proteins = []
for line in genes:
    proteins.append(str(line))