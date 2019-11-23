--[[ 6.1: Write a function integral that receives a function f and returns an
approximation of its integral]]

-- I don't understand integrals so Ill have to skip this one


--[[ 6.2: Exercise 3.3 asked you to write a function that receives a polynomial
and a value for its variable, and returns the polynomial value. Write the
curried version of that function. Your function should receive a polynomial
and returns a function that, when called with a value for x, returns the value
of the polynomial for that x]]

function newpoly(coefs)
  return function (x)
          local n = #coefs - 1
          local total = 0
          for i = 1, n + 1 do
            print(n)
            next = coefs[#coefs] * x^n
            coefs[#coefs] = nil
            n = n-1
            total = total + next
          end
          print(total)
        end
end


--[[ 6.3: wrtie a function that performs and unbounded call chain without
 recursion.]]

--[[ This could be done with "load", where the user enters a new function
repeatedely. Maybe.]]


--[[ 6.4: A tail call is a goto in disguise. Using this idea, reimplement the
simple maze game from section 4.4 using tail calls. Each block should become
a new function, and each goto becomes a tail call.]]

function room1()
  local move = io.read()
  if move == "south" then return room3()
  elseif move == "east" then return room2()
  else
    print("invalid move")
    return room1()
  end
end

function room2()
  local move = io.read()
  if move == "south" then return room4()
  elseif move == "west" then return room1()
  else
    print("invalid move")
    return room2()
  end
end

function room3()
  local move = io.read()
  if move == "north" then return room1()
  elseif move == "east" then return room4()
  else
    print("invalid move")
    return room3()
  end
end

function room4()
  print "Congratulations, you won!"
end
