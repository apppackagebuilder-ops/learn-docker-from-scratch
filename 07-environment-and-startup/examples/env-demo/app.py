import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--mode', default='demo')
args = parser.parse_args()

print('Application name:', os.getenv('APP_NAME', 'DockerCourseApp'))
print('Application environment:', os.getenv('APP_ENV', 'local'))
print('Selected mode:', args.mode)
