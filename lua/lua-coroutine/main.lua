local ping, pong
total = 0

local actor = function (other, value, id)
  while value < 1000000 do
    -- print(coroutine.running())
    total = total + 1
    value = value + 1
    if id % 2 == 0 then
      coroutine.resume(other, coroutine.running(), value, id + 1)
    else
      coroutine.yield()
    end
  end
end
ping = coroutine.create(actor)
pong = coroutine.create(actor)

local success, start

start = os.clock()
coroutine.resume(ping, pong, 1, 0)
print(os.clock() - start)
print(total)
