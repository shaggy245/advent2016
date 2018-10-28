input = File.readlines(ARGV.first, chomp: true)

keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
current = [1, 1]
min = 0
max = 2

moves = {"U" => [-1, 0], "D" => [1, 0], "L" => [0, -1], "R" => [0, 1]}

input.each do |line|
  line.split('').each do |dir|  
    current = [current, moves[dir]].transpose.map {|x| x.reduce(:+)} 
    if current[0] < min
      current[0] = min
    elsif current[0] > max
      current[0] = max
    end

    if current[1] < min
      current[1] = min
    elsif current[1] > max
      current[1] = max
    end
    #puts "#{current}"
  end
  puts "KEY: #{keypad[current[0]][current[1]]}"
  #current = [1, 1]
end

