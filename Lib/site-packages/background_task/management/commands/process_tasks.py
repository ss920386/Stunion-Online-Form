from django.core.management.base import BaseCommand
from django import VERSION
import time
import logging
import sys

from background_task.tasks import tasks, autodiscover


class Command(BaseCommand):
    help = 'Run tasks that are scheduled to run on the queue'

    LOG_LEVELS = ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG']

    # Command options are specified in an abstract way to enable Django < 1.8 compatibility
    OPTIONS = (
        (('--duration', ), {
            'action': 'store',
            'dest': 'duration',
            'type': int,
            'default': 0,
            'help': 'Run task for this many seconds (0 or less to run forever) - default is 0',
        }),
        (('--sleep', ), {
            'action': 'store',
            'dest': 'sleep',
            'type': float,
            'default': 5.0,
            'help': 'Sleep for this many seconds before checking for new tasks (if none were found) - default is 5',
        }),
        (('--queue', ), {
            'action': 'store',
            'dest': 'queue',
            'help': 'Only process tasks on this named queue',
        }),
        (('--log-file', ), {
            'action': 'store',
            'dest': 'log_file',
            'help': 'Log file destination',
        }),
        (('--log-std', ), {
            'action': 'store_true',
            'dest': 'log_std',
            'help': 'Redirect stdout and stderr to the logging system',
        }),
        (('--log-level', ), {
            'action': 'store',
            'choices': LOG_LEVELS,
            'dest': 'log_level',
            'help': 'Set logging level (%s)' % ', '.join(LOG_LEVELS),
        }),
    )

    if VERSION < (1, 8):
        from optparse import make_option
        option_list = BaseCommand.option_list + tuple([make_option(*args, **kwargs) for args, kwargs in OPTIONS])

    # Used in Django >= 1.8
    def add_arguments(self, parser):
        for (args, kwargs) in self.OPTIONS:
            parser.add_argument(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self._tasks = tasks

    
    def _configure_logging(self, log_level, log_file, log_std):

        if log_level:
            log_level = getattr(logging, log_level)
        
        config = {}
        if log_level:
            config['level'] = log_level
        if log_file:
            config['filename'] = log_file
        
        if config:
            logging.basicConfig(**config)

        if log_std:
            class StdOutWrapper(object):
                def write(self, s):
                    logging.info(s)
            class StdErrWrapper(object):
                def write(self, s):
                    logging.error(s)
            sys.stdout = StdOutWrapper()
            sys.stderr = StdErrWrapper()

    
    def handle(self, *args, **options):
        log_level = options.pop('log_level', None)
        log_file = options.pop('log_file', None)
        log_std = options.pop('log_std', False)
        duration = options.pop('duration', 0)
        sleep = options.pop('sleep', 5.0)
        queue = options.pop('queue', None)
        
        self._configure_logging(log_level, log_file, log_std)
        
        autodiscover()
        
        start_time = time.time()
        
        while (duration <= 0) or (time.time() - start_time) <= duration:
            if not self._tasks.run_next_task(queue):
                logging.debug('waiting for tasks')
                time.sleep(sleep)
