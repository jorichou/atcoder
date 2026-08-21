# encoding: utf-8

n, a, b = gets.split.map(&:to_i)
s = gets

puts(s[a..n-1-b])