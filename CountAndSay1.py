def countAndSay(n):
        def recursive(i,result):
            if i == n:
                return result
            
            number, count = [],[]
            for idx,d in enumerate(result):
                
                if idx > 0 and result[idx-1] == result[idx]:
                    count[-1] += 1 
                else:
                    number.append(d)
                    count.append(1)
            
            result = ''
            for k,v in zip(number,count):
                result += str(v) + k
            
            result = recursive(i+1,result)
            return result
                                
        return recursive(1,"1")


if __name__ == "__main__":
    n = 4
    print(countAndSay(n))
    

