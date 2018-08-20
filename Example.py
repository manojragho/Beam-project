#Basic Apache-beam pipeline

import apache_beam as beam
import re



PROJECT='Beam-wordcount'
BUCKET='words-count'

def run():
   argv = [
      '--project={0}'.format(PROJECT),
      '--job_name=examplejob2',
      '--save_main_session',
      '--staging_location=gs://{0}/staging/'.format(BUCKET),
      '--temp_location=gs://{0}/staging/'.format(BUCKET)
      #'--runner=DataflowRunner'
   ]

   p = beam.Pipeline(argv=argv)
   input = 'celebs-1.txt' #.format(BUCKET)
   output_prefix = 'new.txt'#.format(BUCKET)



   (p
      | 'Read_file' >> beam.io.ReadFromText(input)

      | 'write' >> beam.io.WriteToText(output_prefix)
   )

   p.run()

if __name__ == '__main__':
   run()