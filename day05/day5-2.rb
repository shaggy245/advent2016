require 'digest'

input = File.readlines(ARGV.first, chomp: true)

input.each do |line|
  counter = 0
  found = 0
  coded = ''
  password = '________'
  puts password
  until found == 8 do
    md5 = Digest::MD5.new
    coded = md5.hexdigest line + counter.to_s
    #puts coded
    if coded.start_with?('00000') && ('0'..'7').to_a.include?(coded[5]) && password[coded[5].to_i] == '_'
      password[coded[5].to_i] = coded[6]
      puts password
      found += 1
    end
    counter += 1
  end
  puts password
end

