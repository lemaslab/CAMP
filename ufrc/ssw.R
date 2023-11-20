# 

cd /blue/djlemas/haswanthpopuri/Complete-Striped-Smith-Waterman-Library/
  

src/ssw_test -c demo/1M.fa demo/1k.fa


src/pyssw.py -l src/ -c /blue/djlemas/share/data/Benchmark/receptors133.fa/1cjr.recep.fa /blue/djlemas/share/data/Benchmark/ligands133.fa/1cjr.lig.fa

src/ssw_test -c /blue/djlemas/share/data/Benchmark/receptors133.fa/1cjr.recep.fa /blue/djlemas/share/data/Benchmark/ligands133.fa/1cjr.lig.fa