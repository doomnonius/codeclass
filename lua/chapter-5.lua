--[[ 5.1: write a function that receives an arbitrary number of strings and returns them
all concatenated together]]--

function concat (...)
  local result = ''
  for i, v in ipairs{...} do
    result = result .. v
  end
  return result
end

--[[ 5.2: write a function that receives an array and prints all elements in that
array. Consider the pros and cons of using table.unpack in this function]]--

function prEach (a)
  for i = 1, #a do
    print (a[i])
    --print (table.unpack(a))
  end
end

--[[ 5.3: Write a function that receives an arbitrary number of values and
returns all of them except the first one]]--

function removeFirst (a, ...)
  return ...
end

--[[ 5.4: Write a function that receives an array and prints all combinations of
the elements in the array]]

-- so this is basically the power set of the array

function nextT (first, second)
  local out = {}
  for i, v in ipairs(first) do
    table.insert(out, v)
  end
  table.insert(out, second)
  return out
end

function combos (a)
  local totals = {{}}
  while #a >= 0 do
    if #a == 0 then
      for i, v in ipairs(totals) do
        print(table.unpack(v))
      end
      break
    end
    for i = 1, #totals do
      table.insert(totals, nextT(totals[i], a[1]))
      --print(#totals)
    end
    table.remove(a, 1)
    --print (#a)
  end
end
