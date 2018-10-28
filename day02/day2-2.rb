input = File.readlines(ARGV.first, chomp: true)

p = nil
keypad = [[p, p, "1", p, p], \
          [p, "2", "3", "4", p], \
          ["5", "6", "7", "8", "9"], \
          [p,"A", "B", "C", p], \
          [p, p, "D", p, p]]
current = [2, 0]
min = 0
max = 4

moves = {"U" => [-1, 0], "D" => [1, 0], "L" => [0, -1], "R" => [0, 1]}

input.each do |line|
  line.split('').each do |dir|
    old = current.dup
    current = [current, moves[dir]].transpose.map {|x| x.reduce(:+)}
    if current[0] < min || current[0] > max || keypad[current[0]][current[1]].nil?
      current[0] = old[0]
    end

    if current[1] < min || current[1] > max || keypad[current[0]][current[1]].nil?
      current[1] = old[1]
    end
  end
  puts "KEY: #{keypad[current[0]][current[1]]}"
end
