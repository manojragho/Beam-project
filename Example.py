#Basic Apache beam program model
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
   input = 'tweets.csv' #.format(BUCKET)
   output_prefix = 'new.csv'#.format(BUCKET)
   searchTerm = '#'


   (p
      | 'Read_file' >> beam.io.ReadFromText(input)
      | 'find_words' >> beam.FlatMap(lambda x: re.findall(r'[A-Za-z\']+', x))
      | beam.combiners.Count.PerElement()
      | beam.Map(lambda word_count: '%s  %s' % (word_count[0], word_count[1]))
      | 'write' >> beam.io.WriteToText(output_prefix)
   )

   p.run()

