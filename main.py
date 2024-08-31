from lexer import lexer
from parser1 import parser

print("The prompt shows up as long as the expression is valid")
while True:
   try:
       s = input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)

