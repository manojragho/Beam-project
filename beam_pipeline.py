import apache_beam as beam
import re
import sys

p = beam.Pipeline()

input ='C:\Users\Manoj Raghorte\PycharmProjects\Beam-project\celebs-1.txt'
output = '\output.txt'

(p
 | 'Get_stuff' >> beam.io.ReadFromText(input)
 | 'Operation' >>
 | 'write' >> beam.io.WriteToText(output)
 )

p.run()