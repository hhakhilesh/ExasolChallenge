import string
import random
import hashlib
import cProfile
import time
from multiprocessing import Pool, cpu_count, Process, Manager

def generate_str(str_len):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars)for _ in range(str_len))

def checkhash_p1():
    prefix = '0'*4
    fixed_str = 'zesTjyNDXrGJYByPVojNByVOkqdWtDCLvCuGeoyiMmalsbibNDPdwvMzNwhXRtbU'
    while True:
        rand_str = generate_str(16)
        data = (fixed_str + rand_str).encode('utf-8')
        hash = hashlib.sha1(data).hexdigest()
        if hash.startswith(prefix):
            # print(hash)
            # print(rand_str)
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

def gen_and_check_parallel(fixed_str,prefix,str_len,return_dict,process_index):
    while True:
        rand_str = generate_str(str_len)
        data = (fixed_str + rand_str).encode('utf-8')
        hash = hashlib.sha1(data).hexdigest()
        if hash.startswith(prefix):
            # print(hash)
            # print(rand_str)
            break
            
    return_dict[str(process_index)] =[hash, rand_str]

def psuedo_tt():
    time.sleep(10)
    
def checkhash_p2():
    
    fixed_str = 'zesTjyNDXrGJYByPVojNByVOkqdWtDCLvCuGeoyiMmalsbibNDPdwvMzNwhXRtbU'
    prefix = '0'*3
    str_len = 16
    num_process = cpu_count()
    manager = Manager()
    return_dict = manager.dict()
    
    args_list = [fixed_str,prefix,str_len,return_dict,0]
    
    ProcessList =[]
    for j in range(num_process):
        args_list[-1] = j
        ProcessList.append(Process(target=gen_and_check_parallel,args=args_list))
        ProcessList[j].start()

    while True:    
        exitcodes=[]
        for process in ProcessList:
            exitcodes.append(process.exitcode)

        if 0 in exitcodes:
            break

    hash, random_str = return_dict[str(exitcodes.index(0))]
    print(hash,random_str)
    
    for process in ProcessList:
        process.terminate()
        
def main():
    for j in range(20):
        checkhash_p2()

if __name__ == "__main__":
    cProfile.run('main()',sort='tottime')
