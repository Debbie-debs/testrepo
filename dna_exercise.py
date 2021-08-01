#AT content of a sequence 
#AT content = (at_count / len(seq)) * 100

seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

a_count = seq.count ("A")
t_count = seq.count ("T")

at_count = a_count + t_count
print(at_count)

at_percent = (at_count / len(seq)) * 100
print(at_percent)