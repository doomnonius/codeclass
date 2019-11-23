local socket = require("socket")

function download(host, file)
  local c = assert(socket.connect(host, 80))
  local count = 0 -- counts number of bytes read
  c:send("GET " .. file .. " HTTP/1.0\r\n\r\n")
  while true do
    local s, status = receive(c)
    count = count + #s
    if status == "closed" then break end
  end
  c:close()
  print(file, count)
end


