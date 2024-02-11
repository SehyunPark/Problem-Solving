<i>

  
## Two Pointers

<details>
  
<summary>click</summary>

- (1) x starts from 0 / y starts from n-1(arr length: n)
  
✅ cond1: two-pointers approach can be used in arr <br>
<br>
✅ cond2: answer hacked! <br>
<br>
✅ cond3: answer failed and x should be moved toward right dir <br>
<br>
✅ cond4: answer failed and y should be moved toward left dir

```python
x,y=0,n-1
while x<y:
    total=l[x]+l[y]
    if cond2:
        #answer update
        x+=1
        y-=1
    elif cond3:
        x+=1
    else: #cond4
        y-=1
```

- (2) x, y starts from 0(arr length: n)
  
✅ cond1: two-pointers approach can be used in arr <br>
<br>
✅ cond2: answer hacked! <br>
<br>
✅ cond3: usually not aligned with cond2 - iterating until we get an answer<br>
<br>
✅ code4: processing for getting out of the previous pointer x (e.x length-=1 / cum-=l[x] / del freq[kinds[x]] / X.discard(x) etc)

```python
for x in range(N): #pointer x
    #ans update here or ... 
    while y<N and cond3:
        #YOUR CODE
        y+=1 #pointer y 
    if cond2:
      #ans update here ...
    #code4
```
</details>









</i>
