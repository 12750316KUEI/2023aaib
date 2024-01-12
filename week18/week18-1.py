Class ...
  def ...
    N = len(s)
    a = s[ :N//2]
    b = s[N//2: ]
    motherA = 0
    motherB = 0
    mother = "aeiouAEIOU"
    for c in a:
      if c in mother: motherA += 1
    for c in b:
      if c in mother: motherB += 1
    if motherA == motherB: return True
    else: return False