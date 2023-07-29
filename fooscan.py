from dotenv import load_dotenv
from scanner import *

load_dotenv('foo.env')

scanner = Scanner()
scanner.scanBlock(100390)