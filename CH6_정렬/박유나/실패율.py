#실패율                                   
def solution(n, stages):
  answer = {}
  length = len(stages)                         
  for i in range(1, n+1):
    if length != 0:                
      cnt = stages.count(i)                    
      answer[i] = cnt / length                
      length = length - cnt                           
    else:
      answer[i] = 0
  return sorted(answer, key=lambda x: answer[x], reverse=True)       
