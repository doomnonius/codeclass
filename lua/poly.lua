function poly (coefs, x)
  -- list goes from a0 to an
  -- function looks from an to a0
  local n = #coefs - 1
  local total = 0
  for i = 1, n+1 do
    print(n)
    next = coefs[#coefs] * x^n
    coefs[#coefs] = nil
    n = n - 1
    total = total + next
  end
  print(total)
end


function makelist ()  
  l = {}
  print("Enter the coefficients, and type done when finished.")
  while true do
    a = io.read("*n")
    print(a)
    if a == nil then
      break
    end
    l.insert(a)
  end
  return l
end
