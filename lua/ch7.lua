n, m = 16, 1000

local function fromto(a, b)
  return function () a = a + 1; if a <= b+1 then return a-1 end end
end

function one()
  for i in fromto(n, m) do
    print(i)
  end
end

function two()
  for i = n, m do
    print(i)
  end
end
