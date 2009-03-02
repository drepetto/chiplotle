#! /usr/bin/env python

from chiplotle.cfg.cfg import CHIPLOTLE_DIR
import os
import subprocess
import sys
import time


os.system('clear')
CHAPTERSDIR = os.path.join(CHIPLOTLE_DIR, 'documentation', 'chapters')
chapters = os.listdir(CHAPTERSDIR)

#chapters.remove('.svn')
for ch in chapters:
   if ch.startswith('.'):
      chapters.remove(ch)

chapters.sort( )
print 'Rebuilding %s chapters ...\n' % len(chapters)

start_time = time.time( )
for i, chapter in enumerate(chapters):
   status = 'Chapter %d: %s ' % (i + 1, chapter)
   print status,
   sys.stdout.flush( )
   chapter_directory = os.path.join(CHAPTERSDIR, chapter)
   chapter_files = os.listdir(chapter_directory)
   if 'text.html' in chapter_files:
      os.chdir(chapter_directory)
      raw_chapter_file = os.path.join(chapter_directory, 'text.html')
      script = os.sep.join([CHIPLOTLE_DIR, 
         'documentation', 'scr', 'wrap_html.py'])
      #os.system('%s -f %s' % (script, raw_chapter_file))
      p = subprocess.Popen('%s -f %s' % (script, raw_chapter_file), 
         shell = True, stdout = sys.stdout, stderr = subprocess.PIPE)
      out, error = p.communicate( )
      if error:
         print '\n'
         print error,
      print ''

print ''
stop_time = time.time( )
print 'Total runtime: %d seconds.\n' % (stop_time - start_time)
