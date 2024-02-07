s='''Siam ChitLom
ChitLom PhloenChit
PhloenChit Nana
Siam NationalStadium 
Ratchadamri Siam
Siam PhayaThai
Ratchadamri SalaDaeng 
ThongLo Ekkamai
Ekkamai ThongLo'''
station_info=dict() 
for line in s.split('\n'):
  s1,s2=line.split() 
  if s1 in station_info:
    station_info[s1].append(s2) 
  else:
    station_info[s1] = [s2] 
  s2,s1=line.split() 
  if s1 in station_info:
    station_info[s1].append(s2) 
  else:
    station_info[s1] = [s2] 

print(station_info)

ans=[]
s_station='Siam'
ans.append(s_station)
# first hop 
ans+=station_info[s_station]
print(ans)
for station in ans[1:]:
  ans+=station_info[station]
ans=set(ans)
sorted(list(ans))