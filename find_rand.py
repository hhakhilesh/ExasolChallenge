import string
import random
import hashlib
import cProfile
from multiprocessing import Pool, cpu_count

def generate_str(str_len):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars)for _ in range(str_len))

def checkhash_p1():
    prefix = '0'*3
    fixed_str = 'zesTjyNDXrGJYByPVojNByVOkqdWtDCLvCuGeoyiMmalsbibNDPdwvMzNwhXRtbU'
    while True:
        rand_str = generate_str(16)
        data = (fixed_str + rand_str).encode('utf-8')
        hash = hashlib.sha1(data).hexdigest()
        if hash.startswith(prefix):
            print(hash)
            print(rand_str)
            break

def gen_and_check(fixed_str,prefix,str_len):
    while True:
        rand_str = generate_str(str_len)
        data = (fixed_str + rand_str).encode('utf-8')
        hash = hashlib.sha1(data).hexdigest()
        if hash.startswith(prefix):
            # print(hash)
            # print(rand_str)
            break
            
    return hash, rand_str
    
def checkhash_p2():
    
    fixed_str = 'zesTjyNDXrGJYByPVojNByVOkqdWtDCLvCuGeoyiMmalsbibNDPdwvMzNwhXRtbU'
    prefix = '0'*5
    str_len = 16
    num_process = cpu_count()
    pool = Pool(processes=num_process-6)
    args_list = (fixed_str,prefix,str_len)
    
    results =[]
    for j in range(num_process-6):
        result=pool.apply(gen_and_check,args_list)
        results.append(result)
    
    pool.close()
    pool.join()
    
    
def main():
    for j in range(1):
        checkhash_p2()


cProfile.run('main()',sort='tottime')