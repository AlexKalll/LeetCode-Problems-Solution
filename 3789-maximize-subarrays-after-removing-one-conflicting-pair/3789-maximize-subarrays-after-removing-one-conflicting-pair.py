class Solution:
 def maxSubarrays(_,n,c):
  for x in c:x.sort()
  c.sort();i=len(c)-1;a=b=n+1;s=0;d=[0]*(n+2)
  for l in range(n,0,-1):
   while i>=0 and c[i][0]==l:r=c[i][1];a,b=(r,a)if r<a else(a,r)if r<b else(a,b);i-=1
   s+=a;d[a]+=b-a
  return s-n*-~n//2+max(d[r]for _,r in c)